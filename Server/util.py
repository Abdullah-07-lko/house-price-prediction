import pickle
import json
import numpy as np
import pandas as pd
import os

__locations = None
__data_columns = None
__model = None


def get_estimated_price(location, sqft, bhk, bath):

    # Find location without worrying about uppercase/lowercase
    location = location.lower()

    loc_index = -1

    for i, column in enumerate(__data_columns):
        if column.lower() == "location_" + location:
            loc_index = i
            break

    x = np.zeros(len(__data_columns))

    x[0] = sqft
    x[1] = bath
    x[2] = bhk

    if loc_index >= 0:
        x[loc_index] = 1

    # Use the exact feature names used during model training
    x = pd.DataFrame([x], columns=__model.feature_names_in_)

    return round(__model.predict(x)[0], 2)


def load_saved_artifacts():

    print("loading saved artifacts...start")

    global __data_columns
    global __locations
    global __model

    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Load columns
    with open(
        os.path.join(base_dir, "artifacts", "columns.json"),
        "r"
    ) as f:

        __data_columns = json.load(f)["data_columns"]
        __locations = __data_columns[3:]

    # Load model
    if __model is None:

        with open(
            os.path.join(
                base_dir,
                "artifacts",
                "banglore_home_prices_model.pickle"
            ),
            "rb"
        ) as f:

            __model = pickle.load(f)

    print("loading saved artifacts...done")


def get_location_names():
    return __locations


def get_data_columns():
    return __data_columns


if __name__ == "__main__":

    load_saved_artifacts()

    print(get_location_names())

    print(
        get_estimated_price(
            "1st Phase JP Nagar",
            1000,
            3,
            3
        )
    )

    print(
        get_estimated_price(
            "1st Phase JP Nagar",
            1000,
            2,
            2
        )
    )

    print(
        get_estimated_price(
            "Kalhalli",
            1000,
            2,
            2
        )
    )

    print(
        get_estimated_price(
            "Ejipura",
            1000,
            2,
            2
        )
    )


    