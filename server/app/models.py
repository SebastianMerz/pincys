from app import db

class pintrest_picture(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    pintrest_ID = db.Column(db.Integer, unique = True)
    picture_URL = db.Column(db.String(256), unique = True)
    suggestions = db.relationship('suggestion', backref = 'pintrest_pin', lazy='dynamic')
    
    def __repr__(self):
        return 'Pinterest picture: ' + str(self.pintrest_ID) + ' Url: ' + self.picture_URL

class suggestion(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    picture_URL = db.Column(db.String(256), unique = True)
    user_rating = db.Column(db.Integer, unique = True)
    mturk_rating = db.Column(db.Integer, unique = True)
    click_thru_rate = db.Column(db.Integer, unique = True)
    view_count = db.Column(db.Integer, unique = True)
    product_URL = db.Column(db.String(256), unique = True)
    product_title = db.Column(db.String(128), unique = True)
    pintrest_id = db.Column(db.Integer, db.ForeignKey('pintrest_picture.id'))
    
    def __repr__(self):
        return 'Suggestion: ' + self.product_title + ' product url: ' + self.product_URL