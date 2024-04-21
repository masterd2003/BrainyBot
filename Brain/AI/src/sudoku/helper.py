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
    matcher = MatchingSudoku(screenshot,debug,validation,iteration)
    print(matcher.find_numbers())
    """
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

    fieldmatrix = [[0, 0, 0, 0, 0, 1, 2, 3, 0],
                   [1, 2, 3, 0, 0, 8, 0, 4, 0],
                   [8, 0, 4, 0, 0, 7, 6, 5, 0],
                   [7, 6, 5, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 1, 2, 3],
                   [0, 1, 2, 3, 0, 0, 8, 0, 4],
                   [0, 8, 0, 4, 0, 0, 7, 6, 5],
                   [0, 7, 6, 5, 0, 0, 0, 0, 0]]
    
    # if fieldmatrix!=None:
    #     input,colors,tubes,balls,on = asp_input(balls_chart)
    # else:
    #     input=[]
    #     tubes=[]
    if(debug):
        # no idea what canny_threshold is look in ballsort helper
        # return matcher.canny_threshold
        return "patatjes"
    solution = DLVSolution()
    moves = solution.call_asp(fieldmatrix)

    # i dont think sorting is needed
    # moves.sort(key=lambda x: x.get_step())
    # ons.sort(key=lambda x: x.get_step())

    os.chdir(CLIENT_PATH)

    button_x, button_y, x, y = 0, 0, 0, 0
    if moves == zeros:
        print("No moves found.")
        return
    feedback=Feedback()
    
    for i in range(len(moves)):
        for j in range(len(moves[0])):
            x_botton = "x coordinaat van knop " + str(moves[i][j])
            y_button = "y coordinaat van knop " + str(moves[i][j])
            x = "x coordinaat van vakje" + str(i + 1) + ", " + str(j + 1)
            y = "y coordinaat van vakje" + str(i + 1) + ", " + str(j + 1)
            print(x_botton, "; ", y_button)
            print(x , "; ", y)
    """

            

def sudoku1(screenshot, debug = False, validation=None,iteration=0):
    matcher = MatchingSudoku(screenshot,debug,validation,iteration)
    print(matcher.find_numbers())

    fieldmatrix = matcher.find_numbers()

    # if fieldmatrix!=None:
    #     input,colors,tubes,balls,on = asp_input(balls_chart)
    # else:
    #     input=[]
    #     tubes=[]
    if(debug):
        # no idea what canny_threshold is look in ballsort helper
        # return matcher.canny_threshold
        return "patatjes"
    solution = DLVSolution()
    moves = solution.call_asp(fieldmatrix)

    # i dont think sorting is needed
    # moves.sort(key=lambda x: x.get_step())
    # ons.sort(key=lambda x: x.get_step())

    os.chdir(CLIENT_PATH)

    coordinates = []
    button_x, button_y, x, y = 0, 0, 0, 0
    if len(moves)==0:
        print("No moves found.")
        return
    feedback=Feedback()
    
    for i in range(len(moves)):
        move=moves[i]
        for edge in move:
            button_x = edge.get_x1()
            button_y = edge.get_y1()
            x = edge.get_xOnScreen()
            y = edge.get_yOnScreen()
        # previous_tube = __get_ball_tube(move.get_ball(), ons, move.get_step())
        # next_tube = move.get_tube()
        # for tube in tubes:
        #     if tube.get_id() == previous_tube:
        #         x1 = tube.get_x()
        #         y1 = tube.get_y()
        #     elif tube.get_id() == next_tube:
        #         x2 = tube.get_x()
        #         y2 = tube.get_y()
        coordinates.append({'x1': button_x, 'y1': button_x, 'x2': x, 'y2': y})
        os.system(f"python3 client3.py --url http://{TAPPY_ORIGINAL_SERVER_IP}:8000 --light 'tap {button_x} {button_y}'")
        time.sleep(0.25)
        os.system(f"python3 client3.py --url http://{TAPPY_ORIGINAL_SERVER_IP}:8000 --light 'tap {x} {y}'")
        