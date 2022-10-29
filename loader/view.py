from flask import Blueprint, render_template, request
from functions import *
import logging

logging.basicConfig(filename='basic.log', level=logging.INFO)

loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='templates', url_prefix='/')


@loader_blueprint.route('/post')
def create_post():
    return render_template('post_form.html')


@loader_blueprint.route('/post', methods=['POST'])
def upload_post():
    picture = request.files.get('picture')
    content = request.form.get('content')

    picture_url = save_picture(picture)

    if not picture_url:
        logging.info(f'{picture_url}: not an image')
        return 'Not an image'

    add_post({"pic": picture_url, "content": content})

    return render_template('post_uploaded.html', picture_url=picture_url, content=content)
