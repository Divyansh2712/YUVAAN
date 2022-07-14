import sign_detector
# trained cascade classifier for each object to detect
# left_cascade = cv2.CascadeClassifier('haar_trained_xml/left/cascade.xml')
# right_cascade = cv2.CascadeClassifier('haar_trained_xml/right/cascade.xml')

# left_signs = sign_detector.classify_signs(image, left_cascade)
#             right_signs = sign_detector.classify_signs(image, right_cascade)
            
#             # draw bounding box to the object detected
#             sign_detector.show_box(image, left_signs)
#             sign_detector.show_box(image, right_signs)
            
#             # check if it is time to turn
#             if len(left_signs) > 0:
#                 x,y,w,h = left_signs[0]
#                 distance = distance_to_camera(8, 50, w)-1
#                 print(distance)
#                 if distance < 5:
#                     car.speed = 100
#                     car.turn_left()
#                     time.sleep(0.6)
#                     car.stop()
#             elif len(right_signs) > 0:
#                 x,y,w,h = right_signs[0]
#                 distance = distance_to_camera(8, 50, w)-1
#                 print(distance)
#                 if distance < 5:
#                     car.speed = 100
#                     car.turn_right()
#                     time.sleep(0.6)
#                     car.stop()

import cv2

cap = cv2.VideoCapture(0)

while cap.isOpened(): # cap.isOpened() returns true if video is successfully been read
    success , img = cap.read()
    if(success):
        # trained cascade classifier for each object to detect
        left_cascade = cv2.CascadeClassifier('haar_trained_xml/left/cascade.xml')
        right_cascade = cv2.CascadeClassifier('haar_trained_xml/right/cascade.xml')

        left_signs = sign_detector.classify_signs(img, left_cascade)
        right_signs = sign_detector.classify_signs(img, right_cascade)

        # draw bounding box to the object detected
        sign_detector.show_box(img, left_signs)
        sign_detector.show_box(img, right_signs)

        if len(left_signs) > 0:
            print("left")
        elif len(right_signs) > 0:
            print("Right")

        cv2.imshow("Output" ,img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        print("Error getting feed")
        break

# after reading is finished it is important to release the cap variable to free up the memory resources
cap.release()
cv2.destroyAllWindows()