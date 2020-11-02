import zipfile



filelist = []

user = getpass.getuser()
location = "C:/Users/" + user + "/Desktop"



def ZipFile(filelist):
    with zipfile.ZipFile(location/ZipName(), w) as zip_file:
        for file in filelist:
            zip_file.write(file)
        zip_file.close()

def ZipName():
    zipName = input("Zip Name?: ")
    return zipName


def FileUpload(filename): # 목적지로 파일 업로드 할 때
    try:
        print("File : " + filelist + "Upload Start")

    except:
        pass
    pass

def FileDownload(filename): # 출발지에서 파일 다운로드 받을때
    try:
        print("File : " + filelist + "Download Start")
        pass
    except:
        pass
    pass
