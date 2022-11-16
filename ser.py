import serial
import cv2
import math
import numpy as np


class ACLink():

    def __init__(self, *args, **kwargs) -> None:
        self.ser_input = None
        self.the_order = b'm'
        self.number = 100
        self.number1 = 100
        self.number2 = 100
        self.open(*args, **kwargs)

    def send_order(self):
        self.ser_input.write(self.the_order.encode("gbk"))
        self.ser_input.write([int(self.number)])
        self.ser_input.write([int(self.number1)])
        self.ser_input.write([int(self.number2)])
        print(self.the_order, int(self.number),
              int(self.number1), int(self.number2))

    def open(self, port='/dev/ttyAMAO', baundrate=115200) -> None:
        try:
            self.ser_input = serial.Serial(port, baundrate)
        except Exception as error:
            print('___open error___:', error)

    def set_order_wjs(self, the_angle, the_pos_y, the_pos_x) -> None:
        self.the_order = 'm'
        self.number = little_check(the_pos_x + 100)
        self.number1 = little_check(the_pos_y + 100)
        self.number2 = little_check(the_angle + 100)

    def order_check(self):
        self.number = little_check(self.number)
        self.number1 = little_check(self.number1)
        self.number2 = little_check(self.number2)
    
    def order_reset(self) -> None:
        self.the_order = b'm'
        self.number = 100
        self.number1 = 100
        self.number2 = 100

def little_check(self, number) -> int:
    if 80 > self.number > 120 :
        return number
    elif number > 120 :
        number = 120
        return number
    elif number < 80 :
        number = 80
        return number
    else:
        return number


def find_hough_line(thresh, is_all_return=0):

    thresh = cv2.Canny(thresh, 50, 120, apertureSize=5)

    lines = cv2.HoughLinesP(thresh, 3, np.pi / 180, 100,
                            minLineLength=40, maxLineGap=50)

    list_lines_angle = []
    list_lines_pos = []

    list_all_line = []

    if lines is not None:
        line1 = lines[:, 0, :]
        for x1, y1, x2, y2 in line1[::]:
            if (y1 - y2) == 0:

                h = np.pi / 2
            else:

                h = math.atan((x1 - x2) / (y1 - y2))

                if is_all_return == 0:

                    list_lines_angle.append(int(math.degrees(h)) * -1)
                    list_lines_pos.append([(x1 + x2) / 2, (y1 + y2) / 2])
                else:
                    list_all_line.append(
                        [[x1, y1], [x2, y2], int(math.degrees(h)) * -1])

    if is_all_return == 0:
        the_angle = 100
        the_pos_x = 100
        the_pos_y = 100

        if list_lines_angle:

            the_angle = int(np.average(list_lines_angle))
            the_pos_x, the_pos_y = np.average(list_lines_pos, axis=0)

    #    return the_angle, int(the_pos_y * 100 / 1280), int(the_pos_x * 100 / 720)
        return the_angle, int(the_pos_y), int(the_pos_x)
    else:
        return list_all_line


def pic(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    thresh_img = cv2.adaptiveThreshold(
        gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 5)
    return thresh_img


if __name__ == '__main__':
    frameWidth = 1280
    frameHeight = 720
    order = 's'
    acfly = ACLink(port='/dev/ttyAMAO', baundrate=115200)

  # try:
    # ser = serial.Serial("/dev/ttyAMA0", 115200)
  # except Exception as error:
   #    print('___open error___:', error)

    cap = cv2.VideoCapture(1)
    while cap.isOpened():
        ret, frame = cap.read()
        thresh = pic(frame)

        list = find_hough_line(thresh, is_all_return=0)
        # rho_err = list[2] - frameWidth/2

        # if rho_err < 0:
        #     rho_err = -rho_err

        # number = int(list[1] * 100 / 1280)
        # number2 = int(rho_err * 100 / 720)
        # #  open(ser_input=ser_input)

        #  print(list[0], number, number2)
        # send(ser, order, number, number2)
        acfly.set_order_wjs(list[0], list[1], list[2])
