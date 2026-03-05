import flask
from flask import url_for, redirect, render_template


def texml(resp):
    resp = flask.Response(resp)
    resp.headers['Content-Type'] = 'text/xml'
    return resp


def view(view_name, form=None):
    if form is None:
        return render_template("{0}.html".format(view_name))
    return render_template("{0}.html".format(view_name), form=form)


def view_with_params(view_name, **options):
    return render_template("{0}.html".format(view_name), **options)


def redirect_to(view_name, **options):
    if len(options) == 0:
        return redirect(url_for(view_name))
    return redirect(url_for(view_name, **options))
