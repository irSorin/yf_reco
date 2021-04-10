def yf_reco(ticker):
    
    #source: https://towardsdatascience.com/parse-thousands-of-stock-recommendations-in-minutes-with-python-6e3e562f156d
    
    import requests
    
    lhs_url = 'https://query2.finance.yahoo.com/v10/finance/quoteSummary/'
    rhs_url = '?formatted=true&crumb=swg7qs5y9UP&lang=en-US&region=US&' \
              'modules=upgradeDowngradeHistory,recommendationTrend,' \
              'financialData,earningsHistory,earningsTrend,industryTrend&' \
              'corsDomain=finance.yahoo.com'
   
    url = lhs_url + ticker + rhs_url
    r = requests.get(url)
   
    if not r.ok:
        recommendation = 6
    try:
        result = r.json()['quoteSummary']['result'][0]
        recommendation =result['financialData']['recommendationMean']['fmt']
    except:
        recommendation = 6

    if int(float(recommendation)) <= 2:
        print('\033[32m' + recommendation)
    elif int(float(recommendation)) == 3:
        print('\033[33m' + recommendation)
    else: print('\033[31m' + recommendation)
