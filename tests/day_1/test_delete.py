import pytest
from restaurant_reviews import RestaurantReviews

def test_delete_existing():
    rr = RestaurantReviews()
    rr.add_review("Bokit i bon", "un bokit pou tout moun epi i bon !", 5)
    result = rr.delete_review("Bokit i bon")
    assert (result == "review not found")
    result2 = rr.get_review("Bokit i bon")
    assert(result2 == "Review not found")

# Vérification du cas de "non fonctionnement" avec exception
def test_delete_non_existing():
    rr = RestaurantReviews()
    with pytest.raises(ValueError) as e:
        rr.delete_review('Unkown Restaurant')
    assert str(e.value) == "Review not found to delete." 