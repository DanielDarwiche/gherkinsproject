from behave import given, when, then

@given('att användaren är på webbsidan för att se böcker')
def step_given_books_page(context):
    context.shopping_cart = {}
    context.page = "Books_page"
    print("Användaren är på webbsidan för böcker")

@when('användaren klickar på knappen "Add to cart" för en bok')
def step_adding_book_to_cart(context):
    book = "test_book"
    if book in context.shopping_cart:
        context.shopping_cart[book] += 1
    else:
        context.shopping_cart[book] = 1

@then('ska boken "{book}" läggas till i varukorgen')
def step_book_added_to_cart(context, book):
    assert book in context.shopping_cart
    assert context.shopping_cart[book] >= 1

@then('antalet av boken i varukorgen ska öka med ett')
def step_book_quantity_increased(context):
    book = "test_book"
    assert context.shopping_cart[book] == 1, f"Förväntade 1 bok, men fick {context.shopping_cart.get(book, 0)}"
