% Facts
location(new_york, new_york_state).
location(boston, massachusetts).
location(chicago, illinois).
location(san_francisco, california).

stays(john, new_york).
stays(mary, boston).
stays(bob, chicago).
stays(alice, san_francisco).

% Rules
list_persons_states_cities :-
    stays(Person, City),
    location(City, State),
    format('Person: ~w, State: ~w, City: ~w~n', [Person, State, City]),
    fail.
list_persons_states_cities.

find_state(Person, State) :-
    stays(Person, City),
    location(City, State),
    format('~w is staying in ~w~n', [Person, State]).
