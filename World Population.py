import json
from pygal.maps.world import COUNTRIES
from pygal.maps.world import World
from pygal.style import RotateStyle
from pygal.style import LightColorizedStyle as LCS


def get_country_code(country_name):
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
    return None


filename = 'population_data.json'
with open(filename) as file:
    pop_data = json.load(file)

    world_population = {}
    for pop_dict in pop_data:
        if pop_dict['Year'] == '2010':
            country_name = pop_dict['Country Name']
            population = int(float(pop_dict['Value']))
            code = get_country_code(country_name)
            if code:
                world_population[code] = population

    group_1 = {}
    group_2 = {}
    group_3 = {}
    for code, population in world_population.items():
        if population < 1000000:
            group_1[code] = population
        if population < 1000000000:
            group_2[code] = population
        else:
            group_3[code] = population

    wm_style = RotateStyle('#336699', base_style=LCS)
    wm = World(style=wm_style)
    wm.add('Small Coutries', group_1)
    wm.add('Medium Coutries', group_2)
    wm.add('Big Countries', group_3)
    wm.title = 'World Population in 2010, by Country'
    wm.render_to_file('World.svg')
