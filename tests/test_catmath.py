from catinabox import catmath


def test__cat_years_to_hooman_years__middle_age__succeeds():
    hooman_years = catmath.cat_years_to_hooman_years(10)
    assert hooman_years == 50


def test__cat_years_to_hooman_years__less_than_one_year__succeeds():
    hooman_years = catmath.cat_years_to_hooman_years(0.5)
    assert hooman_years == 2.5


def test__cat_years_to_hooman_years__0__returns_0():
    hooman_years = catmath.cat_years_to_hooman_years(0)
    assert hooman_years == 0


# BONUS MATERIAL FOR STEP 2

def test__is_cat_leap_year__succeeds():
    assert catmath.is_cat_leap_year(2016) is True
