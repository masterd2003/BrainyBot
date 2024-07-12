import os

from languages.asp.asp_input_program import ASPInputProgram
from languages.asp.asp_mapper import ASPMapper

from AI.src.sudoku.constant import RESOURCES_PATH
from AI.src.sudoku.dlvsolution.helpers import chooseDLVSystem, Edge


class DLVSolution:

    def __init__(self):
        try:
            self.__handler = chooseDLVSystem()
            # these are the game fields
            self.__static_facts = ASPInputProgram()
            # these are the sudoku rules
            self.__fixed_input_program = ASPInputProgram()

        except Exception as e:
            print(str(e))

    def __init_static_facts(self, fieldmatrix):
        # converts fieldmatrix to asp facts
        for row in range(0, 9):
            for col in range(0, 9):
                if fieldmatrix[row][col] != 0:
                # +1 because asp starts counting from 1
                    self.__static_facts.add_object_input(Edge(row+1, col+1, fieldmatrix[row][col]))


    def __init_fixed(self):
        self.__fixed_input_program.add_files_path(os.path.join(RESOURCES_PATH, "sudoku.txt"))

    # main function that calls the asp solver
    def call_asp(self, fieldmatrix: []):

        ASPMapper.get_instance().register_class(Edge)

        # add the static facts to the asp program (here this is the starting soduku field)
        self.__init_static_facts(fieldmatrix)
        # add the sudoku rules
        self.__init_fixed()

        self.__handler.add_program(self.__static_facts)
        self.__handler.add_program(self.__fixed_input_program)

        moves = []

        # asp is called here and then you get the answer set
        answer_sets = self.__handler.start_sync()

        # answer set is split into a list of strings
        splitList = answer_sets.get_output().split(", ")
        cellList = []
        for i in splitList:
            if "sudoku" in i:
                cellList.append(i)
        print(cellList)

        # outputmatrix is constructed from the answer set
        # outputmatrix is the sudoku field after the asp solver has solved it
        outputmatrix = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0]]
        for elem in cellList:
            row = int(elem[7])
            col = int(elem[9])
            val = int(elem[11])
            outputmatrix[row-1][col-1] = val
        
        print(outputmatrix)
        return outputmatrix
        