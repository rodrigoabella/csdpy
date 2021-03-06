Feature: Rosko


Scenario: ingreso a la pantalla inicial

    Given rosko iniciado
    Then muestra titulo del juego pasapalabras

Scenario: visualizar respuesta
	Given rosko iniciado
  When escribo prueba
	And envio la respuesta
	Then se visualiza la respuesta

Scenario: mostrar pregunta A
  Given rosko iniciado
  Then muestra pregunta A

Scenario: formular pregunta A
  Given rosko iniciado
  When pregunta A es tiene color marron y hojas verdes
  Then muestra letra A con pregunta tiene color marron y hojas verdes

Scenario: mostrar OK para resultado correcto 
  Given rosko iniciado

  When pregunta A es tiene color marron y hojas verdes
  And escribo arbol
  And envio la respuesta
  Then se muestra un OK en pantalla  

Scenario: mostrar NOK para resultado incorrecto 
  Given rosko iniciado
  When escribo una respuesta incorrecta
  And envio la respuesta
  Then se muestra un NOK en pantalla 

Scenario: mostrar PASS para resultado pass 
  Given rosko iniciado
  When presiono boton pass
  Then se muestra un PASS en pantalla  
