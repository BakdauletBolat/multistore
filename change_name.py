from config import APP_NAME
import os, sys

NEW_NAME = input()


def changeSettingsFile():
    with open (f'{APP_NAME}/settings.py', 'r') as f:
        old_data = f.read()

    new_data = old_data.replace(f'{APP_NAME}', NEW_NAME)

    with open (f'{APP_NAME}/settings.py', 'w') as f:
        f.write(new_data)


def changeASGIFile():
    with open (f'{APP_NAME}/asgi.py', 'r') as f:
        old_data = f.read()

    new_data = old_data.replace(f'{APP_NAME}', NEW_NAME)

    with open (f'{APP_NAME}/asgi.py', 'w') as f:
        f.write(new_data)



def changeWSGIFile():
    with open (f'{APP_NAME}/wsgi.py', 'r') as f:
        old_data = f.read()

    new_data = old_data.replace(f'{APP_NAME}', NEW_NAME)

    with open (f'{APP_NAME}/wsgi.py', 'w') as f:
        f.write(new_data)


def changeManagePYFile():
    with open (f'manage.py', 'r') as f:
        old_data = f.read()

    new_data = old_data.replace(f'{APP_NAME}', NEW_NAME)

    with open (f'manage.py', 'w') as f:
        f.write(new_data)


def changeFolderName():
    os.rename(APP_NAME,NEW_NAME)

def changeConfigFile():
    with open ('config.py', 'r') as f:
        old_data = f.read()

    new_data = old_data.replace(f'{APP_NAME}', NEW_NAME)

    with open ('config.py', 'w') as f:
        f.write(new_data)


def main():
    changeSettingsFile()
    changeASGIFile()
    changeWSGIFile()
    changeConfigFile()
    changeFolderName()
    changeManagePYFile()

main()