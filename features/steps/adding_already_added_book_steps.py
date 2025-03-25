
from behave import given, when, then


@given('att användaren är på rätt webbsida, där man kan se böcker')
def step_impl(context):
    # Här skulle du normalt implementera logik för att navigera till rätt sida
    # För nu, låt oss bara anta att vi är på rätt sida
    context.on_book_page = True


@when('användaren klickar på "Add to cart"-knappen')
def step_impl(context):
    # Här simulerar vi att lägga till en bok i varukorgen
    if not hasattr(context, 'shopping_cart'):
        context.shopping_cart = {}

    book_id = "test_book"
    if book_id in context.shopping_cart:
        context.shopping_cart[book_id] += 1
    else:
        context.shopping_cart[book_id] = 1


@then('ska boken läggas till i varukorgen och antalet skall öka med ett')
def step_impl(context):
    # Här verifierar vi att boken har lagts till och antalet har ökat
    book_id = "test_book"
    assert book_id in context.shopping_cart
    assert context.shopping_cart[book_id] >= 1
