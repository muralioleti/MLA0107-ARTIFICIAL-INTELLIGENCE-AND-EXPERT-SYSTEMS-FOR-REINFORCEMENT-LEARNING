% Rule to calculate the factorial of a number
factorial(0, 1). % Base case: factorial of 0 is 1
factorial(N, Result) :-
    N > 0,
    Prev is N - 1,
    factorial(Prev, PrevResult),
    Result is N * PrevResult.
