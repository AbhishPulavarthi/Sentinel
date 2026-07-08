from pathlib import Path
import tkinter.filedialog as fd
import hashlib
from datetime import datetime

print("\n==============================")
print("       SENTINEL v0.3")
print("==============================")
file_path=fd.askopenfilename(initialdir="C:/Users",title="Select a File")
if file_path:
   print("✅File selected")
   file_path_obj=Path(file_path)
   with open (file_path_obj,"rb") as file_object:
      file_byte=file_object.read()
   
   print(f"File name      : {file_path_obj.name}")
   print(f"File Type      : {file_path_obj.suffix}")
   print(f"File Name Only : {file_path_obj.stem}")
#File size section
   print("File Size")
   print("------------")
   file_stat=file_path_obj.stat()
   file_Size=file_stat.st_size
   kb=file_Size/1024
   mb=kb/1024
   print(f"{file_Size:.2f} bytes")
   print(f"{kb:.2f} KB")
   print(f"{mb:.2f} MB")
#File Time Section
   file_LA=file_stat.st_atime
   file_LM=file_stat.st_mtime
   file_CT=file_stat.st_birthtime

   dt_object_LA = datetime.fromtimestamp(file_LA)
   text_format_LA = dt_object_LA.strftime("%B %d, %Y at %I:%M %p")
   dt_object_LM = datetime.fromtimestamp(file_LM)
   text_format_LM = dt_object_LM.strftime("%B %d, %Y at %I:%M %p")
   dt_object_CT = datetime.fromtimestamp(file_CT)
   text_format_CT = dt_object_CT.strftime("%B %d, %Y at %I:%M %p")
   print("\nFile Timestamps")
   print("----------------")
   print(f"Creation Time    : {text_format_CT}")
   print(f"Last Modified    : {text_format_LM}")
   print(f"Last Accessed    : {text_format_LA}")
#Hash section
   print("\nHashes")
   print("------------")
   file_sha=hashlib.sha256(file_byte)
   file_md5=hashlib.md5(file_byte)

   print(f"SHA-256 : {file_sha.hexdigest()}")
   print(f"MD5      : {file_md5.hexdigest()}")
else:
   print("❎No file selected")