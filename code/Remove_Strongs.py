import os
import re


def Remove_Strongs(Directory):
    for Root, Dirs, Files in os.walk(Directory):
        for File_Name in Files:
            File_Path = os.path.join(Root, File_Name)

            with open(File_Path, "r", encoding="utf-8") as Current_File:
                File_Content = Current_File.read()

                Modified_Content = (
                    File_Content.replace("\w ", "")
                    .replace("|strong=", "")
                    .replace("\w*", "")
                )
                Pattern = r'"[G,H]\d{4}"'
                Modified_Content = re.sub(Pattern, "", Modified_Content)

                with open(File_Path, "w", encoding="utf-8") as Current_File:
                    Current_File.write(Modified_Content)


Current_Directory = os.path.dirname(os.path.abspath(__file__))
Bibles_Directory = os.path.join(Current_Directory, "..", "Bibles")
for Root, Dirs, Files in os.walk(Bibles_Directory):
    for Directory in Dirs:
        Directory_Path = os.path.join(Root, Directory)
        Remove_Strongs(Directory_Path)
