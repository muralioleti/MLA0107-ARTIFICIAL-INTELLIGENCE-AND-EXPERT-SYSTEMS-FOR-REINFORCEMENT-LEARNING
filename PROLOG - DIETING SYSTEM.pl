% Facts defining dietary recommendations for different diseases

% Diabetes
diet_recommendation(diabetes, [
    'Consume complex carbohydrates like whole grains and legumes.',
    'Limit the intake of sugary foods and drinks.',
    'Include plenty of non-starchy vegetables in your diet.',
    'Choose lean protein sources such as poultry and fish.',
    'Monitor portion sizes to manage carbohydrate intake.'
]).

% Hypertension (High Blood Pressure)
diet_recommendation(hypertension, [
    'Reduce sodium intake by avoiding high-salt foods.',
    'Eat potassium-rich foods like bananas and oranges.',
    'Include more fruits and vegetables in your diet.',
    'Choose lean sources of protein, such as poultry and fish.',
    'Limit processed and fried foods to reduce saturated fat intake.'
]).

% Obesity
diet_recommendation(obesity, [
    'Focus on a balanced diet with a variety of nutrients.',
    'Include more fruits and vegetables in your meals.',
    'Choose whole grains over refined grains.',
    'Limit the intake of sugary and high-calorie foods.',
    'Engage in regular physical activity to support weight loss.'
]).

% Rule to suggest a diet based on a specific disease
suggest_diet_for_disease(Disease) :-
    diet_recommendation(Disease, Recommendations),
    write('Diet recommendations for '), write(Disease), write(':'), nl,
    print_recommendations(Recommendations).

% Helper rule to print dietary recommendations
print_recommendations([]).
print_recommendations([Recommendation | Rest]) :-
    write('- '), write(Recommendation), nl,
    print_recommendations(Rest).
