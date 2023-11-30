% Facts about birds and their ability to fly
can_fly(sparrow).
can_fly(eagle).
cannot_fly(penguin).

% Prolog query to determine if a specific bird can fly
query_can_fly(Bird) :-
    can_fly(Bird),
    write(Bird), write(' can fly.'),
    nl.
query_can_fly(Bird) :-
    cannot_fly(Bird),
    write(Bird), write(' cannot fly.'),
    nl.
query_can_fly(Bird) :-
    \+ (can_fly(Bird); cannot_fly(Bird)),
    write(Bird), write(' is not mentioned in the facts.'),
    nl.
