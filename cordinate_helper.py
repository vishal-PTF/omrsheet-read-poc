import cv2
import numpy as np
import os
import requests
import helper


all_cor="./input/correctans.png"
url = "http://127.0.0.1:8000/json-file"

pg_no=1

img = cv2.imread(all_cor)
widthImg=700
heightImg=700
img=cv2.resize(img,(widthImg, heightImg))
    
# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


all_cor=helper.need_img(all_cor)
gray = cv2.cvtColor(all_cor, cv2.COLOR_BGR2GRAY)
inverted_image = cv2.bitwise_not(gray)


cir_all_cor=helper.cir_cordinates(inverted_image)

arr_cir_all_cor=helper.rearrangeCoordinates(cir_all_cor)
print(arr_cir_all_cor)
data={}
script_directory = os.path.dirname(os.path.abspath(__file__))
output_directory = os.path.join(script_directory, "cord_img")
# output_directory = './cord_img'
output_path = os.path.join(output_directory, f'saved_image{pg_no}.jpg') 
print(output_path)

for i, (center, radius) in enumerate(arr_cir_all_cor):


        text = f"{center}"
        font = cv2.FONT_HERSHEY_SIMPLEX
        x=center[0]
        y=center[1]
        r=radius
        data=[{"page_no":pg_no,"x":x,"y":y,"r":r}]
        response = requests.post(url, json=data)
        if response.status_code == 200:
            print("Data added successfully")

        image_copy=cv2.circle(all_cor, center, radius, (0, 255, 0), 2)
        image_copy = cv2.putText(image_copy, text, center, font, 0.5, (255, 0, 0), 1, cv2.LINE_AA)

        cv2.imshow("img",image_copy)
        cv2.imwrite(output_path,image_copy)

 
        print(f"Circle {i+1}: Center = {center}, Radius = {radius}")




cv2.waitKey(0)
cv2.destroyAllWindows()