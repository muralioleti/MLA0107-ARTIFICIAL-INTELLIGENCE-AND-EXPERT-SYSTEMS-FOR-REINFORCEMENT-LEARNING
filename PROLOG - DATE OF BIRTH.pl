% Facts: individuals with names and dates of birth
dob(john, '1990-05-15').
dob(mary, '1985-10-22').
dob(jane, '1995-02-28').
dob(bob, '1978-08-10').
dob(alice, '1982-12-05').

% Rule to retrieve the DOB of a specific person given their name
get_dob(Name, DOB) :-
    dob(Name, DOB).

% Rule to find all individuals who are older than a certain age
older_than_age(Name, Age) :-
    dob(Name, DOB),
    date('2023-01-01', CurrentDate),  % Assuming the current date is '2023-01-01'
    age(DOB, CurrentDate, Age),
    Age > 30.

% Rule to determine who is the youngest person in the database
youngest_person(Name) :-
    dob(_, DOB),
    findall(Age, age(DOB, '2023-01-01', Age), Ages),
    min_list(Ages, MinAge),
    dob(Name, YoungestDOB),
    age(YoungestDOB, '2023-01-01', MinAge).

% Rule to check if a specific person is older than another specific person
is_older(Person1, Person2) :-
    dob(Person1, DOB1),
    dob(Person2, DOB2),
    age(DOB1, '2023-01-01', Age1),
    age(DOB2, '2023-01-01', Age2),
    Age1 > Age2.

% Rule to calculate age
age(DOB, CurrentDate, Age) :-
    date_time_stamp(DOB, DOBStamp),
    date_time_stamp(CurrentDate, CurrentStamp),
    StampDiff is CurrentStamp - DOBStamp,
    Age is floor(StampDiff / (365.25 * 24 * 3600)).

% Sample queries
% a. Retrieve the DOB of a specific person given their name.
% ?- get_dob(john, DOB).
%
% b. Find all individuals who are older than a certain age (e.g., 30 years old) based on their DOBs.
% ?- older_than_age(Name, 30).
%
% c. Determine who is the youngest person in the database.
% ?- youngest_person(Youngest).
%
% d. Check if a specific person is older than another specific person.
% ?- is_older(jane, bob).
