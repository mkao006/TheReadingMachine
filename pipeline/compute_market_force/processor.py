import pandas as pd
import controller as ctr

target_data_table = 'MarketForce'
price_variables = ['GOI', 'Wheat', 'Maize', 'Barley', 'Soyabean', 'Rice']

market_sentiments = list()
for price in price_variables:
    model_data = ctr.create_model_data(price, price_variables)
    # TODO (Michael): Add in the ability to load previous weights as
    #                 prior. This will improve the stability of the
    #                 construction.
    weights = ctr.estimate_sentiment_weights(model_data, price)
    individual_price_sentiments = ctr.compute_market_sentiments(
        model_data, weights, 'date', price)
    market_sentiments.append(individual_price_sentiments)
    ctr.create_sentiment_plot(individual_price_sentiments, price)

market_sentiments_df = pd.concat(market_sentiments)
market_sentiments_df.to_sql(con=ctr.engine, name=target_data_table,
                            index=False, if_exists='replace')
