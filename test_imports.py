import importlib
mods = ['pyautogui', 'pynput', 'PIL', 'pytesseract']
for m in mods:
    try:
        importlib.import_module(m)
        print(m + ' ok')
    except Exception as e:
        print('ERR', m, type(e).__name__, e)

