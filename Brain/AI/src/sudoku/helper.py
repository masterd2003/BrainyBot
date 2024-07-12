import os
import sys
import time
import re
from AI.src.constants import CLIENT_PATH, TAPPY_ORIGINAL_SERVER_IP
from AI.src.sudoku.detect.new_detect import MatchingSudoku
from AI.src.sudoku.dlvsolution.dlvsolution import DLVSolution
from AI.src.sudoku.dlvsolution.helpers import Edge
from AI.src.ball_sort.dlvsolution.helpers import get_colors, get_balls_and_tubes, get_balls_position
from AI.src.abstraction.elementsStack import ElementsStacks
from AI.src.sudoku.constant import SRC_PATH

from AI.src.vision.feedback import Feedback


from AI.src.sudoku.detect.new_detect import MatchingSudoku

# atm only prints the numbers and doesnt call asp
# helper should call asp and tappy server to give imputs to the game
def sudoku(screenshot, debug = False, validation=None,iteration=0):
    start_time = time.time()
    start_process_time = time.process_time()
    matcher = MatchingSudoku(screenshot,debug,validation,iteration)

    debug = False

    zeros = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0]]

    fieldmatrix = matcher.find_numbers()
    coordinatesMatrix = matcher.get_coordinates()
    buttons = matcher.get_button_coordinates()
    vision_time = time.time()
    vision_process_time = time.process_time()

    think_start = time.time()
    think_start_process_time = time.process_time()
    if(debug):
        # no idea what canny_threshold is look in ballsort helper
        # return matcher.canny_threshold
        return "patatjes"
    solution = DLVSolution()
    moves = solution.call_asp(fieldmatrix)

    os.chdir(CLIENT_PATH)

    coordinates = []
    button_x, button_y, x, y = 0, 0, 0, 0
    if moves == zeros:
        print("No moves found.")
        return
    feedback=Feedback()
    
    for i in range(len(moves)):
        for j in range(len(moves[0])):
            x_button = buttons[moves[i][j]-1][0]
            y_button = buttons[moves[i][j]-1][1]
            x = coordinatesMatrix[i][j][0]
            y = coordinatesMatrix[i][j][1]
            x_button_str = "x coordinaat van knop " + str(moves[i][j]) + " = " + str(x_button)
            y_button_str = "y coordinaat van knop " + str(moves[i][j]) + " = " + str(y_button)
            x_str = "x coordinaat van vakje " + str(i + 1) + ", " + str(j + 1) + " = " + str(x)
            y_str = "y coordinaat van vakje " + str(i + 1) + ", " + str(j + 1) + " = " + str(y)
            print(x_button_str, "; ", y_button_str)
            print(x_str , "; ", y_str)
            
            # only press the button if it wasnt an initially filled in field
            # if fieldmatrix[i][j] == 0:

            #     coordinates.append({'x1': x_button, 'y1': y_button, 'x2': x, 'y2': y})
            #     os.system(f"python3 client3.py --url http://{TAPPY_ORIGINAL_SERVER_IP}:8000 --light 'tap {x_button} {y_button}'")
            #     time.sleep(0.25)
            #     os.system(f"python3 client3.py --url http://{TAPPY_ORIGINAL_SERVER_IP}:8000 --light 'tap {x} {y}'")

    total_time = time.time()
    total_process_time = time.process_time()
    print("empty fields: " + str(count_zeros(fieldmatrix)))
    print("actual time:")
    print("vision time = " + str(vision_time - start_time))
    print("think time = " + str(total_time - think_start))
    print("total time = " + str(total_time - start_time))
    print("process time:")
    print("vision time = " + str(vision_process_time - start_process_time))
    print("think time = " + str(total_process_time - think_start_process_time))
    print("total time = " + str(total_process_time - start_process_time))        

        
