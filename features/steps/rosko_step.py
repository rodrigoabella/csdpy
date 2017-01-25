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

@then(u'muestra pregunta {letra}')
def step_impl(context, letra):
	assert letra.upper() + '-' in browser.html

@when(u'pregunta {letra} es {pregunta}')
def step_impl(context, letra, pregunta):
    assert letra.upper() + '-' + ' ' + pregunta

@then(u'muestra letra {letra} con pregunta {pregunta}')
def step_impl(context, letra, pregunta):
	assert letra.upper()+ '-' + ' ' + pregunta in browser.html