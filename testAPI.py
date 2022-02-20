import api_data


def test_gettop250():
    top250_results = api_data.get_top_250_data()
    assert len(top250_results) == 250