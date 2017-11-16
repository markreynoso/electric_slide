"""Various tests for state_almanac_generator.py."""

from electric_slide.scripts.state_almanac_generator import generate_unique_states_from_sets
import pytest


@pytest.fixture(scope="session")
def almanac():
    """Fixture of the set almanac."""
    set_almanac = {0: {"[[1, 2, 3], [4, 5, 6], [7, 8, 9]]"}}

    for i in range(31):
        set_almanac.setdefault(i + 1, set())

    for i in range(32):
        generate_unique_states_from_sets(i, set_almanac)
    return set_almanac


def test_generate_output_is_correct_type(almanac):
    """Test that the generator outputs a dict, as expected."""
    assert type(almanac) == dict


def test_dict_entries_are_correct_type(almanac):
    """Test that the dict contains values which are sets."""
    for i in range(32):
        assert type(almanac[i]) == set


def test_sets_are_correct_length(almanac):
    """Test that each set of states contains the expected number of states."""
    correct_num_of_states = [1, 2, 4, 8, 16, 20, 39, 62, 116, 152, 286, 396, 748, 1024, 1893, 2512, 4485, 5638, 9529, 10878, 16993, 17110, 23952, 20224, 24047, 15578, 14560, 6274, 3910, 760, 221, 2]
    total = 0

    for i in range(32):
        total += len(almanac[i])
        assert len(almanac[i]) == correct_num_of_states[i]

    assert total == 181440
