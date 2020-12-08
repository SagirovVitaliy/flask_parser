from webapp.db import db


class Announcement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    search_phrase = db.Column(db.String())
    region = db.Column(db.String())


class QuantityAnnouncement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quantity_announcement = db.Column(db.Integer())
    time = db.Column(db.DateTime)

    announcement = db.Column(
        db.Integer(),
        db.ForeignKey('announcement.id', ondelete='CASCADE')
        )
