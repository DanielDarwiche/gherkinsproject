@finished
Feature: Om användaren försöker lägga en bok som redan finns i varukorgen
  ska antal av just den boken öka istället för att skapa en ny rad

  Scenario: Användaren lägger till en bok i varukorgen
    Given att användaren är på rätt webbsida, där man kan se böcker
    When användaren klickar på "Add to cart"-knappen
    Then ska boken läggas till i varukorgen och antalet skall öka med ett

