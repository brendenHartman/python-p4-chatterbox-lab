from flask import Flask, request, make_response, jsonify
from flask_cors import CORS
from flask_migrate import Migrate

from models import db, Message

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

CORS(app)
migrate = Migrate(app, db)

db.init_app(app)

@app.route('/messages', methods=['GET','POST'])
def messages():
    if request.method == 'GET':
        messages = []
        for message in Message.query.order_by(Message.created_at).all():
            dicts = message.to_dict()
            messages.append(dicts)
        return make_response(messages, 200)
    elif request.method == 'POST':
        new = Message(
            body = request.get_json().get('body'),
            username = request.get_json().get('username'),
        )
        db.session.add(new)
        db.session.commit()
        new_dict = new.to_dict()
        resp = make_response(new_dict,201)
        return resp

@app.route('/messages/<int:id>', methods=['PATCH','DELETE'])
def messages_by_id(id):
    pass
    message = Message.query.filter_by(id=id).first()
    if request.method == 'PATCH':
        setattr(message, 'body', request.get_json().get('body'))
        db.session.add(message)
        db.session.commit()
        dicts=message.to_dict()
        return make_response(dicts, 200)
        
    elif request.method == 'DELETE':
        db.session.delete(message)
        db.session.commit()

        return make_response({
            'delete_successful': True,
            'message': 'Message deleted.'
        },200)

if __name__ == '__main__':
    app.run(port=5555)
