
def get_current_price(symbol):
    ticker = exchange.fetch_ticker(symbol)
    return ticker['last']

def place_sell_order(amount):
    try:
        order = exchange.create_order(
            symbol=symbol, 
            type='market', 
            side='sell', 
            amount=amount
        )
        print(f"Sell order placed: {order}")
        return order
    except Exception as e:
        print(f"Error placing sell order: {str(e)}")


def run_trailing_close():
    global initial_price, trailing_price
    
    initial_price = get_current_price(symbol)
    trailing_price = initial_price * (1 - trailing_percentage / 100) 
    print(f"Initial price: {initial_price}, Trailing price: {trailing_price}")

    while True:
        try:
            current_price = get_current_price(symbol)
            print(f"Current price: {current_price}")
            

            if current_price > initial_price:
                initial_price = current_price
                trailing_price = current_price * (1 - trailing_percentage / 100)
                print(f"New trailing price set at: {trailing_price}")


            if current_price <= trailing_price:
                print(f"Trailing price hit: {trailing_price}, closing position...")
                place_sell_order(amount_to_sell)
                break  
            
            time.sleep(10) 

        except Exception as e:
            print(f"Error in trailing close logic: {str(e)}")
            time.sleep(10)


if __name__ == "__main__":
    run_trailing_close()
