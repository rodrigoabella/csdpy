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

@when(u'escribo una respuesta')
def step_impl(context):
    browser.fill('response_a', 'prueba')
    
@when(u'envio la respuesta')
def step_impl(context):
    browser.find_by_id('ok_button')[0].click()


@then(u'se visualiza la respuesta')
def step_impl(context):
    print(browser.html)
    assert 'prueba' in browser.html

