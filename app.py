from pathlib import Path
import os

# initialization of project
print("-- APP INITIALIZATION COMPLETED --")


def READ_FILESFOLDERS():
    path = Path("")
    for i, v in enumerate(path.rglob("*")):
        print(f"{i+1}. {v}")
    print("-- TOTAL FILE FOLDER PRESENT --")


while True:
    try:
        print(
            "1. CREATE FOLDER\n2. UPDATE FOLDER NAME\n3. READ ALL FOLDERS\n4. DELETE FOLDER")
        print(
            "5. CREATE FILE\n6. UPDATE FILE\n7. READ ALL FILES\n8. DELETE FILE\n0. EXIT APP")
        n = int(input("Choose option: "))
        if n == 1:
            pathdir = input("enter directory/path name: ")
            path = Path(pathdir)
            path.mkdir(exist_ok=False)
            print("-- FOLDER CREATED SUCCESSFULLY --")
        elif n == 2:
            pathdir = input("enter directory/path name: ")
            path = Path(pathdir)
            path.rename(input("ENTER UPDATED DIRECTORY/NAME: "))
            print("-- FOLDER RENAMED SUCCESSFULLY --")
        elif n == 3:
            READ_FILESFOLDERS()
            print("-- FOLDER READ SUCCESSFULLY --")
        elif n == 4:
            READ_FILESFOLDERS()
            pathdir = input("enter directory/path name to delete folder: ")
            path = Path(pathdir)
            folderdata = list(path.rglob("*"))
            if len(folderdata) > 0:
                for i in folderdata:
                    if i.is_file():
                        os.remove(i)
                    else:
                        i.rmdir()
            path.rmdir()
            print("-- FOLDER DELETED SUCCESSFULLY --")
        if n == 5:
            READ_FILESFOLDERS()
            filepath = input("enter file name/path to create: ")
            with open(filepath, 'w') as c:
                txt = input(
                    "WANT TO WRITE SOMETHING IN FILE ?(press ENTER to skip): ")
                c.write(txt)
            print("-- FILE CREATED SUCCESSFULLY --")
        if n == 6:
            READ_FILESFOLDERS()
            filepath = input("enter file name/path to update: ")
            ask = int(input(
                "1. RENAME FILE\n2. REPLACE FILE DATA\n3. APPEND FILE DATA\nChoose any one:  "))
            if ask == 1:
                os.rename(filepath, input("ENTER NEW FILE NAME/PATH: "))
                print("-- UPDATION SUCCESSFULLY COMPLETED --")
            elif ask == 2:
                with open(filepath, 'r') as fr, open(filepath, 'w') as fw:
                    print("-- FILE DATA >> ", fr.read())
                    fw.write(input(
                        "START WRITING FROM HERE : "))
                print("-- UPDATION SUCCESSFULLY COMPLETED --")
            elif ask == 3:
                with open(filepath, 'r') as fr, open(filepath, 'a') as fw:
                    print("-- FILE DATA >> ", fr.read())
                    fw.write(input(
                        "START WRITING FROM HERE : "))
                print("-- UPDATION SUCCESSFULLY COMPLETED --")
            else:
                print("-- WRONG INPUT -- ")
        elif n == 0:
            print("-- APPLICATION CLOSED --")
            break
    except Exception as err:
        print(err)
