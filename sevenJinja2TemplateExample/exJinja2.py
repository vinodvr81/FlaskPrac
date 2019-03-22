from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def template_test():
    return render_template('jinja2Ex.html', my_string="Vinod Rangaswamy Vukkalam!", my_dict={'Name':'Vinod','age':37})


if __name__ == '__main__':
    app.run(debug=True)
