#!/usr/bin/env python
import logging
import argparse
from datetime import datetime

import settings
from quiniela import models, io


def parse_seasons(value):
    if value == "all":
        return "all"
    return value


parser = argparse.ArgumentParser()
task_subparser = parser.add_subparsers(help='Task to perform', dest='task')
train_parser = task_subparser.add_parser("train")
train_parser.add_argument(
    "--training_seasons",
    default="all",
    type=parse_seasons,
    help="Seasons to use for training. Write them separated with ',' or use range with ':'. "
         "For instance, '2004:2006' is the same as '2004-2005,2005-2006'. "
         "Use 'all' to train with all seasons available in database.",
)
train_parser.add_argument(
    "--model_name",
    default="my_quiniela.model",
    help="The name to save the model with.",
)
predict_parser = task_subparser.add_parser("predict")
predict_parser.add_argument(
    "season",
    help="Season to predict",
)
predict_parser.add_argument(
    "division",
    type=int,
    choices=[1, 2],
    help="Division to predict (either 1 or 2)",
)
predict_parser.add_argument(
    "matchday",
    type=int,
    help="Matchday to predict",
)
predict_parser.add_argument(
    "--model_name",
    default="my_quiniela.model",
    help="The name of the model you want to use.",
)

if __name__ == "__main__":
    args = parser.parse_args()
    if args.task == "train":
        model = models.QuinielaModel()
        training_data = io.load_historical_data(args.training_seasons)
        model.train(training_data)
        model.save(settings.MODELS_PATH / args.model_name)
        print(
            f"Model succesfully trained and saved in {settings.MODELS_PATH / args.model_name}")
    if args.task == "predict":
        model = models.QuinielaModel.load(
            settings.MODELS_PATH / args.model_name)
        predict_data = io.load_matchday(
            args.season, args.division, args.matchday)
        predict_data["pred"] = model.predict(predict_data)
        print(
            f"Matchday {args.matchday} - LaLiga - Division {args.division} - Season {args.season}")
        print("=" * 70)
        for _, row in predict_data.iterrows():
            print(
                f"{row['home_team']:^30s} vs {row['away_team']:^30s} --> {row['pred']}")
        io.save_predictions(predict_data)
