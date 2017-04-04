
#Michael Pu
#2016/10/13
#ICS2O1
#Ms.Strelkovska
#If/Else Exercises C - 9

#Input
fileName = input("Enter a file name: ")

#Calculations
if len(fileName) > 12:
    print("ERROR: Length of File Name Exceeds 12 Characters")
    exit()
else:
    dot = fileName.find(".")
    ext = fileName[dot+1:].lower()
    if ext == "doc":
        fileType = "Microsoft Word Document"
    elif ext == "txt":
        fileType = "Plain Text File"
    elif ext == "rtf":
        fileType = "Rich Text Format File"
    elif ext == "csv":
        fileType = "Comma Separated Values File"
    elif ext == "ppt":
        fileType = "Microsoft PowerPoint Presentation"
    elif ext == "pps":
        fileType = "Microsoft PowerPoint Slide Show"
    elif ext == "mp3":
        fileType = "MP3 Audio File"
    elif ext == "wma":
        fileType = "Windows Media Audio File"
    elif ext == "mp4":
        fileType = "MPEG-4 Video File"
    elif ext == "jpg" or ext == "jpeg":
        fileType = "JPEG Image"
    elif ext == "png":
        fileType = "Portable Network Graphic"
    elif ext == "gif":
        fileType = "Graphical Interchange Format File"
    elif ext == "psd":
        fileType = "Adobe Photoshop Document"
    elif ext == "apk":
        fileType = "Android Package File"
    elif ext == "jar":
        fileType = "Java Archive File"
    elif ext == "exe":
        fileType = "Windows Executable File"
    elif ext == "nes":
        fileType = "Nintendo (NES) ROM File"
    elif ext == "xhtml":
        fileType = "Extensible Hypertext Markup Language File"
    elif ext == "html" or ext == "htm":
        fileType = "Hypertext Markup Language File"
    elif ext == "zip":
        fileType = "Zipped File"
    elif ext == "py":
        fileType = "Python Script"
    elif ext == "crdownload":
        fileType = "Chrome Partially Downloaded File"
    elif ext == "ics":
        fileType = "Calendar File"
    elif ext == "torrent":
        fileType = "BitTorrent File"
    else:
        print ("File Type is Not Supported")
        exit()

#Output
print('The file you entered is a ' + fileType)
