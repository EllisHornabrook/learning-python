from classes_methods import Star_wars
    # import a class from another file

new = Star_wars('Purple', 'Mace Windu', 'Jedi')
print(f'Name: {new.name}')
print(new.description('great film'))


from space.planet import Planet
from space.calc import planet_mass, planet_vol

earth = Planet('Earth', 'yes', 45000, 8)
earth_mass = planet_mass(earth.gravity, earth.radius)
earth_vol = planet_vol(earth.radius)
print(f'{earth.name} has a mass of {earth_mass} and a volume of {earth_vol}')
