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

Scenario: Cuando la respuesta es incorrecta, no se muestra el resultado 
  Given rosko iniciado
  When pregunta A es tiene color marron y hojas verdes
  And escribo pajaro
  And envio la respuesta
  Then se muestra un None en pantalla