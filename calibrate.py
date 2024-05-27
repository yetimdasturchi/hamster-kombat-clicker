import pyautogui
import time
import configparser
import cv2
import os
import pytesseract
import numpy as np
from pynput import mouse

def get_mouse_position_on_click():
    print("Aniqlash uchun kerakli pozitsiya ustiga bosing.")
    positions = []

    def on_click(x, y, button, pressed):
        if pressed:
            print(f'Saqlangan pozitsiya: (x={x}, y={y})')
            positions.append((x, y))
            return False  # Stop listener

    with mouse.Listener(on_click=on_click) as listener:
        listener.join()
    
    return positions[0]

def capture_and_show_region(region):
    screenshot = pyautogui.screenshot(region=region)
    screenshot_np = np.array(screenshot)
    gray_image = cv2.cvtColor(screenshot_np, cv2.COLOR_BGR2GRAY)

    _, thresholded_image = cv2.threshold(gray_image, 150, 255, cv2.THRESH_BINARY_INV)

    cv2.imshow("Aniqlangan maydon", thresholded_image)
    
    text = pytesseract.image_to_string(thresholded_image, config='--psm 7')
    print(f"Aniqlangan matn: {text.strip()}")
    
    cv2.waitKey(500)
    cv2.destroyAllWindows()

def generate_config_file(x_position, y_position, region):
    config = configparser.ConfigParser()
    config['settings'] = {
        'x_position': x_position,
        'y_position': y_position,
        'interval': 0.1,
        'variation': 60,
        'check_interval': 3,
        'lower_threshold_min': 900,
        'lower_threshold_max': 1100,
        'upper_threshold_min': 1400,
        'upper_threshold_max': 1600,
        'screenshot_region': ','.join(map(str, region))
    }

    with open('config.ini', 'w') as configfile:
        config.write(configfile)
    print("'config.ini' konfiguratsiya fayli yaratildi.")

if __name__ == "__main__":
    print("Bosish nuqtasini aniqlash...")
    x_position, y_position = get_mouse_position_on_click()

    print("\nEndi matnni aniqlash maydonini sozlang...")
    print("Aniqlash maydonini yuqori chap burchagini bosing.")
    top_left_x, top_left_y = get_mouse_position_on_click()
    print("Aniqlash maydonini pastki o'ng burchagini bosing.")
    bottom_right_x, bottom_right_y = get_mouse_position_on_click()

    width = abs(bottom_right_x - top_left_x)
    height = abs(bottom_right_y - top_left_y)
    left = min(top_left_x, bottom_right_x)
    top = min(top_left_y, bottom_right_y)
    region = (left, top, width, height)

    print(f"Kalibrovka qilingan maydon: {region}")
    generate_config_file(x_position, y_position, region)

    print("\nSkriptni to'xtatish uchun 'Ctrl + C' tugmalarini bosing.")
    try:
        while True:
            capture_and_show_region(region)
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nSkript foydalanuvchi tomonidan to'xtatildi.")
        cv2.destroyAllWindows()
