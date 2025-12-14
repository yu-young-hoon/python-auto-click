import time
import sys
import os
import pyautogui
import pyperclip
import win32gui
import win32con
import win32api

def get_kakao_chat_text(chat_room_title):
    """
    카카오톡 채팅방의 핸들을 찾아 모든 텍스트를 가져옵니다.
    """
    try:
        # 디버깅을 위해 발견된 모든 창 제목을 저장할 리스트
        all_windows = []
        hwnd = [0]

        def find_window_callback(h, p):
            window_text = win32gui.GetWindowText(h)
            if window_text: # 비어있지 않은 제목만 처리
                all_windows.append(window_text) # 디버깅용: 모든 창 제목 추가
                # 대소문자 구분 없이 비교
                if chat_room_title.lower() in window_text.lower():
                    # 창을 찾았으면 hwnd[0]에 저장하고 열거를 중단합니다.
                    hwnd[0] = h
                    return False
            return True

        win32gui.EnumWindows(find_window_callback, None)
        hwnd = hwnd[0]

        if hwnd == 0:
            # 창을 찾지 못했을 경우, 디버깅을 위해 찾은 모든 창 제목을 출력합니다.
            print("\n[디버그] 지정된 창을 찾지 못했습니다. 현재 열려있는 창 목록:")
            if all_windows:
                for title in sorted(all_windows): # 가나다순으로 정렬하여 출력
                    print(f"- {title}")
            else:
                print("[디버그] 활성 창 제목을 하나도 찾지 못했습니다. (관리자 권한으로 실행해 보세요)")
            print("[디버그] 목록 끝.")
            return None

        hwnd_main = win32gui.FindWindowEx(hwnd, None, "EVA_Window_Dblclk", None)
        if hwnd_main == 0:
            return None
        hwnd_edit = win32gui.FindWindowEx(hwnd_main, None, "EVA_RICHEDIT20W", None)
        if hwnd_edit == 0:
            return None

        text_len = win32api.SendMessage(hwnd_edit, win32con.WM_GETTEXTLENGTH, 0, 0)
        if text_len == 0:
            return ""

        buffer = win32gui.PyMakeBuffer(text_len + 1)
        win32api.SendMessage(hwnd_edit, win32con.WM_GETTEXT, text_len + 1, buffer)

        return buffer.tobytes().decode('utf-16', errors='ignore')
    except Exception as e:
        print(f"Error getting text: {e}")
        return None

def main():
    # TODO: 여기에 실제 카카오톡 채팅방의 정확한 제목을 입력하세요.
    chat_room_title = "검키우기"
    last_text = ""
    window_found_message_printed = False

    try:
        print(f"'{chat_room_title}' 채팅방 모니터링 시작... (Ctrl+C로 강제종료)")
        while True:
            current_text = get_kakao_chat_text(chat_room_title)

            if current_text is None:
                if not window_found_message_printed:
                    # 창을 찾지 못했다는 메시지와 디버그 목록이 지워지지 않도록 한 번만 출력합니다.
                    # get_kakao_chat_text 함수에서 디버그 목록을 먼저 출력합니다.
                    print(f"\n'{chat_room_title}' 창을 찾는 중...", end='')
                    window_found_message_printed = True
                else:
                    # 계속 찾고 있다는 것을 점으로 표시
                    print('.', end='')
                time.sleep(2)
                continue

            window_found_message_printed = False # 창을 찾았으므로 플래그 리셋

            if current_text == last_text:
                time.sleep(1) # 새 메시지가 없으면 잠시 대기
                continue

            new_text = current_text[len(last_text):].strip()
            last_text = current_text

            if not new_text:
                continue

            print(f"\n새 메시지: {new_text}")

            if ('낡은' in new_text or '몽둥' in new_text or '몽덩' in new_text or '몽동' in new_text or '남은' in new_text):
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
                time.sleep(3)
            else:
                if '[+10]' in new_text or '[+11]' in new_text or '[+12]' in new_text:
                    print('강화 판매 진행')
                    pyautogui.press('/')
                    pyperclip.copy('판매')
                    pyautogui.hotkey('ctrl', 'v')
                else:
                    print('강화 진행')
                    pyautogui.press('/')
                    pyperclip.copy('강화')
                    pyautogui.hotkey('ctrl', 'v')

                time.sleep(0.5)
                pyautogui.press('enter')
                pyautogui.press('enter')
                time.sleep(3)

    except KeyboardInterrupt:
        print('사용자에 의해 중단됨')

if __name__ == '__main__':
    main()
