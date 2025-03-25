Feature: Det skall gå att tömma varukorgen helt

  Scenario: Användaren tömmer hela varukorgen
    Given att användaren har lagt till flera böcker i varukorgen
    When användaren klickar på "Töm varukorg"-knappen
    Then ska alla böcker tas bort från varukorgen
    And varukorgen ska visa att den är tom
    And användaren ska se en bekräftelse på att varukorgen har tömts

  Scenario: Användaren försöker tömma en redan tom varukorg
    Given att användarens varukorg är tom
    When användaren klickar på "Töm varukorg"-knappen
    Then ska knappen vara inaktiverad
