Feature: Användaren kan lägga böcker i varukorg

  Scenario: Lägga till en bok i varukorgen
    Given att användaren är på rätt webbsida, där man kan se böcker
    When användaren klickar på "Add to cart"-knappen
    Then ska boken läggas till i varukorgen
    And användaren ska se en bekräftelse av att boken har lagts till

  Scenario: Lägga till flera böcker i varukorgen
    Given att användaren är på rätt webbsida, där man kan se böcker
    When användaren klickar på "Add to cart"-knappen, för tre olika böcker
    Then ska alla tre böcker läggas till i användarens varukorg
    And antalet artiklar i varukorgen ska öka med 3

  Scenario: Försöka lägga till en bok som är slut i lager
    Given att användaren är på rätt webbsida, där man kan se böcker
    When användaren klickar på "Add to cart"-knappen
    Then ska knappen vara inaktiverad
    And användaren ska se ett meddelande om att "Boken är slut i lager"
