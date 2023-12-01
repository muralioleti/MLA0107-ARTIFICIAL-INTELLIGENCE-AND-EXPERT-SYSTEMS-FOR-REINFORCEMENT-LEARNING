% Predicate to convert Celsius to Fahrenheit
celsius_to_fahrenheit(Celsius, Fahrenheit) :-
    Fahrenheit is (Celsius * 9/5) + 32.

% Predicate to check if a temperature is below freezing (0 degrees Celsius)
below_freezing(Temperature) :-
    Temperature < 0.

% Example Queries
% a. Convert 20 degrees Celsius to Fahrenheit
% celsius_to_fahrenheit(20, Fahrenheit).
%
% b. Check if -5 degrees Celsius is below freezing
% below_freezing(-5).
