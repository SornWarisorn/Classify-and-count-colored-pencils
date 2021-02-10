from imutils.video import VideoStream
import cv2
import numpy as np
import argparse
from tkinter import *
import tkinter
from helper import obj
import PIL.Image, PIL.ImageTk
import time



gui = Tk()
gui.geometry("540x330")
cv_img = cv2.cvtColor(cv2.imread("bgg.jpg"), cv2.COLOR_BGR2RGB)

height, width, no_channels = cv_img.shape

canvas = tkinter.Canvas(gui, width = width, height = height)
canvas.pack()

photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(cv_img))

canvas.create_image(0, 0, image=photo, anchor=tkinter.NW)

def VDO():

    disjoint_set = {}
    free_set = [False] * 100

    ap = argparse.ArgumentParser()
    ap.add_argument("-v", "--video",
                    help="path to the (optional) video file")
    ap.add_argument("-b", "--buffer", type=int, default=64,
                    help="max buffer size")
    # QR
    ap.add_argument("-o", "--output", type=str, default="barcodes.csv",
                    help="path to output CSV file containing barcodes")
    #
    args = vars(ap.parse_args())

    vs = VideoStream(src=0).start()
    time.sleep(2.0)
    csv = open(args["output"], "w")
    found = set()
    count = 0

    ############# long ############
    count_yellow = 0
    count_light_green = 0
    count_dark_green = 0
    count_dark_blue = 0
    count_pink = 0
    count_light_blue = 0
    count_egg_color = 0
    count_black = 0
    count_brown = 0
    count_red = 0
    count_orange = 0
    count_purple = 0
    ################################
    
    ############# short ############
    count_yellow_short = 0
    count_light_green_short = 0
    count_dark_green_short = 0
    count_dark_blue_short = 0
    count_pink_short = 0
    count_light_blue_short = 0
    count_egg_color_short = 0
    count_black_short = 0
    count_brown_short = 0
    count_red_short = 0
    count_orange_short = 0
    count_purple_short = 0
    ################################
    
    lineX1 = 410
    lineX2 = 430
    cap = cv2.VideoCapture("My Video3.mp4")
    bg = cv2.imread('bg.jpg')

    def process(x, y, w, h, target):
        ########################### yellow ###########################
        if not disjoint_set and cx < lineX1:
            tmp_id = 0
            for f_id in range(len(free_set)):
                if free_set[f_id] == False:
                    tmp_id = f_id
                    free_set[f_id] = True
                    break
            tmp_obj = obj(tmp_id)
            tmp_obj.insert(x, y, w, h, 'yellow')

            disjoint_set[tmp_id] = tmp_obj
        else:
            inserted = False

            for key, val in disjoint_set.items():
                l_x, l_y, l_w, l_h, _ = val.last()
                l_cx, l_cy = int((2 * l_x + l_w) / 2), int((2 * l_y + l_h) / 2)
                if l_x <= centroid[0] <= l_x + l_w:  # joint set
                    val.insert(x, y, w, h, target)
                    inserted = True
                    if l_cx >= lineX1:
                        val.counted = True
            if not inserted and cx < lineX1:
                tmp_id = 0
                for f_id in range(len(free_set)):
                    if free_set[f_id] == False:
                        tmp_id = f_id
                        free_set[f_id] = True
                        break
                tmp_obj = obj(tmp_id)
                tmp_obj.insert(x, y, w, h, target)

                disjoint_set[tmp_id] = tmp_obj
        #############################################################

        ########################### yellow_short ###########################
        if not disjoint_set and cx < lineX1:
            tmp_id = 0
            for f_id in range(len(free_set)):
                if free_set[f_id] == False:
                    tmp_id = f_id
                    free_set[f_id] = True
                    break
            tmp_obj = obj(tmp_id)
            tmp_obj.insert(x, y, w, h, 'yellow_short')

            disjoint_set[tmp_id] = tmp_obj
        else:
            inserted = False

            for key, val in disjoint_set.items():
                l_x, l_y, l_w, l_h, _ = val.last()
                l_cx, l_cy = int((2 * l_x + l_w) / 2), int((2 * l_y + l_h) / 2)
                if l_x <= centroid[0] <= l_x + l_w:  # joint set
                    val.insert(x, y, w, h, target)
                    inserted = True
                    if l_cx >= lineX1:
                        val.counted = True
            if not inserted and cx < lineX1:
                tmp_id = 0
                for f_id in range(len(free_set)):
                    if free_set[f_id] == False:
                        tmp_id = f_id
                        free_set[f_id] = True
                        break
                tmp_obj = obj(tmp_id)
                tmp_obj.insert(x, y, w, h, target)

                disjoint_set[tmp_id] = tmp_obj
        #############################################################

        ########################### light_green ###########################
        if not disjoint_set and cx < lineX1:
            tmp_id = 0
            for f_id in range(len(free_set)):
                if free_set[f_id] == False:
                    tmp_id = f_id
                    free_set[f_id] = True
                    break
            tmp_obj = obj(tmp_id)
            tmp_obj.insert(x, y, w, h, 'light_green')

            disjoint_set[tmp_id] = tmp_obj
        else:
            inserted = False

            for key, val in disjoint_set.items():
                l_x, l_y, l_w, l_h, _ = val.last()
                l_cx, l_cy = int((2 * l_x + l_w) / 2), int((2 * l_y + l_h) / 2)
                if l_x <= centroid[0] <= l_x + l_w:  # joint set
                    val.insert(x, y, w, h, target)
                    inserted = True
                    if l_cx >= lineX1:
                        val.counted = True
            if not inserted and cx < lineX1:
                tmp_id = 0
                for f_id in range(len(free_set)):
                    if free_set[f_id] == False:
                        tmp_id = f_id
                        free_set[f_id] = True
                        break
                tmp_obj = obj(tmp_id)
                tmp_obj.insert(x, y, w, h, target)

                disjoint_set[tmp_id] = tmp_obj
        #############################################################

        ########################### dark_green ###########################
        if not disjoint_set and cx < lineX1:
            tmp_id = 0
            for f_id in range(len(free_set)):
                if free_set[f_id] == False:
                    tmp_id = f_id
                    free_set[f_id] = True
                    break
            tmp_obj = obj(tmp_id)
            tmp_obj.insert(x, y, w, h, 'dark_green')

            disjoint_set[tmp_id] = tmp_obj
        else:
            inserted = False

            for key, val in disjoint_set.items():
                l_x, l_y, l_w, l_h, _ = val.last()
                l_cx, l_cy = int((2 * l_x + l_w) / 2), int((2 * l_y + l_h) / 2)
                if l_x <= centroid[0] <= l_x + l_w:  # joint set
                    val.insert(x, y, w, h, target)
                    inserted = True
                    if l_cx >= lineX1:
                        val.counted = True
            if not inserted and cx < lineX1:
                tmp_id = 0
                for f_id in range(len(free_set)):
                    if free_set[f_id] == False:
                        tmp_id = f_id
                        free_set[f_id] = True
                        break
                tmp_obj = obj(tmp_id)
                tmp_obj.insert(x, y, w, h, target)

                disjoint_set[tmp_id] = tmp_obj
        #############################################################

        ########################### dark_blue ###########################
        if not disjoint_set and cx < lineX1:
            tmp_id = 0
            for f_id in range(len(free_set)):
                if free_set[f_id] == False:
                    tmp_id = f_id
                    free_set[f_id] = True
                    break
            tmp_obj = obj(tmp_id)
            tmp_obj.insert(x, y, w, h, 'dark_blue')

            disjoint_set[tmp_id] = tmp_obj
        else:
            inserted = False

            for key, val in disjoint_set.items():
                l_x, l_y, l_w, l_h, _ = val.last()
                l_cx, l_cy = int((2 * l_x + l_w) / 2), int((2 * l_y + l_h) / 2)
                if l_x <= centroid[0] <= l_x + l_w:  # joint set
                    val.insert(x, y, w, h, target)
                    inserted = True
                    if l_cx >= lineX1:
                        val.counted = True
            if not inserted and cx < lineX1:
                tmp_id = 0
                for f_id in range(len(free_set)):
                    if free_set[f_id] == False:
                        tmp_id = f_id
                        free_set[f_id] = True
                        break
                tmp_obj = obj(tmp_id)
                tmp_obj.insert(x, y, w, h, target)

                disjoint_set[tmp_id] = tmp_obj
        #############################################################

        ########################### pink ###########################
        if not disjoint_set and cx < lineX1:
            tmp_id = 0
            for f_id in range(len(free_set)):
                if free_set[f_id] == False:
                    tmp_id = f_id
                    free_set[f_id] = True
                    break
            tmp_obj = obj(tmp_id)
            tmp_obj.insert(x, y, w, h, 'pink')

            disjoint_set[tmp_id] = tmp_obj
        else:
            inserted = False

            for key, val in disjoint_set.items():
                l_x, l_y, l_w, l_h, _ = val.last()
                l_cx, l_cy = int((2 * l_x + l_w) / 2), int((2 * l_y + l_h) / 2)
                if l_x <= centroid[0] <= l_x + l_w:  # joint set
                    val.insert(x, y, w, h, target)
                    inserted = True
                    if l_cx >= lineX1:
                        val.counted = True
            if not inserted and cx < lineX1:
                tmp_id = 0
                for f_id in range(len(free_set)):
                    if free_set[f_id] == False:
                        tmp_id = f_id
                        free_set[f_id] = True
                        break
                tmp_obj = obj(tmp_id)
                tmp_obj.insert(x, y, w, h, target)

                disjoint_set[tmp_id] = tmp_obj
        #############################################################

        ########################### light_blue ###########################
        if not disjoint_set and cx < lineX1:
            tmp_id = 0
            for f_id in range(len(free_set)):
                if free_set[f_id] == False:
                    tmp_id = f_id
                    free_set[f_id] = True
                    break
            tmp_obj = obj(tmp_id)
            tmp_obj.insert(x, y, w, h, 'light_blue')

            disjoint_set[tmp_id] = tmp_obj
        else:
            inserted = False

            for key, val in disjoint_set.items():
                l_x, l_y, l_w, l_h, _ = val.last()
                l_cx, l_cy = int((2 * l_x + l_w) / 2), int((2 * l_y + l_h) / 2)
                if l_x <= centroid[0] <= l_x + l_w:  # joint set
                    val.insert(x, y, w, h, target)
                    inserted = True
                    if l_cx >= lineX1:
                        val.counted = True
            if not inserted and cx < lineX1:
                tmp_id = 0
                for f_id in range(len(free_set)):
                    if free_set[f_id] == False:
                        tmp_id = f_id
                        free_set[f_id] = True
                        break
                tmp_obj = obj(tmp_id)
                tmp_obj.insert(x, y, w, h, target)

                disjoint_set[tmp_id] = tmp_obj
        #############################################################

        ########################### egg_color ###########################
        if not disjoint_set and cx < lineX1:
            tmp_id = 0
            for f_id in range(len(free_set)):
                if free_set[f_id] == False:
                    tmp_id = f_id
                    free_set[f_id] = True
                    break
            tmp_obj = obj(tmp_id)
            tmp_obj.insert(x, y, w, h, 'egg_color')

            disjoint_set[tmp_id] = tmp_obj
        else:
            inserted = False

            for key, val in disjoint_set.items():
                l_x, l_y, l_w, l_h, _ = val.last()
                l_cx, l_cy = int((2 * l_x + l_w) / 2), int((2 * l_y + l_h) / 2)
                if l_x <= centroid[0] <= l_x + l_w:  # joint set
                    val.insert(x, y, w, h, target)
                    inserted = True
                    if l_cx >= lineX1:
                        val.counted = True
            if not inserted and cx < lineX1:
                tmp_id = 0
                for f_id in range(len(free_set)):
                    if free_set[f_id] == False:
                        tmp_id = f_id
                        free_set[f_id] = True
                        break
                tmp_obj = obj(tmp_id)
                tmp_obj.insert(x, y, w, h, target)

                disjoint_set[tmp_id] = tmp_obj
        #############################################################

        ########################### black ###########################
        if not disjoint_set and cx < lineX1:
            tmp_id = 0
            for f_id in range(len(free_set)):
                if free_set[f_id] == False:
                    tmp_id = f_id
                    free_set[f_id] = True
                    break
            tmp_obj = obj(tmp_id)
            tmp_obj.insert(x, y, w, h, 'black')

            disjoint_set[tmp_id] = tmp_obj
        else:
            inserted = False

            for key, val in disjoint_set.items():
                l_x, l_y, l_w, l_h, _ = val.last()
                l_cx, l_cy = int((2 * l_x + l_w) / 2), int((2 * l_y + l_h) / 2)
                if l_x <= centroid[0] <= l_x + l_w:  # joint set
                    val.insert(x, y, w, h, target)
                    inserted = True
                    if l_cx >= lineX1:
                        val.counted = True
            if not inserted and cx < lineX1:
                tmp_id = 0
                for f_id in range(len(free_set)):
                    if free_set[f_id] == False:
                        tmp_id = f_id
                        free_set[f_id] = True
                        break
                tmp_obj = obj(tmp_id)
                tmp_obj.insert(x, y, w, h, target)

                disjoint_set[tmp_id] = tmp_obj
        #############################################################

        ########################### brown ###########################
        if not disjoint_set and cx < lineX1:
            tmp_id = 0
            for f_id in range(len(free_set)):
                if free_set[f_id] == False:
                    tmp_id = f_id
                    free_set[f_id] = True
                    break
            tmp_obj = obj(tmp_id)
            tmp_obj.insert(x, y, w, h, 'brown')

            disjoint_set[tmp_id] = tmp_obj
        else:
            inserted = False

            for key, val in disjoint_set.items():
                l_x, l_y, l_w, l_h, _ = val.last()
                l_cx, l_cy = int((2 * l_x + l_w) / 2), int((2 * l_y + l_h) / 2)
                if l_x <= centroid[0] <= l_x + l_w:  # joint set
                    val.insert(x, y, w, h, target)
                    inserted = True
                    if l_cx >= lineX1:
                        val.counted = True
            if not inserted and cx < lineX1:
                tmp_id = 0
                for f_id in range(len(free_set)):
                    if free_set[f_id] == False:
                        tmp_id = f_id
                        free_set[f_id] = True
                        break
                tmp_obj = obj(tmp_id)
                tmp_obj.insert(x, y, w, h, target)

                disjoint_set[tmp_id] = tmp_obj
        #############################################################

        ########################### red ###########################
        if not disjoint_set and cx < lineX1:
            tmp_id = 0
            for f_id in range(len(free_set)):
                if free_set[f_id] == False:
                    tmp_id = f_id
                    free_set[f_id] = True
                    break
            tmp_obj = obj(tmp_id)
            tmp_obj.insert(x, y, w, h, 'red')

            disjoint_set[tmp_id] = tmp_obj
        else:
            inserted = False

            for key, val in disjoint_set.items():
                l_x, l_y, l_w, l_h, _ = val.last()
                l_cx, l_cy = int((2 * l_x + l_w) / 2), int((2 * l_y + l_h) / 2)
                if l_x <= centroid[0] <= l_x + l_w:  # joint set
                    val.insert(x, y, w, h, target)
                    inserted = True
                    if l_cx >= lineX1:
                        val.counted = True
            if not inserted and cx < lineX1:
                tmp_id = 0
                for f_id in range(len(free_set)):
                    if free_set[f_id] == False:
                        tmp_id = f_id
                        free_set[f_id] = True
                        break
                tmp_obj = obj(tmp_id)
                tmp_obj.insert(x, y, w, h, target)

                disjoint_set[tmp_id] = tmp_obj
        #############################################################

        ########################### orange ###########################
        if not disjoint_set and cx < lineX1:
            tmp_id = 0
            for f_id in range(len(free_set)):
                if free_set[f_id] == False:
                    tmp_id = f_id
                    free_set[f_id] = True
                    break
            tmp_obj = obj(tmp_id)
            tmp_obj.insert(x, y, w, h, 'orange')

            disjoint_set[tmp_id] = tmp_obj
        else:
            inserted = False

            for key, val in disjoint_set.items():
                l_x, l_y, l_w, l_h, _ = val.last()
                l_cx, l_cy = int((2 * l_x + l_w) / 2), int((2 * l_y + l_h) / 2)
                if l_x <= centroid[0] <= l_x + l_w:  # joint set
                    val.insert(x, y, w, h, target)
                    inserted = True
                    if l_cx >= lineX1:
                        val.counted = True
            if not inserted and cx < lineX1:
                tmp_id = 0
                for f_id in range(len(free_set)):
                    if free_set[f_id] == False:
                        tmp_id = f_id
                        free_set[f_id] = True
                        break
                tmp_obj = obj(tmp_id)
                tmp_obj.insert(x, y, w, h, target)

                disjoint_set[tmp_id] = tmp_obj
        #############################################################

        ########################### purple ###########################
        if not disjoint_set and cx < lineX1:
            tmp_id = 0
            for f_id in range(len(free_set)):
                if free_set[f_id] == False:
                    tmp_id = f_id
                    free_set[f_id] = True
                    break
            tmp_obj = obj(tmp_id)
            tmp_obj.insert(x, y, w, h, 'purple')

            disjoint_set[tmp_id] = tmp_obj
        else:
            inserted = False

            for key, val in disjoint_set.items():
                l_x, l_y, l_w, l_h, _ = val.last()
                l_cx, l_cy = int((2 * l_x + l_w) / 2), int((2 * l_y + l_h) / 2)
                if l_x <= centroid[0] <= l_x + l_w:  # joint set
                    val.insert(x, y, w, h, target)
                    inserted = True
                    if l_cx >= lineX1:
                        val.counted = True
            if not inserted and cx < lineX1:
                tmp_id = 0
                for f_id in range(len(free_set)):
                    if free_set[f_id] == False:
                        tmp_id = f_id
                        free_set[f_id] = True
                        break
                tmp_obj = obj(tmp_id)
                tmp_obj.insert(x, y, w, h, target)

                disjoint_set[tmp_id] = tmp_obj
        #############################################################
    while True:
        _, frame = cap.read()
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        kernel3 = np.ones((3, 3), np.uint8)
        kernel5 = np.ones((5, 5), np.uint8)
        kernel7 = np.ones((7, 7), np.uint8)
        kernel9 = np.ones((9, 9), np.uint8)

        #############################################################
        hsv_yellow_long1 = cv2.morphologyEx(hsv,cv2.MORPH_OPEN,kernel5)
        hsv_yellow_long = cv2.morphologyEx(hsv_yellow_long1, cv2.MORPH_CLOSE, kernel5)

        hsv_yellow_short1 = cv2.morphologyEx(hsv,cv2.MORPH_OPEN,kernel5)
        hsv_yellow_short = cv2.morphologyEx(hsv_yellow_short1, cv2.MORPH_CLOSE, kernel5)

        #############################################################
        hsv_dark_blue_long1 = cv2.morphologyEx(hsv,cv2.MORPH_OPEN,kernel5)
        hsv_dark_blue_long = cv2.morphologyEx(hsv_yellow_long1, cv2.MORPH_CLOSE, kernel5)

        hsv_dark_blue_short1 = cv2.morphologyEx(hsv,cv2.MORPH_OPEN,kernel5)
        hsv_dark_blue_short = cv2.morphologyEx(hsv_yellow_short1, cv2.MORPH_CLOSE, kernel5)

        #############################################################
        hsv_light_blue_long1 = cv2.morphologyEx(hsv,cv2.MORPH_OPEN,kernel5)
        hsv_light_blue_long = cv2.morphologyEx(hsv_light_blue_long1, cv2.MORPH_CLOSE, kernel5)

        hsv_light_blue_short1 = cv2.morphologyEx(hsv,cv2.MORPH_OPEN,kernel5)
        hsv_light_blue_short = cv2.morphologyEx(hsv_light_blue_short1, cv2.MORPH_CLOSE, kernel5)

        #############################################################
        hsv_black_long1 = cv2.morphologyEx(hsv,cv2.MORPH_OPEN,kernel5)
        hsv_black_long = cv2.morphologyEx(hsv_black_long1, cv2.MORPH_CLOSE, kernel5)

        hsv_black_short1 = cv2.morphologyEx(hsv,cv2.MORPH_OPEN,kernel5)
        hsv_black_short = cv2.morphologyEx(hsv_black_short1, cv2.MORPH_CLOSE, kernel5)

        #############################################################
        hsv_brown_long1 = cv2.morphologyEx(hsv,cv2.MORPH_OPEN,kernel5)
        hsv_brown_long = cv2.morphologyEx(hsv_brown_long1, cv2.MORPH_CLOSE, kernel5)

        hsv_brown_short1 = cv2.morphologyEx(hsv,cv2.MORPH_OPEN,kernel5)
        hsv_brown_short = cv2.morphologyEx(hsv_brown_short1, cv2.MORPH_CLOSE, kernel5)

        #############################################################
        hsv_purple_long1 = cv2.morphologyEx(hsv,cv2.MORPH_OPEN,kernel5)
        hsv_purple_long = cv2.morphologyEx(hsv_purple_long1, cv2.MORPH_CLOSE, kernel5)

        hsv_purple_short1 = cv2.morphologyEx(hsv,cv2.MORPH_OPEN,kernel5)
        hsv_purple_short = cv2.morphologyEx(hsv_purple_short1, cv2.MORPH_CLOSE, kernel5)

        

        
        
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.line(frame, (lineX1, 0), (lineX1, 600), (0, 0, 255), 2)
        cv2.line(frame, (lineX2, 0), (lineX2, 600), (0, 255, 255), 2)

        colors = {'red': (0, 0, 255), 'green': (0, 255, 0), 'blue': (255, 0, 0), 'yellow': (255, 0, 0)}

        if disjoint_set:
            for key, val in disjoint_set.items():

                for his in val.history:
                    l_x, l_y, l_w, l_h, _ = his
                    l_cx, l_cy = int((2 * l_x + l_w) / 2), int((2 * l_y + l_h) / 2)
                    cv2.circle(frame, (l_cx, l_cy), 2, (255, 255, 255), -2)
                l_x, l_y, l_w, l_h, _ = val.last()

                if val.counted == True:
                    color = val.checkcolor()

         ############################### long ##################################
                    if color == 'yellow':
                        count_yellow += 1
                    if color == 'light_green':
                        count_light_green += 1
                    if color == 'dark_green':
                        count_dark_green += 1
                    if color == 'dark_blue':
                        count_dark_blue += 1
                    if color == 'pink':
                        count_pink += 1
                    if color == 'light_blue':
                        count_light_blue += 1
                    if color == 'egg_color':
                        count_egg_color = 1
            
                    if color == 'black':
                        count_black += 1
                    if color == 'brown':
                        count_brown += 1
                    if color == 'red':
                        count_red += 1
                    if color == 'orange':
                        count_orange += 1
                    if color == 'purple':
                        count_purple += 1
        ########################################################################

        ############################### short ##################################
                    if color == 'yellow_short':
                        count_yellow_short += 1
                    if color == 'light_green_short':
                        count_light_green_short += 1
                    if color == 'dark_green_short':
                        count_dark_green_short += 1
                    if color == 'dark_blue_short':
                        count_dark_blue_short += 1
                    if color == 'pink_short':
                        count_pink_short += 1
                    if color == 'light_blue_short':
                        count_light_blue_short += 1
                    if color == 'egg_color_short':
                        count_egg_color_short += 1
                    if color == 'black_short':
                        count_black_short += 1
                    if color == 'brown_short':
                        count_brown_short += 1
                    if color == 'red_short':
                        count_red_short += 1
                    if color == 'orange_short':
                        count_orange_short += 1
                    if color == 'purple_short':
                        count_purple_short += 1
        ########################################################################

                        

                    free_set[key] = False
                    disjoint_set.pop(key)
                    break

        ############################### yellow ###############################      
        lower_yellow = np.array([20,100,192])
        upper_yellow = np.array([50,255,255])
        mask_yellow_long = cv2.inRange(hsv_yellow_long, lower_yellow, upper_yellow)
        mask_yellow_short = cv2.inRange(hsv_yellow_short, lower_yellow, upper_yellow)
        
        contours_yellow_long, _ = cv2.findContours(mask_yellow_long, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        contours_yellow_short, _ = cv2.findContours(mask_yellow_short, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

        for contour in contours_yellow_long:            ## long
            area = cv2.contourArea(contour)
            (x, y, w, h) = cv2.boundingRect(contour)
            rect = cv2.minAreaRect(contour)
            box = cv2.boxPoints(rect)
            box = np.int0(box)
            cx = int((2 * x + w) / 2)
            cy = int((2 * y + h) / 2)
            centroid = cx, cy

            if (area > 9000 and cx <= lineX2):
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(frame, 'Yellow' + str(area) , (x, h), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 2)
            
                process(x, y, w, h, 'yellow')
        cv2.putText(frame, str(count_yellow), (140, 45), font, 1, (0, 255, 0), 2)

        for contour in contours_yellow_short:            ## short
            area = cv2.contourArea(contour)
            (x, y, w, h) = cv2.boundingRect(contour)
            rect = cv2.minAreaRect(contour)
            box = cv2.boxPoints(rect)
            box = np.int0(box)
            cx = int((2 * x + w) / 2)
            cy = int((2 * y + h) / 2)
            centroid = cx, cy

            if (1000 < area < 5000 and cx <= lineX2):
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(frame, 'Yellow_short'+ str(area), (x, h), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 2)
            
                process(x, y, w, h, 'yellow_short')
        cv2.putText(frame, str(count_yellow_short), (190, 45), font, 1, (0, 255, 0), 2)

        ###########################################################################

        ############################### light_green ###############################
        lower_light_green = np.array([45,100,50])
        upper_light_green = np.array([58,255,255])
        mask_light_green = cv2.inRange(hsv, lower_light_green, upper_light_green)
        res_light_green = cv2.bitwise_and(hsv,hsv, mask= mask_light_green)
        kernel = np.ones((3,3),np.uint8)
        opening = cv2.morphologyEx(res_light_green,cv2.MORPH_OPEN,kernel)
        contours, _ = cv2.findContours(mask_light_green, cv2.RETR_TREE,  cv2.CHAIN_APPROX_NONE)

        for contour in contours:            ## long
            area = cv2.contourArea(contour)
            (x, y, w, h) = cv2.boundingRect(contour)
            rect = cv2.minAreaRect(contour)
            box = cv2.boxPoints(rect)
            box = np.int0(box)
            cx = int((2 * x + w) / 2)
            cy = int((2 * y + h) / 2)
            centroid = cx, cy

            if (area > 7500 and cx <= lineX2):
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(frame, 'light_green'+ str(area), (x, h), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 2)
            
                process(x, y, w, h, 'light_green')
        cv2.putText(frame, str(count_light_green), (250, 85), font, 1, (0, 255, 0), 2)

        for contour in contours:            ## short
            area = cv2.contourArea(contour)
            (x, y, w, h) = cv2.boundingRect(contour)
            rect = cv2.minAreaRect(contour)
            box = cv2.boxPoints(rect)
            box = np.int0(box)
            cx = int((2 * x + w) / 2)
            cy = int((2 * y + h) / 2)
            centroid = cx, cy

            if (1000 < area < 5000 and cx <= lineX2):
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(frame, 'light_green_short'+ str(area), (x, h), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 2)
                
                process(x, y, w, h, 'light_green_short')
        cv2.putText(frame, str(count_light_green_short), (300, 85), font, 1, (0, 255, 0), 2)

        ##########################################################################

        ############################### dark_green ###############################
        lower_dark_green = np.array([65,68,40])
        upper_dark_green = np.array([85,255,200])
        mask_dark_green = cv2.inRange(hsv, lower_dark_green, upper_dark_green)
        res_dark_green = cv2.bitwise_and(hsv,hsv, mask= mask_light_green)
        kernel = np.ones((3,3),np.uint8)
        dilation = cv2.dilate(res_dark_green,kernel,iterations = 1)
        contours, _ = cv2.findContours(mask_dark_green, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

        for contour in contours:            ## long
            area = cv2.contourArea(contour)
            (x, y, w, h) = cv2.boundingRect(contour)
            rect = cv2.minAreaRect(contour)
            box = cv2.boxPoints(rect)
            box = np.int0(box)
            cx = int((2 * x + w) / 2)
            cy = int((2 * y + h) / 2)
            centroid = cx, cy

            if (area > 9000 and cx <= lineX2):
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(frame, 'dark_green'+ str(area), (x, h), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 2)
                
                process(x, y, w, h, 'dark_green')
        cv2.putText(frame, str(count_dark_green), (240, 125), font, 1, (0, 255, 0), 2)

        for contour in contours:            ## short
            area = cv2.contourArea(contour)
            (x, y, w, h) = cv2.boundingRect(contour)
            rect = cv2.minAreaRect(contour)
            box = cv2.boxPoints(rect)
            box = np.int0(box)
            cx = int((2 * x + w) / 2)
            cy = int((2 * y + h) / 2)
            centroid = cx, cy

            if (1000 < area < 5000 and cx <= lineX2):
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(frame, 'dark_green_short'+ str(area), (x, h), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 2)
               
                process(x, y, w, h, 'dark_green_short')
        cv2.putText(frame, str(count_dark_green_short), (290, 125), font, 1, (0, 255, 0), 2)

        ##########################################################################

        ############################### dark_blue ###############################
        lower_dark_blue = np.array([110,60,60])
        upper_dark_blue = np.array([120,255,255])
        mask_dark_blue = cv2.inRange(hsv, lower_dark_blue, upper_dark_blue)
        res_dark_blue = cv2.bitwise_and(hsv,hsv, mask= mask_dark_blue)
        kernel = np.ones((3,3),np.uint8)
        dilation = cv2.dilate(res_dark_blue,kernel,iterations = 1)
        contours, _ = cv2.findContours(mask_dark_blue, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

        for contour in contours:            ## long
            area = cv2.contourArea(contour)
            (x, y, w, h) = cv2.boundingRect(contour)
            rect = cv2.minAreaRect(contour)
            box = cv2.boxPoints(rect)
            box = np.int0(box)
            cx = int((2 * x + w) / 2)
            cy = int((2 * y + h) / 2)
            centroid = cx, cy

            if (area > 6000 and cx <= lineX2):
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(frame, 'dark_blue'+ str(area), (x, h), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 2)
                #cv2.circle(frame, (cx, cy), 2, (255, 255, 255), -2)
                #cv2.circle(mask_dark_blue, (cx, cy), 2, (0, 0, 255), -2)
                process(x, y, w, h, 'dark_blue')
        cv2.putText(frame, str(count_dark_blue), (240, 165), font, 1, (0, 255, 0), 2)

        for contour in contours:            ## short
            area = cv2.contourArea(contour)
            (x, y, w, h) = cv2.boundingRect(contour)
            rect = cv2.minAreaRect(contour)
            box = cv2.boxPoints(rect)
            box = np.int0(box)
            cx = int((2 * x + w) / 2)
            cy = int((2 * y + h) / 2)
            centroid = cx, cy

            if (1000 < area < 5000 and cx <= lineX2):
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(frame, 'dark_blue_short'+ str(area), (x, h), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 2)
                #cv2.circle(frame, (cx, cy), 2, (255, 255, 255), -2)
                #cv2.circle(mask_dark_blue, (cx, cy), 2, (0, 0, 255), -2)
                process(x, y, w, h, 'dark_blue_short')
        cv2.putText(frame, str(count_dark_blue_short), (290, 165), font, 1, (0, 255, 0), 2)

        ##########################################################################

        ############################### pink ###############################
        lower_pink = np.array([155,80,60])
        upper_pink = np.array([200,255,255])
        mask_pink = cv2.inRange(hsv, lower_pink, upper_pink)
        res_pink = cv2.bitwise_and(hsv,hsv, mask= mask_pink)
        kernel = np.ones((3,3),np.uint8)
        dilation = cv2.dilate(res_pink,kernel,iterations = 1)
        contours, _ = cv2.findContours(mask_pink, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

        for contour in contours:            ## long
            area = cv2.contourArea(contour)
            (x, y, w, h) = cv2.boundingRect(contour)
            rect = cv2.minAreaRect(contour)
            box = cv2.boxPoints(rect)
            box = np.int0(box)
            cx = int((2 * x + w) / 2)
            cy = int((2 * y + h) / 2)
            centroid = cx, cy

            if (area > 7600 and cx <= lineX2):
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(frame, 'pink'+ str(area), (x, h), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 2)
                #cv2.circle(frame, (cx, cy), 2, (255, 255, 255), -2)
                #cv2.circle(mask_pink, (cx, cy), 2, (0, 0, 255), -2)
                process(x, y, w, h, 'pink')
        cv2.putText(frame, str(count_pink), (150, 205), font, 1, (0, 255, 0), 2)

        for contour in contours:            ## short
            area = cv2.contourArea(contour)
            (x, y, w, h) = cv2.boundingRect(contour)
            rect = cv2.minAreaRect(contour)
            box = cv2.boxPoints(rect)
            box = np.int0(box)
            cx = int((2 * x + w) / 2)
            cy = int((2 * y + h) / 2)
            centroid = cx, cy

            if (1000 < area < 1500 and cx <= lineX2):
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(frame, 'pink_short'+ str(area), (x, h), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 2)
                #cv2.circle(frame, (cx, cy), 2, (255, 255, 255), -2)
                #cv2.circle(mask_pink, (cx, cy), 2, (0, 0, 255), -2)
                process(x, y, w, h, 'pink_short')
        cv2.putText(frame, str(count_pink_short), (200, 205), font, 1, (0, 255, 0), 2)

        ##########################################################################

        ############################### light_blue ###############################
        lower_light_blue = np.array([92,100,160])
        upper_light_blue = np.array([120,255,255])
        
        mask_light_blue_long = cv2.inRange(hsv_light_blue_long, lower_light_blue, upper_light_blue)
        mask_light_blue_short = cv2.inRange(hsv_light_blue_short, lower_light_blue, upper_light_blue)
        
        contours_light_blue_long, _ = cv2.findContours(mask_light_blue_long, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        contours_light_blue_short, _ = cv2.findContours(mask_light_blue_short, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

        for contour in contours_light_blue_long:            ## long
            area = cv2.contourArea(contour)
            (x, y, w, h) = cv2.boundingRect(contour)
            rect = cv2.minAreaRect(contour)
            box = cv2.boxPoints(rect)
            box = np.int0(box)
            cx = int((2 * x + w) / 2)
            cy = int((2 * y + h) / 2)
            centroid = cx, cy

            if (area > 9000 and cx <= lineX2):
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(frame, 'light_blue'+ str(area), (x, h), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 2)
                #cv2.circle(frame, (cx, cy), 2, (255, 255, 255), -2)
                #cv2.circle(mask_light_blue_long, (cx, cy), 2, (0, 0, 255), -2)
                process(x, y, w, h, 'light_blue')
        cv2.putText(frame, str(count_light_blue), (200, 245), font, 1, (0, 255, 0), 2)

        for contour in contours_light_blue_short:            ## short
            area = cv2.contourArea(contour)
            (x, y, w, h) = cv2.boundingRect(contour)
            rect = cv2.minAreaRect(contour)
            box = cv2.boxPoints(rect)
            box = np.int0(box)
            cx = int((2 * x + w) / 2)
            cy = int((2 * y + h) / 2)
            centroid = cx, cy

            if (1000 < area < 5000 and cx <= lineX2):
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(frame, 'light_blue_short'+ str(area), (x, h), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 2)
                #cv2.circle(frame, (cx, cy), 2, (255, 255, 255), -2)
                #cv2.circle(mask_light_blue_short, (cx, cy), 2, (0, 0, 255), -2)
                process(x, y, w, h, 'light_blue_short')
        cv2.putText(frame, str(count_light_blue_short), (250, 245), font, 1, (0, 255, 0), 2)


        ##########################################################################

        ############################### egg_color ###############################
        lower_egg_color = np.array([12,95,200])
        upper_egg_color = np.array([20,170,255])
        mask_egg_color = cv2.inRange(hsv, lower_egg_color, upper_egg_color)
        res_egg_color = cv2.bitwise_and(hsv,hsv, mask= mask_egg_color)
        kernel = np.ones((3,3),np.uint8)
        dilation = cv2.dilate(res_egg_color,kernel,iterations = 1)
        contours, _ = cv2.findContours(mask_egg_color, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
##        cv2.putText(frame, str(count_egg_color), (200, 285), font, 1, (0, 255, 0), 2)

        for contour in contours:            ## long
            area = cv2.contourArea(contour)
            (x, y, w, h) = cv2.boundingRect(contour)
            rect = cv2.minAreaRect(contour)
            box = cv2.boxPoints(rect)
            box = np.int0(box)
            cx = int((2 * x + w) / 2)
            cy = int((2 * y + h) / 2)
            centroid = cx, cy

            if (area > 6000 and cx <= lineX2):
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(frame, 'egg_color'+ str(area), (x, h), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 2)
                #cv2.circle(frame, (cx, cy), 2, (255, 255, 255), -2)
                #cv2.circle(mask_egg_color, (cx, cy), 2, (0, 0, 255), -2)
                process(x, y, w, h, 'egg_color')
                
        cv2.putText(frame, str(count_egg_color), (200, 285), font, 1, (0, 255, 0), 2)

        for contour in contours:            ## short
            area = cv2.contourArea(contour)
            (x, y, w, h) = cv2.boundingRect(contour)
            rect = cv2.minAreaRect(contour)
            box = cv2.boxPoints(rect)
            box = np.int0(box)
            cx = int((2 * x + w) / 2)
            cy = int((2 * y + h) / 2)
            centroid = cx, cy

            if (1000 < area < 5000 and cx <= lineX2):
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(frame, 'egg_color_short'+ str(area), (x, h), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 2)
                #cv2.circle(frame, (cx, cy), 2, (255, 255, 255), -2)
                #cv2.circle(mask_egg_color, (cx, cy), 2, (0, 0, 255), -2)
                process(x, y, w, h, 'egg_color_short')
        cv2.putText(frame, str(count_egg_color_short), (250, 285), font, 1, (0, 255, 0), 2)

        ##########################################################################

        ############################### black ###############################
        lower_black = np.array([100,0,0])
        upper_black = np.array([130,255,78])
        mask_black_long = cv2.inRange(hsv_black_long, lower_black, upper_black)
        mask_black_short = cv2.inRange(hsv_black_short, lower_black, upper_black)
       
        contours_black_long, _ = cv2.findContours(mask_black_long, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        contours_black_short, _ = cv2.findContours(mask_black_short, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

        for contour in contours_black_long:            ## long
            area = cv2.contourArea(contour)
            (x, y, w, h) = cv2.boundingRect(contour)
            rect = cv2.minAreaRect(contour)
            box = cv2.boxPoints(rect)
            box = np.int0(box)
            cx = int((2 * x + w) / 2)
            cy = int((2 * y + h) / 2)
            centroid = cx, cy

            if (area > 8000 and cx <= lineX2):
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(frame, 'black'+ str(area), (x, h), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 2)
                #cv2.circle(frame, (cx, cy), 2, (255, 255, 255), -2)
                #cv2.circle(mask_black_long, (cx, cy), 2, (0, 0, 255), -2)
                process(x, y, w, h, 'black')
        cv2.putText(frame, str(count_black), (150, 325), font, 1, (0, 255, 0), 2)

        for contour in contours_black_short:            ## short
            area = cv2.contourArea(contour)
            (x, y, w, h) = cv2.boundingRect(contour)
            rect = cv2.minAreaRect(contour)
            box = cv2.boxPoints(rect)
            box = np.int0(box)
            cx = int((2 * x + w) / 2)
            cy = int((2 * y + h) / 2)
            centroid = cx, cy

            if (1500 < area < 8000 and cx <= lineX2):
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(frame, 'black_short'+ str(area), (x, h), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 2)
                #cv2.circle(frame, (cx, cy), 2, (255, 255, 255), -2)
                #cv2.circle(mask_black_short, (cx, cy), 2, (0, 0, 255), -2)
                process(x, y, w, h, 'black_short')
        cv2.putText(frame, str(count_black_short), (200, 325), font, 1, (0, 255, 0), 2)

        ##########################################################################

        ############################### brown ###############################
        lower_brown = np.array([140,20,20])
        upper_brown = np.array([255,100,100])
        mask_brown_long = cv2.inRange(hsv_brown_long, lower_brown, upper_brown)
        mask_brown_short = cv2.inRange(hsv_brown_short, lower_brown, upper_brown)
       
        contours_brown_long, _ = cv2.findContours(mask_brown_long, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        contours_brown_short, _ = cv2.findContours(mask_brown_short, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

        for contour in contours_brown_long:            ## long
            area = cv2.contourArea(contour)
            (x, y, w, h) = cv2.boundingRect(contour)
            rect = cv2.minAreaRect(contour)
            box = cv2.boxPoints(rect)
            box = np.int0(box)
            cx = int((2 * x + w) / 2)
            cy = int((2 * y + h) / 2)
            centroid = cx, cy

            if (area > 8000 and cx <= lineX2):
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(frame, 'brown'+ str(area), (x, h), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 2)
                #cv2.circle(frame, (cx, cy), 2, (255, 255, 255), -2)
                #cv2.circle(mask_brown_long, (cx, cy), 2, (0, 0, 255), -2)
                process(x, y, w, h, 'brown')
        cv2.putText(frame, str(count_brown), (150, 365), font, 1, (0, 255, 0), 2)

        for contour in contours_brown_short:            ## short
            area = cv2.contourArea(contour)
            (x, y, w, h) = cv2.boundingRect(contour)
            rect = cv2.minAreaRect(contour)
            box = cv2.boxPoints(rect)
            box = np.int0(box)
            cx = int((2 * x + w) / 2)
            cy = int((2 * y + h) / 2)
            centroid = cx, cy

            if (1500 < area < 8000 and cx <= lineX2):
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(frame, 'brown_short'+ str(area), (x, h), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 2)
                #cv2.circle(frame, (cx, cy), 2, (255, 255, 255), -2)
                #cv2.circle(mask_brown_short, (cx, cy), 2, (0, 0, 255), -2)
                process(x, y, w, h, 'brown_short')
        cv2.putText(frame, str(count_brown_short), (200, 365), font, 1, (0, 255, 0), 2)

        ##########################################################################

        ############################### red ###############################
        lower_red = np.array([0,160,130])
        upper_red = np.array([5,255,255])
        mask_red = cv2.inRange(hsv, lower_red, upper_red)
        res_red = cv2.bitwise_and(hsv,hsv, mask= mask_red)
        kernel = np.ones((3,3),np.uint8)
        dilation = cv2.dilate(res_red,kernel,iterations = 1)
        contours, _ = cv2.findContours(mask_red, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

        for contour in contours:            ## long
            area = cv2.contourArea(contour)
            (x, y, w, h) = cv2.boundingRect(contour)
            rect = cv2.minAreaRect(contour)
            box = cv2.boxPoints(rect)
            box = np.int0(box)
            cx = int((2 * x + w) / 2)
            cy = int((2 * y + h) / 2)
            centroid = cx, cy

            if (area > 7500 and cx <= lineX2):
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(frame, 'red'+ str(area), (x, h), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 2)
                #cv2.circle(frame, (cx, cy), 2, (255, 255, 255), -2)
                #cv2.circle(mask_red, (cx, cy), 2, (0, 0, 255), -2)
                process(x, y, w, h, 'red')
        cv2.putText(frame, str(count_red), (150, 405), font, 1, (0, 255, 0), 2)

        for contour in contours:            ## short
            area = cv2.contourArea(contour)
            (x, y, w, h) = cv2.boundingRect(contour)
            rect = cv2.minAreaRect(contour)
            box = cv2.boxPoints(rect)
            box = np.int0(box)
            cx = int((2 * x + w) / 2)
            cy = int((2 * y + h) / 2)
            centroid = cx, cy

            if (1000 < area < 5000 and cx <= lineX2):
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(frame, 'red_short'+ str(area), (x, h), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 2)
                #cv2.circle(frame, (cx, cy), 2, (255, 255, 255), -2)
                #cv2.circle(mask_red, (cx, cy), 2, (0, 0, 255), -2)
                process(x, y, w, h, 'red_short')
        cv2.putText(frame, str(count_red_short), (200, 405), font, 1, (0, 255, 0), 2)

        ##########################################################################

        ############################### orange ###############################
        lower_orange = np.array([5,160,100])
        upper_orange = np.array([20,255,255])
        mask_orange = cv2.inRange(hsv, lower_orange, upper_orange)
        res_orange = cv2.bitwise_and(hsv,hsv, mask= mask_orange)
        kernel = np.ones((3,3),np.uint8)
        dilation = cv2.dilate(res_orange,kernel,iterations = 1)
        contours, _ = cv2.findContours(mask_orange, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

        for contour in contours:            ## long
            area = cv2.contourArea(contour)
            (x, y, w, h) = cv2.boundingRect(contour)
            rect = cv2.minAreaRect(contour)
            box = cv2.boxPoints(rect)
            box = np.int0(box)
            cx = int((2 * x + w) / 2)
            cy = int((2 * y + h) / 2)
            centroid = cx, cy

            if (area > 7500 and cx <= lineX2):
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(frame, 'orange'+ str(area), (x, h), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 2)
                #cv2.circle(frame, (cx, cy), 2, (255, 255, 255), -2)
                #cv2.circle(mask_orange, (cx, cy), 2, (0, 0, 255), -2)
                process(x, y, w, h, 'orange')
        cv2.putText(frame, str(count_orange), (150, 445), font, 1, (0, 255, 0), 2)

        for contour in contours:            ## short
            area = cv2.contourArea(contour)
            (x, y, w, h) = cv2.boundingRect(contour)
            rect = cv2.minAreaRect(contour)
            box = cv2.boxPoints(rect)
            box = np.int0(box)
            cx = int((2 * x + w) / 2)
            cy = int((2 * y + h) / 2)
            centroid = cx, cy

            if (1000 < area < 5000 and cx <= lineX2):
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(frame, 'orange_short'+ str(area), (x, h), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 2)
                #cv2.circle(frame, (cx, cy), 2, (255, 255, 255), -2)
                #cv2.circle(mask_orange, (cx, cy), 2, (0, 0, 255), -2)
                process(x, y, w, h, 'orange_short')
        cv2.putText(frame, str(count_orange_short), (200, 445), font, 1, (0, 255, 0), 2)

        ##########################################################################

        ############################### purple ###############################
        lower_purple = np.array([120,50,10])
        upper_purple = np.array([130,255,255])
        mask_purple_long = cv2.inRange(hsv_brown_long, lower_purple, upper_purple)
        mask_purple_short = cv2.inRange(hsv_brown_short, lower_purple, upper_purple)
       
        contours_purple_long, _ = cv2.findContours(mask_purple_long, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        contours_purple_short, _ = cv2.findContours(mask_purple_short, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

        for contour in contours_purple_long:            ## long
            area = cv2.contourArea(contour)
            (x, y, w, h) = cv2.boundingRect(contour)
            rect = cv2.minAreaRect(contour)
            box = cv2.boxPoints(rect)
            box = np.int0(box)
            cx = int((2 * x + w) / 2)
            cy = int((2 * y + h) / 2)
            centroid = cx, cy

            if (area > 7500 and cx <= lineX2):
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(frame, 'purple'+ str(area), (x, h), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 2)
                #cv2.circle(frame, (cx, cy), 2, (255, 255, 255), -2)
                #cv2.circle(mask_purple_long, (cx, cy), 2, (0, 0, 255), -2)
                process(x, y, w, h, 'purple')
        cv2.putText(frame, str(count_purple), (150, 485), font, 1, (0, 255, 0), 2)

        for contour in contours_purple_short:            ## short
            area = cv2.contourArea(contour)
            (x, y, w, h) = cv2.boundingRect(contour)
            rect = cv2.minAreaRect(contour)
            box = cv2.boxPoints(rect)
            box = np.int0(box)
            cx = int((2 * x + w) / 2)
            cy = int((2 * y + h) / 2)
            centroid = cx, cy

            if (1500 < area < 5000 and cx <= lineX2):
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(frame, 'purple_short'+ str(area), (x, h), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 2)
                #cv2.circle(frame, (cx, cy), 2, (255, 255, 255), -2)
                #cv2.circle(mask_purple_short, (cx, cy), 2, (0, 0, 255), -2)
                process(x, y, w, h, 'purple_short')
        cv2.putText(frame, str(count_purple_short), (200, 485), font, 1, (0, 255, 0), 2)

        ##########################################################################

        cv2.putText(frame, 'Yellow :', (20, 45), font, 1, (0, 255, 0), 2)
        cv2.putText(frame, 'Light green :', (20, 85), font, 1, (0, 255, 0), 2)
        cv2.putText(frame, 'Dark green :', (20, 125), font, 1, (0, 255, 0), 2)
        cv2.putText(frame, 'Dark blue :', (20, 165), font, 1, (0, 255, 0), 2)
        cv2.putText(frame, 'Pink :', (20, 205), font, 1, (0, 255, 0), 2)
        cv2.putText(frame, 'Light blue :', (20, 245), font, 1, (0, 255, 0), 2)
        cv2.putText(frame, 'Egg color :', (20, 285), font, 1, (0, 255, 0), 2)
        cv2.putText(frame, 'Black :', (20, 325), font, 1, (0, 255, 0), 2)
        cv2.putText(frame, 'Brown :', (20, 365), font, 1, (0, 255, 0), 2)
        cv2.putText(frame, 'Red :', (20, 405), font, 1, (0, 255, 0), 2)
        cv2.putText(frame, 'Orange :', (20, 445), font, 1, (0, 255, 0), 2)
        cv2.putText(frame, 'Purple :', (20, 485), font, 1, (0, 255, 0), 2)

        binary = mask_yellow_long + mask_yellow_short +mask_light_green +mask_dark_green +mask_dark_blue +mask_pink +mask_light_blue_long + mask_light_blue_short +mask_egg_color +mask_black_long +mask_black_short +mask_brown_long +mask_brown_short +mask_red +mask_orange +mask_purple_long+mask_purple_short
        
        cv2.imshow("binary", binary)
        #cv2.imshow('Video', frame)
        #cv2.imwrite('./bg.jpg', frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()

gui.title('Pencil Color Detection')
video = Button(gui, text = "Start", command = VDO,bg="red",width = 12,height = 1,fg="white",font='time12')
video.place(x = 200,y = 100)

gui.mainloop()


