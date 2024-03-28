from AI.src.sudoku.detect.new_detect import MatchingSudoku

def sudoku(screenshot, debug = False, validation=None,iteration=0):
    matcher = MatchingSudoku(screenshot,debug,validation,iteration)
    print(matcher.find_numbers())