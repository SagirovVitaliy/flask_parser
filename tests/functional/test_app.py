
def test_add_page_with_fixture(test_client):
    '''
    GIVEN a Flask application configured for testing
    WHEN the '/add' page is requested (GET)
    THEN check that the response is valid
    '''
    response = test_client.get('/add')
    assert response.status_code == 200


def test_add_page_with_fixture_post(test_client):
    '''
    GIVEN a Flask application configured for testing
    WHEN the '/add' page is requested (POST)
    THEN check that the response is valid
    '''
    response = test_client.post('/add', data=dict(
        search_prhase='гитара',
        region='izhevsk',
        date1='2020-12-07',
        date2='2020-12-09'
        ))
    assert response.status_code == 302


def test_add_page_with_fixture_post_bad_region(test_client):
    '''
    GIVEN a Flask application configured for testing
    WHEN the '/add' page is requested with bad data region(POST)
    THEN check that the response is valid
    '''
    response = test_client.post('/add', data=dict(
        search_prhase='гитара',
        region='izhevskkkkk',
        date1='2020-12-07',
        date2='2020-12-09'
        ))
    assert response.status_code == 200


def test_add_page_with_fixture_post_search_prhase(test_client):
    '''
    GIVEN a Flask application configured for testing
    WHEN the '/add' page is requested with bad data search_prhase(POST)
    THEN check that the response is valid
    '''
    response = test_client.post('/add', data=dict(
        search_prhase='втмовтмлмьвл',
        region='izhevsk',
        date1='2020-12-07',
        date2='2020-12-09'
        ))
    assert response.status_code == 200


def test_stat_page_with_fixture(test_client):
    '''
    GIVEN a Flask application configured for testing
    WHEN the '/stat/<int:announcement_id>/<date1>/<date2>' page is requested (GET)
    THEN check that the response is valid
    '''
    response = test_client.get('stat/1/2020-12-07/2020-12-09')
    assert response.status_code == 200


def test_stat_page_with_fixture_bad_announcement_id(test_client):
    '''
    GIVEN a Flask application configured for testing
    WHEN the '/stat/<int:announcement_id>/<date1>/<date2>' page is requested non-existent announcement_id(GET)
    THEN check that the response is valid
    '''
    response = test_client.get('stat/550/2020-12-07/2020-12-09')
    assert response.status_code == 200

