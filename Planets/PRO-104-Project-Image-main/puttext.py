import cv2
img=cv2.imread('solar-system.jpg')
cv2.putText(img,
            "Sun",
            (20,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )

cv2.putText(img,
            "mercury",
            (130,230),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )

cv2.putText(img,
            "venus",
            (190,260),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )

cv2.putText(img,
            "Earth",
            (300,260),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )

cv2.putText(img,
            "Mars",
            (390,260),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )

cv2.putText(img,
            "Saturn",
            (790,260),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )
cv2.putText(img,
            "Juipiter",
            (546,260),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )
cv2.putText(img,
            "Uranes",
            (990,260),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )
cv2.putText(img,
            "Neptune",
            (1090,260),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )




cv2.imshow('output',img)
cv2.waitKey(0)
