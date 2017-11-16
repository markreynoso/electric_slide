"""."""
from pyramid import testing
from pyramid.testing import DummyRequest

import pytest


@pytest.fixture
def dummy_request():
    """Instantiate a fake HTTP Request, complete with a database session."""
    return testing.DummyRequest()


def test_shuffle_route(dummy_request):
    """Test if shuffle route returns dictionary."""
    from electric_slide.views.default import shuffle
    state = shuffle(dummy_request)
    assert isinstance(state, dict)


def test_shuffle_route_returns_dict_with_key_shuffle(dummy_request):
    """Test if shuffle route returns dictionary."""
    from electric_slide.views.default import shuffle
    state = shuffle(dummy_request)
    print(state)
    assert state['shuffle']
