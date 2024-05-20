from flask import jsonify, request
from models.approved import Approved
from models.databaseconfig import db


def add_approved():
    user_id = request.json['user_id']
    message_id = request.json['message_id']
    message = request.json['message']
    approved = Approved(user_id=user_id, message_id=message_id, message=message)
    db.session.add(approved)
    db.session.commit()
    return approved.to_dict()
def get_approved(user_id):
    approved = Approved.query.filter_by(user_id=user_id).all()
    return approved.to_dict()

def delete_approved(user_id):
    approved = Approved.query.filter_by(user_id=user_id).delete()
    db.session.commit()
    return jsonify({'message_id': 'Deleted successfully'})

