% Rule to calculate the nth Fibonacci number
fibonacci(0, 0). % Base case: Fibonacci of 0 is 0
fibonacci(1, 1). % Base case: Fibonacci of 1 is 1
fibonacci(N, Result) :-
    N > 1,
    Prev1 is N - 1,
    Prev2 is N - 2,
    fibonacci(Prev1, Prev1Result),
    fibonacci(Prev2, Prev2Result),
    Result is Prev1Result + Prev2Result.
