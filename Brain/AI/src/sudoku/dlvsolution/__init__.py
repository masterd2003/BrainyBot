from languages.asp.asp_mapper import ASPMapper

from AI.src.sudoku.dlvsolution.helpers import Edge
'''
def get_ancestor_classes(cls):
    ancestors = []
    for ancestor in cls.__bases__:
        ancestors.append(ancestor)
        ancestors.extend(get_ancestor_classes(ancestor))
    return ancestors

#print(f"SWAP has:{get_ancestor_classes(Swap)}")
'''

# idk of die map hier moet staan of gwn in de call asp zoals bij ball sort kga zien

# ASPMapper.get_instance().register_class(Swap)
ASPMapper.get_instance().register_class(Edge)
# ASPMapper.get_instance().register_class(InputNode)
# ASPMapper.get_instance().register_class(InputBomb)
# ASPMapper.get_instance().register_class(InputHorizontal)
# ASPMapper.get_instance().register_class(InputVertical)
# ASPMapper.get_instance().register_class(AtLeast3Adjacent)
