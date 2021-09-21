# XOR and NOT OR
# 0 -- OFF 1-- ON
import cv2 as cv
import numpy as np

blank=np.zeros((400,400),dtype='uint8')
rec=cv.rectangle(blank.copy(),(30,30),(370,370),255,-1)
cir=cv.circle(blank.copy(),(200,200),200,255,-1)
cv.imshow("Reactangle",rec)
cv.imshow("Circle",cir)
cv.waitKey(0)

# Bitwise AND --> intersecting
bit_and=cv.bitwise_and(rec,cir)
cv.imshow("Bitwise AND",bit_and)
cv.waitKey(0)

# Bitwise OR -->inter and non
bit_or=cv.bitwise_or(rec,cir)
cv.imshow("Bitwise OR",bit_or)
cv.waitKey(0)

# Bitwise XOR -->Non
bit_xor=cv.bitwise_xor(rec,cir)
cv.imshow("Bitwise XOR",bit_xor)
cv.waitKey(0)

# Bitwise NOt
bit_not=cv.bitwise_not(rec)
cv.imshow("Bitwise NOT",bit_not)
cv.waitKey(0)
