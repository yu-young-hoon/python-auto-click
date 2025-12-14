from pynput import mouse
import pyautogui

_selected_bbox = None

class RegionSelector:
    """마우스 드래그로 영역(bbox)을 선택합니다. 사용 예:
    selector = RegionSelector(); bbox = selector.select()
    bbox = (left, top, width, height)
    """
    def __init__(self):
        self.start = None
        self.end = None
        self._done = False

    def _on_click(self, x, y, button, pressed):
        # left 버튼 눌림/놓임 감지 - 안전한 비교로 변경
        if button != mouse.Button.left:
            return
        if pressed:
            self.start = (int(x), int(y))
        else:
            self.end = (int(x), int(y))
            self._done = True
            return False

    def select(self):
        """사용자가 마우스로 드래그하면 bbox 반환 (left, top, width, height)"""
        print('왼쪽 버튼으로 드래그하여 영역을 선택하세요...')
        with mouse.Listener(on_click=self._on_click) as listener:
            listener.join()

        if not self.start or not self.end:
            raise RuntimeError('영역 선택 실패')

        left = min(self.start[0], self.end[0])
        top = min(self.start[1], self.end[1])
        right = max(self.start[0], self.end[0])
        bottom = max(self.start[1], self.end[1])
        width = right - left
        height = bottom - top
        return (left, top, width, height)


def capture_region(bbox):
    """bbox = (left, top, width, height). 반환값: PIL.Image"""
    left, top, w, h = bbox
    img = pyautogui.screenshot(region=(left, top, w, h))
    return img
