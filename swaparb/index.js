const { ChainId, Fetcher, WETH, Trade, Route, TokenAmount, TradeType } = require('@uniswap/sdk')

const chainId = ChainId.MAINNET;
const DAI_TOKEN_ADDRESS = "0x6B175474E89094C44Da98b954EedeAC495271d0F";

const res = async () => {
	const dai = await Fetcher.fetchTokenData(chainId, DAI_TOKEN_ADDRESS);
	const weth = WETH[chainId];
	const pair = await Fetcher.fetchPairData(dai, weth);
	const route = new Route([pair], weth);
	const trade = new Trade(route, new TokenAmount(weth, '817223992'), TradeType.EXACT_INPUT);
	console.log(trade.executionPrice.toSignificant(6));
	console.log(trade.nextMidPrice.toSignificant(6));
}

res();
