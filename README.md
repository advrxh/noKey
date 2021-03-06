![banner](https://raw.githubusercontent.com/AadilVarsh/noKey/main/images/banner-logo.png)

# A simple yet to be powerful google meet utility bot made with selenium🐍!

<br>
<br>
<br>

* JOIN MEETINGS 
* RECORD AND FORMAT ATTENDEE LIST IN EXCEL SHEETS AND JSON FORMAT

# Installation

### **CLONE THE REPO** - 🆑⭕NE
```bash
$ git clone https://github.com/AadilVarsh/noKey.git

```

### **CREATE A VIRTUAL ENV** 🚀
```bash
$ python3 -m venv .env

```

### **INSTALL DEPENDENCIES** 💻
```bash
$ python3 -m pip install -r requirements.txt

```

```txt
arrow==1.1.1
openpyxl==3.0.7
selenium==3.141.0
typer==0.3.2
typer-cli==0.0.12
```

### **UPDATE** -> `nokey/configs.json` 🔻

example `configs.json` 👇🏻
```json

{
    "chrome_driver_path": "path/to/chrome/driver.exe",
    "chrome_profile_path": "path/to/chrome/profile/",
    "output_dir_path": "path/to/excel/output/dir/",
    "chrome_args": [<insert chrome args>],
    "startup": {
        "audio": true,
        "video": true
    }
}

```

### **RUNNING noKey CLI** 🎇
<br>

* ### *BASIC* usage
```bash
python3 nokey.py url https://meet.google.com/abc-defg-hij
```

* ### **CUSTOM USER** 
```bash
python3 nokey.py url https://meet.google.com/abc-defg-hij --user 0
```

### What is user ❓
#### They are unique USER index identifiers for your google or gsuite account. 

![user_id_tut](https://raw.githubusercontent.com/AadilVarsh/noKey/main/images/user_id_tut.png)

* ### JOINING USING MEET CODE 👩🏻‍💻

```bash
python3 nokey.py code abc-defg-hij --user 0
```

* ### HELP MENU

```bash
python3 nokey.py --help
```

# *HOW TO CONTRIBUTE ❓*

## Have an issue? you know what to do😉. Want to make any advancements fork the repo and commit a PR I'll get to you and review it asap! 🏃🏻‍♂️💨

[🐦Twitter](https://twitter.com/aadilvarsh)


