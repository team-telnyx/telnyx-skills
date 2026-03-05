model_settings = {
    'db': None,
    'bcrypt': None,
    'app': None,
}


def init_models_module(db, bcrypt, flask_app):
    model_settings['db'] = db
    model_settings['bcrypt'] = bcrypt
    model_settings['app'] = flask_app


def app_db():
    return model_settings['db']


def bcrypt():
    return model_settings['bcrypt']


def telnyx_api_key():
    return model_settings['app'].config['TELNYX_API_KEY']


def telnyx_phone_number():
    return model_settings['app'].config['TELNYX_PHONE_NUMBER']


def telnyx_messaging_profile_id():
    return model_settings['app'].config['TELNYX_MESSAGING_PROFILE_ID']


def telnyx_connection_id():
    return model_settings['app'].config['TELNYX_CONNECTION_ID']
