from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import (
    StaleElementReferenceException,
    NoSuchElementException,
    WebDriverException,
)

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


import openpyxl as xl

from time import sleep
import datetime
import json, pathlib
import arrow

from nokey.configs import Config
from nokey.selectors import Selectors
from nokey.cliUtil import Util


class Setup:
    def __init__(self) -> None:
        self.config = Config()
        self.selectors = Selectors()

        self.driver_options = Options()
        self.driver_options.add_argument(
            f"user-data-dir={self.config.CHROME_PROFILE_PATH}"
        )
        self.driver_options.add_experimental_option(
            "excludeSwitches", ["enable-logging"]
        )

        self.driver = webdriver.Chrome(
            options=self.driver_options, executable_path=self.config.CHROME_DRIVER_PATH
        )
        self.action = ActionChains(self.driver)

        self.WAIT = WebDriverWait(self.driver, 100)

    def run(self, meet_url):
        self.url = meet_url
        self.util = Util(meet_url)
        self.driver.get(meet_url)
        self.startup()
        self.join()
        self.on_join()
        self.listen()

    def startup(self):

        STARTUP_CONF = self.config.STARTUP
        ElementSelector = self.selectors.SELECTORS["mute_odo_vdo_on_load"]

        Elements = self.WAIT.until(
            ec.presence_of_all_elements_located((By.CLASS_NAME, ElementSelector["val"]))
        )

        if len(Elements) == 2:
            for el in Elements:
                el.click()
        else:
            for el in Elements:
                el.click()

    def join(self):

        elSel = self.selectors.SELECTORS["join_ask_to_join"]

        self.WAIT.until(
            ec.text_to_be_present_in_element((By.CLASS_NAME, elSel["val"]), "Join now")
        )

        self.driver.find_element_by_class_name("NPEfkd").click()

        self.util.join_msg()

    def on_join(self):
        ElementSelector = self.selectors.SELECTORS["atendee_list_btn"]

        Element = self.WAIT.until(
            ec.presence_of_element_located((By.XPATH, ElementSelector["val"]))
        )

        Element.click()

    def writeData(self, data):

        dataFilePath = pathlib.Path(
            pathlib.Path(__file__).parent.resolve(),
            f"JsonRec/AtendeeData.{str(datetime.date.today())}.{self.driver.current_url[24:24+12]}.json",
        )

        try:
            dataFilePath.unlink()
        except Exception:
            pass
        dataFilePath.touch()

        with dataFilePath.open("r+", encoding="utf-8") as dataFile:
            json.dump(data, dataFile)
        self.writeCSV()

    def writeCSV(self):
        jsonPath = pathlib.Path(
            pathlib.Path(__file__).parent.resolve(),
            f"JsonRec/AtendeeData.{str(datetime.date.today())}.{self.driver.current_url[24:24+12]}.json",
        )
        xl_path = pathlib.Path(
            pathlib.Path(self.config.OUTPUT_DIR_PATH),
            f"AtendeeData.{str(datetime.date.today())}.{self.driver.current_url[24:24+12]}.xlsx",
        )

        try:
            xl_path.unlink()
        except Exception as e:
            pass
        xl_path.touch()

        wb = xl.Workbook()
        ws = wb.active

        ws.append(
            [
                "Name",
                "Joined At",
                "Last Rejoin At",
                "Last Left At",
                "Leave rate",
            ]
        )

        with jsonPath.open("r+", encoding="utf-8") as jsonFile:
            data = json.load(jsonFile)

        for student in data.keys():
            ws.append(
                [
                    student,
                    data[student]["joined"],
                    data[student]["last rejoin"],
                    data[student]["left"],
                    data[student]["leave_rate"],
                ]
            )

        wb.save(xl_path)

    def close(self):
        self.driver.close()

    def listen(self):
        self.util.listen()
        sleep(5)
        Num_Of_Participants_ElementSelector = self.selectors.SELECTORS[
            "no_of_participants"
        ]

        num_El = self.WAIT.until(
            ec.presence_of_element_located(
                (By.CLASS_NAME, Num_Of_Participants_ElementSelector["val"])
            )
        )

        Names_Element_Selector = self.selectors.SELECTORS["participant_name"]

        NamesEl = self.WAIT.until(
            ec.presence_of_all_elements_located(
                (By.CLASS_NAME, Names_Element_Selector["val"])
            )
        )

        for x in NamesEl:
            self.util.newPt(x.text)

        participants = int(num_El.text)
        participants_names_arr = [x.text for x in NamesEl]
        participants_data = {}

        for participant in participants_names_arr:
            participants_data[participant] = {
                "joined": str(arrow.now().format("hh:mm-A")),
                "last rejoin": str(arrow.now().format("hh:mm-A")),
                "left": None,
                "leave_rate": 0,
            }
        self.writeData(participants_data)

        while True:
            sleep(0.1)
            try:
                num_El = self.driver.find_element_by_class_name(
                    Num_Of_Participants_ElementSelector["val"]
                )

                newParticipants = int(num_El.text)

                NamesEl = self.driver.find_elements_by_class_name(
                    Names_Element_Selector["val"]
                )
                new_participants_name_arr = []

                for i in NamesEl:
                    new_participants_name_arr.append(i.text)

                if newParticipants > participants:
                    for participant in participants_names_arr:
                        if participant in new_participants_name_arr:
                            new_participants_name_arr.remove(participant)

                    # print("New Participants : " + ",".join(new_participants_name_arr))
                    self.util.newPt(",".join(new_participants_name_arr))

                    for newParticipant in new_participants_name_arr:
                        if newParticipant in participants_data.keys():
                            _ = participants_data[newParticipant]
                            del participants_data[newParticipant]
                            participants_data[newParticipant] = {
                                "joined": _["joined"],
                                "last rejoin": str(arrow.now().format("hh:mm-A")),
                                "left": _["left"],
                                "leave_rate": _["leave_rate"],
                            }
                        else:
                            participants_data[newParticipant] = {
                                "joined": str(arrow.now().format("hh:mm-A")),
                                "last rejoin": None,
                                "left": None,
                                "leave_rate": 0,
                            }
                    participants = newParticipants
                    participants_names_arr = [x.text for x in NamesEl]
                    self.writeData(participants_data)

                elif newParticipants < participants:

                    uqNewPt = sorted(list(set(new_participants_name_arr)))

                    left_arr = []

                    for NewPt in uqNewPt:
                        z = 0
                        for Pt in new_participants_name_arr:
                            if NewPt == Pt:
                                z += 1
                        if z > 1:
                            new_participants_name_arr.remove(NewPt)

                    for participant in participants_names_arr:
                        if participant not in new_participants_name_arr:
                            left_arr.append(participant)

                    # print("Participant Left " + ",".join(left_arr))
                    self.util.levPt(",".join(left_arr))

                    for left in left_arr:
                        if left in participants_data.keys():
                            _ = participants_data[left]
                            del participants_data[left]
                            participants_data[left] = {
                                "joined": _["joined"],
                                "last rejoin": _["last rejoin"],
                                "left": str(arrow.now().format("hh:mm-A")),
                                "leave_rate": _["leave_rate"] + 1,
                            }

                    participants = newParticipants
                    participants_names_arr = [x.text for x in NamesEl]
                    self.writeData(participants_data)
            except StaleElementReferenceException:
                continue
            except WebDriverException:
                self.close()
                break
