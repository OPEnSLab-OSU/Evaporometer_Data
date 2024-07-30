import numpy as np
import pandas as pd

#
# Returns the mean of an array
#
def mean(array):
    sum = 0
    for i in array:
        sum = sum + i
    return sum / len(array)

#
# Returns covariance of 2 equal size arrays
#
def covariance(a,b):
    assert len(a) == len(b)
    sum = 0
    mean_a = mean(a)
    mean_b = mean(b)
    for i in range(0, len(a) - 1):
        sum = sum + ((a[i]-mean_a)*(b[i]-mean_b))
    return sum / len(a)

def main():
    csv_file_path = "../field_data/july11_to_july17_2024.csv"
    data_file = pd.read_csv(csv_file_path)

    temp_series = data_file["Temperature"].to_numpy().copy()
    weight_series = data_file["weight"].to_numpy().copy()

    print(covariance(temp_series,weight_series))

if __name__=="__main__":
    main()