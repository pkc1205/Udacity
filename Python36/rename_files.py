    
import os
import string

def rename_files():
    file_list = os.listdir(r"C:\oop\prank")
    print(file_list)
    saved_path = os.getcwd()
    print("Current Directory is"+saved_path)
    os.chdir(r"C:\oop\prank")
    file_destination_table =  str.maketrans(dict.fromkeys('0123456789'))
    print(file_destination_table)
    for file_name in file_list:
        print("Old Name -"+file_name)
        print("New Name - "+file_name.translate(file_destination_table))
        os.rename(file_name,file_name.translate(file_destination_table ))
    print(file_list)
    os.chdir(saved_path)

rename_files()
    
