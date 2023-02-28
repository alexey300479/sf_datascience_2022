import pandas as pd
import json
from deep_translator import GoogleTranslator


train_data = pd.read_csv("train_data.csv", usecols=["vehicle_model"])
test_data = pd.read_csv("test.csv", usecols=["vehicle_model"])

test_data.vehicle_model.fillna("no", inplace=True)

models = list(train_data.vehicle_model.unique()) + list(
    test_data.vehicle_model.unique()
)

translator = GoogleTranslator(source="ka", target="en")

models_dict = {}

for i, model in enumerate(models, 1):
    if model in models_dict:
        continue
    if model.isnumeric():
        models_dict[model] = model
    else:
        models_dict[model] = translator.translate(model)
    print(f"{i} of {models_count} model names translated                  ", end="\r")

with open("models_dict.json", "w") as outfile:
    json.dump(models_dict, outfile)
