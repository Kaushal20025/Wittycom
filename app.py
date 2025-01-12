from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

# Function to load JSON data
def load_resources():
    with open('resources.json') as f:
        return json.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_resource/<chapter_name>/<resource_type>')
def get_resource(chapter_name, resource_type):
    resources = load_resources()
    # Return the appropriate resources based on chapter and resource type
    chapter = resources.get(chapter_name)
    if chapter:
        return jsonify(chapter.get(resource_type, []))
    return jsonify([])

# Other routes
@app.route('/resources')
def resources():
    return render_template('resources.html')

@app.route('/jee')
def jee():
    return render_template('jee.html')

@app.route('/jee_physics')
def jee_physics():
    return render_template('jee_physics.html')

if __name__ == '__main__':
    app.run(debug=True)
