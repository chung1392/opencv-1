import cv2 as cv

#img = cv.imread('Photos\cat_large2.jpg')    
#cv.imshow('Cat', img)   

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimenstions = (width,height)

    return cv.resize(frame, dimenstions, interpolations=cv.INTER_AREA)

# Reading Videos

capture = cv.VideoCapture('Videos/dog.mp4')

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame)

    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'): # 20 times to end or press key "D" to break
       break

capture.release()
cv.destroyAllWindows() 

