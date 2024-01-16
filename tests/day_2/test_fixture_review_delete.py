import pytest
from restaurant_reviews import RestaurantReviews

# @pytest.fixture.... -> conf_test.py

@pytest.mark.parametrize("restaurant_title, review_text, review_rating, expected_output",[
    ("Cafe Mocha","Great coffee and pastries.", 4, "Review deleted for Cafe Mocha."),
    ("Cafe Bürger","Great coffee and Bürger.", 2, "Review deleted for Cafe Bürger."),
    ("Cafe Pizza","Great coffee and Pizza.", 3, "Review deleted for Cafe Pizza."),
    ("Cafe Sushi","Great coffee and Sushi.", 5, "Review deleted for Cafe Sushi."),
    ("Cafe Tacos","Great coffee and Tacos.", 1, "Review deleted for Cafe Tacos."),
])

def test_remove_valid_review(restaurant_title, review_text, review_rating, expected_output):
    rr = RestaurantReviews()
    rr.add_review(restaurant_title, review_text, review_rating)
    result = rr.delete_review(restaurant_title)
    assert (result == expected_output)
    result2 = rr.get_review(restaurant_title) 
    assert(result2 == "Review not found.")


@pytest.mark.parametrize("non_existing_restaurant, expected_output",[
    ("Cafe Mocha", "Review not found to delete."),
    ("Cafe Bürger", "Review not found to delete."),
    ("Cafe Pizza", "Review not found to delete."),
    ("Cafe Sushi", "Review not found to delete."),
    ("Cafe Tacos", "Review not found to delete."),
])

def test_delete_non_existing(non_existing_restaurant, expected_output):
    rr = RestaurantReviews()
    with pytest.raises(ValueError) as e:
        rr.delete_review(non_existing_restaurant)
    assert str(e.value) == expected_output