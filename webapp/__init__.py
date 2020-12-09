from flask import Flask, render_template, flash, redirect, url_for, request
from webapp.db import db
from webapp.form import SearchForm
from webapp.models import Announcement, QuantityAnnouncement
from flask_migrate import Migrate

import requests
from bs4 import BeautifulSoup as BS
from datetime import datetime, date, timedelta


def create_app(config='config.py'):
    app = Flask(__name__)
    app.config.from_pyfile(config)
    db.init_app(app)
    migrate = Migrate(app, db)

    @app.route('/add', methods=['GET', 'POST'])
    def add():
        form = SearchForm()

        if request.method == 'POST':
            if form.validate_on_submit():
                region = form.region.data
                search_phrase = form.search_prhase.data
                date1 = form.date1.data
                date2 = form.date2.data
                try:
                    headers = {
                        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
                    }

                    result = requests.get(
                        'https://www.avito.ru/' + region +
                        '?q=' + search_phrase,
                        headers=headers
                        )
                    result.raise_for_status()
                except(requests.RequestException, ValueError):
                    flash('Неправильно задан регион или таких объявлений не существует')
                    return render_template('add.html', form=form)

                announcement_exists = Announcement.query.filter(
                        Announcement.search_phrase == search_phrase,
                        Announcement.region == region
                        ).count()

                if announcement_exists:
                    announcement = Announcement.query.filter(
                        Announcement.search_phrase == search_phrase,
                        Announcement.region == region
                        ).one()
                    announcement_id = announcement.id
                    return redirect(url_for('stat', announcement_id=announcement_id, date1=date1, date2=date2))
                else:
                    announcement = Announcement(
                        search_phrase=search_phrase, 
                        region=region
                        )
                    db.session.add(announcement)
                    db.session.commit()
                    announcement_id = announcement.id
                    return redirect(url_for('stat', announcement_id=announcement_id, date1=date1, date2=date2))

        return render_template('add.html', form=form)

    @app.route('/stat/<int:announcement_id>/<date1>/<date2>', methods=['GET', 'POST'])
    def stat(announcement_id: int, date1: str, date2: str):

        exists_quantity_announcement = QuantityAnnouncement.query.filter(
            QuantityAnnouncement.announcement == announcement_id
            ).count()

        if exists_quantity_announcement:
            quantity_announcement = QuantityAnnouncement.query.filter(
                QuantityAnnouncement.announcement == announcement_id,
                QuantityAnnouncement.time.between(date1, date2)
                ).all()
        else:
            try:
                announcement = Announcement.query.filter(Announcement.id == announcement_id).one()
                region = announcement.region
                search_phrase = announcement.search_phrase

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

                quantity_announcement = QuantityAnnouncement.query.filter(
                    QuantityAnnouncement.announcement == announcement_id,
                    QuantityAnnouncement.time.between(date.today(), date.today() + timedelta(days=1))
                    ).all()

                flash('Ваш запрос зарегистрирован и теперь будет собирать информацию каждый час!')
            
            except:
                flash('Такого обявления не существует!!(хватит баловаться с URL)')
                return render_template('stat.html')

        return render_template('stat.html', quantity_announcement=quantity_announcement)

    return app
