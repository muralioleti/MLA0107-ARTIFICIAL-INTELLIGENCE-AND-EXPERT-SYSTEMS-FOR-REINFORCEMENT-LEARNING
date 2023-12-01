% Facts: Define initial facts about individuals, their genders, and parent-child relationships
gender(john, male).
gender(jane, female).
gender(bob, male).
gender(alice, female).

parent(john, alice).
parent(jane, alice).
parent(bob, john).

% Rules: Define rules to determine parenthood based on gender and parent-child relationships
is_parent(Person) :- parent(Person, _).
is_parent(Person) :- parent(_, Person).

% Forward chaining rule: If a person has a child, they are considered a parent
update_parent_status :-
    gender(Person, _),
    \+ is_parent(Person),
    asserta(is_parent(Person)),
    writeln(Person has become a parent).

% Example usage:
% Run update_parent_status to iteratively apply the rules and derive new facts
% ?- update_parent_status.
