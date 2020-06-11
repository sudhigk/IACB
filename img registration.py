import cv2
import numpy as np
im1 = cv2.imread('images/monkeys.jpg')
im2 = cv2.imread('images/monkey 1.jpeg')
img1 = cv2.cvtColor(im1,cv2.COLOR_BGR2GRAY)
img2 = cv2.cvtColor(im2,cv2.COLOR_BGR2GRAY)

orb = cv2.ORB_create(50)
kp1, des1 = orb.detectAndCompute(img1,None)
kp2, des2 = orb.detectAndCompute(img2,None)
matcher = cv2.DescriptorMatcher_create(cv2.DESCRIPTOR_MATCHER_BRUTEFORCE_HAMMING)
matches = matcher.match(des1,des2,None)
matches = sorted(matches,key=lambda x:x.distance)
img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10],None)
cv2.imshow("matches",img3)
cv2.waitKey(0)

