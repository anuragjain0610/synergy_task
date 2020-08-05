# import the opencv module
import cv2

# create a capture object(file pointer) by loading the given video 
# video file downloaded from [https://drive.google.com/file/d/1il2yWyr7-t9XfG1nDVL7QlfmnmNDf_9I/view?usp=sharing]
cap = cv2.VideoCapture('cut.mp4')

# initializing the initial values to Average of RGB Channel variables 
# and no. of frames processed variable 
R_Avg, G_Avg, B_Avg = None, None, None
frames_processed = 0

# while loop to read each frame one by one and calculating the running average 
while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Splititng the current frame into respective channels and converting them to float
    (B, G, R) = cv2.split(frame.astype("float"))

    # if the frame averages are None, initialize them
    if R_Avg is None or B_Avg is None or G_Avg is None:
        R_Avg = R
        B_Avg = B
        G_Avg = G

    # otherwise, compute the average between the average_of_previous_frames and the current_frame
    else:
        R_Avg = ((frames_processed * R_Avg) + R) / (frames_processed + 1.0)
        G_Avg = ((frames_processed * G_Avg) + G) / (frames_processed + 1.0)
        B_Avg = ((frames_processed * B_Avg) + B) / (frames_processed + 1.0)

    # increment the total number of frames processed so far
    frames_processed += 1


print('Total No. of frames processed: ', frames_processed)
avg_result = cv2.merge([B_Avg, G_Avg, R_Avg]).astype("uint8")
cv2.imwrite('output.jpg', avg_result)

# releasing the file pointer
cap.release()

# References
# Long exposure with OpenCV and Python (https://www.pyimagesearch.com/2017/08/14/long-exposure-with-opencv-and-python/#:~:text=The%20averaging%20computation%20is%20quite,this%20is%20a%20fresh%20frame)
# OpenCV Python Documentaion (https://opencv-python-tutroals.readthedocs.io/en/latest/index.html)
