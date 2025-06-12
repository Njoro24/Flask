from flask import Flask, jsonify
from flask_migrate import Migrate
from models import db, Customer
from flask import make_response

app = Flask(__name__)

# Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecom.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize db and migrations
db.init_app(app)
migrate = Migrate(app, db)

@app.get('/customers')
def get_all_customers():
    customers = Customer.query.all()
    customer_list = [
        {
            "id": customer.id,
            "first_name": customer.first_name,
            "last_name": customer.last_name,
            "email": customer.email,
            "phone": customer.phone,
            "gender": customer.gender,
            "age": customer.age,
            "created_at": customer.created_at.strftime('%Y-%m-%d %H:%M:%S')
        }
        for customer in customers
    ]

    return jsonify(customers=customer_list)

@app.get("/customers/<int:id>")
def get_one_customer(id):
    # query the databse and we get a customer by the customer id
    # if the customer exists -> return the details of that customer
    # else -> rreturn an appropriate response and the appropriate status code

    # .get(id)
    # technique 1
    # customer = Customer.query.get(id)

    # filter_by - technique 2
    customer = Customer.query.filter_by(id=id).first()

    if customer:
        customer_dict = {
            "id": customer.id,
            "first_name": customer.first_name,
            "last_name": customer.last_name,
            "email": customer.email,
            "phone": customer.phone,
            "gender": customer.gender,
            "age": customer.age,
        }
        return make_response(customer_dict, 200)
    else:
        return make_response({"status": 404, "message": "No customer found"}, 404)


# post
# serialization to_dict()