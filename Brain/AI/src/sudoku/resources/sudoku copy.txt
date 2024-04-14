% code inspiratie: https://ddmler.github.io/asp/2018/07/10/answer-set-programming-sudoku-solver.html



row(1..9).

col(1..9).

val(1..9).



{cell(X,Y,N): val(N)}=1 :- row(X) ,col(Y).



:- cell(X1,Y,N), cell(X2,Y,N), X1 != X2.

:- cell(X,Y1,N), cell(X,Y2,N), Y1 != Y2.



block(1..3,1..3,1).

block(1..3,4..6,2).

block(1..3,7..9,3).



block(4..6,1..3,4).

block(4..6,4..6,5).

block(4..6,7..9,6).



block(7..9,1..3,7).

block(7..9,4..6,8).

block(7..9,7..9,9).



:- cell(X1,Y1,N), cell(X2,Y2,N), block(X1,Y1,B), block(X2,Y2,B), X1 != X2, Y1 != Y2.