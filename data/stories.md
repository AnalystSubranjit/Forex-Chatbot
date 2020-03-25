## exchange rate enquiry
* get_exrate{"buy_currency": "nzd", "sell_currency": "aud"}
    - slot{"buy_currency": "nzd"}
    - slot{"sell_currency": "aud"}
    - get_exchange_rate
    - slot{"exchange_rate": 0.9243600805}
    - utter_exrate
    - action_listen
    - utter_askanything
* deny
    - utter_thanksforenquiry
    - action_restart

## exchange rate enquiry
* get_exrate{"sell_currency": "usd", "buy_currency": "chf"}
    - slot{"buy_currency": "chf"}
    - slot{"sell_currency": "usd"}
    - get_exchange_rate
    - slot{"exchange_rate": 1.0039122919}
    - utter_exrate
    - action_listen
    - utter_askanything
* deny
    - utter_thanksforenquiry
    - action_restart

## exrate enquiry + sep currency
* get_exrate{"currency_pair": "nzdaud"}
    - slot{"currency_pair": "nzdaud"}
    - sep_currency
    - slot{"sell_currency": "aud"}
    - slot{"buy_currency": "nzd"}
    - get_exchange_rate
    - slot{"exchange_rate": 0.9243600805}
    - utter_exrate
    - action_listen
    - utter_askanything
* deny
    - utter_thanksforenquiry
    - action_restart

## buy order example 1
* buy_currency1{"buy_currency": "jpy"}
    - slot{"buy_currency": "jpy"}
    - order_form
    - form{"name": "order_form"}
    - slot{"buy_currency": "jpy"}
    - slot{"buy_currency": "jpy"}
    - slot{"requested_slot": "amount"}
* form: enter_amount{"amount": "1", "currency_unit": "million"}
    - slot{"amount": "1"}
    - slot{"currency_unit": "million"}
    - form: order_form
    - slot{"currency_unit": "million"}
    - slot{"amount": "1"}
    - slot{"requested_slot": "sell_currency"}
* form: enter_sell_currency{"sell_currency": "usd"}
    - slot{"sell_currency": "usd"}
    - form: order_form
    - slot{"sell_currency": "usd"}
    - slot{"requested_slot": "date"}
* form: enter_date{"date": "today"}
    - slot{"date": "today"}
    - form: order_form
    - slot{"date": "today"}
    - slot{"date": "11/14/2019"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - get_exchange_rate
    - slot{"exchange_rate": 0.0091877452}
    - utter_exrate
    - action_listen
* affirm
    - utter_confirm
    - utter_askanything
* deny
    - utter_goodbye
    - action_restart

## buy order example 2
* buy_currency1{"buy_currency": "cad"}
    - slot{"buy_currency": "cad"}
    - order_form
    - form{"name": "order_form"}
    - slot{"buy_currency": "cad"}
    - slot{"buy_currency": "cad"}
    - slot{"requested_slot": "amount"}
* form: enter_amount{"amount": "3", "currency_unit": "million"}
    - slot{"amount": "3"}
    - slot{"currency_unit": "million"}
    - form: order_form
    - slot{"currency_unit": "million"}
    - slot{"amount": "3"}
    - slot{"requested_slot": "sell_currency"}
* form: enter_sell_currency{"sell_currency": "nzd"}
    - slot{"sell_currency": "nzd"}
    - form: order_form
    - slot{"sell_currency": "nzd"}
    - slot{"requested_slot": "date"}
* form: enter_date{"date": "today"}
    - slot{"date": "today"}
    - form: order_form
    - slot{"date": "today"}
    - slot{"date": "11/14/2019"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - get_exchange_rate
    - slot{"exchange_rate": 1.1806469298}
    - utter_exrate
    - action_listen
* affirm
    - utter_askanything
* deny
    - utter_goodbye
    - action_restart

## sell order example 1
* sell_currency1{"sell_currency": "inr"}
    - slot{"sell_currency": "inr"}
    - order_form
    - form{"name": "order_form"}
    - slot{"sell_currency": "inr"}
    - slot{"sell_currency": "inr"}
    - slot{"requested_slot": "amount"}
* form: enter_amount{"amount": "1", "currency_unit": "million"}
    - slot{"amount": "1"}
    - slot{"currency_unit": "million"}
    - form: order_form
    - slot{"currency_unit": "million"}
    - slot{"amount": "1"}
    - slot{"requested_slot": "buy_currency"}
* form: enter_buy_currency{"buy_currency": "usd"}
    - slot{"buy_currency": "usd"}
    - form: order_form
    - slot{"buy_currency": "usd"}
    - slot{"requested_slot": "date"}
* form: enter_date{"date": "tomorrow"}
    - slot{"date": "tomorrow"}
    - form: order_form
    - slot{"date": "tomorrow"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - get_exchange_rate
    - slot{"exchange_rate": 72.0688715246}
    - utter_exrate
    - action_listen
* affirm
    - utter_confirm
    - utter_askanything
* deny
    - utter_goodbye
    - action_restart

## total information
* buy_currency1{"amount": "2.5", "currency_unit": "million", "buy_currency": "cad", "sell_currency": "usd", "date": "today"}
    - slot{"amount": "2.5"}
    - slot{"buy_currency": "cad"}
    - slot{"currency_unit": "million"}
    - slot{"date": "today"}
    - slot{"sell_currency": "usd"}
    - get_exchange_rate
    - slot{"exchange_rate": 0.7542489035}
    - utter_exrate
* affirm
    - utter_verify_tradeorder
* affirm{"amount": "2.5", "currency_unit": "million", "buy_currency": "cad", "exchange_rate": "0.754", "date": "today"}
    - slot{"amount": "2.5"}
    - slot{"buy_currency": "cad"}
    - slot{"currency_unit": "million"}
    - slot{"date": "today"}
    - slot{"exchange_rate": "0.754"}
    - utter_confirm
    - utter_askanything
* deny
    - utter_goodbye
    - action_restart

## getting exchange rate
* get_exrate{"buy_currency": "usd", "sell_currency": "eur", "date": "today"}
    - slot{"buy_currency": "usd"}
    - slot{"date": "today"}
    - slot{"sell_currency": "eur"}
    - get_exchange_rate
    - slot{"exchange_rate": 0.9085953116}
    - utter_exrate
* deny
    - utter_thanksforenquiry
    - action_restart

## buy order with missing sell currency and date
* buy_currency1{"amount": "5", "currency_unit": "million", "buy_currency": "eur"}
    - slot{"amount": "5"}
    - slot{"buy_currency": "eur"}
    - slot{"currency_unit": "million"}
    - order_form
    - form{"name": "order_form"}
    - slot{"amount": "5"}
    - slot{"buy_currency": "eur"}
    - slot{"currency_unit": "million"}
    - slot{"amount": "5"}
    - slot{"buy_currency": "eur"}
    - slot{"currency_unit": "million"}
    - slot{"requested_slot": "sell_currency"}
* form: enter_sell_currency{"sell_currency": "GBP"}
    - slot{"sell_currency": "GBP"}
    - form: order_form
    - slot{"sell_currency": null}
    - slot{"requested_slot": "sell_currency"}
* form: enter_sell_currency{"sell_currency": "gbp"}
    - slot{"sell_currency": "gbp"}
    - form: order_form
    - slot{"sell_currency": "gbp"}
    - slot{"requested_slot": "date"}
* form: enter_date{"date": "tomorrow"}
    - slot{"date": "tomorrow"}
    - form: order_form
    - slot{"date": "tomorrow"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - get_exchange_rate
    - slot{"exchange_rate": 0.8576}
    - utter_exrate
* affirm
    - utter_confirm
    - utter_askanything
* goodbye
    - utter_goodbye
    - action_restart

## interactive_story_1
* get_exrate{"buy_currency": "inr", "sell_currency": "usd"}
    - slot{"buy_currency": "inr"}
    - slot{"sell_currency": "usd"}
    - get_exchange_rate
    - slot{"exchange_rate": 0.0138756162}
    - utter_exrate
    - utter_askanything
* buy_currency1{"buy_currency": "inr", "sell_currency": "usd", "amount": "2.5", "currency_unit": "million"}
    - slot{"amount": "2.5"}
    - slot{"buy_currency": "inr"}
    - slot{"currency_unit": "million"}
    - slot{"sell_currency": "usd"}
    - utter_verify_tradeorder
* affirm
    - utter_confirm
    - utter_askanything
* goodbye
    - utter_goodbye
    - action_restart

## interactive_story_2
* sell_currency1{"sell_currency": "gbp"}
    - slot{"sell_currency": "gbp"}
    - order_form
    - form{"name": "order_form"}
    - slot{"sell_currency": "gbp"}
    - slot{"sell_currency": "gbp"}
    - slot{"requested_slot": "amount"}
* form: enter_amount{"amount": "20", "currency_unit": "billion"}
    - slot{"amount": "20"}
    - slot{"currency_unit": "billion"}
    - form: order_form
    - slot{"currency_unit": "billion"}
    - slot{"amount": "20"}
    - slot{"requested_slot": "buy_currency"}
* form: enter_buy_currency{"buy_currency": "CAD"}
    - slot{"buy_currency": "CAD"}
    - form: order_form
    - slot{"buy_currency": null}
    - slot{"requested_slot": "buy_currency"}
* form: enter_buy_currency{"buy_currency": "cad"}
    - slot{"buy_currency": "cad"}
    - form: order_form
    - slot{"buy_currency": "cad"}
    - slot{"requested_slot": "date"}
* form: enter_date{"date": "today"}
    - slot{"date": "today"}
    - form: order_form
    - slot{"date": "today"}
    - slot{"date": "11/13/2019"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - get_exchange_rate
    - slot{"exchange_rate": 0.5877192982}
    - utter_exrate
* affirm
    - utter_askanything
* goodbye
    - action_restart

## interactive_story_3
* buy_currency1{"buy_currency": "cad", "sell_currency": "aud", "amount": "1100000", "exchange_rate": "1.13", "date": "14nov2019"}
    - slot{"amount": "1100000"}
    - slot{"buy_currency": "cad"}
    - slot{"date": "14nov2019"}
    - slot{"exchange_rate": "1.13"}
    - slot{"sell_currency": "aud"}
    - utter_verify_tradeorder
* affirm{"amount": "1100000", "buy_currency": "cad"}
    - slot{"amount": "1100000"}
    - slot{"buy_currency": "cad"}
    - utter_confirm
    - utter_askanything
* goodbye
    - action_restart

## interactive_story_1
* buy_currency1{"buy_currency": "inr"}
    - slot{"buy_currency": "inr"}
    - order_form
    - form{"name": "order_form"}
    - slot{"buy_currency": "inr"}
    - slot{"buy_currency": "inr"}
    - slot{"requested_slot": "amount"}
* form: enter_amount{"amount": "20", "currency_unit": "million"}
    - slot{"amount": "20"}
    - slot{"currency_unit": "million"}
    - form: order_form
    - slot{"currency_unit": "million"}
    - slot{"amount": "20"}
    - slot{"requested_slot": "sell_currency"}
* form: enter_sell_currency{"sell_currency": "usd"}
    - slot{"sell_currency": "usd"}
    - form: order_form
    - slot{"sell_currency": "usd"}
    - slot{"requested_slot": "date"}
* form: enter_date{"date": "today"}
    - slot{"date": "today"}
    - form: order_form
    - slot{"date": "today"}
    - slot{"date": "11/13/2019"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - get_exchange_rate
    - slot{"exchange_rate": 0.0138756162}
    - utter_exrate
* affirm
    - utter_confirm
    - utter_askanything
* goodbye
    - utter_goodbye
    - action_restart

## interactive_story_2
* sell_currency1{"amount": "5", "currency_unit": "million", "sell_currency": "eur", "buy_currency": "gbp", "date": "1 week"}
    - slot{"amount": "5"}
    - slot{"buy_currency": "gbp"}
    - slot{"currency_unit": "million"}
    - slot{"date": "1 week"}
    - slot{"sell_currency": "eur"}
    - utter_denying_exrate
    - utter_askanything
* deny
    - utter_thanksforenquiry
    - action_restart

## interactive_story_1
* buy_currency1{"buy_currency": "usd"}
    - slot{"buy_currency": "usd"}
    - order_form
    - form{"name": "order_form"}
    - slot{"buy_currency": "usd"}
    - slot{"buy_currency": "usd"}
    - slot{"requested_slot": "amount"}
* form: enter_amount{"amount": "20", "currency_unit": "billion"}
    - slot{"amount": "20"}
    - slot{"currency_unit": "billion"}
    - form: order_form
    - slot{"currency_unit": "billion"}
    - slot{"amount": "20"}
    - slot{"requested_slot": "sell_currency"}
* form: enter_sell_currency{"sell_currency": "jpy"}
    - slot{"sell_currency": "jpy"}
    - form: order_form
    - slot{"sell_currency": "jpy"}
    - slot{"requested_slot": "date"}
* form: enter_date{"date": "tomorrow"}
    - slot{"date": "tomorrow"}
    - form: order_form
    - slot{"date": "tomorrow"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - get_exchange_rate
    - slot{"exchange_rate": 108.8406323823}
    - utter_exrate
* affirm
    - utter_confirm
    - utter_askanything
* goodbye
    - utter_goodbye
    - action_restart

## interactive_story_1
* buy_currency1{"buy_currency": "cad", "sell_currency": "usd"}
    - slot{"buy_currency": "cad"}
    - slot{"sell_currency": "usd"}
    - get_exchange_rate
    - slot{"exchange_rate": 0.7542489035}

## interactive_story_2
* greet
    - welcome_user
* buy_currency1{"buy_currency": "cad", "sell_currency": "usd"}
    - slot{"buy_currency": "cad"}
    - slot{"sell_currency": "usd"}
    - get_exchange_rate
    - slot{"exchange_rate": 0.7542489035}
    - utter_exrate
* affirm
    - order_form
    - form{"name": "order_form"}
    - slot{"buy_currency": "cad"}
    - slot{"sell_currency": "usd"}
    - slot{"requested_slot": "amount"}
* form: enter_amount{"amount": "1000000"}
    - slot{"amount": "1000000"}
    - form: order_form
    - slot{"amount": "1000000"}
    - slot{"requested_slot": "date"}
* enter_date{"date": "14 nov2019"}
    - slot{"date": "14 nov2019"}
    - utter_verify_tradeorder
* affirm
    - utter_confirm
    - utter_askanything
* goodbye
    - utter_goodbye
    - action_restart

## interactive_story_1
* buy_currency1{"amount": "5.5", "currency_unit": "million", "buy_currency": "cad", "sell_currency": "gbp"}
    - slot{"amount": "5.5"}
    - slot{"buy_currency": "cad"}
    - slot{"currency_unit": "million"}
    - slot{"sell_currency": "gbp"}
    - order_form
    - form{"name": "order_form"}
    - slot{"amount": "5.5"}
    - slot{"buy_currency": "cad"}
    - slot{"sell_currency": "gbp"}
    - slot{"currency_unit": "million"}
    - slot{"amount": "5.5"}
    - slot{"buy_currency": "cad"}
    - slot{"sell_currency": "gbp"}
    - slot{"currency_unit": "million"}
    - slot{"requested_slot": "date"}
* form: enter_date{"date": "tomorrow"}
    - slot{"date": "tomorrow"}
    - form: order_form
    - slot{"date": "tomorrow"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - get_exchange_rate
    - slot{"exchange_rate": 0.5877192982}
    - utter_exrate
* affirm
    - utter_verify_tradeorder
* affirm
    - utter_confirm
    - utter_askanything
* deny
    - utter_goodbye
    - action_restart

## interactive_story_2
    - welcome_user
* get_exrate{"sell_currency": "aud"}
    - slot{"sell_currency": "aud"}
    - utter_ask_buy_currency
* enter_buy_currency{"buy_currency": "usd"}
    - slot{"buy_currency": "usd"}
    - get_exchange_rate
    - slot{"exchange_rate": 1.4652916591}
    - utter_exrate
* deny
    - utter_thanksforenquiry
    - action_restart

## interactive_story_3
    - welcome_user
* get_exrate{"buy_currency": "nzd", "sell_currency": "aud"}
    - slot{"buy_currency": "nzd"}
    - slot{"sell_currency": "aud"}
    - get_exchange_rate
    - slot{"exchange_rate": 0.9360924077}
    - utter_exrate
* goodbye
    - utter_thanksforenquiry
    - action_restart

## interactive_story_4
    - welcome_user
* get_exrate{"buy_currency": "nzd", "sell_currency": "eur"}
    - slot{"buy_currency": "nzd"}
    - slot{"sell_currency": "eur"}
    - get_exchange_rate
    - slot{"exchange_rate": 0.5804504295}
    - utter_exrate
* buy_currency1{"amount": "2000000", "buy_currency": "nzd", "sell_currency": "eur", "exchange_rate": "0.5804", "date": "tomorrow"}
    - slot{"amount": "2000000"}
    - slot{"buy_currency": "nzd"}
    - slot{"date": "tomorrow"}
    - slot{"exchange_rate": "0.5804"}
    - slot{"sell_currency": "eur"}
    - utter_verify_tradeorder
* affirm
    - utter_confirm
    - utter_askanything
* goodbye
    - utter_goodbye
    - action_restart

## interactive_story_5
* get_exrate{"currency_pair": "cnysgd"}
    - slot{"currency_pair": "cnysgd"}
    - sep_currency
    - slot{"sell_currency": "sgd"}
    - slot{"buy_currency": "cny"}
    - get_exchange_rate
    - slot{"exchange_rate": 0.1940968673}
    - utter_exrate
* goodbye
    - utter_thanksforenquiry
    - action_restart

## interactive_story_1
* buy_currency1{"amount": "2.5", "currency_unit": "million", "buy_currency": "usd"}
    - slot{"amount": "2.5"}
    - slot{"buy_currency": "usd"}
    - slot{"currency_unit": "million"}
    - order_form
    - form{"name": "order_form"}
    - slot{"amount": "2.5"}
    - slot{"buy_currency": "usd"}
    - slot{"currency_unit": "million"}
    - slot{"amount": "2.5"}
    - slot{"buy_currency": "usd"}
    - slot{"currency_unit": "million"}
    - slot{"requested_slot": "sell_currency"}
* form: enter_sell_currency{"sell_currency": "jpy"}
    - slot{"sell_currency": "jpy"}
    - form: order_form
    - slot{"sell_currency": "jpy"}
    - slot{"requested_slot": "date"}
* enter_date{"date": "2 weeks"}
    - slot{"date": "2 weeks"}
    - utter_denying_exrate
    - utter_askanything
* goodbye
    - utter_thanksforenquiry
    - action_restart

## interactive_story_2
* greet
    - welcome_user
* buy_currency1{"amount": ".04", "currency_unit": "trillion", "buy_currency": "sgd", "date": "tomorrow"}
    - slot{"amount": ".04"}
    - slot{"buy_currency": "sgd"}
    - slot{"currency_unit": "trillion"}
    - slot{"date": "tomorrow"}
    - order_form
    - form{"name": "order_form"}
    - slot{"amount": ".04"}
    - slot{"buy_currency": "sgd"}
    - slot{"date": "tomorrow"}
    - slot{"currency_unit": "trillion"}
    - slot{"amount": ".04"}
    - slot{"buy_currency": "sgd"}
    - slot{"date": "tomorrow"}
    - slot{"currency_unit": "trillion"}
    - slot{"requested_slot": "sell_currency"}
* form: enter_sell_currency{"sell_currency": "nzd"}
    - slot{"sell_currency": "nzd"}
    - form: order_form
    - slot{"sell_currency": "nzd"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - get_exchange_rate
    - slot{"exchange_rate": 1.1485333333}
    - utter_exrate
* affirm
    - utter_confirm
    - utter_askanything
* goodbye
    - utter_goodbye
    - action_restart

## interactive_story_3
* sell_currency1{"sell_currency": "usd", "buy_currency": "jpy", "date": "tomorrow"}
    - slot{"buy_currency": "jpy"}
    - slot{"date": "tomorrow"}
    - slot{"sell_currency": "usd"}
    - order_form
    - form{"name": "order_form"}
    - slot{"buy_currency": "jpy"}
    - slot{"sell_currency": "usd"}
    - slot{"date": "tomorrow"}
    - slot{"buy_currency": "jpy"}
    - slot{"sell_currency": "usd"}
    - slot{"date": "tomorrow"}
    - slot{"requested_slot": "amount"}
* form: enter_amount{"amount": "6898999"}
    - slot{"amount": "6898999"}
    - form: order_form
    - slot{"amount": "6898999"}
    - slot{"requested_slot": "currency_unit"}
* form: enter_amount{"currency_unit": "million"}
    - slot{"currency_unit": "million"}
    - form: order_form
    - slot{"currency_unit": "million"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - get_exchange_rate
    - slot{"exchange_rate": 0.0091877452}
    - utter_exrate
* affirm
    - utter_verify_tradeorder
* affirm
    - utter_confirm
    - utter_askanything
* goodbye
    - utter_goodbye
    - action_restart

## interactive_story_1
* buy_currency1{"buy_currency": "usd"}
    - slot{"buy_currency": "usd"}
    - order_form
    - form{"name": "order_form"}
    - slot{"buy_currency": "usd"}
    - slot{"buy_currency": "usd"}
    - slot{"requested_slot": "amount"}
* form: enter_amount{"amount": "2.5", "currency_unit": "billion"}
    - slot{"amount": "2.5"}
    - slot{"currency_unit": "billion"}
    - form: order_form
    - slot{"currency_unit": "billion"}
    - slot{"amount": "2.5"}
    - slot{"requested_slot": "sell_currency"}
* form: enter_sell_currency{"sell_currency": "php"}
    - slot{"sell_currency": "php"}
    - form: order_form
    - slot{"sell_currency": null}
    - slot{"requested_slot": "sell_currency"}
* form: enter_sell_currency{"sell_currency": "aud"}
    - slot{"sell_currency": "aud"}
    - form: order_form
    - slot{"sell_currency": "aud"}
    - slot{"requested_slot": "date"}
* enter_date{"date": " 1 week"}
    - slot{"date": " 1 week"}
    - utter_denying_exrate
    - utter_askanything
* deny
    - utter_thanksforenquiry
    - action_restart

## interactive_story_2
* sell_currency1{"sell_currency": "usd", "amount": "20", "currency_unit": "billion", "buy_currency": "mxn", "date": "tomorrow"}
    - slot{"amount": "20"}
    - slot{"buy_currency": "mxn"}
    - slot{"currency_unit": "billion"}
    - slot{"date": "tomorrow"}
    - slot{"sell_currency": "usd"}
    - get_exchange_rate
    - slot{"exchange_rate": 0.0514965633}
    - utter_exrate
* affirm
    - utter_verify_tradeorder
* affirm
    - utter_confirm
    - utter_askanything
* goodbye
    - utter_goodbye
    - action_restart

## interactive_story_3
* get_exrate{"sell_currency": "jpy"}
    - slot{"sell_currency": "jpy"}
    - utter_ask_buy_currency
* enter_buy_currency{"buy_currency": "cny"}
    - slot{"buy_currency": "cny"}
    - get_exchange_rate
    - slot{"exchange_rate": 15.5005758207}
    - utter_exrate
* buy_currency1{"buy_currency": "cny", "sell_currency": "jpy", "amount": "200", "currency_unit": "million", "exchange_rate": "15.500"}
    - slot{"amount": "200"}
    - slot{"buy_currency": "cny"}
    - slot{"currency_unit": "million"}
    - slot{"exchange_rate": "15.500"}
    - slot{"sell_currency": "jpy"}
    - utter_verify_tradeorder
* affirm
    - utter_confirm
    - utter_askanything
* goodbye
    - utter_goodbye
    - action_restart

## interactive_story_1
* sell_currency1{"amount": "5", "currency_unit": "million", "sell_currency": "eur"}
    - slot{"amount": "5"}
    - slot{"currency_unit": "million"}
    - slot{"sell_currency": "eur"}
    - order_form
    - form{"name": "order_form"}
    - slot{"amount": "5"}
    - slot{"sell_currency": "eur"}
    - slot{"currency_unit": "million"}
    - slot{"amount": "5"}
    - slot{"sell_currency": "eur"}
    - slot{"currency_unit": "million"}
    - slot{"requested_slot": "buy_currency"}
* form: enter_buy_currency{"buy_currency": "nzd"}
    - slot{"buy_currency": "nzd"}
    - form: order_form
    - slot{"buy_currency": "nzd"}
    - slot{"requested_slot": "date"}
* form: enter_date{"date": "today"}
    - slot{"date": "today"}
    - form: order_form
    - slot{"date": "today"}
    - slot{"date": "11/14/2019"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - get_exchange_rate
    - slot{"exchange_rate": 0.5804504295}
    - utter_exrate
* affirm
    - utter_verify_tradeorder
* affirm
    - utter_goodbye
    - action_restart

## interactive_story_1
* get_exrate{"sell_currency": "aud"}
    - slot{"sell_currency": "aud"}
    - utter_ask_buy_currency
* enter_buy_currency{"buy_currency": "jpy"}
    - slot{"buy_currency": "jpy"}
    - get_exchange_rate
    - slot{"exchange_rate": 0.0134627264}
    - utter_exrate
* affirm
    - order_form
    - form{"name": "order_form"}
    - slot{"buy_currency": "jpy"}
    - slot{"sell_currency": "aud"}
    - slot{"requested_slot": "amount"}
* form: enter_amount{"amount": "20", "currency_unit": "million"}
    - slot{"amount": "20"}
    - slot{"currency_unit": "million"}
    - form: order_form
    - slot{"currency_unit": "million"}
    - slot{"amount": "20"}
    - slot{"requested_slot": "date"}
* form: enter_date{"date": "today"}
    - slot{"date": "today"}
    - form: order_form
    - slot{"date": "today"}
    - slot{"date": "11/14/2019"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - get_exchange_rate
    - slot{"exchange_rate": 0.0134627264}
    - utter_exrate
* affirm
    - utter_confirm
    - utter_askanything
* goodbye
    - utter_goodbye
    - action_restart

## interactive_story_2
* buy_currency1{"buy_currency": "eur", "sell_currency": "gbp", "date": "today"}
    - slot{"buy_currency": "eur"}
    - slot{"date": "today"}
    - slot{"sell_currency": "gbp"}
    - order_form
    - form{"name": "order_form"}
    - slot{"buy_currency": "eur"}
    - slot{"sell_currency": "gbp"}
    - slot{"date": "today"}
    - slot{"buy_currency": "eur"}
    - slot{"sell_currency": "gbp"}
    - slot{"date": "today"}
    - slot{"requested_slot": "amount"}
* form: enter_amount{"amount": ".3", "currency_unit": "billion"}
    - slot{"amount": ".3"}
    - slot{"currency_unit": "billion"}
    - form: order_form
    - slot{"currency_unit": "billion"}
    - slot{"amount": ".3"}
    - slot{"date": "11/14/2019"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - get_exchange_rate
    - slot{"exchange_rate": 0.8576}
    - utter_exrate
* affirm
    - utter_verify_tradeorder
    - utter_confirm
    - utter_askanything
* goodbye
    - utter_goodbye
    - action_restart

## interactive_story_3
* sell_currency1{"sell_currency": "usd", "amount": "2.5", "currency_unit": "million"}
    - slot{"amount": "2.5"}
    - slot{"currency_unit": "million"}
    - slot{"sell_currency": "usd"}
    - order_form
    - form{"name": "order_form"}
    - slot{"amount": "2.5"}
    - slot{"sell_currency": "usd"}
    - slot{"currency_unit": "million"}
    - slot{"amount": "2.5"}
    - slot{"sell_currency": "usd"}
    - slot{"currency_unit": "million"}
    - slot{"requested_slot": "buy_currency"}
* form: enter_buy_currency{"buy_currency": "gbp"}
    - slot{"buy_currency": "gbp"}
    - form: order_form
    - slot{"buy_currency": "gbp"}
    - slot{"requested_slot": "date"}
* enter_date{"date": "yesterday"}
    - slot{"date": "yesterday"}
    - utter_denying_exrate
    - utter_askanything
* goodbye
    - utter_thanksforenquiry
    - action_restart

## interactive_story_4
* sell_currency1{"currency_pair": "cadcny", "date": "tomorrow"}
    - slot{"currency_pair": "cadcny"}
    - slot{"date": "tomorrow"}
    - sep_currency
    - slot{"sell_currency": "cny"}
    - slot{"buy_currency": "cad"}
    - get_exchange_rate
    - slot{"exchange_rate": 5.2961211623}
    - order_form
    - form{"name": "order_form"}
    - slot{"buy_currency": "cad"}
    - slot{"sell_currency": "cny"}
    - slot{"date": "tomorrow"}
    - slot{"requested_slot": "amount"}
* enter_amount{"amount": "200000"}
    - slot{"amount": "200000"}
    - utter_exrate
* affirm
    - utter_confirm
    - utter_askanything
* goodbye
    - utter_goodbye
    - action_restart

## New Story

* buy_currency1{"buy_currency":"eur","sell_currency":"gbp","date":"today"}
    - slot{"buy_currency":"eur"}
    - slot{"date":"today"}
    - slot{"sell_currency":"gbp"}
    - order_form
    - slot{"buy_currency":"eur"}
    - slot{"date":"today"}
    - slot{"sell_currency":"gbp"}
    - utter_goodbye

## interactive_story_1
* sell_currency1{"sell_currency": "usd", "amount": "2.5", "currency_unit": "million"}
    - slot{"amount": "2.5"}
    - slot{"currency_unit": "million"}
    - slot{"sell_currency": "usd"}
    - order_form
    - form{"name": "order_form"}
    - slot{"amount": "2.5"}
    - slot{"sell_currency": "usd"}
    - slot{"currency_unit": "million"}
    - slot{"amount": "2.5"}
    - slot{"sell_currency": "usd"}
    - slot{"currency_unit": "million"}
    - slot{"requested_slot": "buy_currency"}
* form: enter_buy_currency{"buy_currency": "jpy"}
    - slot{"buy_currency": "jpy"}
    - form: order_form
    - slot{"buy_currency": "jpy"}
    - slot{"requested_slot": "date"}
* form: enter_date{"date": "today"}
    - slot{"date": "today"}
    - form: order_form
    - slot{"date": "today"}
    - slot{"date": "11/14/2019"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - get_exchange_rate
    - slot{"exchange_rate": 0.0091877452}
    - utter_exrate
* affirm
    - utter_verify_tradeorder
* affirm
    - utter_confirm
    - utter_askanything
* deny
    - utter_goodbye
    - action_restart

## interactive_story_2
* get_exrate{"buy_currency": "sgd", "date": "today"}
    - slot{"buy_currency": "sgd"}
    - slot{"date": "today"}
    - order_form
    - form{"name": "order_form"}
    - slot{"buy_currency": "sgd"}
    - slot{"date": "today"}
    - slot{"requested_slot": "amount"}
* form: enter_amount{"amount": "56", "currency_unit": "million"}
    - slot{"amount": "56"}
    - slot{"currency_unit": "million"}
    - form: order_form
    - slot{"currency_unit": "million"}
    - slot{"amount": "56"}
    - slot{"requested_slot": "sell_currency"}
* form: enter_sell_currency{"sell_currency": "usd"}
    - slot{"sell_currency": "usd"}
    - form: order_form
    - slot{"sell_currency": "usd"}
    - slot{"date": "11/14/2019"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - get_exchange_rate
    - slot{"exchange_rate": 0.7337333333}
    - utter_exrate
* affirm
    - utter_confirm
    - utter_goodbye
* goodbye
    - action_restart

## interactive_story_3
* get_exrate{"date": "today"}
    - slot{"date": "today"}
    - utter_ask_buy_currency
* enter_buy_currency{"buy_currency": "cny"}
    - slot{"buy_currency": "cny"}
    - utter_ask_sell_currency
* enter_sell_currency{"sell_currency": "jpy"}
    - slot{"sell_currency": "jpy"}
    - get_exchange_rate
    - slot{"exchange_rate": 15.5005758207}
    - utter_exrate
* goodbye
    - utter_thanksforenquiry
    - action_restart

## interactive_story_4
* sell_currency1{"sell_currency": "inr", "date": "today"}
    - slot{"date": "today"}
    - slot{"sell_currency": "inr"}
    - order_form
    - form{"name": "order_form"}
    - slot{"sell_currency": "inr"}
    - slot{"date": "today"}
    - slot{"sell_currency": "inr"}
    - slot{"date": "today"}
    - slot{"requested_slot": "amount"}
* form: enter_amount{"amount": "200006"}
    - slot{"amount": "200006"}
    - form: order_form
    - slot{"amount": "200006"}
    - slot{"requested_slot": "buy_currency"}
* enter_buy_currency{"buy_currency": "cny"}
    - slot{"buy_currency": "cny"}
    - get_exchange_rate
    - slot{"exchange_rate": 10.2447869447}
    - utter_exrate
* affirm
    - utter_verify_tradeorder
* affirm
    - utter_confirm
    - utter_askanything
* affirm
    - utter_goodbye
    - action_restart

## New Story

* sell_currency1{"sell_currency":"usd","amount":"2.5","currency_unit":"million"}
    - slot{"amount":"2.5"}
    - slot{"currency_unit":"million"}
    - slot{"sell_currency":"usd"}
    - order_form
    - form{"name":"order_form"}
    - slot{"amount":"2.5"}
    - slot{"sell_currency":"usd"}
    - slot{"currency_unit":"million"}
    - slot{"amount":"2.5"}
    - slot{"sell_currency":"usd"}
    - slot{"currency_unit":"million"}
    - slot{"requested_slot":"buy_currency"}
* enter_buy_currency{"buy_currency":"inr"}
    - slot{"buy_currency":"inr"}
    - order_form
    - slot{"buy_currency":"inr"}
    - slot{"requested_slot":"date"}
* enter_date{"date":"today"}
    - slot{"date":"today"}
    - order_form
    - slot{"date":"today"}
    - slot{"date":"11/14/2019"}
    - form{"name":null}
    - slot{"requested_slot":null}
    - get_exchange_rate
    - slot{"exchange_rate":0.0139026549}
    - utter_exrate
* affirm
    - utter_verify_tradeorder
* affirm
    - utter_confirm
    - utter_askanything
* goodbye
    - utter_goodbye
    - action_restart

## interactive_story_1
* buy_currency1{"currency_pair": "eurgbp", "amount": "1", "currency_unit": "million", "date": "today"}
    - slot{"amount": "1"}
    - slot{"currency_pair": "eurgbp"}
    - slot{"currency_unit": "million"}
    - slot{"date": "today"}
    - sep_currency
    - slot{"sell_currency": "gbp"}
    - slot{"buy_currency": "eur"}
    - get_exchange_rate
    - slot{"exchange_rate": 0.8576}
    - utter_exrate
* buy_currency1{"amount": "20", "currency_unit": "trillion", "buy_currency": "eur", "sell_currency": "gbp", "exchange_rate": "0.8576", "date": "14nov2019"}
    - slot{"amount": "20"}
    - slot{"buy_currency": "eur"}
    - slot{"currency_unit": "trillion"}
    - slot{"date": "14nov2019"}
    - slot{"exchange_rate": "0.8576"}
    - slot{"sell_currency": "gbp"}
    - utter_verify_tradeorder
* affirm
    - utter_confirm
    - utter_askanything
* goodbye
    - utter_goodbye
    - action_restart

## interactive_story_1
* buy_currency1{"amount": "10000", "buy_currency": "usd", "sell_currency": "aud", "date": "tomorrow"}
    - slot{"amount": "10000"}
    - slot{"buy_currency": "usd"}
    - slot{"date": "tomorrow"}
    - slot{"sell_currency": "aud"}
    - get_exchange_rate
    - slot{"exchange_rate": 1.4700924415}
    - utter_exrate
* affirm{"amount": "10000", "buy_currency": "usd", "sell_currency": "aud", "exchange_rate": "1.4700", "date": "tomorrow"}
    - slot{"amount": "10000"}
    - slot{"buy_currency": "usd"}
    - slot{"date": "tomorrow"}
    - slot{"exchange_rate": "1.4700"}
    - slot{"sell_currency": "aud"}
    - utter_confirm
    - utter_askanything
* deny
    - utter_goodbye
    - action_restart

## interactive_story_1
* buy_currency1{"buy_currency": "usd", "sell_currency": "inr", "date": "tomorrow"}
    - slot{"buy_currency": "usd"}
    - slot{"date": "tomorrow"}
    - slot{"sell_currency": "inr"}
    - order_form
    - form{"name": "order_form"}
    - slot{"buy_currency": "usd"}
    - slot{"sell_currency": "inr"}
    - slot{"date": "tomorrow"}
    - slot{"buy_currency": "usd"}
    - slot{"sell_currency": "inr"}
    - slot{"date": "tomorrow"}
    - slot{"requested_slot": "amount"}
* form: enter_amount{"amount": "100000"}
    - slot{"amount": "100000"}
    - form: order_form
    - slot{"amount": "100000"}
    - slot{"requested_slot": "currency_unit"}
* form: enter_amount{"currency_unit": "million"}
    - slot{"currency_unit": "million"}
    - form: order_form
    - slot{"currency_unit": "million"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - get_exchange_rate
    - slot{"exchange_rate": 71.8072507007}
    - utter_exrate
* affirm{"amount": "100000", "currency_unit": "million", "buy_currency": "usd"}
    - slot{"amount": "100000"}
    - slot{"buy_currency": "usd"}
    - slot{"currency_unit": "million"}
    - utter_confirm
    - utter_askanything
* get_exrate{"currency_pair": "eurgbp"}
    - slot{"currency_pair": "eurgbp"}
    - sep_currency
    - slot{"sell_currency": "gbp"}
    - slot{"buy_currency": "eur"}
    - get_exchange_rate
    - slot{"exchange_rate": 0.8533}
    - utter_exrate
* deny
    - utter_thanksforenquiry
    - action_restart

## interactive_story_1
* buy_currency1{"amount": "2.5", "currency_unit": "million", "buy_currency": "usd"}
    - slot{"amount": "2.5"}
    - slot{"buy_currency": "usd"}
    - slot{"currency_unit": "million"}
    - order_form
    - form{"name": "order_form"}
    - slot{"amount": "2.5"}
    - slot{"buy_currency": "usd"}
    - slot{"currency_unit": "million"}
    - slot{"amount": "2.5"}
    - slot{"buy_currency": "usd"}
    - slot{"currency_unit": "million"}
    - slot{"requested_slot": "sell_currency"}
* form: enter_sell_currency{"sell_currency": "php"}
    - slot{"sell_currency": "php"}
    - form: order_form
    - slot{"sell_currency": null}
    - slot{"requested_slot": "sell_currency"}
* form: enter_sell_currency{"sell_currency": "gbp"}
    - slot{"sell_currency": "gbp"}
    - form: order_form
    - slot{"sell_currency": "gbp"}
    - slot{"requested_slot": "date"}
* form: enter_date{"date": "today"}
    - slot{"date": "today"}
    - form: order_form
    - slot{"date": "today"}
    - slot{"date": "11/19/2019"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - get_exchange_rate
    - slot{"exchange_rate": 0.7714492361}
    - utter_exrate
* deny
    - utter_thanksforenquiry
    - action_restart

## interactive_story_2
    - welcome_user
* buy_currency1{"amount": "2.5", "currency_unit": "million", "buy_currency": "eur"}
    - slot{"amount": "2.5"}
    - slot{"buy_currency": "eur"}
    - slot{"currency_unit": "million"}
    - utter_ask_sell_currency
* enter_sell_currency{"sell_currency": "gbp"}
    - slot{"sell_currency": "gbp"}
    - utter_ask_date
* enter_date{"date": "today"}
    - slot{"date": "today"}
    - get_exchange_rate
    - slot{"exchange_rate": 0.8533}
    - utter_exrate
* deny
    - utter_thanksforenquiry
    - action_restart

## interactive_story_3
* sell_currency1{"sell_currency": "inr", "amount": "200", "currency_unit": "billion"}
    - slot{"amount": "200"}
    - slot{"currency_unit": "billion"}
    - slot{"sell_currency": "inr"}
    - utter_ask_buy_currency
* enter_buy_currency{"buy_currency": "jpy"}
    - slot{"buy_currency": "jpy"}
    - utter_ask_date
* enter_date{"date": "today"}
    - slot{"date": "today"}
    - get_exchange_rate
    - slot{"exchange_rate": 0.6588635421}
    - utter_exrate
* affirm
    - utter_verify_tradeorder
* affirm
    - utter_confirm
    - utter_askanything
* chitchat{"date": "tomorrows"}
    - slot{"date": "tomorrows"}
    - utter_default
* goodbye
    - utter_goodbye
    - action_restart

## interactive_story_4
* chitchat
    - welcome_user
* buy_currency1{"amount": ".03", "currency_unit": "trillion", "currency_pair": "phpthb", "date": "today"}
    - slot{"amount": ".03"}
    - slot{"currency_pair": "phpthb"}
    - slot{"currency_unit": "trillion"}
    - slot{"date": "today"}
    - sep_currency
    - slot{"sell_currency": "thb"}
    - slot{"buy_currency": "php"}
    - get_exchange_rate
    - slot{"exchange_rate": 0.5988635421}
    - utter_exrate
* goodbye
    - utter_thanksforenquiry
    - action_restart

## interactive_story_1
* greet
    - welcome_user
* chitchat{"date": "today"}
    - slot{"date": "today"}
    - utter_chitchat
* affirm
    - utter_goahead
* sell_currency1{"sell_currency": "cnh", "buy_currency": "jpy"}
    - slot{"buy_currency": "jpy"}
    - slot{"sell_currency": "cnh"}
    - utter_ask_amount
* enter_amount{"amount": ".09", "currency_unit": "billion"}
    - slot{"amount": ".09"}
    - slot{"currency_unit": "billion"}
    - utter_ask_date
* enter_date{"date": "tomorrow"}
    - slot{"date": "tomorrow"}
    - get_exchange_rate
    - slot{"exchange_rate": 15.45}
    - utter_exrate
* affirm
    - utter_confirm
    - utter_goodbye
    - action_restart

## interactive_story_1
* buy_currency1{"amount": "2.4", "currency_unit": "million", "buy_currency": "usd"}
    - slot{"amount": "2.4"}
    - slot{"buy_currency": "usd"}
    - slot{"currency_unit": "million"}
    - utter_ask_sell_currency
* enter_sell_currency{"sell_currency": "inr"}
    - slot{"sell_currency": "inr"}
    - utter_ask_date
* enter_date{"date": "today"}
    - slot{"date": "today"}
    - get_exchange_rate
    - slot{"exchange_rate": 71.8072507007}
    - utter_exrate
* affirm{"amount": "2.4", "currency_unit": "million", "buy_currency": "usd", "sell_currency": "inr", "exchange_rate": "71.807"}
    - slot{"amount": "2.4"}
    - slot{"buy_currency": "usd"}
    - slot{"currency_unit": "million"}
    - slot{"exchange_rate": "71.807"}
    - slot{"sell_currency": "inr"}
    - utter_confirm
    - utter_askanything
* goodbye
    - utter_goodbye
    - action_restart

## interactive_story_2
* chitchat{"date": "today"}
    - slot{"date": "today"}
    - utter_chitchat
* affirm
    - utter_goahead
* sell_currency1{"currency_pair": "sgdinr", "date": "tomorrow"}
    - slot{"currency_pair": "sgdinr"}
    - slot{"date": "tomorrow"}
    - sep_currency
    - slot{"sell_currency": "inr"}
    - slot{"buy_currency": "sgd"}
    - get_exchange_rate
    - slot{"exchange_rate": 52.7852728119}
    - utter_exrate
* affirm
    - utter_ask_amount
* enter_amount{"amount": ".02", "currency_unit": "trillion"}
    - slot{"amount": ".02"}
    - slot{"currency_unit": "trillion"}
    - utter_verify_tradeorder
* affirm
    - utter_confirm
    - utter_goodbye
    - action_restart

## interactive_story_3
* greet
    - welcome_user
* sell_currency1{"sell_currency": "usd", "buy_currency": "chf"}
    - slot{"buy_currency": "chf"}
    - slot{"sell_currency": "usd"}
    - get_exchange_rate
    - slot{"exchange_rate": 1.0092153285}
    - utter_exrate
* affirm
    - utter_ask_amount
* enter_amount{"amount": "1000000"}
    - slot{"amount": "1000000"}
    - utter_verify_tradeorder
* affirm
    - utter_confirm
    - utter_askanything
* goodbye
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - welcome_user
* buy_currency1{"amount": "50", "currency_unit": "million", "buy_currency": "usd"}
    - slot{"amount": "50"}
    - slot{"buy_currency": "usd"}
    - slot{"currency_unit": "million"}
    - order_form
    - form{"name": "order_form"}
    - slot{"amount": "50"}
    - slot{"buy_currency": "usd"}
    - slot{"currency_unit": "million"}
    - slot{"amount": "50"}
    - slot{"buy_currency": "usd"}
    - slot{"currency_unit": "million"}
    - slot{"requested_slot": "sell_currency"}
* form: enter_sell_currency{"sell_currency": "inr"}
    - slot{"sell_currency": "inr"}
    - form: order_form
    - slot{"sell_currency": "inr"}
    - slot{"requested_slot": "date"}
* enter_exchangerate{"date": "19nov2019"}
    - slot{"date": "19nov2019"}
    - get_exchange_rate
    - slot{"exchange_rate": 71.6778008486}
    - utter_exrate
* affirm
    - utter_confirm
    - utter_askanything
* affirm
    - utter_goahead
* sell_currency1{"sell_currency": "sgd", "buy_currency": "inr"}
    - slot{"buy_currency": "inr"}
    - slot{"sell_currency": "sgd"}
    - utter_ask_amount
* enter_amount{"amount": "2800000"}
    - slot{"amount": "2800000"}
    - utter_ask_date
* enter_date{"date": "today"}
    - slot{"date": "today"}
    - get_exchange_rate
    - slot{"exchange_rate": 0.0189804465}
    - utter_exrate
* deny
    - utter_thanksforenquiry
    - action_restart

## interactive_story_2
* get_exrate{"buy_currency": "usd"}
    - slot{"buy_currency": "usd"}
    - utter_ask_sell_currency
* enter_sell_currency{"sell_currency": "aud"}
    - slot{"sell_currency": "aud"}
    - get_exchange_rate
    - slot{"exchange_rate": 1.4655592669}
    - utter_exrate
* deny
    - utter_thanksforenquiry
    - action_restart

## interactive_story_3
* greet
    - welcome_user
* get_exrate{"sell_currency": "usd", "buy_currency": "jpy"}
    - slot{"buy_currency": "jpy"}
    - slot{"sell_currency": "usd"}
    - get_exchange_rate
    - slot{"exchange_rate": 0.0091955836}
    - utter_exrate
* sell_currency1{"sell_currency": "usd", "buy_currency": "jpy", "exchange_rate": "0.0091955836"}
    - slot{"buy_currency": "jpy"}
    - slot{"exchange_rate": "0.0091955836"}
    - slot{"sell_currency": "usd"}
    - utter_ask_amount
* enter_amount{"amount": ".0029", "currency_unit": "million"}
    - slot{"amount": ".0029"}
    - slot{"currency_unit": "million"}
    - utter_verify_tradeorder
* affirm
    - utter_confirm
    - utter_goodbye
    - action_restart

## interactive_story_4
* chitchat{"date": "today"}
    - slot{"date": "today"}
    - utter_default
* chitchat
    - utter_chitchat
* goodbye
    - utter_goodbye
    - action_restart

## interactive_story_1
* sell_currency1{"sell_currency": "usd"}
    - slot{"sell_currency": "usd"}
    - utter_ask_buy_currency
* enter_buy_currency{"buy_currency": "aud"}
    - slot{"buy_currency": "aud"}
    - utter_ask_date
* enter_date{"date": "19nov2019"}
    - slot{"date": "19nov2019"}
    - utter_ask_amount
* enter_amount{"amount": "2000000"}
    - slot{"amount": "2000000"}
    - get_exchange_rate
    - slot{"exchange_rate": 0.6823333744}
    - utter_exrate
* affirm{"amount": "2000000", "buy_currency": "aud", "sell_currency": "usd"}
    - slot{"amount": "2000000"}
    - slot{"buy_currency": "aud"}
    - slot{"sell_currency": "usd"}
    - utter_confirm
    - utter_askanything
* affirm
    - utter_goodbye
    - action_restart

## interactive_story_2
* chitchat{"date": "tomorrow"}
    - slot{"date": "tomorrow"}
    - utter_default
* get_exrate{"currency_pair": "AUDJPY"}
    - slot{"currency_pair": "AUDJPY"}
    - utter_askchoice
* buy_currency1{"buy_currency": "aud"}
    - slot{"buy_currency": "aud"}
    - sep_currency
    - slot{"sell_currency": "JPY"}
    - slot{"buy_currency": "AUD"}
    - get_exchange_rate
    - slot{"exchange_rate": 74.202291487}
    - utter_exrate
* deny
    - utter_thanksforenquiry
    - action_restart

## interactive_story_1
* chitchat{"date": "today"}
    - slot{"date": "today"}

## interactive_story_1
* greet
    - welcome_user
* nontrade{"date": "tomorrow"}
    - slot{"date": "tomorrow"}
    - utter_nontrade
* deny
    - utter_goahead
* get_exrate{"currency_pair": "sgdusd"}
    - slot{"currency_pair": "sgdusd"}
    - sep_currency
    - slot{"sell_currency": "usd"}
    - slot{"buy_currency": "sgd"}
    - get_exchange_rate
    - slot{"exchange_rate": 0.7350364964}
    - utter_exrate
* affirm
    - utter_ask_amount
* enter_amount{"amount": "0.25", "currency_unit": "trillion"}
    - slot{"amount": "0.25"}
    - slot{"currency_unit": "trillion"}
    - utter_verify_tradeorder
* affirm
    - utter_confirm
    - utter_goodbye
    - action_restart

## interactive_story_2
* nontrade
    - utter_nontrade
* goodbye
    - utter_goodbye
    - action_restart

## interactive_story_3
* nontrade
    - utter_nontrade
* affirm
    - utter_goahead
* buy_currency1{"amount": "2550000", "buy_currency": "usd", "date": " 1 week"}
    - slot{"amount": "2550000"}
    - slot{"buy_currency": "usd"}
    - slot{"date": " 1 week"}
    - utter_denying_exrate
    - utter_askanything
* buy_currency1{"buy_currency": "jpy", "date": "today"}
    - slot{"buy_currency": "jpy"}
    - slot{"date": "today"}
    - utter_ask_sell_currency
* enter_sell_currency{"sell_currency": "cny"}
    - slot{"sell_currency": "cny"}
    - get_exchange_rate
    - slot{"exchange_rate": 0.064609829}
    - utter_exrate
* enter_amount{"amount": "2.5", "currency_unit": "million"}
    - slot{"amount": "2.5"}
    - slot{"currency_unit": "million"}
    - utter_verify_tradeorder
* affirm
    - utter_confirm
    - utter_askanything
* goodbye
    - utter_goodbye
    - action_restart

## exchange rate with choice and continuing order
* get_exrate
    - utter_askchoice
* get_exrate{"buy_currency": "inr", "sell_currency": "jpy"}
    - slot{"buy_currency": "inr"}
    - slot{"sell_currency": "jpy"}
    - get_exchange_rate
    - slot{"exchange_rate": 1.5103937147}
    - utter_exrate
* buy_currency1{"buy_currency": "inr", "sell_currency": "jpy", "amount": "200", "currency_unit": "billion", "exchange_rate": "1.5103"}
    - slot{"amount": "200"}
    - slot{"buy_currency": "inr"}
    - slot{"currency_unit": "billion"}
    - slot{"exchange_rate": "1.5103"}
    - slot{"sell_currency": "jpy"}
    - utter_confirm
    - utter_askanything
* affirm
    - utter_goahead
* sell_currency1{"amount": "100000", "sell_currency": "php", "buy_currency": "nzd"}
    - slot{"amount": "100000"}
    - slot{"buy_currency": "nzd"}
    - slot{"sell_currency": "php"}
    - utter_ask_date
* enter_date{"date": "today"}
    - slot{"date": "today"}
    - get_exchange_rate
    - slot{"exchange_rate": 32.678550691}
    - utter_exrate
* affirm
    - utter_confirm
    - utter_askanything
* goodbye
    - utter_goodbye
    - action_restart

## interactive_story_1
* buy_currency1{"amount": "2000000"}
    - slot{"amount": "2000000"}
    - utter_ask_sell_currency
* enter_sell_currency{"sell_currency": "chf"}
    - slot{"sell_currency": "chf"}
    - utter_ask_buy_currency
* enter_buy_currency{"buy_currency": "cnh"}
    - slot{"buy_currency": "cnh"}
    - get_exchange_rate
    - utter_exrate
* affirm
    - utter_goahead
* buy_currency1{"amount": "2000000", "buy_currency": "cnh", "sell_currency": "chf", "exchange_rate": "7.09"}
    - slot{"amount": "2000000"}
    - slot{"buy_currency": "cnh"}
    - slot{"exchange_rate": "7.09"}
    - slot{"sell_currency": "chf"}
    - utter_verify_tradeorder
* affirm
    - utter_confirm
    - utter_askanything
* sell_currency1{"sell_currency": "jpy"}
    - slot{"sell_currency": "jpy"}
    - order_form
    - form{"name": "order_form"}
    - slot{"amount": "2000000"}
    - slot{"buy_currency": "cnh"}
    - slot{"sell_currency": "jpy"}
    - slot{"sell_currency": "jpy"}
    - slot{"requested_slot": "date"}
* form: enter_date{"date": "today"}
    - slot{"date": "today"}
    - form: order_form
    - slot{"date": "today"}
    - slot{"requested_slot": "currency_unit"}
* form: enter_amount{"amount": "2", "currency_unit": "million"}
    - slot{"amount": "2"}
    - slot{"currency_unit": "million"}
    - form: order_form
    - slot{"amount": "2"}
    - slot{"currency_unit": "million"}
    - slot{"date": "11/20/2019"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_buy_currency
* enter_buy_currency{"buy_currency": "sgd"}
    - slot{"buy_currency": "sgd"}
    - get_exchange_rate
    - slot{"exchange_rate": 79.6600039843}
    - utter_exrate
* affirm
    - utter_verify_tradeorder
* affirm
    - utter_confirm
    - action_restart

## New Story

* buy_currency1{"amount":"2.5","currency_unit":"million","date":"today","buy_currency":"usd"}
    - slot{"amount":"2.5"}
    - order_form
    - form{"name":"order_form"}
    - slot{"amount":"2.5"}
    - slot{"buy_currency":"usd"}
    - slot{"date":"today"}
    - slot{"currency_unit":"million"}
    - slot{"amount":"2.5"}
    - slot{"buy_currency":"usd"}
    - slot{"date":"today"}
    - slot{"currency_unit":"million"}
    - slot{"requested_slot":"sell_currency"}
* enter_sell_currency{"sell_currency":"aud"}
    - slot{"sell_currency":"aud"}
    - order_form
    - slot{"sell_currency":"aud"}
    - slot{"date":"11/21/2019"}
    - form{"name":null}
    - slot{"requested_slot":null}
    - get_exchange_rate
    - slot{"exchange_rate":1.4673116918}
    - utter_exrate
* affirm
    - utter_confirm
    - utter_askanything
* sell_currency1{"sell_currency":"usd","amount":"200","currency_unit":"million","date":"tomorrow"}
    - slot{"amount":"200"}
    - slot{"currency_unit":"million"}
    - slot{"date":"tomorrow"}
    - slot{"sell_currency":"usd"}
    - utter_denying_exrate
    - utter_askanything
* sell_currency1{"sell_currency":"usd","amount":"200","currency_unit":"million","date":"today"}
    - slot{"amount":"200"}
    - slot{"currency_unit":"million"}
    - slot{"date":"today"}
    - slot{"sell_currency":"usd"}
    - utter_verify_tradeorder
* affirm
    - utter_confirm
    - utter_askanything

## New Story

* get_exrate{"buy_currency":"cad","sell_currency":"jpy"}
    - slot{"buy_currency":"cad"}
    - slot{"sell_currency":"jpy"}
    - get_exchange_rate
    - slot{"exchange_rate":81.6179957992}
    - utter_exrate
* affirm{"amount":"36","currency_unit":"million","date":" 1 week"}
    - slot{"amount":"36"}
    - slot{"currency_unit":"million"}
    - slot{"date":" 1 week"}
    - action_default_fallback
    - slot{"buy_currency":"cad"}
    - slot{"sell_currency":"jpy"}
    - slot{"amount":"36"}
    - slot{"currency_unit":"million"}
    - slot{"date":" 1 week"}
    - utter_exrate
    - slot{"buy_currency":"cad"}
    - slot{"sell_currency":"jpy"}
    - slot{"amount":"36"}
    - slot{"currency_unit":"million"}
    - slot{"date":" 1 week"}
* goodbye
    - utter_goodbye
