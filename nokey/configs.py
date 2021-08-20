from pathlib import Path
import pathlib
import json
import os


class Config:
    def __init__(self) -> None:

        self.CONFIG_PATH = Path(Path(__file__).parent.resolve(), "configs.json")

        with self.CONFIG_PATH.open("r+", encoding="utf-8") as configFile:
            self.CONFIG = json.load(configFile)

        self.CHROME_DRIVER_PATH = self.CONFIG["chrome_driver_path"]
        self.CHROME_PROFILE_PATH = self.CONFIG["chrome_profile_path"].replace(
            "%LOCALAPPDATA%", os.environ["LOCALAPPDATA"]
        )

        self.OUTPUT_DIR_PATH = self.CONFIG["output_dir_path"].replace(
            "%USERPROFILE%", os.environ["USERPROFILE"]
        )
        self.CHROME_ARGS = self.CONFIG["chrome_args"]
        self.STARTUP = self.CONFIG["startup"]

    def spawn_configs(self):

        config_data_format = {
            "chrome_driver_path": "C:\\chromedriver.exe",
            "chrome_profile_path": "%LOCALAPPDATA%\\Google\\Chrome\\User Data",
            "output_dir_path": "%USERPROFILE%\\Desktop\\NokeyBotOutput",
            "chrome_args": [],
            "startup": {"audio": True, "video": True},
        }

        with Path("./configs.json").open("r+", encoding="utf-8") as configFile:
            json.dump(config_data_format, configFile)

    def reset_configs(self):

        Path("./configs.json").unlink()
        Path("./configs.json").touch()

        config_data_format = {
            "chrome_driver_path": "C:\\chromedriver.exe",
            "chrome_profile_path": "%LOCALAPPDATA%\\Google\\Chrome\\User Data",
            "output_dir_path": "%USERPROFILE%\\Desktop\\NokeyBotOutput",
            "chrome_args": [],
            "startup": {"audio": True, "video": True},
        }

        with Path("./configs.json").open("r+", encoding="utf-8") as configFile:
            json.dump(config_data_format, configFile)

    def __call__(self):

        return self.CONFIG
