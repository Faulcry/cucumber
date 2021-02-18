import sys
import pickle
from pathlib import Path
import json

def jpickle(path):
    filetopickle = path
    filename= Path(filetopickle).stem
    with open(filetopickle, "r") as rfile:
        with open(f"{filename}.bin", "wb") as sfile:
            content = json.load(rfile)
            pickle.dump(content, sfile)

def junpickle(path):
    filetounpickle = path
    filename= Path(filetounpickle).stem
    with open(filetounpickle, "rb") as rfile:
        with open(f"{filename}.json", "w") as sfile:
            content = pickle.load(rfile)
            json.dump(content, sfile)
    

