"Predict one delivery, from the command line."

import pandas as pd

from delivery import load_model


def main():
    # TODO: load work/model.joblib, predict one 7 km / 25 min /
    #       traffic 2 / dry order, print the prediction
    model = load_model("work/model.joblib")
    order = pd.DataFrame({
        "distance_km": [7.0],
        "prep_time_min": [25],
        "traffic_level": [2],
        "rain": [0]
    })
    prediction = model.predict(order)
    print(f"PREDICTION: {prediction[0]} minutes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
