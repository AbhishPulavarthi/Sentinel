from pathlib import Path
import tkinter.filedialog as fd
import hashlib
print("\n==============================")
print("       SENTINEL v0.2")
print("==============================")
file_path=fd.askopenfilename(initialdir="C:/Users",title="Select a File")
if file_path:
   print("✅File selected")
   file_path_obj=Path(file_path)
   file_object=open(file_path_obj,"rb")
   file_byte=file_object.read()

   file_sha=hashlib.sha256(file_byte)
   file_md5=hashlib.md5(file_byte)

   print(f"File name      : {file_path_obj.name}")
   print(f"File Type      : {file_path_obj.suffix}")
   print(f"File Name Only : {file_path_obj.stem}")
   print("Size")
   print("------------")
   file_Size=file_path_obj.stat().st_size
   kb=file_Size/1024
   mb=kb/1024
   print(f"{file_Size:.2f} bytes")
   print(f"{kb:.2f} KB")
   print(f"{mb:.2f} MB")
   print("\nHashes")
   print("------------")
   print(f"SHA-256 : {file_sha.hexdigest()}")
   print(f"MD5      : {file_md5.hexdigest()}")
else:
   print("❎No file selected")