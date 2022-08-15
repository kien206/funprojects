import cv2

# read image
image = cv2.imread("cake.jpg")
# convert image to grey scale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# inverse image to enhance detail
inverted_image = 255 - gray_image
# create the pencil sketch by mixing the grayscale image with the inverted blurry image
# dividing grayscale image by inverted blurry image
blurred = cv2.GaussianBlur(inverted_image, (21,21), 0)
inverted_blurred = 255 - blurred
pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale= 250.0)
# display both original and pencil sketched image
cv2.imshow("Pencil sketch image", pencil_sketch)
cv2.waitKey(0)
