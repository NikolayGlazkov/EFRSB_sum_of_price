import requests
import re
from lxml import html 
from data_raw import *
# фио орбитражного упровляющего
def ol_name_info(cookie,number):
    url = 'https://old.bankrot.fedresurs.ru/PublisherListWindow.aspx?rwndrnd=0.25684540750068474'

    data_raw = f'''ctl00%24ScriptManagerWindowMaster=ctl00%24ScriptManagerWindowMaster%7Cctl00%24BodyPlaceHolder%24SearchArbitrManager1%24ibArmSearch&__EVENTTARGET=&__EVENTARGUMENT=&__VIEWSTATE=%2FwEPDwUKMTg2MDgzODM4Nw9kFgJmD2QWAgIDD2QWAgIDD2QWAmYPZBYCZg9kFgQCAQ8UKwACFCsAAg8WAh4XRW5hYmxlQWpheFNraW5SZW5kZXJpbmdoZBAWCGYCAQICAgMCBAIFAgYCBxYIFCsAAg9kFgQeBVN0eWxlBRN3aGl0ZS1zcGFjZTogbm93cmFwHgdvbmNsaWNrBQpDbGlja1RhYigpZBQrAAIPZBYEHwEFE3doaXRlLXNwYWNlOiBub3dyYXAfAgUKQ2xpY2tUYWIoKWQUKwACD2QWBB8BBRN3aGl0ZS1zcGFjZTogbm93cmFwHwIFCkNsaWNrVGFiKClkFCsAAg9kFgIfAgUKQ2xpY2tUYWIoKWQUKwACZGQUKwACZGQUKwACZGQUKwACZGQPFghmZmZmZmZmZhYBBW9UZWxlcmlrLldlYi5VSS5SYWRUYWIsIFRlbGVyaWsuV2ViLlVJLCBWZXJzaW9uPTIwMTIuMy4xMDE2LjQwLCBDdWx0dXJlPW5ldXRyYWwsIFB1YmxpY0tleVRva2VuPTEyMWZhZTc4MTY1YmEzZDRkFghmDw9kFgQfAQUTd2hpdGUtc3BhY2U6IG5vd3JhcB8CBQpDbGlja1RhYigpZAIBDw9kFgQfAQUTd2hpdGUtc3BhY2U6IG5vd3JhcB8CBQpDbGlja1RhYigpZAICDw9kFgQfAQUTd2hpdGUtc3BhY2U6IG5vd3JhcB8CBQpDbGlja1RhYigpZAIDDw9kFgIfAgUKQ2xpY2tUYWIoKWQCAw8UKwACDxYCHwBoZBUIDFJhZFBhZ2VWaWV3MQxSYWRQYWdlVmlldzIMUmFkUGFnZVZpZXczDlJhZFBhZ2VWaWV3U3JvElJhZFBhZ2VWaWV3Q29tcGFueRFSYWRQYWdlVmlld1BlcnNvbg5SYWRQYWdlVmlld0ZucwxSYWRQYWdlVmlldzQWCmYPZBYCAgEPZBYCZg9kFgICAQ9kFgJmD2QWAmYPZBYCAgEPZBYEAgEPZBYGZg8PZBYCHwIFQk9wZW5Nb2RhbFdpbmRvd19jdGwwMF9Cb2R5UGxhY2VIb2xkZXJfU2VhcmNoQXJiaXRyTWFuYWdlcjFfbXNTcm8oKWQCAQ8PZBYCHwIFQk9wZW5Nb2RhbFdpbmRvd19jdGwwMF9Cb2R5UGxhY2VIb2xkZXJfU2VhcmNoQXJiaXRyTWFuYWdlcjFfbXNTcm8oKWQCAg8PZBYCHwIFOENsZWFyX2N0bDAwX0JvZHlQbGFjZUhvbGRlcl9TZWFyY2hBcmJpdHJNYW5hZ2VyMV9tc1NybygpZAILDxYCHgVzdHlsZQUhZGlzcGxheTogbm9uZTsgdmlzaWJpbGl0eTogaGlkZGVuZAIED2QWAgIBD2QWAmYPZBYCAgEPZBYCAgEPZBYCZg9kFgICAQ88KwARAgEQFgAWABYADBQrAABkAgUPZBYCAgEPZBYCZg9kFgICAQ9kFgICAQ9kFgJmD2QWAgIBDzwrABECARAWABYAFgAMFCsAAGQCBg9kFgICAQ9kFgJmD2QWAgIBD2QWAgIBD2QWAmYPZBYCAgEPPCsAEQIBEBYAFgAWAAwUKwAAZAIHD2QWAgIBD2QWAmYPZBYCAgEPZBYCAgEPPCsAEQMADxYEHgtfIURhdGFCb3VuZGceC18hSXRlbUNvdW50AgVkARAWABYAFgAMFCsAABYCZg9kFgwCAQ8PZBYEHwMFD2N1cnNvcjpwb2ludGVyOx8CBaABamF2YXNjcmlwdDpjbG9zZURpYWxvZygnRm9yZWlnblN5c3RlbXwxfNCT0L7RgdGD0LTQsNGA0YHRgtCy0LXQvdC90LDRjyDQutC%2B0YDQv9C%2B0YDQsNGG0LjRjyDCq9CQ0LPQtdC90YLRgdGC0LLQviDQv9C%2BINGB0YLRgNCw0YXQvtCy0LDQvdC40Y4g0LLQutC70LDQtNC%2B0LLCuycpOxYCZg9kFgJmDxUBddCT0L7RgdGD0LTQsNGA0YHRgtCy0LXQvdC90LDRjyDQutC%2B0YDQv9C%2B0YDQsNGG0LjRjyDCq9CQ0LPQtdC90YLRgdGC0LLQviDQv9C%2BINGB0YLRgNCw0YXQvtCy0LDQvdC40Y4g0LLQutC70LDQtNC%2B0LLCu2QCAg8PZBYEHwMFD2N1cnNvcjpwb2ludGVyOx8CBU5qYXZhc2NyaXB0OmNsb3NlRGlhbG9nKCdFeHRlcm5hbE9yZ3wyOHzQptC10L3RgtGA0LDQu9GM0L3Ri9C5INCx0LDQvdC6INCg0KQnKTsWAmYPZBYCZg8VASTQptC10L3RgtGA0LDQu9GM0L3Ri9C5INCx0LDQvdC6INCg0KRkAgMPD2QWBB8DBQ9jdXJzb3I6cG9pbnRlcjsfAgVxamF2YXNjcmlwdDpjbG9zZURpYWxvZygnRXh0ZXJuYWxPcmd8MzB80KTQtdC00LXRgNCw0LvRjNC90LDRjyDRgdC70YPQttCx0LAg0YHRg9C00LXQsdC90YvRhSDQv9GA0LjRgdGC0LDQstC%2B0LInKTsWAmYPZBYCZg8VAUfQpNC10LTQtdGA0LDQu9GM0L3QsNGPINGB0LvRg9C20LHQsCDRgdGD0LTQtdCx0L3Ri9GFINC%2F0YDQuNGB0YLQsNCy0L7QsmQCBA8PZBYEHwMFD2N1cnNvcjpwb2ludGVyOx8CBWBqYXZhc2NyaXB0OmNsb3NlRGlhbG9nKCdFeHRlcm5hbE9yZ3wzMXzQpNC10LTQtdGA0LDQu9GM0L3QsNGPINC90LDQu9C%2B0LPQvtCy0LDRjyDRgdC70YPQttCx0LAnKTsWAmYPZBYCZg8VATbQpNC10LTQtdGA0LDQu9GM0L3QsNGPINC90LDQu9C%2B0LPQvtCy0LDRjyDRgdC70YPQttCx0LBkAgUPD2QWBB8DBQ9jdXJzb3I6cG9pbnRlcjsfAgVFamF2YXNjcmlwdDpjbG9zZURpYWxvZygnRXh0ZXJuYWxPcmd8MzJ80J7Qv9C10YDQsNGC0L7RgCDQldCk0KDQodCRJyk7FgJmD2QWAmYPFQEb0J7Qv9C10YDQsNGC0L7RgCDQldCk0KDQodCRZAIGDw8WAh4HVmlzaWJsZWhkZBgJBS1jdGwwMCRCb2R5UGxhY2VIb2xkZXIkUGVyc29uTGlzdCRndlBlcnNvbkxpc3QPZ2QFKGN0bDAwJEJvZHlQbGFjZUhvbGRlciR1Y1Nyb0xpc3QxJGd2U3JvZXMPZ2QFPmN0bDAwJEJvZHlQbGFjZUhvbGRlciRPcmdUcmFkZU9yZ2FuaXplckxpc3QxJGd2VHJhZGVPcmdhbml6ZXJzD2dkBUFjdGwwMCRCb2R5UGxhY2VIb2xkZXIkUGVyc29uVHJhZGVPcmdhbml6ZXJMaXN0MSRndlRyYWRlT3JnYW5pemVycw9nZAUxY3RsMDAkQm9keVBsYWNlSG9sZGVyJHVjQ29tcGFueUxpc3QkZ3ZDb21wYW55TGlzdA9nZAU7Y3RsMDAkQm9keVBsYWNlSG9sZGVyJFNlYXJjaEFyYml0ck1hbmFnZXIxJGd2QXJiaXRyTWFuYWdlcnMPZ2QFJ2N0bDAwJEJvZHlQbGFjZUhvbGRlciRGbnNMaXN0JGd2Rm5zTGlzdA9nZAUwY3RsMDAkQm9keVBsYWNlSG9sZGVyJEZvcmVpZ25TeXN0ZW1MaXN0MSRndk90aGVyDzwrAAwBCAIBZAUeX19Db250cm9sc1JlcXVpcmVQb3N0QmFja0tleV9fFg8FJmN0bDAwJEJvZHlQbGFjZUhvbGRlciRydHNQdWJsaXNoZXJUeXBlBR5jdGwwMCRCb2R5UGxhY2VIb2xkZXIkcmFkTXVsdGkFRGN0bDAwJEJvZHlQbGFjZUhvbGRlciRTZWFyY2hBcmJpdHJNYW5hZ2VyMSRjaGJXaXRoUHVibGljYXRlZE1lc3NhZ2VzBTZjdGwwMCRCb2R5UGxhY2VIb2xkZXIkU2VhcmNoQXJiaXRyTWFuYWdlcjEkaWJBcm1TZWFyY2gFNWN0bDAwJEJvZHlQbGFjZUhvbGRlciRTZWFyY2hBcmJpdHJNYW5hZ2VyMSRpYkFybUNsZWFyBTljdGwwMCRCb2R5UGxhY2VIb2xkZXIkT3JnVHJhZGVPcmdhbml6ZXJMaXN0MSRidG5TZWFyY2hPcmcFPGN0bDAwJEJvZHlQbGFjZUhvbGRlciRQZXJzb25UcmFkZU9yZ2FuaXplckxpc3QxJGJ0blNlYXJjaFBycwUsY3RsMDAkQm9keVBsYWNlSG9sZGVyJHVjU3JvTGlzdDEkaWJTcm9TZWFyY2gFK2N0bDAwJEJvZHlQbGFjZUhvbGRlciR1Y1Nyb0xpc3QxJGliU3JvQ2xlYXIFNGN0bDAwJEJvZHlQbGFjZUhvbGRlciR1Y0NvbXBhbnlMaXN0JGJ0bkNvbXBhbnlTZWFyY2gFOWN0bDAwJEJvZHlQbGFjZUhvbGRlciR1Y0NvbXBhbnlMaXN0JGJ0bkNsZWFyQ29tcG5heUZpbHRlcgUwY3RsMDAkQm9keVBsYWNlSG9sZGVyJFBlcnNvbkxpc3QkYnRuUGVyc29uU2VhcmNoBTVjdGwwMCRCb2R5UGxhY2VIb2xkZXIkUGVyc29uTGlzdCRidG5DbGVhclBlcnNvbkZpbHRlcgUqY3RsMDAkQm9keVBsYWNlSG9sZGVyJEZuc0xpc3QkYnRuRm5zU2VhcmNoBS9jdGwwMCRCb2R5UGxhY2VIb2xkZXIkRm5zTGlzdCRidG5DbGVhckZuc0ZpbHRlcnbq1kt2dvlcp%2BlwecAtI58L4%2BW4&__VIEWSTATEGENERATOR=B54F2736&__EVENTVALIDATION=%2FwEdACUtzM%2BMgBmqDCNS%2FCDCesHF8GT3Qp5%2Fiyzq9V7XhZLN2Y7HhgdTgGra9PRFp4GAvMLtjZ1kAuMZjVUjdSST0iThTfUXqioHwXTYQ6Qe76nkanqbqqvyYiWMKm1JdR2YNfQOaeyFYxWC423fzgSBjKqcyiAD9tq9SCtWJ8PtyAW7AsrTdyggQfr90KR0aAYh27NYIz2YoYyJ8O2wT8jQeWvtTy%2FoRtSzpiVwAGhR39DsuzazIlHyte1HSO4JFOtKDW%2B7igjWvWF52wXkcsE9g8xz%2FBlra%2B0HXrF7j8ELRQ4NDq7RKKFBAngy4SfhR4aoACvFIVC7lNsdNB8Aq6CEKYwEpbIIiNGckZEwkDQqyIkTpld5UUbodeIpt9VkUywVpRLyCjrxRrNSz%2FtwF9Wt6Za3Eo5hXun1pQDChkRJmQ8oK6Dk3u575SQM0Y65PXw0Es%2FdutFiqhunsaER7vo%2FwaNkraUXic7c4AFo2D3BGTqI6hCpaDs3lZDyLAZGt39Df241SQPCcFuEe9X3o4Asmi9TDLYQFEHsZicgE%2F%2FLFD%2BUyAZQJ3nSNgR3GHrnK98iaEGatjfIxRysJFI7bZF1uX6KjDDZX7%2Flf0W207RbXq7Px626WCzwDhPUCehYPy9moVROO3IWV%2FXjdFo%2FizsD4vaNUr63fvD8ajjGhVfxHgquAC297WvfOJaTQAmwZLeoLjzWh39gvUIlZ0PyDuCNAgaxqEWuz0kWf7aJMPR6KAzFcwyZVDeio3Hf8cID%2FGZI1%2Fy%2FIRtVxzp2nV90zz54h%2BtfhuzZSsiZXbZ3hoJ49fXxjFMDNtE%3D&ctl00_BodyPlaceHolder_rtsPublisherType_ClientState=%7B%22selectedIndexes%22%3A%5B%220%22%5D%2C%22logEntries%22%3A%5B%5D%2C%22scrollState%22%3A%7B%7D%7D&ctl00%24BodyPlaceHolder%24SearchArbitrManager1%24msSro%24tbSelectedText=&ctl00%24BodyPlaceHolder%24SearchArbitrManager1%24msSro%24hfSelectedValue=&ctl00%24BodyPlaceHolder%24SearchArbitrManager1%24msSro%24hfSelectedType=&ctl00%24BodyPlaceHolder%24SearchArbitrManager1%24tbLastName=&ctl00%24BodyPlaceHolder%24SearchArbitrManager1%24tbFirstName=&ctl00%24BodyPlaceHolder%24SearchArbitrManager1%24tbMiddleName=&ctl00%24BodyPlaceHolder%24SearchArbitrManager1%24tbRegNumFrs={number}&ctl00%24BodyPlaceHolder%24SearchArbitrManager1%24hfMaxSize=&ctl00%24BodyPlaceHolder%24OrgTradeOrganizerList1%24tbOrgName=&ctl00%24BodyPlaceHolder%24OrgTradeOrganizerList1%24tbOrgAddress=&ctl00%24BodyPlaceHolder%24PersonTradeOrganizerList1%24tbPrsLastName=&ctl00%24BodyPlaceHolder%24PersonTradeOrganizerList1%24tbPrsFirstName=&ctl00%24BodyPlaceHolder%24PersonTradeOrganizerList1%24tbPrsMiddleName=&ctl00%24BodyPlaceHolder%24PersonTradeOrganizerList1%24tbPrsAddress=&ctl00%24BodyPlaceHolder%24ucSroList1%24tbRegNum=&ctl00%24BodyPlaceHolder%24ucSroList1%24tbName=&ctl00%24BodyPlaceHolder%24ucCompanyList%24tbCompanyName=&ctl00%24BodyPlaceHolder%24PersonList%24tbLastName=&ctl00%24BodyPlaceHolder%24PersonList%24tbFirstName=&ctl00%24BodyPlaceHolder%24PersonList%24tbMiddleName=&ctl00%24BodyPlaceHolder%24FnsList%24tbFnsDepartmentName=&ctl00%24BodyPlaceHolder%24FnsList%24tbFnsDepartmentInn=&ctl00%24BodyPlaceHolder%24FnsList%24tbFnsDepartmentCode=&ctl00_BodyPlaceHolder_radMulti_ClientState=&__ASYNCPOST=true&ctl00%24BodyPlaceHolder%24SearchArbitrManager1%24ibArmSearch.x=57&ctl00%24BodyPlaceHolder%24SearchArbitrManager1%24ibArmSearch.y=15'''

    headers = { 'Accept': '*/*', 'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'https://old.bankrot.fedresurs.ru',
    'Referer': 'https://old.bankrot.fedresurs.ru/PublisherListWindow.aspx?rwndrnd=0.25684540750068474',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'X-MicrosoftAjax': 'Delta=true',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': 'Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': "macOS"}
    x = requests.post(url, data=data_raw,headers= headers,cookies=cookie)
    # регулярка для поиска фио и номера
    
    

    pattern = re.compile(
    r'onclick="javascript:closeDialog\(&#39;ArbitrManager\|(\d+)\|(.+?)&#39;\);".*?'
    r'<td style="width:29%;">\s*(.+?)\s*</td>',
    re.DOTALL
)

    matches = pattern.findall(x.text)

    for match in matches:
        number = match[0]
        name_from_onclick = match[1]
        name_from_td = match[2]

    return (number, name_from_onclick)

# ссылка со всесеми сообщениями
def get_oll_mssege(cookie,data_raw):
    url = 'https://old.bankrot.fedresurs.ru/Messages.aspx?attempt=1'


    headers = { 'Accept': '*/*', 'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'https://old.bankrot.fedresurs.ru',
    'Referer': 'https://old.bankrot.fedresurs.ru/PublisherListWindow.aspx?rwndrnd=0.25684540750068474',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'X-MicrosoftAjax': 'Delta=true',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': 'Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': "macOS"}
    x = requests.post(url, data=data_raw,headers= headers,cookies=cookie)
    # s = 
    # result = re.search(s, x.text)
    return x.text

