from paddleocr import PaddleOCR


def OCR(img_path): #文字提取
    ocr = PaddleOCR(use_angle_cls=True, lang="ch") 
    result = ocr.ocr(img_path, cls=True)
    texts = [line[1][0] for sublist in result for line in sublist] #提取识别文字
    return texts

