Feature: Användaren kan ta bort böcker från varukorgen

  Scenario: Användaren kan ta bort en bok från varukorgen
    Given att användaren är på rätt webbsida, där man kan se böcker
    When användaren trycker på varukorgen och "Ta bort"-knappen för en vald bok
    Then försvinner boken från varukorgen
    And boken är inte i varukorgen

  Scenario: Användaren kan ta bort en dublett från varukorgen
    Given att användaren är på rätt webbsida, där man kan se böcker
    When användaren trycker på varukorgen och "-"-knappen för en vald bok
    Then förminskas antalet med ett från boken, i varukorgen
    And bokens dublett är borta från varukorgen
