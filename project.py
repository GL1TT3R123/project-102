import os
import shutil
from_dir= "C:/Users/user/Downloads"
to_dir= "C:/Users/user/Downloads/test"

list_of_files = os.listdir(from_dir)

for i in list_of_files:
    name,extension = os.path.splitext(i)

    if extension =="":
        continue
    
    if extension in [".txt",".doc",".docx",".pdf"]:
        path1= from_dir+"/"+i
        path2= to_dir+"/"+"documentFolder"
        path3= to_dir+"/"+"documentFolder"+i

        if os.path.exists(path2):
          print(f"moving {i} ...")
          shutil.move(path1,path3)

        else: 
            os.makedirs(path2)
            print(f"moving {i} ...")
            shutil.move(path1,path3)



