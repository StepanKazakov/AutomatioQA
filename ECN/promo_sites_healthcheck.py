import requests
import time


while True:

    url = 'https://client.ecnbroker.lv/api/server_status'
    ecn_kim = 'https://client.ecn-broker.org/api/server_status' #ECN Ким Версия для Кима на англ
    ecn_matvey = 'https://client.ecnbroker.in/api/server_status' # 	ECN Матвей 	Русский
    ecn_osipov = 'https://client.ecnbroker.li/api/server_status' # ECN Осипов Русский
    ecn_vladimir ='https://client.ecnbroker.markets/api/server_status' # ECN Владимир 	Русский
    ecn_kim_partners ='https://client.ecnbroker.bz/api/server_status' # 	ECN Партнеры Кима Русский
    ecn_suspicious_group = 'http://client.ecn-broker.casa/api/server_status' # ECN Подозрительная группа 	Русский
    #esplanade_ms_domains_ru = 'https://client.esplanade-ms.space/api/server_status' # Домены Esplanade-ms ru
    esplanade_ms_domains_eng = 'https://client.esplanade-ms.com/api/server_status' # Домены Esplanade-ms eng

    try:
        response = requests.get(url, timeout=60)
        if response.status_code == 200:
            print('Сайт доступен')
            #time.sleep(300)

        else:
            print("Сайт не доступен")
            bot_url = f"https://api.telegram.org/bot6032682668:AA1EnILzFn9yIAUU5pivu3Rr4DYPT5t3F1YU/sendMessage?chat_id={id}&text={url}"
            response = requests.get(bot_url,timeout=60)

        response = requests.get(ecn_kim)
        if response.status_code == 200:
            print('Сайт доступен')
            #time.sleep(300)

        else:
            print("Сайт не доступен")
            bot_url = f"https://api.telegram.org/bot6032682668:AA1EnILzFn9yIAUU5pivu3Rr4DYPT5t3F1YU/sendMessage?chat_id={id}&text={ecn_kim}"
            response = requests.get(bot_url)

        response = requests.get(ecn_matvey,timeout=60)
        if response.status_code == 200:
            print('Сайт доступен')
            #time.sleep(300)

        else:
            print("Сайт не доступен")
            bot_url = f"https://api.telegram.org/bot6032682668:AA1EnILzFn9yIAUU5pivu3Rr4DYPT5t3F1YU/sendMessage?chat_id={id}&text={ecn_matvey}"
            response = requests.get(bot_url)
        response = requests.get(ecn_osipov,timeout=60)
        if response.status_code == 200:
            print('Сайт доступен')
            #time.sleep(300)

        else:
            print("Сайт не доступен")
            bot_url = f"https://api.telegram.org/bot6032682668:AA1EnILzFn9yIAUU5pivu3Rr4DYPT5t3F1YU/sendMessage?chat_id={id}&text={ecn_osipov}"
            response = requests.get(bot_url)

        response = requests.get(ecn_vladimir,timeout=60)
        if response.status_code == 200:
            print('Сайт доступен')
            #time.sleep(300)

        else:
            print("Сайт не доступен")
            bot_url = f"https://api.telegram.org/bot6032682668:AA1EnILzFn9yIAUU5pivu3Rr4DYPT5t3F1YU/sendMessage?chat_id={id}&text={ecn_vladimir}"
            response = requests.get(bot_url)

        response = requests.get(ecn_kim_partners,timeout=60)
        if response.status_code == 200:
            print('Сайт доступен')
            #time.sleep(300)

        else:
            print("Сайт не доступен")
            bot_url = f"https://api.telegram.org/bot6032682668:AA1EnILzFn9yIAUU5pivu3Rr4DYPT5t3F1YU/sendMessage?chat_id={id}&text={ecn_kim_partners}"
            response = requests.get(bot_url)

        response = requests.get(ecn_suspicious_group,timeout=60)
        if response.status_code == 200:
            print('Сайт доступен')
            #time.sleep(300)

        else:
            print("Сайт не доступен")
            bot_url = f"https://api.telegram.org/bot6032682668:AA1EnILzFn9yIAUU5pivu3Rr4DYPT5t3F1YU/sendMessage?chat_id={id}&text={ecn_suspicious_group}"
            response = requests.get(bot_url)

        # response = requests.get(esplanade_ms_domains_ru)
        # if response.status_code == 200:
        #     print('Сайт доступен')
        #     #time.sleep(300)
        #
        # else:
        #     print("Сайт не доступен")
        #     bot_url = f"https://api.telegram.org/bot6032682668:AA1EnILzFn9yIAUU5pivu3Rr4DYPT5t3F1YU/sendMessage?chat_id={id}&text={esplanade_ms_domains_ru}"
        #     response = requests.get(bot_url)

        response = requests.get(esplanade_ms_domains_eng,timeout=60)
        if response.status_code == 200:
            print('Сайт доступен')
            time.sleep(60)

        else:
            print("Сайт не доступен")
            bot_url = f"https://api.telegram.org/bot6032682668:AA1EnILzFn9yIAUU5pivu3Rr4DYPT5t3F1YU/sendMessage?chat_id={id}&text={esplanade_ms_domains_eng}"
            response = requests.get(bot_url)

    except requests.exceptions.ConnectionError:
        print('Website is unavailable')


#https://client.ecnbroker.lv/img/vn.svg