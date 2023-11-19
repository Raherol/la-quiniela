import pandas as pd

import settings


def load_matchday(season, division, matchday):
    data = pd.read_excel(settings.DATA_PATH)

    data = data[(data['season'] == season) & (data['division']
                                              == division) & (data['matchday'] == matchday)]

    if data.empty:
        raise ValueError("There is no matchday data for the values given")
    return data


def load_historical_data(seasons):
    data = pd.read_excel(settings.DATA_PATH)

    if seasons == "all":
        return data
    else:
        first_season = seasons.split(
            ':')[0] + '-' + str(int(seasons.split(':')[0]) + 1)
        last_season = seasons.split(
            ':')[1] + '-' + str(int(seasons.split(':')[1]) + 1)
        data = data[(data['season'] >= first_season) &
                    (data['season'] <= last_season)]
        if data.empty:
            raise ValueError(f"No data for seasons {seasons}")
        return data


def save_predictions(predictions):
    predictions.to_excel(settings.PREDICTION_PATH)
