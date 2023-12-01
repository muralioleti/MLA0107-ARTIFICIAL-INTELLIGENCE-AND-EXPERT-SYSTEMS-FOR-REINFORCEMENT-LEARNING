% Facts
child(X) :- boy(X).
child(X) :- girl(X).

toy(X, doll) :- child(X).
toy(X, train) :- child(X).
toy(X, coal) :- child(X).

good(john). % Assuming John is a child who is good.

boy(jack). % Jack is a boy.

% Rules
no_doll(X) :- boy(X).
no_lump_of_coal(X) :- good(X), child(X).
