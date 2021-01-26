import cv2
from random import randrange
# load some pre-trained data on face frontals from opencv(haar cascade algorithm)
trained_face_data = cv2.CascadeClassifier(
    'haarcascade_frontalface_default.xml')

# Choose an image to detect the faces in
img = cv2.imread('Img1.JPG')


# Make the convert to Grayscaled
grayscaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect Faces
face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)
# print(face_coordinates)


# Draw rectangle around the faces
# cv2.rectangle(img, (x,y), (x+w, y+h), 2)
# x, y = coordinates of top left corner of the images
# x+w, y+h = add width and height to  the x,y coordinate to form a rectangle bcz rectangle has same width and height..
# To draw rectangle for a single person and we have to mention the index value bcz we are getting coordinates in list inside list.
# (x, y, w, h) = face_coordinates[0]
for (x, y, w, h) in face_coordinates:
    # created a random color using randrange to add color to our rectangle....
    # cv2.rectangle(img, (x, y), (x + w, y + h), (randrange(128, 255),randrange(128, 255), randrange(128, 255)), 2)
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 10)
# Display  the image with  faces
cv2.imshow("Image display", img)

# It just wait to see the image
cv2.waitKey()
print("Code Complete")
