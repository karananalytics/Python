import csv,os,shutil
import logging as log
LOG_FILENAME = "G:\\PYTHON LEARNINGS\\first_folder\\file.log"
log.basicConfig(filename=LOG_FILENAME,level=log.DEBUG)
#CREATE A NEW FILE IN FOLDER IF NOT EXIXTS AND ADD A DATA TO IT
path = 'G:\\PYTHON LEARNINGS\\first_folder\\test'
if not os.path.exists(path):
    os.mkdir(path)
filename = 'two.csv'
row = ['Name','Age','Salary']
columns = [['Ravi','28','6000'],['Karan','25','5000']]
#TO APPEND
with open(os.path.join(path,filename),'a',newline='') as f:
#TO OVERWRITE A FILE
#with open(os.path.join(path,filename),'w+',newline='') as f:
    writer = csv.writer(f)
    writer.writerow(row)
    writer.writerows(columns)
f.close()
os.getcwd()
#DELETE THE FILE AND FOLDER 
filepath = 'G:\\PYTHON LEARNINGS\\first_folder\\test'
try:
    shutil.rmtree(filepath)
    #os.mkdir(filepath)
except OSError as e:
    print((e.filename,e.strerror))
    log.debug((e.filename,e.strerror))



