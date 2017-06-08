import numpy as np 
import cv2
import PIL

image1 = cv2.imread("1.jpg")
image2 = cv2.imread("2.jpg")

print "Convert the images to double precision and rescale them to stretch from minimum value 0 to maximum value 1."
print "image1 data"
out1 = cv2.normalize(image1.astype("float"), None, 0.0, 1.0, cv2.NORM_MINMAX)
print "image2 data"
out2 = cv2.normalize(image2.astype("float"), None, 0.0, 1.0, cv2.NORM_MINMAX)

print out1
print out2

# image blending
# 70% of image1 and 30% of image2
image3 = cv2.addWeighted(image1, 0.7, image2, 0.3, 0)
print "image3 is a combination of image1 and image2"
out3 = cv2.normalize(image3.astype("float"), None, 0.0, 1.0, cv2.NORM_MINMAX)
# cv2.imshow("image3", image3)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

images = [image1, image2]
images_vert = np.vstack(images)
images_vert = PIL.Image.fromarray(images_vert)
images_vert.save("image3")
