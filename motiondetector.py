import cv2, time

first_frame=None


#this triggers video objects to open the camera
video=cv2.VideoCapture(0)


while True:

    #to see 
    check, frame = video.read()
    


    #converting the video frame into a gray image
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray=cv2.GaussianBlur(gray,(21,21),0)

    if first_frame is None:
        first_frame = gray
        continue 
    
    delta_frame=cv2.absdiff(first_frame, gray)
    #thresh hold methods return two values 
    tresh_frame=cv2.threshold(delta_frame, 30, 225, cv2.THRESH_BINARY)[1]
    tresh_frame=cv2.dilate(tresh_frame, None, iterations=2)

   
    #we store contours to store the data
    (cnts,_)  = cv2.findContours(tresh_frame.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


    for contour in cnts: 
        if cv2.contourArea(contour) < 1000:
            continue

        (x, y, w, h)=cv2.boundingRect(contour)
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 3)

    #to see the two data frames
    cv2.imshow("Gray Frame", gray)
    cv2.imshow("Delta Frame", delta_frame)
    cv2.imshow("Threshold Frame", tresh_frame)
    cv2.imshow("Color Frame", frame)

    # The time library holds the release for 3 seconds
    # time.sleep(3)

    #creates a window to show the first frame of the video

    key=cv2.waitKey(1)
    print(gray)
    print(delta_frame)


    if key==ord('q'):
        break

video.release()
cv2.destroyAllWindows