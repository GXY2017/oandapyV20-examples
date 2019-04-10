# -*- coding: utf-8 -*-
"""retrieve the tradable instruments for account."""

import json
import oandapyV20
import oandapyV20.endpoints.accounts as accounts
from exampleauth import exampleAuth
from pandas.io.json import json_normalize

accountID, token = exampleAuth()
client = oandapyV20.API(access_token=token)

r = accounts.AccountInstruments(accountID=accountID)
rv = client.request(r)
print(json.dumps(rv, indent=2))
all_instru = json_normalize(rv['instruments'])

