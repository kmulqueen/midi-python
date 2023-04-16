
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def convert_data(row):
    converted = np.ndarray([])
    for i in row:
        if type(i) is not float:
            converted = np.append(converted, float(i))
    return converted


def convert_range(value, in_min, in_max, out_min, out_max):
    return out_min + (value - in_min) / (in_max - in_min) * (out_max - out_min)


def read_and_plot(file, dict_of_effects, plot):
    d = pd.read_csv(file)
    effect_list = list(dict_of_effects.keys())
    returned_dict = {}

    for effect in effect_list:
        returned_dict[effect] = d[dict_of_effects[effect]].values

    plt.scatter(returned_dict[plot['x']], returned_dict[plot['y']], s=returned_dict[dict_of_effects[plot['s']]], c=returned_dict[dict_of_effects[plot['c']]])
    plt.xlabel(plot.get('xlabel', 'X'))
    plt.ylabel(plot.get('ylabel', 'Y'))
    plt.show()
    return returned_dict


data_structure = {
    "pitch": "latitude",
    "length": "depth",
    "velocity": "mag",
    "size": "longitude"
}

plot_config = {
    'x': "pitch",
    'y': "length",
    's': "size",
    'c': "velocity",
    'xlabel': 'Latitude',
    'ylabel': 'Depth'
}

data = read_and_plot("../../rand_data/Significant_Earthquakes.csv", data_structure, plot_config)



kms_per_beat = 8.0
scaled_x = []
for duration in data[plot_config['x']]:
    if not pd.isna(duration):
        scaled_x.append(round(duration * kms_per_beat))

x = sorted(scaled_x)
y = convert_range(data[plot_config['y']], min(data[plot_config['y']]), max(data[plot_config['y']]), 0, 1)

vel = convert_range(data['velocity'], min(data['velocity']), max(data['velocity']), 0, 127)
v = [round(v) for v in vel]
plt.scatter(x, y, s=data["size"], c=v)
plt.show()
print("x >>>>>")
print(len(x))

print("y >>>>>")
print(len(y))

print("v >>>>>")
print(len(v))
