Python 화면 캡처 + OCR로 '17' 감지 시 멈춤

요약
- 마우스 드래그로 영역을 지정합니다.
- 주기적으로 해당 영역을 캡처하여 OCR(pytesseract)로 텍스트를 읽습니다.
- 텍스트에 '17'이 포함되면 프로그램을 즉시 종료합니다.

설치
1. Python 3.8+ 설치
2. Tesseract-OCR 설치 (Windows): https://github.com/tesseract-ocr/tesseract
   설치 후 환경 변수 PATH에 tesseract.exe 경로를 추가하거나, 실행 시 pytesseract.pytesseract.tesseract_cmd를 설정하세요.
3. 의존성 설치:

```powershell
python -m pip install -r requirements.txt
```

사용법
1. `main.py` 실행
2. 프로그램이 실행되면 마우스로 영역을 드래그하여 캡처 영역을 지정
3. 지정 후 OCR이 주기적으로 실행됩니다n4. '17'이 감지되면 프로그램이 종료됩니다

주의
- OCR 정확도는 해상도와 폰트에 따라 달라집니다. 필요하면 이미지 전처리를 조정하세요.