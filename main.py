from pathlib import Path
import tkinter.filedialog as fd
print("\n==============================")
print("       SENTINEL v0.1")
print("==============================")
file_path=fd.askopenfilename(initialdir="C:/Users",title="Select a File")
if file_path:
   print("✅File selected")
   file_path_obj=Path(file_path)

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
else:
   print("❎No file selected")
