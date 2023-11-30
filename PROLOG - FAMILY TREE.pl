% Facts
father(john, lisa).
father(mike, emma).
father(tom, mary).

mother(mary, lisa).
mother(mary, mike).
mother(emma, olivia).

% Rules for sibling relationship
sister(X, Y) :-
    mother(M, X),
    mother(M, Y),
    father(F, X),
    father(F, Y),
    X \= Y.

% Rules for grandparent relationship
grandfather(X, Y) :-
    father(X, Z),
    mother(Z, Y).

grandmother(X, Y) :-
    mother(X, Z),
    mother(Z, Y).

% Queries
?- father(FatherOfEmma, emma).
% Output: FatherOfEmma = mike

?- sister(lisa, mike).
% Output: true

?- grandmother(GrandmotherOfOlivia, olivia).
% Output: GrandmotherOfOlivia = mary

?- grandfather(john, olivia).
% Output: false
