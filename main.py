import cv2
import numpy as np
import utils
import helper
import requests

page_no=1

url = f"http://127.0.0.1:8000/json-file"


response = requests.get(url)
data = response.json()

ans_omr="./input/checkans.png"





img = cv2.imread(ans_omr)
widthImg=700
heightImg=700
img=cv2.resize(img,(widthImg, heightImg))
    
# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
_, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)


ans_omr=helper.need_img(ans_omr)
gray = cv2.cvtColor(ans_omr, cv2.COLOR_BGR2GRAY)
inverted_image = cv2.bitwise_not(gray)
# cv2.imwrite("test2.jpg",inverted_image)
_, binary = cv2.threshold(inverted_image, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)





# cir_ans_omr=helper.cir_cordinates(ans_omr)



if str(page_no) in data:
        coordinates = data[str(page_no)]["coordinates"]
        
        # Iterate through the coordinates
        for coordinate in coordinates:
            x = coordinate["x"]
            y = coordinate["y"]
            r = coordinate["r"]
            question_no = coordinate["question_no"]
            option = coordinate["option"]
                
            

            is_filled, fill_ratio = utils.is_circle_filled(binary,(x,y), r)
            status = "Filled" if is_filled else "Not Filled"

            if status=="Filled":
                    text = f"{option}"
                    font = cv2.FONT_HERSHEY_SIMPLEX
                    print(f"question_no {question_no} : {option}")
                    image_copy=cv2.circle(ans_omr, (x,y), r, (0, 255, 0), 2)
                    image_copy = cv2.putText(image_copy, text, (x,y), font, 0.5, (255, 0, 0), 1, cv2.LINE_AA)
                    cv2.imshow("marker img",image_copy)





cv2.waitKey(0)
cv2.destroyAllWindows()