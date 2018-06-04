from pytest import fixture
from tmdbwrapper import TV
import vcr

@fixture
def tv_keys():
    """Return a static list of response keys
    
       This fixture is responsible to return only
       the data for testing
    """
    return ['id', 'origin_country', 'poster_path', 'name',
            'overview', 'popularity', 'backdrop_path',
            'first_air_date', 'vote_count', 'vote_average']

@vcr.use_cassette('tests/vcr_cassettes/tv-info.yml', filter_query_parameters=['api_key'])
def test_tv_info(tv_keys):
    """Tests an API call to get a TV show's info"""

    tv_instance = TV(1396)
    response = tv_instance.info()

    assert isinstance(response, dict)
    assert response['id'] == 1396, "The ID should be in the response"
    assert set(tv_keys).issubset(response.keys()), "All keys should be in response"

@vcr.use_cassette('tests/vcr_cassettes/tv-popular.yml', filter_query_parameters=['api_key'])
def test_tv_popular(tv_keys):
    """Test an API call to get popular TV shows"""

    # @staticmethod popular in action
    response = TV.popular()

    assert isinstance(response, dict)
    assert isinstance(response['results'], list)
    assert isinstance(response['results'][0], dict)
    assert set(tv_keys).issubset(response['results'][0].keys())
