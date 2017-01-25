from rosko import *
from behave import *
from splinter import Browser
browser = Browser('flask',app=app)

@given(u'rosko iniciado')
def step_impl(context):
    browser.visit('http://127.0.0.1:5000')

@then(u'muestra titulo del juego {mensaje}')
def step_impl(context, mensaje):
    assert mensaje.upper() in browser.html

