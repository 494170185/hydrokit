from hydrokit.core.errors import FitError, HydroError, ValidationError


def test_hierarchy():
    assert issubclass(FitError, HydroError)
    assert issubclass(ValidationError, HydroError)


def test_codes():
    assert FitError.code != ValidationError.code
