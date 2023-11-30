% Facts
planet(mercury, distance_from_sun(0.39), mass(0.0553)). % Distance in AU, Mass in Earth masses

planet(saturn, orbital_period(29.46), day_length(0.44)). % Orbital period in Earth years, Day length in Earth days

% Rule to find the distance between two planets based on their positions from the Sun
distance_between_planets(Planet1, Planet2, Distance) :-
    planet(Planet1, distance_from_sun(Dist1), _),
    planet(Planet2, distance_from_sun(Dist2), _),
    Distance is abs(Dist1 - Dist2).

% Example query to find the distance between Planet Venus and Planet Jupiter
?- distance_between_planets(venus, jupiter, Distance).
% This query will calculate and return the absolute distance between Venus and Jupiter.

% Query to find all planets that are closer to the Sun than Planet Earth
closer_to_sun(Planet) :-
    planet(Planet, distance_from_sun(Dist), _),
    planet(earth, earth_distance),
    Dist < earth_distance.

% Example query to list planets closer to the Sun than Planet Earth
?- closer_to_sun(CloserPlanet).
% This query will return planets that are closer to the Sun than Earth.
