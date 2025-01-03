import requests
from datetime import datetime

def get_weather(city: str) -> str:
    """
    指定された都市の天気情報を取得し、フォーマットされた文字列として返します。
    Args:
        city (str): 天気情報を取得する都市のID。
    Returns:
        str: フォーマットされた天気情報の文字列。取得に失敗した場合はエラーメッセージを返します。
    Raises:
        requests.exceptions.RequestException: リクエストの送信に失敗した場合。
        KeyError: 予期しないデータ形式の場合。
    """
    try:
        url = f"https://weather.tsukumijima.net/api/forecast?city={city}"
        response  = requests.get(url)
        response.raise_for_status()

        data_json = response.json()
    
        date_str = data_json["forecasts"][1]["date"]
        date = datetime.strptime(date_str,"%Y-%m-%d").strftime("%Y年%m月%d日")
        title = data_json["title"]
        weather = data_json["forecasts"][1]["telop"]
        max_temp = data_json["forecasts"][1]["temperature"]["max"]["celsius"]
        min_temp = data_json["forecasts"][1]["temperature"]["min"]["celsius"]
        
        results = f"{date}の{title}は{weather}です。\n最高気温は{max_temp}度、最低気温は{min_temp}度です。\n"
        T00_06 = data_json['forecasts'][1]['chanceOfRain']['T00_06']
        T06_12 = data_json['forecasts'][1]['chanceOfRain']['T06_12']
        T12_18 = data_json['forecasts'][1]['chanceOfRain']['T12_18']
        T18_24 = data_json['forecasts'][1]['chanceOfRain']['T18_24']

        results += f"降水確率は0時から6時まで{T00_06}、6時から12時まで{T06_12}、12時から18時まで{T12_18}、18時から24時まで{T18_24}です。"
        print(data_json["link"])
        return results
    
    except requests.exceptions.RequestException as e:
        return f"天気情報の取得に失敗しました: {e}"
        
    except KeyError as e:
        return f"予期しないデータ形式です: {e}"

if __name__ == '__main__':
    pass
