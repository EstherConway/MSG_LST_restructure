
import os, shutil

src = "/group_workspaces/cems2/prise/LSASAF/MSG/2018"

for dirpath, dirs, files in os.walk(src):
    for file in files:
        if not file.endswith('.part'):
            filedate = file.split("_")[5]
            print filedate
            fileday = filedate[6:8]
            print fileday
            filemonth = filedate[4:6]
            print filemonth
            newDir = os.path.join(src,filemonth,fileday)
            print newDir
            if (not os.path.exists(newDir)):
                os.mkdir(newDir)
                print 'does not exist'

            shutil.move(os.path.join(dirpath, file), newDir)
