from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField
from wtforms.validators import DataRequired


class SearchForm(FlaskForm):
    '''
    Это создание формы имеющая следующие поля 

    
    '''
    search_prhase = StringField('Объявление', validators=[DataRequired()])
    region = StringField('Регион', validators=[DataRequired()])
    date1 = DateField('Начальная дата', validators=[DataRequired()], render_kw={"placeholder": "гггг-мм-дд"})
    date2 = DateField('Конечная дата', validators=[DataRequired()], render_kw={"placeholder": "гггг-мм-дд"})
    submit = SubmitField('Поиск', render_kw={'class': 'btn btn-dark'})