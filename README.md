EN / [RU](https://github.com/AmbreKitsune/ambrekitsune/blob/main/README.ru.md)

<h1 align="center">📒TEST APP FOR TODO📖</h1>
</br>

---

# Description 😼

A project created for educational purposes.</br>
My goal was to create a working app for Flet, spending exactly the amount of time it took, without regard for a beautiful design, a cool and powerful stack, or unnecessary problems.
The task was simple, so we could add and delete tasks.

---

# Application functionality ✅

The app can:
 - add new tasks;
 - delete;
 - save existing tasks to a JSON file.

---

# Screenshot of the application 🗺️

![Todo App](assets/screenshots/todo-app.png)

---

# Installation and launch 🛠️

### 1) Setting up the environment.

#### Windows: CMD
```
python -m venv .venv
.venv\Scripts\activate
```

#### Windows: Powershell
```
python -m venv .venv
.\.venv\Scripts\Activate.ps1

При ошибке Execution Policy:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

#### Linux / macOS
```
Если нет python-venv:
sudo apt install python3-venv

python3 -m venv .venv
source .venv/bin/activate
```

### 2) Installing dependencies.

```
pip install flet pydantic pyinstaller
```
P.s. If you don't want to create the `.exe` file yourself in the future, I recommend deleting pyinstaller to avoid littering the project.

### 3) Start application.
```
flet run -m app.main -r -d
```

### 4) Build exe.
```
flet pack app/main.py --name TodoFletApp --product-name "Todo Flet App" --onedir --distpath release -y
```
P.S. If you're comfortable with Flet and want to build your project using `flet build windows`, that's also a viable option. In my case, `flet pack` worked more reliably.

---

# Errors ❌

**Error:** The program/exe-file does not start or starts but crashes.
**Solution:** Make sure the `_internal` folder is located next to the executable folder.

**Error:** The save file does not remember and/or load tasks.
**Solution:** Do not install the portable version to `C:\Program Files`. Move the application to `%LOCALAPPDATA%\Ambre\TodoFletApp` or any other folder where the application has write access.

**Error:** The task file is corrupted.
**Solution:** Deleting the tasks file in the root folder, and then `data/tasks.json`. While this is a rare error, and usually occurs only because the user has tampered with it, if you don't want to dig into `data/tasks.json`, it's best to just delete it.

**Error:** Antivirus blocks the program or the program's launch.
**Solution:** It's also possible that your antivirus will complain about a given program, even if it's completely safe. In this case, I recommend verifying that the program isn't malicious and then adding it to the exception list in your antivirus.

---

# Important ⚠️

I intentionally didn't describe the full installation and configuration of Flet to avoid overloading the README and unnecessary details.

This project is for educational purposes. Its purpose is to demonstrate a simple working example of a Flet desktop application with the ability to add, delete, and save tasks.

If you encounter any problems using the program, you can contact me on social media. If you're a developer, feel free to take the code, modify it, and use it for your own purposes.

---

# Connection 🙀

- **Telegram**: [@NightAmbreKitsune](https://t.me/NightAmbreKitsune)
- **Discord Server**: [Присоединиться](https://discord.gg/U59cgYUNwv)
