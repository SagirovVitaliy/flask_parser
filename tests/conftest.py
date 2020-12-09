import pytest
from webapp.models import Announcement, QuantityAnnouncement

from webapp import create_app


@pytest.fixture(scope='module')
def new_announcement():
    announcement = Announcement(
        search_phrase='авто',
        region='moskva'
        )
    return announcement


@pytest.fixture(scope='module')
def new_quantity_announcement():
    quantity_announcement = QuantityAnnouncement(
        quantity_announcement=300,
        announcement=2,
        time='2020-12-10'
        )
    return quantity_announcement


@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app('config_test.py')

    with flask_app.test_client() as testing_client:
        with flask_app.app_context():
            yield testing_client
