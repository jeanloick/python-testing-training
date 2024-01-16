import pytest
from restau_menu import RestauMenu, MenuItemNotFoundException, RestaurantDoesNotExist

@pytest.mark.parametrize("restaurant, item, expected_output", [
    # ... (paramètres pour les tests de suppression)
])
def test_delete_valid_menu_item(restaurant, item, expected_output):
    rm = RestauMenu()
    rm.add_menu_item(restaurant, item, "Original description", 2)
    result = rm.delete_menu_item(restaurant, item)
    assert result == expected_output

@pytest.mark.parametrize("restaurant, item, expected_error_message", [
    # ... (paramètres pour les tests de suppression invalides)
])
def test_invalid_delete_menu_item(restaurant, item, expected_error_message):
    rm = RestauMenu()
    with pytest.raises((MenuItemNotFoundException, RestaurantDoesNotExist)) as e:
        rm.delete_menu_item(restaurant, item)
    assert str(e.value) == expected_error_message
