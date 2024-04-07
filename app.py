from flask import Flask, request, render_template
from stories import story

app = Flask(__name__)

@app.route('/')
def madlibs_form():
    """ Generate and show form """
    prompts = story.prompts

    return render_template('madlib_home.html', prompts = prompts)

@app.route('/stories')
def generate_story():
    """ Show the story """

    text = story.generate(request.args)

    return render_template('stories.html', text = text)
