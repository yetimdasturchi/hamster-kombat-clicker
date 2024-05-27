import pyautogui
import time
import keyboard
import os
import random
import cv2
import pytesseract
import numpy as np
import re
import configparser

def get_counter_from_screen(region):
    screenshot = pyautogui.screenshot(region=region)
    screenshot_np = np.array(screenshot)
    gray_image = cv2.cvtColor(screenshot_np, cv2.COLOR_BGR2GRAY)
    
    _, thresholded_image = cv2.threshold(gray_image, 150, 255, cv2.THRESH_BINARY_INV)
    
    cv2.imshow("Chegarani aniqlash", thresholded_image)
    cv2.waitKey(500)
    cv2.destroyAllWindows()
    
    text = pytesseract.image_to_string(thresholded_image, config='--psm 7')
    print(f"Aniqlangan matn: {text.strip()}")
    
    match = re.search(r'(\d+)\s*/\s*\d+', text)
    if match:
        current_value = int(match.group(1))
    else:
        current_value = 0
    
    return current_value

def multiple_clicks(x, y, interval_between_clicks, variation=60, check_interval=3, lower_threshold_min=900, lower_threshold_max=1100, upper_threshold_min=1400, upper_threshold_max=1600, region=(3890, 1030, 100, 50)):
    time_since_last_check = time.time()

    try:
        while True:
            lower_threshold = random.randint(lower_threshold_min, lower_threshold_max)
            upper_threshold = random.randint(upper_threshold_min, upper_threshold_max)
            print(f"Ballar uchun pastki chegara: {lower_threshold}, Ballar uchun yuqori chegara: {upper_threshold}")

            while True:
                if time.time() - time_since_last_check >= check_interval:
                    current_value = get_counter_from_screen(region)
                    print(f"Joriy hisoblagich: {current_value}")

                    if current_value < lower_threshold:
                        print(f"Hisoblagich {lower_threshold} dan pastda. {upper_threshold} ga yetguncha bosishlar toʻxtatilmoqda...")
                        while current_value < upper_threshold:
                            current_value = get_counter_from_screen(region)
                            print(f"Joriy hisoblagich: {current_value}")
                            if keyboard.is_pressed('esc'):
                                print("\nSkript foydalanuvchi tomonidan to'xtatildi.")
                                return
                            time.sleep(check_interval)
                        break

                    time_since_last_check = time.time()

                dynamic_x = x + random.randint(-variation, variation)
                dynamic_y = y + random.randint(-variation, variation)
                pyautogui.click(x=dynamic_x, y=dynamic_y)
                print(f'Bosishni amalga oshirish: ({dynamic_x}, {dynamic_y})')

                if keyboard.is_pressed('esc'):
                    print("\nSkript foydalanuvchi tomonidan to'xtatildi.")
                    return

                time.sleep(interval_between_clicks)

    except KeyboardInterrupt:
        print("\nSkript foydalanuvchi tomonidan to'xtatildi.")

if __name__ == "__main__":
    if os.geteuid() != 0:
        print("Ushbu skript root foydalanuvchi nomidan ishga tushirilishi kerak.")
        exit(1)

    config = configparser.ConfigParser()
    config.read('config.ini')

    x_position = int(config['settings']['x_position'])
    y_position = int(config['settings']['y_position'])
    interval = float(config['settings']['interval'])
    variation = int(config['settings']['variation'])
    check_interval = int(config['settings']['check_interval'])
    lower_threshold_min = int(config['settings']['lower_threshold_min'])
    lower_threshold_max = int(config['settings']['lower_threshold_max'])
    upper_threshold_min = int(config['settings']['upper_threshold_min'])
    upper_threshold_max = int(config['settings']['upper_threshold_max'])
    screenshot_region = tuple(map(int, config['settings']['screenshot_region'].split(',')))

    print("To'xtatish uchun 'Esc' tugmasini bosing.")
    multiple_clicks(x_position, y_position, interval, variation, check_interval, lower_threshold_min, lower_threshold_max, upper_threshold_min, upper_threshold_max, screenshot_region)
