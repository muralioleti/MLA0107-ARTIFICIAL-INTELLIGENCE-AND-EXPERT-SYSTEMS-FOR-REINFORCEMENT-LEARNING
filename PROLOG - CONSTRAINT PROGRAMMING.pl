:- use_module(library(clpfd)).

% N-Queens Problem Solver
n_queens(N, Queens) :-
    length(Queens, N),
    Queens ins 1..N,
    safe_queens(Queens),
    label(Queens).

% Check if two queens are safe from attacking each other
safe_queens([]).
safe_queens([Q|Queens]) :-
    no_attack(Q, Queens, 1),
    safe_queens(Queens).

% Check if a queen can attack any queen in the list
no_attack(_, [], _).
no_attack(Q1, [Q2|Queens], Dist) :-
    Q1 #\= Q2,
    Q1 + Dist #\= Q2,
    Q1 - Dist #\= Q2,
    NextDist is Dist + 1,
    no_attack(Q1, Queens, NextDist).

% Print the chessboard with queens
print_chessboard(Queens) :-
    length(Queens, N),
    between(1, N, Row),
    nl,
    print_row(Queens, Row, 1, N),
    fail.
print_chessboard(_).

print_row([], _, _, _).
print_row([Q|Queens], Row, Col, N) :-
    (Q =:= Col -> write('Q ') ; write('. ')),
    NextCol is Col + 1,
    print_row(Queens, Row, NextCol, N).

% Example usage for 4-Queens
?- n_queens(4, Queens), print_chessboard(Queens).
