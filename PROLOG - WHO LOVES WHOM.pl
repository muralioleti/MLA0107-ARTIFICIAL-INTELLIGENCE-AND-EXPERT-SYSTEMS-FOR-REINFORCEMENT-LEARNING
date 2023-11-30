% Define relationships
loves(john, mary).
loves(jane, peter).
loves(peter, alice).
loves(john, alice).

% Define rule to find out who loves Alice
who_loves_alice(X) :- loves(X, alice).
