import os

def make_files(path):
    try:
        os.mkdir(path)
    except Exception:
        return False
    
    return True