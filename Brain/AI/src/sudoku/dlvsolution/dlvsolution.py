# imports fixen
import os

from base.option_descriptor import OptionDescriptor
from languages.asp.asp_input_program import ASPInputProgram
from languages.asp.asp_mapper import ASPMapper
import numpy as np

from AI.src.sudoku.constant import RESOURCES_PATH
# from AI.src.ball_sort.dlvsolution.helpers import choose_dlv_system, Color, Ball, Tube, Move, On, GameOver
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
        # self.__fixed_input_program.add_files_path(os.path.join(RESOURCES_PATH, "sudoku.txt"))
        # self.__fixed_input_program.add_files_path("/home/david/Documents/GitHub/BrainyBot/Brain/AI/src/sudoku/resources/sudoku.txt")

    # main function that calls the asp solver
    def call_asp(self, fieldmatrix: []):

        ASPMapper.get_instance().register_class(Edge)

        # add the static facts to the asp program (here this is the starting soduku field)
        self.__init_static_facts(fieldmatrix)
        # add the sudoku rules
        self.__init_fixed()

        # hier kijken voor of de facts fout zijn
        print("static facts")
        print(self.__static_facts.get_programs())

        # print("fixed input program")
        # print(self.__fixed_input_program.get_programs())
        
        print("fixed input program path")
        print(self.__fixed_input_program.get_files_paths())
        print("kroketjes")
        self.__handler.add_program(self.__static_facts)
        self.__handler.add_program(self.__fixed_input_program)

        # print("handler")
        # print("handler 1")
        # print(self.__handler.get_input_program(0).get_programs())
        # print("handler 2")
        # print(self.__handler.get_input_program(1).get_programs())
        # # for i in self.__handler._collect_options(None):
        # #     print(i.get_programs())
        # print("einde handler")

        # option = OptionDescriptor("--filter=on/4, move/3, gameOver/1")
        # self.__handler.add_option(option)

        moves = []
        # ons = []

        # asp is called here and then you get the answer set
        answer_sets = self.__handler.start_sync()

        # print (f"Answer sets: {answer_sets.get_output()}")

        splitList = answer_sets.get_output().split(", ")
        cellList = []
        for i in splitList:
            if "sudoku" in i:
                cellList.append(i)
        print(cellList)
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
        
#         # idk if this is needed
#         print(answer_sets)

#         print("dit is de answer set ding")
#         answer_sets.get_answer_sets_string()
#         print("einde answer sets ding")

#         # staat in answer_sets
#         answer_set =  answer_sets.get_optimal_answer_sets()

#         # answer_set =  answer_sets.get_answer_sets
#         # for ans in answer_set:
#         #     print (ans)

#         print("answer set")
#         print(answer_set)

        
#         print("patatjes")
#         # otherwise
#         # answer_set = answer_sets[0]

#         for obj in answer_set.get_atoms():
#             if isinstance(obj, Edge):
#                 moves.append(obj)
#             else: print("Not an edge, this is not supposed to happen")
        
#         return moves







#         # game_over = False

#         # step = 1
#         # while not game_over and step <= MAX_STEPS:
#         #     # for a in range(0,LOOK_AHEAD):
#         #     self.__dinamic_facts.add_program(f"step({str(step)}).")

#         #     # asp is called here and then you get the answer set
#         #     answer_sets = self.__handler.start_sync()

#         #     self.__dinamic_facts.clear_all()

#         #     print (f"Answer sets: {len(answer_sets.get_optimal_answer_sets())}")
#         #     assert_true(answer_sets is not None,"No solutions found for this level.")
            
#         #     #assert_true(answer_sets.get_errors() is None,
#         #     #            "Found error:\n" + str(answer_sets.get_errors()))
#         #     assert_true(len(answer_sets.get_optimal_answer_sets()) != 0,"No optimal solutions found for this level.")

#         #     for answer_set in answer_sets.get_optimal_answer_sets():
#         #         for obj in answer_set.get_atoms():
#         #             if isinstance(obj, Move):
#         #                 if obj.get_step() == step:
#         #                 #if step <= obj.get_step() < step+LOOK_AHEAD:
#         #                     self.__dinamic_facts.add_object_input(obj)
#         #                     moves.append(obj)

#         #             if isinstance(obj, On):
#         #                 if obj.get_step() == 1:
#         #                 #if 1 <= obj.get_step() < step+LOOK_AHEAD:
#         #                     ons.append(obj)
#         #                 if obj.get_step() == step + 1:
#         #                 #if step + 1 <= obj.get_step() < step+LOOK_AHEAD:
#         #                     self.__dinamic_facts.add_object_input(obj)
#         #                     ons.append(obj)

#         #             if isinstance(obj, GameOver):
#         #                 game_over = True
#         #         break # GB: 16 9 2023. Will not look a more than one optimal answer set
#         #     #step += LOOK_AHEAD
#         #     step+=1

#         # return moves, ons







# # class DLVSolution:

# #     def __init__(self):
# #         try:
# #             self.__handler = chooseDLVSystem()
# #             self.__variableInputProgram = None
# #             self.__fixedInputProgram = ASPInputProgram()

# #             self.__init_fixed()
# #         except Exception as e:
# #             print(str(e))

# #     def __init_fixed(self):
# #         print (f"Looking for rules in {os.path.join(RESOURCES_PATH, 'rules.dlv2')}")
# #         self.__fixedInputProgram.add_files_path(os.path.join(RESOURCES_PATH, "rules.dlv2"))
# #         self.__handler.add_program(self.__fixedInputProgram)

# #     def recall_asp(self, input):
# #         try:
# #             print (f"Calling ASP Solver.")
            
# #             self.__handler.remove_program_from_value(self.__variableInputProgram)
# #             self.__variableInputProgram = ASPInputProgram()
# #             print (f"Created ASP program.")
            
# #             # insert nodes from graph to asp program
# #             for element in input:
# #                 #print(element)
# #                 self.__variableInputProgram.add_object_input(element)
# #             print (f"Created Nodes.")
            
# #             '''
# #             for edge in edges:  # add edges input to dlv solution program
# #                 self.__variableInputProgram.add_object_input(edge)
# #             print (f"Created Edges.")
# #             '''
# #             index = self.__handler.add_program(self.__variableInputProgram)
# #             print (f"Let's start the solver.")
# #             answerSets = self.__handler.start_sync()
# #             print (f"Answer sets: {answerSets.get_output()}")
# #             #assert_true(answerSets is not None)
# #             #assert_true(isinstance(answerSets, Swap),
# #             #                "Error, result object is not Swap")
# #             #assert_true(answerSets.get_errors() == "",
# #             #            "Found error:\n" + str(answerSets.get_errors()))
# #             #assert_true(len(answerSets.get_optimal_answer_sets()) != 0)

# #             swap = None
# #             as_to_return = None
# #             for answerSet in answerSets.get_optimal_answer_sets():
# #                 print(answerSet)
# #                 for obj in answerSet.get_atoms():
# #                     print(obj)
# #                     if isinstance(obj, Swap):
# #                         swap = Swap(obj.get_id1(), obj.get_id2())
# #                         as_to_return = answerSet

# #             self.__handler.remove_program_from_id(index)
# #             return swap,as_to_return

# #         except Exception as e:
# #             print(str(e))
