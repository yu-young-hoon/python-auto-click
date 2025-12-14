import pytesseract
from PIL import Image, ImageOps, ImageFilter
import re
import pandas as pd
from io import StringIO

# Windows 사용자의 경우 Tesseract 실행파일 경로를 설정하세요.
# 기본값을 비워두면 시스템 PATH에서 찾습니다. 필요시 경로를 수정하세요.
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def preprocess_image(image):
    """간단한 전처리: 흑백 변환, 대비 강화, 필터적용"""
    gray = ImageOps.grayscale(image)
    # 소형 이미지의 경우 리사이즈하여 OCR 정확도를 올릴 수 있음
    w, h = gray.size
    if w < 300:
        gray = gray.resize((int(w * 2), int(h * 2)), Image.LANCZOS)
    # 잡음 제거
    gray = gray.filter(ImageFilter.MedianFilter())
    # 대비 향상(선택적)
    # 이진화 (한글 인식률 저하의 원인이 될 수 있어 주석 처리)
    # gray = gray.point(lambda x: 0 if x < 150 else 255, '1')
    return gray


def ocr_text_from_image(image):
    """이미지에서 텍스트 추출 후 정규화하여 반환"""
    # img = preprocess_image(image)
    # digits 옵션을 사용하여 숫자 인식에 최적화
    try:
        text = pytesseract.image_to_string(image, config='--psm 6 -c tessedit_char_whitelist=『』[]+0123456789')
    except Exception:
        # 실패하면 기본 옵션으로 재시도
        text = pytesseract.image_to_string(image)
    # 정규화: 모든 공백과 줄바꿈 제거
    text = re.sub(r"\s+", "", text)
    return text

def ocr_data_from_image(image):
    # img = preprocess_image(image)
    """이미지에서 텍스트 추출 후 정규화하여 반환"""
    try:
        text = pytesseract.image_to_string(image, lang='kor', config='--psm 6')
    except Exception:
        # 실패하면 기본 옵션으로 재시도
        text = pytesseract.image_to_string(image)
    # 정규화: 모든 공백과 줄바꿈 제거
    # text = re.sub(r"\s+", "", text)
    return text
