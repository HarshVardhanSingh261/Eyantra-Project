'''
*****************************************************************************************
*
*        		===============================================
*           		Nirikshak Bot (NB) Theme (eYRC 2020-21)
*        		===============================================
*
*  This script is to implement Task 1A - Part 1 of Nirikshak Bot (NB) Theme (eYRC 2020-21).
*  
*  This software is made available on an "AS IS WHERE IS BASIS".
*  Licensee/end user indemnifies and will keep e-Yantra indemnified from
*  any and all claim(s) that emanate from the use of the Software or 
*  breach of the terms of this agreement.
*  
*  e-Yantra - An MHRD project under National Mission on Education using ICT (NMEICT)
*
*****************************************************************************************
'''

# Team ID:			[ 2433 ]
# Author List:		[ Names of team members worked on this file separated by Comma: Harsh,Saksham,Rahul,Bhargav ]
# Filename:			task_1a_part1.py
# Functions:		scan_image
# 					[ Comma separated list of functions in this file ]
# Global variables:	shapes
# 					[ List of global variables defined in this file ]


####################### IMPORT MODULES #######################
## You are not allowed to make any changes in this section. ##
## You have to implement this task with the three available ##
## modules for this task (numpy, opencv, os)                ##
##############################################################
import cv2
import numpy as np
import os

##############################################################


# Global variable for details of shapes found in image and will be put in this dictionary, returned from scan_image function
shapes = {}


################# ADD UTILITY FUNCTIONS HERE #################
## You can define any utility functions for your code.      ##
## Please add proper comments to ensure that your code is   ##
## readable and easy to understand.                         ##
##############################################################


##############################################################


def scan_image(img_file_path):
    """
    Purpose:
    ---
    this function takes file path of an image as an argument and returns dictionary
    containing details of colored (non-white) shapes in that image

    Input Arguments:
    ---
    `img_file_path` :		[ str ]
        file path of image

    Returns:
    ---
    `shapes` :              [ dictionary ]
        details of colored (non-white) shapes present in image at img_file_path
        { 'Shape' : ['color', Area, cX, cY] }
    
    Example call:
    ---
    shapes = scan_image(img_file_path)
    """

    global shapes

    ##############	ADD YOUR CODE HERE	##############
    shapes1 = {}
    shapes={}
    count=0
    if(type(img_file_path) is np.ndarray):
        img=img_file_path
       
    else: img = cv2.imread(img_file_path)

    mask = {}
    sh = []
    arr= []

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    for i in range(2):


        if (i == 0):
            l_b = np.array([81, 0, 0])
            u_b = np.array([134, 255, 255])
            mask[0] = cv2.inRange(hsv, l_b, u_b)

        if (i == 1):
            l_b = np.array([0, 51, 0])
            u_b = np.array([47, 255, 255])
            mask[1] = cv2.inRange(hsv, l_b, u_b)
    for i in range(2):
        _, thrash = cv2.threshold(mask[i], 240, 255, cv2.THRESH_BINARY)
        contours, _ = cv2.findContours(thrash, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

        cv2.waitKey(0)
        for contour in contours:
            approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)

            if len(approx) == 3:
                s = 'Triangle'

                if (i == 0):
                    cl = 'blue'
                elif (i == 1):
                    cl = 'red'
            elif len(approx) == 4:
                x1, y1, w, h = cv2.boundingRect(approx)
                aspectRatio = float(w) / h

                if aspectRatio >= 0.95 and aspectRatio <= 1.05:
                    s = 'Square'

                    if (i == 0):
                        cl = 'blue'
                    elif (i == 1):
                        cl = 'red'

                else:
                    p = {}

                    for k in range(4):
                        p[k] = approx[k].ravel()

                    p1 = (p[0] - p[1]) - (p[3] - p[2])
                    p2 = (p[1] - p[2]) - (p[0] - p[3])

                    if ((np.all(p1 < 2) and np.all(p1 > -2)) or (np.all(p2 < 2) and np.all(p2 > -2))):
                        if ((np.all(p1 < 2) and np.all(p1 > -2)) and (np.all(p2 < 2) and np.all(p2 > -2))):
                            r = np.linalg.norm(p[0] - p[1]) / np.linalg.norm(p[1] - p[2])
                            if (r >= 0.95 and r <= 1.05):
                                s = 'Rhombus'
                            else:
                                s = 'Parallelogram'
                        else:
                            s = 'Trapezium'
                    else:
                        s = 'Quadrilateral'

                    if (i == 0):
                        cl = 'blue'
                    elif (i == 1):
                        cl = 'red'


            elif len(approx) == 5:
                s = 'Pentagon'

                if (i == 0):
                    cl = 'blue'
                elif (i == 1):
                    cl = 'red'

            elif len(approx) == 6:
                s = 'Hexagon'

                if (i == 0):
                    cl = 'blue'
                elif (i == 1):
                    cl = 'red'

            else:
                s = 'Circle'

                if (i == 0):
                    cl = 'blue'
                elif (i == 1):
                    cl = 'red'
            ar = cv2.contourArea(contour)
            M = cv2.moments(contour)
            if M['m00'] == 0:
                continue
            else:
                cx = int(M['m10'] / M['m00'])
            if M['m00'] == 0:
                continue
            else:
                cy = int(M['m01'] / M['m00'])
            al = cv2.arcLength(contour, True)
            al = round(al, 1)
            #shapes1[s] = [cl,cx+1,cy+1]
            shapes1.setdefault(s, []).append([cl,cx,cy])
            count=count+1
            

            sh.append(s)
            #arr.append(ar+al)

    #arr=sorted(arr,reverse=True)
    #for a in arr:
        #for s in sh:
            #if(shapes1[s][1]==a):
                #shapes[s]=shapes1[s]
    for s in sh:
        if(count==1):
                shapes[s]=shapes1[s][0]
        else:shapes=shapes1
    
    
    



    ##################################################

    return shapes


# NOTE:	YOU ARE NOT ALLOWED TO MAKE ANY CHANGE TO THIS FUNCTION
# 
# Function Name:    main
#        Inputs:    None
#       Outputs:    None
#       Purpose:    the function first takes 'Sample1.png' as input and runs scan_image function to find details
#                   of colored (non-white) shapes present in 'Sample1.png', it then asks the user whether
#                   to repeat the same on all images present in 'Samples' folder or not

if __name__ == '__main__':

    curr_dir_path = os.getcwd()
    print('Currently working in ' + curr_dir_path)

    # path directory of images in 'Samples' folder
    img_dir_path = curr_dir_path + '/Samples/'

    # path to 'Sample1.png' image file
    file_num = 1
    img_file_path = img_dir_path + 'Sample' + str(file_num) + '.png'

    print('\n============================================')
    print('\nLooking for Sample' + str(file_num) + '.png')

    if os.path.exists('Samples/Sample' + str(file_num) + '.png'):
        print('\nFound Sample' + str(file_num) + '.png')

    else:
        print('\n[ERROR] Sample' + str(file_num) + '.png not found. Make sure "Samples" folder has the selected file.')
        exit()

    print('\n============================================')

    try:
        print('\nRunning scan_image function with ' + img_file_path + ' as an argument')
        shapes = scan_image(img_file_path)

        if type(shapes) is dict:
            print(shapes)
            print('\nOutput generated. Please verify.')

        else:
            print('\n[ERROR] scan_image function returned a ' + str(type(shapes)) + ' instead of a dictionary.\n')
            exit()

    except Exception:
        print('\n[ERROR] scan_image function is throwing an error. Please debug scan_image function')
        exit()

    print('\n============================================')

    choice = input('\nWant to run your script on all the images in Samples folder ? ==>> "y" or "n": ')

    if choice == 'y':

        file_count = 2

        for file_num in range(file_count):

            # path to image file
            img_file_path = img_dir_path + 'Sample' + str(file_num + 1) + '.png'

            print('\n============================================')
            print('\nLooking for Sample' + str(file_num + 1) + '.png')

            if os.path.exists('Samples/Sample' + str(file_num + 1) + '.png'):
                print('\nFound Sample' + str(file_num + 1) + '.png')

            else:
                print('\n[ERROR] Sample' + str(
                    file_num + 1) + '.png not found. Make sure "Samples" folder has the selected file.')
                exit()

            print('\n============================================')

            try:
                print('\nRunning scan_image function with ' + img_file_path + ' as an argument')
                shapes = scan_image(img_file_path)

                if type(shapes) is dict:
                    print(shapes)
                    print('\nOutput generated. Please verify.')

                else:
                    print(
                        '\n[ERROR] scan_image function returned a ' + str(type(shapes)) + ' instead of a dictionary.\n')
                    exit()

            except Exception:
                print('\n[ERROR] scan_image function is throwing an error. Please debug scan_image function')
                exit()

            print('\n============================================')

    else:
        print('')
