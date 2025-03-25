Feature: Varukorgen visar alltid aktuell summa och antal böcker

  Scenario: Varukorgen visar rätt summa och antal böcker
    Given användaren har lagt till några böcker i varukorgen
    When användaren trycker på varukorgen
    Then varukorgen skall visa rätt summa och antal böcker

  Scenario: Varukorgen visar fel summa och rätt antal böcker
    Given användaren har lagt till några böcker i varukorgen
    When användaren trycker på varukorgen
    Then varukorgen skall visa fel summa och rätt antal böcker