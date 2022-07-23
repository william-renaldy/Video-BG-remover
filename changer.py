import os
import cv2
import numpy as np



def change(video_name:str,image_name:str):

    if not os.path.exists(video_name):
        raise FileNotFoundError(f"File named '{video_name}' is not found")
    elif not os.path.exists(image_name):
        raise FileNotFoundError(f"File named '{image_name}' is not found")
    

    video = cv2.VideoCapture(video_name)
    image = cv2.imread(image_name)


    while True:
        ret, frame = video.read()
        
        if ret:

            frame = cv2.resize(frame,(640,480))
            image = cv2.resize(image,(640,480))


            lab = cv2.cvtColor(frame,cv2.COLOR_BGR2LAB)
            a_channel = lab[:,:,1]
            th = cv2.threshold(a_channel,127,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)[1]
            masked = cv2.bitwise_and(frame,frame,mask=th)


            final_frame = np.where(masked==0,image,masked)


            cv2.imshow("Original Video",frame)
            cv2.imshow("Final Video",final_frame)


            if cv2.waitKey(25) == 27:
                break

        else:
            break

    video.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    pass