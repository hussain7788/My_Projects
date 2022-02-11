from app1.models import Product


class Basket():

    def __init__(self, request):
        self.session = request.session
        basket = self.session.get('skey')
        if 'skey' not in request.session:
            basket = self.session['skey'] = {}
        self.basket = basket

    def add(self, product, qty):
        # Adding and updating the users basket session data
        product_id = str(product.id)
        if product_id in self.basket:
            self.basket[product_id]['qty'] = qty
        else:
            self.basket[product_id] = {
                'price': str(product.p_price), 'qty': qty}

        self.save()

    def __len__(self):
        # get the basket qty and count the qty of itemsprint
        return sum(item['qty'] for item in self.basket.values())

    def __iter__(self):
        # Collect the product_id in the session data to query the database and return products
        product_ids = self.basket.keys()
        products = Product.objects.filter(id__in=product_ids)
        basket = self.basket.copy()

        for product in products:
            basket[str(product.id)]['product'] = product

        for item in basket.values():
            item['price'] = float(item['price'])
            item['total_price'] = item['price'] * item['qty']
            print("basket values::", basket)
            yield item

    def update(self, product, qty):
        # Update values in session data

        product_id = str(product)
        if product_id in self.basket:
            self.basket[product_id]['qty'] = qty
        self.save()

    def get_total_price(self):
        return sum(float(item['price']) * item['qty'] for item in self.basket.values())

    def delete(self, product):
        # Delete item from session data
        product_id = str(product)

        if product_id in self.basket:
            del self.basket[product_id]
            print(product_id)
            self.save()

    def save(self):
        self.session.modified = True
