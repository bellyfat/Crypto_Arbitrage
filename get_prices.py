from uniswap import Uniswap

address = None          # or None if you're not going to make transactions
private_key = None  # or None if you're not going to make transactions
version = 2                       # specify which version of Uniswap to use
provider = "https://mainnet.infura.io/v3/76255fe356544859a8229028ee40c291"    # can also be set through the environment variable `PROVIDER`
uniswap = Uniswap(address=address, private_key=private_key, version=version, provider=provider)

# Some token addresses we'll be using later in this guide
eth = "0x0000000000000000000000000000000000000000"
bat = "0x0D8775F648430679A709E98d2b0Cb6250d2887EF"
dai = "0x6B175474E89094C44Da98b954EedeAC495271d0F"
alp = "0x7cA4408137eb639570F8E647d9bD7B7E8717514A"
aave = "0x7Fc66500c84A76Ad7e9c93437bFc5Ac33E2DDaE9"
uma = "0x04Fa0d235C4abf4BcF4787aF4CF447DE572eF828"
sushi = "0x6B3595068778DD592e39A122f4f5a5cF09C90fE2"
link = "0x514910771AF9Ca656af840dff83E8264EcF986CA"
enj = "0xF629cBd94d3791C9250152BD8dfBDF380E2a3B9c"
chi = "0x0000000000004946c0e9F43F4Dee607b0eF1fA1c"
mana = "0x0F5D2fB29fb7d3CFeE444a200298f468908cC942"

currency_map = {'eth': eth, 'bat': bat, 'dai': dai, 'aave': aave, 'alp': alp, 'uma': uma, 'sushi': sushi, 'link': link, 'enj': enj, 'chi': chi, 'mana': mana}
currencies = list(currency_map.keys())

def fetch_price(token0, token1):
    return uniswap.get_price_input(currency_map[token0], currency_map[token1], 10**18)/10**18
