import linedraw
import cv2
import os
import sys


def write_images(video_path,image_path):
    vidcap = cv2.VideoCapture(video_path)
    def getFrame(sec):
        vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
        hasFrames,image = vidcap.read()
        if hasFrames:
            cv2.imwrite(image_path+"/"+"image"+str(count)+".jpg", image)     # save frame as JPG file
        return hasFrames
    sec = 0
    frameRate = 0.5 #//it will capture image in each 0.5 second
    count=1
    success = getFrame(sec)
    while success:
        count = count + 1
        sec = sec + frameRate
        sec = round(sec, 2)
        success = getFrame(sec)




def visualize_images_online(image_path):


    import turtle
    import time
    wn = turtle.Screen()
    t = turtle.Turtle()
    y = turtle.Turtle()
    t.speed('fastest')
    y.speed('fastest')
    turtle.tracer(False)
    t.pencolor('black')
    t.pd()
    y.pd()
    for j in range(1, len(os.listdir(image_path))):
        lines = linedraw.sketch(image_path + "image"+str(j)+".jpg")
        for i in range(0,len(lines)):
            for p in lines[i]:
                t.goto(p[0]*640/1024-320, -(p[1]*640/1024-320))
                t.pencolor('black')
            t.pencolor('black')
        print("Drew image "+ str(j))
        turtle.tracer(True)
        t , y = y , t 
        t.clear()
        turtle.tracer(False)



if __name__ == '__main__':
    VIDEO_LINK=sys.argv[1]

    folder_path = VIDEO_LINK[-8:]
    
    if not os.path.exists(folder_path):
        os.system("mkdir -p " + folder_path+ "/images")
    
    os.system("youtube-dl -f 'bestvideo[ext=mp4]/mp4' --output "+ folder_path  + "/video.mp4  "+VIDEO_LINK)
    print("Done youtube-dl")
    print("Converting video to JPEGs...") 
    write_images(folder_path + "/video.mp4",folder_path+ "/images")
    print("Done images writing..")
    visualize_images_online(folder_path+"/images/")
      
    
