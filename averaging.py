import cv2

cap = cv2.VideoCapture('cut.mp4')

(rAvg, gAvg, bAvg) = (None, None, None)
total = 0


while True:
    ret, frame = cap.read()

    if not ret:
        break

    (B, G, R) = cv2.split(frame.astype("float"))

    # if the frame averages are None, initialize them
    if rAvg is None:
        rAvg = R
        bAvg = B
        gAvg = G
        # otherwise, compute the weighted average between the history of
        # frames and the current frames
    else:
        rAvg = ((total * rAvg) + (1 * R)) / (total + 1.0)
        gAvg = ((total * gAvg) + (1 * G)) / (total + 1.0)
        bAvg = ((total * bAvg) + (1 * B)) / (total + 1.0)
        # increment the total number of frames read thus far
    total += 1

print(total)
avg = cv2.merge([bAvg, gAvg, rAvg]).astype("uint8")
cv2.imwrite('output.jpg', avg)
# do a bit of cleanup on the file pointer
cap.release()
