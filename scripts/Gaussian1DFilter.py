from scipy.ndimage import gaussian_filter1d
from scipy.signal import medfilt
import numpy as np
import pandas as pd

csv_file_path = "../field_data/august.csv"
data_file = pd.read_csv(csv_file_path)

time_series = data_file["Date"].to_numpy().copy()
weight_series = data_file["Weight"].to_numpy().copy()

weight_series = [float(x) + 20 for x in weight_series]

time_int = 15
weight_series_med_filt = medfilt(weight_series, time_int)

sigma_3 = gaussian_filter1d(weight_series_med_filt, 3)
sigma_6 = gaussian_filter1d(weight_series_med_filt, 6)
sigma_15 = gaussian_filter1d(weight_series_med_filt, 15)

data_file['Weight+20'] = weight_series
data_file['Median Filtered Weight (' + str(time_int) + 'min)'] = weight_series_med_filt
data_file['Sigma=3'] = sigma_3
data_file['Sigma=6'] = sigma_6
data_file['Sigma=15'] = sigma_15

data_file = data_file[["Date", "Weight", "Weight+20", "Median Filtered Weight (" + str(time_int) + "min)", "Sigma=3", "Sigma=6", "Sigma=15"]]

data_file.to_csv(csv_file_path, index=False)





