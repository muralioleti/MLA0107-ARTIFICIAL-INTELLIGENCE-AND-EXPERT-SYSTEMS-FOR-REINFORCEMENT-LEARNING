% Facts
male(john).
male(bill).
male(bob).

female(mary).
female(sue).
female(marry).

parent(john, bob).
parent(john, sue).
parent(mary, bob).
parent(mary, sue).
parent(bob, tom).
parent(bob, ann).
parent(sue, jim).
parent(sue, emma).

% Rules
father(X, Y) :- male(X), parent(X, Y).
mother(X, Y) :- female(X), parent(X, Y).

sibling(X, Y) :- parent(Z, X), parent(Z, Y), X \= Y.
brother(X, Y) :- male(X), sibling(X, Y).
sister(X, Y) :- female(X), sibling(X, Y).

grandparent(X, Y) :- parent(X, Z), parent(Z, Y).
grandchild(X, Y) :- grandparent(Y, X).

uncle(X, Y) :- brother(X, Z), parent(Z, Y).

% Queries
% a. Who is the father of Bob?
% father(X, bob).

% b. Who is the grandson of Y?
% grandchild(tom, Y).

% c. Is Bill the uncle of Sue?
% uncle(bill, sue).

% d. Who is the mother of Marry's child?
% mother(X, marry).
