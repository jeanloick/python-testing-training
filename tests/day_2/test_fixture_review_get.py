import pytest
from restaurant_reviews import RestaurantReviews

# @pytest.fixture.... -> conf_test.py

@pytest.mark.parametrize("restaurant_title, review_text, review_rating, expected_output",[
    ("Cafe Mocha","Great coffee and pastries.", 4, "Review added for Cafe Mocha."),
    ("Cafe Bürger","Great coffee and Bürger.", 2, "Review added for Cafe Bürger."),
    ("Cafe Pizza","Great coffee and Pizza.", 3, "Review added for Cafe Pizza."),
    ("Cafe Sushi","Great coffee and Sushi.", 5, "Review added for Cafe Sushi."),
    ("Cafe Tacos","Great coffee and Tacos.", 1, "Review added for Cafe Tacos."),
])

def test_add_valid_review(restaurant_title, review_text, review_rating, expected_output):
    rr = RestaurantReviews()
    result = rr.add_review(restaurant_title, review_text, review_rating)
    assert result == expected_output
    # assert rr.get_review("Cafe Mocha") == {'review_text': "Great coffee and pastries.", 'rating': 4}