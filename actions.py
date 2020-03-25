# import libs
import rasa_sdk
from typing import Dict, Text, Any, List, Union, Optional
from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_sdk.events import SlotSet
from rasa_sdk import Action
from rasa_sdk.events import FollowupAction
from rasa_sdk.events import AllSlotsReset
import forex_python
from forex_python.converter import CurrencyRates
from datetime import datetime
import requests
# from word2number import w2n
import json
import logging
logger = logging.getLogger('fxbot.log')


#----------------------------------------------------------------------------------
# custom action to reset all slots
class AllSlotsReset(Action):
	def name(self):
		return 'action_slot_reset'
	def run(self, dispatcher, tracker, domain):
			return[AllSlotsReset()]

#---------------------------------------------------------------------------------------
## action to welcome
class welcomeuser(Action):
    def name(self) -> Text:
        return 'welcome_user'
    
    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text,Any]]:
        return[
        dispatcher.utter_message("Hi there! I'm fx-bot.I'm here to take your Forex orders.\nPlease go ahead and place your your order")]

#---------------------------------------------------------------------------------------
## custom form to ask for missing info 
class buyform(FormAction):

    def name(self) -> Text:
        return "order_form"

    @staticmethod
    # returns all the required slots
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["amount", "buy_currency", "sell_currency", "date", "currency_unit"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
            "amount": self.from_entity(entity= "amount",intent=["buy_currency1","enter_amount","sell_currency1"]),
            "currency_unit": self.from_entity(entity= "currency_unit",intent= ["buy_currency1","sell_currency1","enter_amount"]),
            "sell_currency": self.from_entity(entity= "sell_currency",intent= ["buy_currency1","sell_currency1","enter_sell_currency"]),
            "buy_currency": self.from_entity(entity= "buy_currency",intent= ["buy_currency1","sell_currency1","enter_buy_currency"]),
            "date": self.from_entity(entity= "date",intent= ["buy_currency1","sell_currency1","enter_date"])
            # "exchange_rate": self.from_entity(entity= "exchange_rate", intent= ["buy_currency1","sell_currency1","enter_exchangerate"]),
        }

## Validation for all required slots------------------------------------------------

    def validate_date(self,
        value:Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> Optional[Text]:
        date= tracker.get_slot("date")
        d= datetime.today().strftime("%m/%d/%Y")
        if (date == 'today'):
            return {'date': SlotSet("date",d)['value']}
        elif(date==d):
            return{'date':value}     
        elif (date == None):
            dispatcher.utter_message("Please enter a valid date")
            return[FollowupAction("action_listen")]
        else:
            dispatcher.utter_message("I'm sorry.For the time being I can only accept today's date or tomorrow's date")
            return{'date':None}

#--------------------------------------------
    
    @staticmethod
    def currency_list()-> List[Text]:
        """Database of supported currencies"""
        return ["inr","jpy","usd","nzd","cnh","cad","aud","eur","gbp","chf","cny","sgd","thb","mxn"]
          
    def validate_buy_currency(
        self,
        value:Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],) -> Dict[Text, Any]:

        # buy_currency= tracker.get_slot("buy_currency")
        # blist = ["inr","jpy","usd","nzd","cnh","cad","aud","eur","gbp","chf","cny","sgd","thb","mxn"]
        if value in self.currency_list():
            return{'buy_currency':value}
        else:
            dispatcher.utter_message("Please enter a valid buy currency")
            return{'buy_currency': None}
#--------------------------------------------------
             
    def validate_sell_currency(
        self,
        value:Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> Optional[Text]:

        # sell_currency= tracker.get_slot("sell_currency")
        # slist = ["inr","jpy","usd","nzd","cnh","cad","aud","eur","gbp","chf","cny","sgd","thb","mxn"]
        if value.lower() in self.currency_list():
            return{'sell_currency':value}
        else:
            dispatcher.utter_message("Please enter a valid sell currency")
            return{'sell_currency': None}
#--------------------------------------------------

    def validate_amount(self,
        value:Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> Optional[Text]:

        amount= tracker.get_slot("amount")
        if (float(amount) > 0):
            return{'amount':value}
        # elif (float(w2n.word_to_num(amount)) > 0):
        #     return{'amount': value}
        else:
            dispatcher.utter_message("Please enter a valid amount")
            return{'amount':None}
#--------------------------------------------------

    @staticmethod
    def currency_unit_list()-> List[Text]:
        """Database of supported currency units"""
        return ["million","billion","trillion"]

    def validate_currency_unit(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],) -> Dict[Text, Any]:
        """Validate currency value."""
        if value.lower() in self.currency_unit_list():
            return {"currency_unit": value}
        else:
            dispatcher.utter_message("Please enter a valid currency unit")
            return {"currency_unit": None}

#--------------------------------------------------
    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],) -> List[Dict]:
        dispatcher.utter_message("Fetching current exchange rates...")
        return[]

#---------------------------------------------------------------------------
class GetExchangerate(Action):
    def name(self) -> Text:
        return "get_exchange_rate"
    
    # base_url variable store base url
        base_url = "https://www.alphavantage.co/query"
        api_key = "L7FIGPZ8BODPN3BA"
    # parameters
        PARAMS = {'function': "CURRENCY_EXCHANGE_RATE", 'from_currency': from_currency,'to_currency': to_currency, 'apikey': api_key}
    # main_url variable store complete url
        main_url = base_url + "&from_currency =" + from_currency + \
            "&to_currency =" + to_currency + "&apikey =" + api_key
    # get method of requests module & return response object
        req_ob = requests.get(url=base_url, params=PARAMS)
        result = req_ob.json()

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text,Any]]:

        buy_currency= tracker.get_slot("buy_currency")
        sell_currency= tracker.get_slot("sell_currency")
        c= CurrencyRates()
        ex_rate = c.get_rate(buy_currency.upper(), sell_currency.upper())
        d= datetime.today().strftime("%m/%d/%Y")
        return [SlotSet("exchange_rate",ex_rate),SlotSet("date",d)]
    
#---------------------------------------------------------------------------------------------
class SepCurrency(Action):

    def name(self) -> Text:
        return "sep_currency"
    
    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text,Any]]:

        cp= tracker.get_slot("currency_pair")
        # cp= currency_pair.replace("/","")
        clist= ["inr","jpy","usd","nzd","cnh","cad","aud","eur","gbp","chf","cny","sgd","thb","mxn"]
        while(len(cp))<=6:
            s= ([cp[i:i+3] for i in range(0,len(cp),3)]) 
            buy_currency= s[0]
            sell_currency= s[1]
            if buy_currency not in clist:
                dispatcher.utter_message("Please enter a valid buy currency")
                return[FollowupAction("action_listen")]
            if sell_currency not in clist:
                dispatcher.utter_message("Please enter a valid sell currency")
                return[FollowupAction("action_listen")]
            dispatcher.utter_message("Fetching current exchange rates...")
            return[SlotSet("sell_currency",sell_currency),SlotSet("buy_currency",buy_currency)]
