import cv2
import numpy as np
import utils

def need_img(image_path):
    img = cv2.imread(image_path)
    widthImg=700
    heightImg=700

    img=cv2.resize(img,(widthImg, heightImg))
    
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    

    
    # Apply binary thresholding
    _, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

    contours, _ = cv2.findContours(binary, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_SIMPLE)
    rect_contours=utils.rectContour(contours)

    boundary_contours=rect_contours[1]
    boundary_contours_points=utils.getCornerPoints(boundary_contours)
    boundary_contours_points=utils.reorder(boundary_contours_points)
    pts1 = np.float32(boundary_contours_points) # PREPARE POINTS FOR WARP
    pts2 = np.float32([[0, 0],[widthImg, 0], [0, heightImg],[widthImg, heightImg]])
    matrix = cv2.getPerspectiveTransform(pts1, pts2) # GET TRANSFORMATION MATRIX
    imgWarpColored = cv2.warpPerspective(img, matrix, (widthImg, heightImg))
    # cv2.imwrite("test1.jpg",imgWarpColored)


    return imgWarpColored


def cir_cordinates(img):
    # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    

    
    # Apply binary thresholding
    # cv2.imwrite("img1.jpg",img)
    _, binary = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

    contours, _ = cv2.findContours(binary, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_SIMPLE)


    # rect_contours=utils.rectContour(contours)
    cir_contours=utils.circleContour(contours)



    return cir_contours


def rearrangeCoordinates(circleCon):
    sorted_circles = sorted(circleCon, key=lambda x: (x[0][1], x[0][0]))
    return sorted_circles


def add_response(response,option,ques):
    if option == 1:
        opt='A'
    elif option ==2:
        opt='B'
    elif option==3:
        opt='C'
    elif option==4:
        opt='D'
    print(f"option {option}opt{opt}ques{ques}")
    ques_opt={}
    ques_opt={ques,opt}
    print(f"ques_opt {ques_opt}")
    response.append(ques_opt)

    return response,ques


