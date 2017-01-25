Feature: Rosko


Scenario: ingreso a la pantalla inicial
    Given rosko iniciado
    Then muestra titulo del juego pasapalabras


Scenario: visualizar respuesta
	Given rosko iniciado
    When escribo una respuesta
	And envio la respuesta
	Then se visualiza la respuesta
