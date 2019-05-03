import requests
from operator import itemgetter
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
submission_ids = r.json()
submission_dicts = []
names = []
for submission_id in submission_ids[:30]:
    url = ('https://hacker-news.firebaseio.com/v0/item/' +
           str(submission_id) + '.json')
    submission_r = requests.get(url)
    response_dict = submission_r.json()
    submission_dict = {'title': response_dict['title'],
                       'xlink': response_dict['url'],
                       'value': response_dict.get('descendants', 0)}
    names.append(submission_dict['title'])
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('value'), reverse=True)
my_style = LS('#333366', base_style=LCS)
my_style.title_font_size = 24
my_style.label_font_size = 14
my_style.major_label_font_size = 18

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Hottest discussion'
chart.x_labels = names
chart.add('', submission_dicts)
chart.render_to_file('Hottest discussion.svg')
