import cv2

img = cv2.imread('../images/00-puppy.jpg')

while True:
    cv2.imshow('Puppy', img)

    # If waited at least 1 ms and pressed esc (27)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()
