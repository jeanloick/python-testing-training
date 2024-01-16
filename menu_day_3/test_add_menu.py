import pytest
from restau_menu import RestauMenu, MenuItemAlreadyExists, RestaurantDoesNotExist

@pytest.mark.parametrize("restaurant, item, description, price, expected_output",[
    ("Cafe Mocha", "Latte", "Delicious latte with frothy milk", 4, "Latte added to Cafe Mocha's menu."),
    ("Cafe Bürger", "Bürger", "Tasty Bürger with special sauce", 2, "Bürger added to Cafe Bürger's menu."),
    ("Cafe Pizza", "Margherita", "Classic Margherita pizza", 3, "Margherita added to Cafe Pizza's menu."),
    ("Cafe Sushi", "Sashimi", "Fresh Sashimi selection", 5, "Sashimi added to Cafe Sushi's menu."),
    ("Cafe Tacos", "Chicken Tacos", "Spicy chicken tacos with salsa", 1, "Chicken Tacos added to Cafe Tacos's menu."),
])

def test_add_valid_menu_item(restaurant, item, description, price, expected_output):
    rm = RestauMenu()
    result = rm.add_menu_item(restaurant, item, description, price)
    assert result == expected_output

@pytest.mark.parametrize("restaurant, item, description, price, expected_error_message",[
    ("Cafe Sushi", "Sashimi", "Fresh Sashimi selection", 5, f"{restaurant} already has {item} in the menu"),
    ("Cafe Tacos", "Spicy Tacos", "Very spicy tacos with extra heat", -1, "Price must be positive"),
    ("Nonexistent Cafe", "Coffee", "Regular coffee", 2, f"{restaurant} does not exist")
])
def test_invalid_add_menu_item(restaurant, item, description, price, expected_error_message):
    rm = RestauMenu()
    with pytest.raises((MenuItemAlreadyExists, ValueError, RestaurantDoesNotExist)) as e:
        rm.add_menu_item(restaurant, item, description, price)
    assert str(e.value) == expected_error_message
