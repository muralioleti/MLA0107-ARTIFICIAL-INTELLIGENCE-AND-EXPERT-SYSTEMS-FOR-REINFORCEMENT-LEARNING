% Knowledge base
student(john).
student(alice).
student(bob).

teacher(prof_smith).
teacher(prof_jones).
teacher(dr_doe).

subject(math).
subject(english).
subject(physics).

code(cse101).
code(eng202).
code(physics301).

% Rule to generate "fill in the blank" questions
generate_question(Question) :-
    random_student(Student),
    random_teacher(Teacher),
    random_subject(Subject),
    random_code(Code),
    atom_concat('Who is the student in ', Subject, Part1),
    atom_concat(' class taught by ', Teacher, Part2),
    atom_concat(' for ', Subject, Part3),
    atom_concat(' with the code ', Code, Part4),
    atom_concat(Part1, Part2, Temp1),
    atom_concat(Temp1, Part3, Temp2),
    atom_concat(Temp2, Part4, Question).

% Rules to select random elements from the knowledge base
random_student(Student) :- student(Student).
random_teacher(Teacher) :- teacher(Teacher).
random_subject(Subject) :- subject(Subject).
random_code(Code) :- code(Code).

% Example usage
?- generate_question(Question).
