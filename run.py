from app import app

@app.route('/test')
def test():
    from models import Customers
    from models import CustomerHistory
    from models import Orders
    customer = Customers.query.filter_by(customerid=1).one()
    return f'<h1>EMAIL: {customer.email} GENERO: {customer.gender}</h1>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)