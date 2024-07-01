import cv2

# Read Image
img = cv2.imread("solar-system.jpg")

cv2.putText(img,  
          "sun",
           (100, 80),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=1,  
           color=(0,0,255)
           )
cv2.putText(img,  
          "Mercury",
           (110, 270),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=1,  
           color=(0,0,255)
           )
cv2.putText(img,  
          "Venus",
           (190, 270),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=1,  
           color=(0,0,255)
           )
cv2.putText(img,  
          "Earth",
           (300, 270),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=1,  
           color=(0,0,255)
           )
cv2.putText(img,  
          "Mars",
           (400, 270),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=1,  
           color=(0,0,255)
           )
cv2.putText(img,  
          "Jupiter",
           (500, 300),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=1,  
           color=(0,0,255)
           )
cv2.putText(img,  
          "Saturn",
           (700, 300),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=1,  
           color=(0,0,255)
           )
cv2.putText(img,  
          "Uranus",
           (950, 300),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=1,  
           color=(0,0,255)
           )
cv2.putText(img,  
          "Neptune",
           (1100, 300),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=1,  
           color=(0,0,255)
           )
# Display Colored Image
cv2.imshow("Display Image",img)
cv2.waitKey(0)

