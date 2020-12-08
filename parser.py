from webapp import create_app
from webapp.db import db
from webapp.models import Announcement, QuantityAnnouncement

import requests
from bs4 import BeautifulSoup as BS
from datetime import datetime

app = create_app()

with app.app_context():
    def avito_parser():
        announcements = Announcement.query.all()

        for announcement in announcements:

            region = announcement.region
            search_phrase = announcement.search_phrase
            announcement_id = announcement.id

            headers = {
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
            }
            result = requests.get(
                'https://www.avito.ru/' + region +
                '?q=' + search_phrase,
                headers=headers
                )
            result.raise_for_status()
            html = BS(result.content, 'lxml')
            content = html.select('.page-title-count-1oJOc')
            quantity_announcement = content[0].text

            quantity_announcement = QuantityAnnouncement(
                quantity_announcement=quantity_announcement,
                announcement=announcement_id,
                time=datetime.now()
                )
            db.session.add(quantity_announcement)
            db.session.commit()
