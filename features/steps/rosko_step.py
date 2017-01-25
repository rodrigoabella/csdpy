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


@when(u'escribo {respuesta}')
def step_impl(context,respuesta):
    browser.fill('response_a', respuesta)
    
@when(u'envio la respuesta')
def step_impl(context):
    browser.find_by_id('ok_button')[0].click()


@then(u'se visualiza la respuesta')
def step_impl(context):
    print(browser.html)
    assert 'prueba' in browser.html

@then(u'muestra pregunta {letra}')
def step_impl(context, letra):
	assert letra.upper() + '-' in browser.html

@when(u'pregunta {letra} es {pregunta}')
def step_impl(context, letra, pregunta):
    assert letra.upper() + '-' + ' ' + pregunta

@then(u'muestra letra {letra} con pregunta {pregunta}')
def step_impl(context, letra, pregunta):
	assert letra.upper()+ '-' + ' ' + pregunta in browser.html


@then(u'se muestra un {resultado} en pantalla')
def step_impl(context,resultado):
    assert resultado in browser.html


@then(u'se muestra un NOK en pantalla')
def step_impl(context):
    assert 'NOK' in browser.html

@when(u'presiono boton pass')
def step_impl(context):
    browser.find_by_id('pass_button')[0].click()    

@then(u'se muestra un PASS en pantalla')
def step_impl(context):
    assert 'PASS' in browser.html

