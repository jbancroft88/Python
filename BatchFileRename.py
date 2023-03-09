import pandas as pd
import subprocess
from tkinter import filedialog

#----Import Excel Data

xlsxfile = "\\\\Server\\Folder\\filename.xlsx"
data = pd.read_excel(xlsxfile)
oldnames = (data['OLD'].values.tolist())
newnames = (data['NEW'].values.tolist())
index = (data['INDEX'].values.tolist())

#----Variables

extension = ".jpg"
path_pre = filedialog.askdirectory()
path = str(path_pre).replace('/','\\')

#----Iterator/RenamingEngine

for count in index:
    old = oldnames[count]
    if type(old) == float:
        old = str(old).rstrip('0').rstrip('.')
    new = newnames[count]
    if type(new) == float:
        new = str(new).rstrip('0').rstrip('.')
    renamer = f'ren "{path}\{old}{extension}" "{new}{extension}"'
    if "nan.jpg" in renamer:
        break
    print(renamer)
    subprocess.call(renamer, shell=True)






