% Facts: Define facts about animals and their classifications
classifies(lion, mammal).
classifies(parrot, bird).
classifies(dolphin, mammal).
classifies(penguin, bird).
classifies(elephant, mammal).
classifies(sparrow, bird).

% Rules: Define rules based on characteristics of mammals and birds (you can extend these rules)
is_mammal(Animal) :- classifies(Animal, mammal), !.
is_bird(Animal) :- classifies(Animal, bird), !.

% Backward chaining rules: Define questions to answer based on the characteristics
is_mammal_or_bird(Animal, mammal) :- is_mammal(Animal).
is_mammal_or_bird(Animal, bird) :- is_bird(Animal).

% Example queries:
% To check if an animal is a mammal:
% ?- is_mammal_or_bird(lion, mammal). % Output: true.

% To check if an animal is a bird:
% ?- is_mammal_or_bird(parrot, bird). % Output: true.
