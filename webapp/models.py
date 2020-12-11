from webapp.db import db


class Announcement(db.Model):
    '''
    Это модель сущности построенная на основе sqlalchemy (db.py).

    search_phrase - атрибут хранящий название объявления.

    region - атрибут хранящий название города.
    '''
    id = db.Column(db.Integer, primary_key=True)
    search_phrase = db.Column(db.String())
    region = db.Column(db.String())


class QuantityAnnouncement(db.Model):
    '''
    Это модель сущности построенная на основе sqlalchemy (db.py),
    связана с сущностью Announcement при помощи ForeignKey.

    quantity_announcement - атрибут хранящий количество объявлений.

    time - атрибут хранящий временую метку.

    announcement - атрибут хранящий id сущности Announcement.
    '''
    id = db.Column(db.Integer, primary_key=True)
    quantity_announcement = db.Column(db.Integer())
    time = db.Column(db.DateTime)

    announcement = db.Column(
        db.Integer(),
        db.ForeignKey('announcement.id', ondelete='CASCADE')
        )