import numpy as np
import cv2
import time

#cap = cv2.VideoCapture('P2F1P2.mp4')
#cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture('C:/Users/liche/Desktop/Video Analysis/P1_F3.mp4')

while(1):
    # Process frame
    ret, org_frame = cap.read()
    #frame = org_frame
    frame= org_frame[10:1500, 100:700]

    #Apply Blurring
    blur = cv2.GaussianBlur(frame, (5,5), 0)

    #Change to grayscale
    gray = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)

    #filter out white
    mask = cv2.inRange(gray, 245, 255)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)

    #filter out black
    mask2 = cv2.inRange(gray, 0, 20)
    #mask2 = cv2.erode(mask2, None, iterations=2)
    #mask2 = cv2.dilate(mask2, None, iterations=2)

    #Change to hsv
    hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)

    #Extract edges 
    edges = cv2.Canny(mask, 20, 50)
    edges2 = cv2.Canny(mask2, 20 ,50)
    lines = cv2.HoughLinesP(edges, 1, np.pi/180, 40, minLineLength=150, maxLineGap=40)
    
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)

    cv2.imshow("gray",gray)
    #cv2.imshow("edges2",edges2)
    cv2.imshow("edges", edges)
    cv2.imshow("frame", frame)
    time.sleep(0.01)
    key = cv2.waitKey(1)
    if key == 27:
        break
cap.release()
cv2.destroyAllWindows()