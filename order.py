import pandas as pd
import numpy as np
from olist.data import Olist

class Order:
    def __init__(self):

        olist = Olist()
        self.data = olist.get_data()

    def get_wait_time(self, is_delivered=True):

        orders = self.data['orders'].copy()

        # Filtering orders by delivery status
        if is_delivered:

            orders = orders.query("order_status=='delivered'").copy()

        # Handling datetime
        orders.loc[:, 'order_purchase_timestamp'] = pd.to_datetime(orders['order_purchase_timestamp'])
        orders.loc[:, 'order_approved_at'] = pd.to_datetime(orders['order_approved_at'])
        orders.loc[:, 'order_delivered_carrier_date'] = pd.to_datetime(orders['order_delivered_carrier_date'])
        orders.loc[:, 'order_delivered_customer_date'] = pd.to_datetime(orders['order_delivered_customer_date'])
        orders.loc[:, 'order_estimated_delivery_date'] = pd.to_datetime(orders['rder_estimated_delivery_date'])

        # Delay vs Expected
        orders.loc[:, 'delay_vs_expected'] = (orders['order_delivered_customer_date'] -
                                              orders['order_estimated_delivery_date']) / np.timedelta64(24, 'h')

        def handle_delay(x):
            if x > 0:
                return x
            else:
                return 0

        orders.loc[:, 'delay_vs_expected'] = orders['delay_vs_expected'].apply(handle_delay)

        # Compute wait_time
        orders.loc[:, 'wait_time'] = (orders['order_delivered_customer_date'] -
                                      orders['order_purchase_timestamp']) / np.timedelta64(24, 'h')

        # Compute expected_wait_time
        orders.loc[:, 'expected_wait_time'] = (orders['order_estimated_delivery_date'] -
                                               orders['order_purchase_timestamp']) / np.timedelta64(24, 'h')


        return orders [['order_id', 'wait_time','expected_wait_time','delay_vs_expected', 'order_status']]

    def get_review_score(self):

        reviews = self.data['order_reviews'].copy()

        # Checking the extreme reviews with 1 and 5 stars
        def dim_is_five_star(d):
            if d == 5:
                return 1
            else:
                return 0
        def dim_is_one_star(d):
            if d == 1:
                return 1
            else:
                return 0

        reviews.loc['dim_is_five_star'] = reviews['review_score'].apply(dim_is_five_star)
        reviews.loc['dim_is_one_star'] = reviews['review_score'].apply(dim_is_one_star)

        return reviews[['order_id', 'dim_is_five_star', 'dim_is_one_star', 'reviews_score']]

    def get_number_items(self):

        data = self.data

        items = data['order_items'].groupby('order_id', as_index = False).agg({'order_item_id' : 'count'})
        items.columns = ['order_id', 'number_of_items']

        return items

    def get_number_of_sellers(self):

        data = self.data

        sellers = data['order_items'].groupby('order_id')['seller_id'].nunique().reset_index()
        sellers.columns = ['seller_id', 'number_of_sellers']

        return sellers

    def get_price_and_freight(self):

        data = self.data

        price_freight = data['order_items'].groupby('order_id', as_index=False).agg({'price': 'sum',
                                                                     'freight_value' : 'sum'})

        return price_freight

    def get_training_set(self, is_delivered=True):
        """
        Returns a clean DataFrame (without NaN), with the following columns:
        ['order_id', 'wait_time', 'expected_wait_time', 'delay_vs_expected',
        'order_status', 'dim_is_five_star', 'dim_is_one_star', 'review_score',
        'number_of_items', 'number_of_sellers', 'price', 'freight_value']
        """

        training_set = self.get_wait_time(is_delivered)\
            .merge(
                self.get_review_score(), on='order_id'
            ).merge(
                self.get_number_items(), on='order_id'
            ).merge(
                self.get_number_of_sellers(), on='order_id'
            ).merge(
                self.get_price_and_freight(), on='order_id'
            )

        return training_set.dropna()
