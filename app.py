from flask import Flask, request, jsonify
from flask_cors import CORS
from models import db, Transaction

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
db.init_app(app)

@app.route('/submit', methods=['POST'])
def submit_transaction():
    data = request.json
    txn = Transaction(**data)
    db.session.add(txn)
    db.session.commit()
    return jsonify({'status': 'success'})

@app.route('/dashboard', methods=['GET'])
def get_dashboard_data():
    txns = Transaction.query.all()
    summary = {}
    for txn in txns:
        summary[txn.department] = summary.get(txn.department, 0) + txn.amount
    return jsonify(summary)

@app.route('/public', methods=['GET'])
def get_public_data():
    total = sum(t.amount for t in Transaction.query.all())
    return jsonify({'totalRevenue': total})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
