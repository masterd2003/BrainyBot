#show swap/2.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  make graph not oriented
edge(Y, X, P) :- edge(X, Y, P).

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%   g&c
%DEN swap(ID1, ID2) | notSwap(ID1, ID2) :- node(ID1, _), node(ID2, _), ID1<ID2.
%DEN swap(ID2, ID1) :- swap(ID1, ID2).
%DEN swappedNodes(ID) :- swap(ID, _).
{swap1(ID1,ID2): node(ID1, T), node(ID2, T1), T1!=T, edge(ID1,ID2, _),ID1<ID2}=1.
swap(ID1,ID2):-swap1(ID1,ID2). 
swap(ID2,ID1):-swap1(ID1,ID2). 


% exchange node`s edges
exchangedEdge(ID1, ID3, P) :- edge(ID2, ID3, P), swap(ID1, ID2), ID1!=ID3.%DEN, node(ID1, T), node(ID3, T).
deletedEdge(ID2, ID3) :- edge(ID2, ID3, P), swap(ID1, ID2).

% at least 3 adjacent
atLeast3Adjacent(ID2, ID3, P) :- exchangedEdge(ID1, ID2, P), exchangedEdge(ID1, ID3, P), ID2!=ID3.
atLeast3Adjacent(ID1, ID3, P) :- exchangedEdge(ID1, ID2, P), edge(ID2, ID3, P), ID1!=ID3, node(ID2, T), node(ID3, T), not deletedEdge(ID2, ID3).
atLeast3Adjacent(ID1, ID3, P) :- atLeast3Adjacent(ID1, ID2, P), edge(ID2, ID3, P), ID1!=ID3, node(ID2, T), node(ID3, T), not deletedEdge(ID2, ID3).

% only a single swap
%DEN :- #count{ID1, ID2 : swap(ID1, ID2)} != 2.
%DEN :- swap(ID1, ID2), not swap(ID2, ID1).

% can t swap between not adjacent nodes
%DEN edgeWithoutPosition(ID1,ID2) :- edge(ID1,ID2, _).

%DEN :- swap(ID1, ID2), not edgeWithoutPosition(ID1,ID2).

% can t swap between nodes with the same candy type
%DEN :- swap(ID1, ID2), node(ID1, T), node(ID2, T).

% at least 3 nodes on the same position
:- #count{ID1, ID3, P : atLeast3Adjacent(ID1, ID3, P)} == 0, not thereIsASwapWithColourBomb(1).


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  adjacent weak
adjacentNodes(ID) :- atLeast3Adjacent(ID, _, _).
adjacentNodes(ID) :- atLeast3Adjacent(_, ID, _).
adjacentNodes(ID) :- exchangedEdge(ID, _).
adjacentNodes(ID) :- exchangedEdge(_, ID).
countAdjacentNodes(C) :- #count{ID : adjacentNodes(ID)} = C.

nodesWithDifferentType(ID) :- node(ID, _), not adjacentNodes(ID).
:~ nodesWithDifferentType(ID). [1@4, ID]

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  bomb weak
:~ bomb(ID), not adjacentNodes(ID). [1@2, ID]

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% horizontal weak
:~ horizontal(ID), not adjacentNodes(ID). [1@3, ID]

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% vertical weak
:~ vertical(ID), not adjacentNodes(ID). [1@3, ID]

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  colour Bomb weak
colourBombCount(ID1, T, C) :- #count{IDX : node(IDX, T)} = C, node(ID1, "colourB"), edge(ID1, ID2, _), node(ID2, T). % count nodes for each colourBomb, max relative
maxCountForColourBomb(K) :- #max{C, ID, T : colourBombCount(ID, T, C)} = K. % max absolute
maxColourBomb(ID, T) :- maxCountForColourBomb(K), colourBombCount(ID, T, K). % find max colourBomb
swapWithColourBomb(ID1, ID2) :- maxColourBomb(ID1, T), edge(ID1, ID2, _), node(ID2, T), maxCountForColourBomb(K), countAdjacentNodes(C), K > C. % choose swap with colourBomb
thereIsASwapWithColourBomb(1) :- swapWithColourBomb(ID1, ID2).

:~ swapWithColourBomb(ID1, ID2), not swap(ID1, ID2). [1@5, ID1, ID2] % if exists a swap can match so much candy

%
% Level 1 demo. Prefer to swap blue candies
%
%:~ exchangedEdge(ID1, ID3, P), node(ID1, T), node(ID3, T), T != "blue". [1@1, ID1, ID2]
