% Facts: Define symptoms and conditions
symptom(fever).
symptom(cough).
symptom(headache).
symptom(sore_throat).
symptom(runny_nose).

condition(cold).
condition(flu).
condition(allergy).

% Rules: Define relationships between symptoms and conditions
has_symptom(cold, cough).
has_symptom(cold, runny_nose).
has_symptom(flu, fever).
has_symptom(flu, cough).
has_symptom(flu, headache).
has_symptom(allergy, runny_nose).
has_symptom(allergy, sore_throat).

% Rule for diagnosis
diagnosis(Patient, Condition) :-
    symptom(Symptom),
    writeln('Do you have the symptom: '), writeln(Symptom),
    read(Answer),
    (Answer = yes -> has_symptom(Condition, Symptom), asserta(has_symptom(Patient, Symptom)); true),
    fail.

% Query example:
% To diagnose a patient, call diagnosis/2 with the patient's name and the resulting condition
% ?- diagnosis(john, Condition).

% Example interaction:
% Do you have the symptom:
% fever
% |: yes.
% Do you have the symptom:
% cough
% |: yes.
% john has flu
