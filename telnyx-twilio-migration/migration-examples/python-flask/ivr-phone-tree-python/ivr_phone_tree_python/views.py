from flask import (
    flash,
    render_template,
    redirect,
    request,
    session,
    url_for,
)

from ivr_phone_tree_python import app
from ivr_phone_tree_python.view_helpers import texml


@app.route('/')
@app.route('/ivr')
def home():
    return render_template('index.html')


@app.route('/ivr/welcome', methods=['POST'])
def welcome():
    response = '''<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Gather numDigits="1" action="{menu_url}" method="POST">
        <Say>Thanks for calling the E T Phone Home Service. Please press 1 for directions.Press 2 for a list of planets to call.</Say>
    </Gather>
</Response>'''.format(menu_url=url_for('menu'))
    return texml(response)


@app.route('/ivr/menu', methods=['POST'])
def menu():
    selected_option = request.form['Digits']
    option_actions = {'1': _give_instructions,
                      '2': _list_planets}

    if selected_option in option_actions:
        response = option_actions[selected_option]()
        return texml(response)

    return _redirect_welcome()


@app.route('/ivr/planets', methods=['POST'])
def planets():
    selected_option = request.form['Digits']
    option_actions = {'2': "+19295566487",
                      '3': "+17262043675",
                      "4": "+16513582243"}

    if selected_option in option_actions:
        response = '''<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Dial>{number}</Dial>
</Response>'''.format(number=option_actions[selected_option])
        return texml(response)

    return _redirect_welcome()


# private methods

def _give_instructions():
    return '''<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Say voice="Polly.Amy" language="en-GB">To get to your extraction point, get on your bike and go down the street. Then Left down an alley. Avoid the police cars. Turn left into an unfinished housing development.Fly over the roadblock. Go past the moon. Soon after you will see your mother ship.</Say>
    <Say voice="Polly.Amy" language="en-GB">Thank you for calling the E T Phone Home Service - the adventurous alien's first choice in intergalactic travel</Say>
    <Hangup/>
</Response>'''


def _list_planets():
    return '''<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Gather numDigits="1" action="{planets_url}" method="POST">
        <Say voice="Polly.Amy" language="en-GB">To call the planet Broh doe As O G, press 2. To call the planet DuhGo bah, press 3. To call an oober asteroid to your location, press 4. To go back to the main menu press the star key.</Say>
    </Gather>
</Response>'''.format(planets_url=url_for('planets'))


def _redirect_welcome():
    response = '''<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Say voice="Polly.Amy" language="en-GB">Returning to the main menu</Say>
    <Redirect>{welcome_url}</Redirect>
</Response>'''.format(welcome_url=url_for('welcome'))
    return texml(response)
