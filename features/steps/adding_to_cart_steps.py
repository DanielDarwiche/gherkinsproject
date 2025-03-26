from behave import given, when, then

@given('att användaren är på rätt webbsida, där man kan se böcker')
def step_given_books_page(context):
    context.shopping_cart = {}  # Initiera varukorgen som tom
    context.page = "Books_page"
    context.add_button = {"enabled": True}  # Initiera knappen som aktiverad
    print("Användaren är på webbsidan")

@when('användaren klickar på "Add to cart"-knappen')
def step_when_add_to_cart(context):
    book = "test_book"
    if book in context.shopping_cart:
        context.shopping_cart[book] += 1
    else:
        context.shopping_cart[book] = 1
    context.cart_confirmation = f"Boken {book} har lagts till i varukorgen"

@then('ska boken läggas till i varukorgen och antalet skall öka med ett')
def step_then_book_in_cart_and_count_increased(context):
    book = "test_book"
    assert book in context.shopping_cart, "Boken finns inte i varukorgen"
    assert context.shopping_cart[book] >= 1, "Antalet i varukorgen är inte korrekt"

@then('användaren ska se en bekräftelse av att boken har lagts till')
def step_then_confirmation_message(context):
    book = "test_book"
    assert context.cart_confirmation == f"Boken {book} har lagts till i varukorgen", "Felmeddelandet är inte korrekt"

# Scenario: Lägga till flera böcker i varukorgen
@when('användaren klickar på "Add to cart"-knappen, för tre olika böcker')
def step_when_add_multiple_books(context):
    books = ["book_1", "book_2", "book_3"]
    for book in books:
        if book in context.shopping_cart:
            context.shopping_cart[book] += 1
        else:
            context.shopping_cart[book] = 1

@then('ska alla tre böcker läggas till i användarens varukorg')
def step_then_three_books_in_cart(context):
    books = ["book_1", "book_2", "book_3"]
    for book in books:
        assert book in context.shopping_cart, f"{book} saknas i varukorgen"
        assert context.shopping_cart[book] == 1, f"Antalet för {book} är inte korrekt"

@then('antalet artiklar i varukorgen ska öka med 3')
def step_then_cart_count_increases(context):
    assert len(context.shopping_cart) == 3, "Det totala antalet artiklar är inte 3"

# Scenario: Försöka lägga till en bok som är slut i lager

@then('ska knappen vara inaktiverad')
def step_then_button_disabled(context):
    assert "enabled" in context.add_button, "add_button.enabled är inte definierad"
    assert not context.add_button["enabled"], "Knappen är inte inaktiverad som förväntat"

@then('användaren ska se ett meddelande om att "Boken är slut i lager"')
def step_then_out_of_stock_message(context):
    assert context.error_message == "Boken är slut i lager", "Felmeddelande saknas eller är inkorrekt"
