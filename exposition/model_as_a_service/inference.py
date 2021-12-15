import pandas as pd
from flask import Flask, jsonify, request

from config import MODEL_PATH
from formation_indus_ds_avancee.feature_engineering import prepare_features
from formation_indus_ds_avancee.train_and_predict import predict

app = Flask(__name__)


@app.route('/health')
def health():
    return jsonify({
        "status": "ok"
    })


@app.route('/predict')
def predict_endpoint():
    received_wind_speed_avg = request.args.get('Ws1_avg')
    received_data = {
        "Wind_turbine_name": "R80721",
        "Date_time": "2017-02-08T08:00:00+01:00",
        "Ba_avg": 44.990002000000004,
        "Ba_min": 44.990002000000004,
        "Ba_max": 44.990002000000004,
        "Ba_std": 0.0,
        "Rt_avg": 14.0,
        "Rt_min": 14.0,
        "Rt_max": 14.0,
        "Rt_std": 0.0,
        "DCs_avg": 38.369999,
        "DCs_min": 17.68,
        "DCs_max": 52.41,
        "DCs_std": 9.3900003,
        "Cm_avg": 2.3900001,
        "Cm_min": 2.0599998999999998,
        "Cm_max": 2.6900001000000002,
        "Cm_std": 0.09000000400000001,
        "P_avg": -1.89,
        "P_min": -2.3599999,
        "P_max": -1.4,
        "P_std": 0.15000001000000002,
        "Q_avg": 0.0,
        "Q_min": 0.0,
        "Q_max": 0.0,
        "Q_std": 0.0,
        "S_avg": 1.89,
        "S_min": 1.4,
        "S_max": 2.3599999,
        "S_std": 0.15000001000000002,
        "Cosphi_avg": 1.0,
        "Cosphi_min": 1.0,
        "Cosphi_max": 1.0,
        "Cosphi_std": 0.0,
        "Ds_avg": 38.110001000000004,
        "Ds_min": 17.27,
        "Ds_max": 51.919998,
        "Ds_std": 9.3999996,
        "Db1t_avg": 33.41,
        "Db1t_min": 33.200001,
        "Db1t_max": 33.599998,
        "Db1t_std": 0.14,
        "Db2t_avg": 30.790001,
        "Db2t_min": 30.6,
        "Db2t_max": 30.85,
        "Db2t_std": 0.029999999000000006,
        "Dst_avg": 45.59,
        "Dst_min": 45.299999,
        "Dst_max": 45.799999,
        "Dst_std": 0.11,
        "Gb1t_avg": 35.360001000000004,
        "Gb1t_min": 35.099998,
        "Gb1t_max": 35.599998,
        "Gb1t_std": 0.15000001000000002,
        "Gb2t_avg": 37.939999,
        "Gb2t_min": 37.799999,
        "Gb2t_max": 38.0,
        "Gb2t_std": 0.079999998,
        "Git_avg": 34.130001,
        "Git_min": 31.799999,
        "Git_max": 35.700001,
        "Git_std": 1.04,
        "Gost_avg": 39.580002,
        "Gost_min": 39.049999,
        "Gost_max": 40.200001,
        "Gost_std": 0.40000001,
        "Ya_avg": 318.12,
        "Ya_min": 318.12,
        "Ya_max": 318.12,
        "Ya_std": 0.0,
        "Yt_avg": 20.610001,
        "Yt_min": 20.5,
        "Yt_max": 20.799999,
        "Yt_std": 0.079999998,
        "": received_wind_speed_avg,
        "Ws1_min": 0.0,
        "Ws1_max": 1.9400001,
        "Ws1_std": 0.44,
        "Ws2_avg": 0.22,
        "Ws2_min": 0.0,
        "Ws2_max": 1.9299999,
        "Ws2_std": 0.52999997,
        "Ws_avg": 0.18000001000000002,
        "Ws_min": 0.0,
        "Ws_max": 1.89,
        "Ws_std": 0.44,
        "Wa_avg": 358.04999,
        "Wa_min": 298.76999,
        "Wa_max": 54.560001,
        "Wa_std": 12.05,
        "Va1_avg": None,
        "Va1_min": None,
        "Va1_max": None,
        "Va1_std": None,
        "Va2_avg": None,
        "Va2_min": None,
        "Va2_max": None,
        "Va2_std": None,
        "Va_avg": 39.939999,
        "Va_min": -19.35,
        "Va_max": 96.449997,
        "Va_std": 12.05,
        "Ot_avg": 4.8000002,
        "Ot_min": 4.8,
        "Ot_max": 4.9000001,
        "Ot_std": 0.0099999998,
        "Nf_avg": 50.0,
        "Nf_min": 49.959998999999996,
        "Nf_max": 50.029999,
        "Nf_std": 0.0099999998,
        "Nu_avg": 698.40002,
        "Nu_min": 696.01001,
        "Nu_max": 708.03003,
        "Nu_std": 2.4000001,
        "Rs_avg": 0.33000001,
        "Rs_min": 0.0,
        "Rs_max": 0.49000001,
        "Rs_std": 0.16,
        "Rbt_avg": 19.02,
        "Rbt_min": 19.0,
        "Rbt_max": 19.1,
        "Rbt_std": 0.039999999,
        "Rm_avg": -18.889999,
        "Rm_min": -438.32999,
        "Rm_max": 0.0,
        "Rm_std": 79.82,
        "Pas_avg": None,
        "Pas_min": None,
        "Pas_max": None,
        "Pas_std": None,
        "Wa_c_avg": 358.04999,
        "Wa_c_min": None,
        "Wa_c_max": None,
        "Wa_c_std": None,
        "Na_c_avg": 358.04999,
        "Na_c_min": None,
        "Na_c_max": None,
        "Na_c_std": None
    }
    received_data_df = pd.DataFrame(received_data, index=[0])
    prepared_features_df = prepare_features(
        received_data_df, training_mode=False)
    prediction = predict(prepared_features_df, MODEL_PATH)[
        'predictions'].to_dict()
    return jsonify(prediction)
