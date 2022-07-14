from utils import import_data, convert_to_boolean
from unidecode import unidecode
from mlxtend.frequent_patterns import association_rules, apriori

class RecommendationSystem:

    def __init__(self):
        self.df = import_data()

    def preprocessing(self):
        #We put the name in lowercase and we remove special characters
        self.df['item_name'] = self.df['item_name'].apply(lambda x: unidecode(x.lower().strip()))
        #We organize the dataset: each row represent one transaction and each column represents all the product options with 0 (auscent) or 1 (present)
        items_by_transaction = self.df.groupby(['order_number', 'item_name'])['item_name'].count().reset_index(name ='Count')
        my_basket = items_by_transaction.pivot_table(index='order_number', columns='item_name', values='Count', aggfunc='sum').fillna(0)
        #We use the following functions because we need only 0 or 1, so if we have more than one unit of a product we should see 1 and not 2 or 3
        self.my_basket = my_basket.applymap(convert_to_boolean)

    def implementation(self):
        #We implement the model with a support of 0.003 and a metric of precision as lift
        frequent_items = apriori(self.my_basket, min_support = 0.03,use_colnames = True)
        rules = association_rules(frequent_items, metric = "lift", min_threshold = 1)
        #We sort by confidence, which is the probability of buying product B if product A is bought
        self.rules = rules.sort_values('confidence', ascending = False)

    def retrieve_rules(self):
        return self.rules

    def retrieve_top_associations(self):
        print("The Top 5 associations that have more likelihood are:")

        for _ in range(0,5):
            product_a = list(self.rules.iloc[_]['antecedents'])
            product_a = ', '.join(product_a)
            product_b = list(self.rules.iloc[_]['consequents'])[0]
            probability = str(round(self.rules.iloc[_]['confidence'],2)*100) + "%"
            print(f"If someone buy {product_a}. Then, the probability of buying this one {product_b} is around {probability}")
