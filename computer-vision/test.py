import cv2

print(cv2.__version__)

def checkCamera():
    for i in range(4):
        cap_x = cv2.VideoCapture(i, cv2.CAP_AVFOUNDATION)

        if not cap_x.isOpened():
            print("\x1b[95mCamera not found at index:", i, "\x1b[0m")
        else:
            print("\x1b[92mCamera found at index:", i, "\x1b[0m")

        cap_x.release()

checkCamera()

cap = cv2.VideoCapture(0, cv2.CAP_AVFOUNDATION)

purple = "\x1b[95m"
highlight_end = "\x1b[0m"

while True:
    ret, frame = cap.read()

    if not ret:
        print(purple+"Failed to grab frame"+highlight_end)
        break
    cv2.imshow("frame", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
