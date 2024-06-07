import sys
import ocr_module
import mysql_module
import table_log_module
import image_upload_module

def main():
    img_path = image_upload_module.select_image()
    texts = ocr_module.OCR(img_path) #识别图片并返回识别到的文本
    table_log_module.create_table_log() #创建记录表
    mysql_module.insert(texts,img_path) #插入数据和图片

if __name__ == '__main__':
    main()