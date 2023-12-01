% Facts: Define the colors of the fruits
color(apple, red).
color(banana, yellow).
color(grape, purple).
color(orange, orange).
color(strawberry, red).
color(blueberry, blue).
color(mango, yellow).
color(kiwi, green).

% Rules: Define relationships between fruits and colors
is_fruit(Fruit) :- color(Fruit, _).

% Query examples:
% Find the color of a specific fruit
% ?- color(apple, Color). % Output: Color = red.

% Find all fruits of a specific color
% ?- color(Fruit, red). % Output: Fruit = apple ; Fruit = strawberry.
