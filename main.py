import time
import os
import pyautogui
import pyperclip
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
            bbox = (1600, 396, 230, 432)
            img = capture_region(bbox)
            img.save(out_dir+"/fname.png")
            # image_bytes_io = io.BytesIO()
            # img.save(image_bytes_io, format='jpeg')
            # image_bytes = image_bytes_io.getvalue()
            # response = client.models.generate_content(
            #     model='gemini-2.5-flash',
            #     contents=[
            #         types.Part.from_bytes(
            #             data=image_bytes,
            #             mime_type='image/jpeg',
            #         ),
            #         '검이나 몽둥이는 1강에 "팔아"라고 해주고. 아니면 10강 이상이면 "팔아"라고 해줘. 그 외에는 "강화"하라고 해줘.'
            #     ]
            # )
            # text = response.text
            # print(f'OCR 결과 [{idx}]:', repr(text))
            # if '팔아' in  text:
            #     pyautogui.press('/')
            #     pyperclip.copy('판매')
            #     pyautogui.hotkey('ctrl', 'v')
            # else:
            #     pyautogui.press('/')
            #     pyperclip.copy('강화')
            #     pyautogui.hotkey('ctrl', 'v')

            # text = ocr_text_from_image(img)
            # text = ocr_data_from_image(img)
            try:
                box1 = pyautogui.locateOnScreen('new/1.png', region=bbox)
            except pyautogui.ImageNotFoundException:
                box1 = None
            try:
                box2 = pyautogui.locateOnScreen('new/2.png', region=bbox)
            except pyautogui.ImageNotFoundException:
                box2 = None
            try:
                box3 = pyautogui.locateOnScreen('new/44.png', region=bbox)
            except pyautogui.ImageNotFoundException:
                box3 = None
            text = ocr_text_from_image(img)
            print('낡은검 결과:', repr(box1))
            print('낡은몽둥이 결과:', repr(box2))
            print('파괴 결과:', repr(box3))
            print('텍스트 결과:', text)
            if (box1 is not None) or (box2 is not None) or (box3 is not None):
                print('바로 판매 진행')
                pyautogui.press('/')
                pyperclip.copy('강화')
                pyautogui.hotkey('ctrl', 'v')
                time.sleep(0.5)
                pyautogui.press('enter')
                pyautogui.press('enter')
                time.sleep(3)
                pyautogui.press('/')
                pyperclip.copy('판매')
                pyautogui.hotkey('ctrl', 'v')
                time.sleep(0.5)
                pyautogui.press('enter')
                pyautogui.press('enter')
            elif ('[+15]' in text or '[+16]' in  text or '[+17]' in  text):
                print('강화 판매 진행')
                pyautogui.press('/')
                pyperclip.copy('판매')
                pyautogui.hotkey('ctrl', 'v')
                time.sleep(0.5)
                pyautogui.press('enter')
                pyautogui.press('enter')
                time.sleep(3)
                pyautogui.press('/')
                pyperclip.copy('판매')
                pyautogui.hotkey('ctrl', 'v')
            else:
                print('강화 진행')
                pyautogui.press('/')
                pyperclip.copy('강화')
                pyautogui.hotkey('ctrl', 'v')

            #감지 시 캡처 저장 후 즉시 종료
            # text = ocr_text_from_image(img)
            # print(f'OCR 결과 [{idx}]:', repr(text))
            # if '[+14]' in text or '[+15]' in  text or '[+16]' in  text:
            #     if activate:
            #         print('pause')
            #         activate = False
            # elif '111111' in  text:
            #     print('pause')
            #     activate = False
            # elif '222222' in  text:
            #     print('restart')
            #     activate = True
            # else:
            #     pyautogui.press('/')
            #     pyperclip.copy('강화')
            #     pyautogui.hotkey('ctrl', 'v')

            time.sleep(0.5)
            pyautogui.press('enter')
            pyautogui.press('enter')

            time.sleep(3)
            idx += 1
    except KeyboardInterrupt:
        print('사용자에 의해 중단됨')

if __name__ == '__main__':
    main()
