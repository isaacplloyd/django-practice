from django.shortcuts import render
from django.views.generic import TemplateView
import poloniex_api

polo = poloniex_api.Poloniex()

# Create your views here.
class GetLtc(TemplateView):
	template_name = 'ltc.html'
	
	def get_context_data(self):
		ctx = {
		"ltc_last":polo('returnTicker')['USDT_LTC']['last']
		}
		return ctx

class GetPrices(TemplateView):
	template_name = 'prices.html'
	
	def get_context_data(self):
		tickers = polo('returnTicker')
		price_btc = tickers['USDT_BTC']['last']
		price_ltc = tickers['USDT_LTC']['last']
		price_xrp = tickers['USDT_XRP']['last']
		
		ctx = {
		"btc_last":price_btc,
		"ltc_last":price_ltc,
		"xrp_last":price_xrp
		}
		return ctx

class Home(TemplateView):
	template_name = 'home.html'