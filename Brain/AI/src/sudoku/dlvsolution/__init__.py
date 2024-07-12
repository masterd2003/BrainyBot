from languages.asp.asp_mapper import ASPMapper

from AI.src.sudoku.dlvsolution.helpers import Edge, X, Y, N, SubGrid
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
ASPMapper.get_instance().register_class(Edge)
ASPMapper.get_instance().register_class(X)
ASPMapper.get_instance().register_class(Y)
ASPMapper.get_instance().register_class(N)
ASPMapper.get_instance().register_class(SubGrid)
