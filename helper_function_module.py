#查找病例ID
def find_ID(texts):
    ID = next((texts[i + 1] for i, item in enumerate(texts) if 'ID号：' in item and i + 1 < len(texts)), None) #查找ID号，通常在ID号后面
    return ID