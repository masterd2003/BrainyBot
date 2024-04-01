from AI.src.sudoku.detect.new_detect import MatchingSudoku

# atm only prints the numbers and doesnt call asp
# helper should call asp and tappy server to give imputs to the game
def sudoku(screenshot, debug = False, validation=None,iteration=0):
    matcher = MatchingSudoku(screenshot,debug,validation,iteration)
    print(matcher.find_numbers())