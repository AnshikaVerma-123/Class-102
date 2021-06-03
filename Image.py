import cv2 
import dropbox
import time
import random
start_time= time.time()
def take_snapshot():
    number = random.randint(0,100)
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while (result):
        ret,frame = videoCaptureObject.read()
        img_name = "img" + str(number) + ".png"
        cv2.imwrite("newPicture1.jpg", frame)
        result = False
    return img_name
    print("Snap Shot taken")
    videoCaptureObject.release()
    cv2.destroyAllWindows()
take_snapshot()
def upload_file (img_name):
    access_token = ""
    file = img_counter
    file_from = file
    file_to = "/newFolder1/" + (img_name)
    dbx = dropbox.Dropbox (access_token)
    with open (file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to, mode= dropbox.files.WriteMode.overwrite)
        print("File Upload It")
def main():
    while(True):
        if((time.time()- start_time)>=300):
            name= take_snapshot()
            upload_file(name)
main()