
def create_grid(lower_price, upper_price, grid_size):
    levels = []
    price = lower_price
    while price <= upper_price:
        levels.append(price)
        price += grid_size
    return levels


def place_order(side, amount, price):
    order = None
    try:
        order = exchange.create_order(
            symbol=symbol, 
            type='limit', 
            side=side, 
            amount=amount / price, 
            price=price
        )
        print(f"Placed {side} order for {amount / price} {symbol} at {price}")
    except Exception as e:
        print(f"Error placing order: {str(e)}")
    return order


def order_exists(price, side):
    open_orders = exchange.fetch_open_orders(symbol)
    for order in open_orders:
        if float(order['price']) == price and order['side'] == side:
            return True
    return False


def run_grid_bot():
    grid_levels = create_grid(lower_price, upper_price, grid_size)
    
    while True:
        try:
            ticker = exchange.fetch_ticker(symbol)
            current_price = ticker['last']
            print(f"Current price: {current_price}")

            for price in grid_levels:
                if current_price <= price and not order_exists(price, 'buy'):
                    place_order('buy', investment_amount, price)

                if current_price >= price and not order_exists(price, 'sell'):
                    place_order('sell', investment_amount, price)

            time.sleep(60)  

        except Exception as e:
            print(f"Error in grid bot: {str(e)}")
            time.sleep(60)


if __name__ == "__main__":
    run_grid_bot()
