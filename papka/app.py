from flask import Flask, render_template, request, url_for
from superhero_api import SuperHeroAPI

app = Flask(__name__)
s = SuperHeroAPI()

@app.route('/', methods=['POST', 'GET'])
def index():
    user_character_name = 'doctor strange'
    print(request.form.get('name'))
    image_url = s.get_hero_image_url(f'{user_character_name}')
    # id_ = s.get_id(f'{user_character_name}')
    # name = user_character_name.title()
    _data = {'url': f'{image_url}', 'fa': 'fa'}

    return render_template('index.html', data=_data)
       
