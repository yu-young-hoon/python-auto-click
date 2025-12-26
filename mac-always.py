import time
import os
import pyautogui
import pyperclip
import random
import time
from capture import capture_region
from ocr import ocr_text_from_image

def main():
    out_dir = os.path.join(os.path.dirname(__file__), 'captures')
    os.makedirs(out_dir, exist_ok=True)

    try:
        # print("모니터링 시작 - '19,20' 발견 시 종료합니다. (Ctrl+C로 강제종료)")
        idx = 0
        activate = True
        while True:
            print('------------------------------------')
            print(time.strftime('%c') + ' 강화 진행')
            pyautogui.keyDown('shift')
            pyautogui.press('@')
            pyautogui.keyUp('shift')
            pyperclip.copy('플레이봇')
            pyautogui.hotkey('command', 'v')
            time.sleep(1)
            pyautogui.press('enter')
            pyperclip.copy('강화')
            pyautogui.hotkey('command', 'v')
            pyautogui.press('enter')
            randomtime = 0#(random.random() * 10) % 5
            time.sleep(2+randomtime)
    except KeyboardInterrupt:
        print('사용자에 의해 중단됨')

if __name__ == '__main__':
    main()
