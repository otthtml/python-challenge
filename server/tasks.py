from json import load
from os.path import exists

def get_auction_market_values(model_id: int, year: int):
    assert(isinstance(model_id, int))
    assert(isinstance(year, int))
    assert(exists('api-response.json'))

    with open('api-response.json') as f:
        data = load(f)

        model = data.get(str(model_id))
        if model is None:
            return 'model_id not found'

        schedule = model.get('schedule')
        if schedule is None:
            return 'schedule not found'

        sale_details = model.get('saleDetails')
        if sale_details is None:
            return 'sale_details not found'

        cost = int(sale_details.get('cost'))
        if cost is None:
            return 'cost not found'

        years = schedule.get('years')
        if years is None:
            return 'years not found'

        default_market_ratio = schedule.get('defaultMarketRatio')
        default_auction_ratio = schedule.get('defaultAuctionRatio')

        year = years.get(str(year))
        if year is None:
            return 'year not found'

        market_ratio = year.get('marketRatio', default_market_ratio)
        auction_ratio = year.get('auctionRatio', default_auction_ratio)

        market_value = cost * float(market_ratio)
        auction_value = cost * float(auction_ratio)
    return {
        'MarketValue': market_value,
        'AuctionValue': auction_value
    }

if '__main__' == __name__:
    print(get_auction_market_values(67352, 2007))
    print(get_auction_market_values(87964, 2011))