

def test_new_announcement_with_fixture(new_announcement):
    '''
    GIVEN Announcement model
    WHEN a new Announcement creating
    THEN check the Announcement fields are defined correct
    '''
    assert new_announcement.search_phrase == 'авто'
    assert new_announcement.region == 'moskva'


def test_new_quantity_announcement_with_fixture(new_quantity_announcement):
    '''
    GIVEN QuantityAnnouncement model
    WHEN a new QuantityAnnouncement creating
    THEN check the QuantityAnnouncement fields are defined correct
    '''
    assert new_quantity_announcement.quantity_announcement == 300
    assert new_quantity_announcement.announcement == 2
    assert new_quantity_announcement.time == '2020-12-10'
