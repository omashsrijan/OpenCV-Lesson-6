import cv2
from PIL import Image
import os

#Change directory a per own folder path where images are placed
os.chdir("C:/Users/Srikanth Mashetty/Desktop/OpenCV Lesson 6/Pics")
path="C:/Users/Srikanth Mashetty/Desktop/OpenCV Lesson 6/Pics"

mean_height=0
mean_width=0

#os.listdir('.')-to list files and directories in a current working directory
imgnum=len(os.listdir('.'))
print("Number of Images:", imgnum)

for file in os.listdir('.'):
    img=Image.open(os.path.join(path,file))
    width,height=img.size
    mean_width=mean_width+width
    mean_height=mean_height+height

#avg=sum/imgnum
mean_width=mean_width//imgnum
mean_height=mean_height//imgnum
print("Mean Width: ",mean_width," Mean Height: ",mean_height)

for file in os.listdir('.'):
    img=Image.open(os.path.join(path,file))
    imgsave=img.resize((mean_width,mean_height))
    imgsave.save(file,'JPEG',quality=95)
    print("Image is being resized")

def VideoGenerator():
    video_name="Deez.avi"
    os.chdir("C:/Users/Srikanth Mashetty/Desktop/OpenCV Lesson 6/Pics")
    images=[]
    for file in os.listdir('.'):
        images.append(file)
    #setting frame width and height
    frame=cv2.imread(os.path.join('.',images[0]))
    height,width,layer=frame.shape
    print("Frame shape: ",frame.shape)
    #cv2.VideoWriter(filename,fourcc,fps,frameSize)
    video=cv2.VideoWriter(video_name,0,1,(width,height))
    for image in images:
        video.write(cv2.imread(os.path.join('.',image)))
    cv2.destroyAllWindows
    video.release()
VideoGenerator()