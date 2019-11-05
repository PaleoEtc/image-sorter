#! python3

# picWorkHrSort.py
#
# This program sorts out weekday business hour pics
#
# it identifies image files   from brandon's phone camera
#                           taken during work hours
#       and moves them into a new folder
# 
# example image file name '2012-09-10 11.55.34.jpg'


# import modules
import os, re, datetime, shutil 

# detect the current working directory and print it
path = os.getcwd()
print ('The current working directory is ' + path)


# define the name of the directory to be created
#print("Name of new folder for these work images?")
#input() = newPath
newPath = path + '/workPics' 

try:
    os.mkdir(newPath)
except OSError:
    print ('Creation of the directory ' + newPath + ' failed')
else:
    print ('Successfully created the directory' + newPath)

    #  mkdir() method cannot create sub-directories on a deeper level than one in a single call.
    #  if you want to create multiple directories at once use makedirs()

            
# Create a regex that matches jpg files with my camera's date format
# example image file name '2012-09-10 11.55.34.jpg'

camDateRegex = re.compile(r"""((19|20)\d\d)-((0|1)\d)-((0|1|2|3)\d)(\s)(\d\d)(\.\d\d)(\.\d\d)""", re.VERBOSE)

#example to simplify
#camDateRegex = re.compile(r"""^(.*?) # all text before the date
#    ((19|20)\d\d)-   # four digits for the year
#    (\d\d)-          # 2 digits for the month
#    ((0|1|2|3)\d)    # 2 digits for the day
#    (\.(0|1|2)\d)    # 2 digits for the hour
#    (\.(0|1|2|3|4|5)\d)     # 2 digits for the minute
#    (\.(0|1|2|3|4|5)\d)     # 2 digits for the second
#    (.*?)$ # all text after the date  
#    """, re.VERBOSE)


for camFilename in os.listdir():
    mo = camDateRegex.search(camFilename)
    if mo == None:
#            print(str(mo)+ ' mo is none')
        continue
    yearPart = mo.group(1)
    monthPart = mo.group(3)
    dayPart = mo.group(5)
    hourPart = mo.group(8)
# check group ref numbers
#    print('year '+ yearPart + ' month ' + monthPart + ' day ' + dayPart + ' hour ' + hourPart + '.')
# detect if date is a weekday or weekend
# Return the day of the week as an integer, where Monday is 0 and Sunday is 6.
    weekday = datetime.datetime(int(yearPart),int(monthPart),int(dayPart)).weekday()
#    print('Day of the week is ' + str(weekday) + '. Monday is 0')
    if weekday <= 4:
        workday = True
#        print('This is a workday')
    if weekday >= 5:
        workday = False
#        print('This is a weekend')
    if int(hourPart) > 7 and int(hourPart) < 17:
        bisHrs = True
#        print('This pic was taken during business hours.')

# TODO ++ homework ++ logging module instead of print

    if weekday == True and bisHrs == True:
        print(camFilename)
        
# CAREFUL with move
#        shutil.move(source, destination)
        shutil.move(path + '/' + camFilename, newPath + '/' + camFilename)

            
                             

