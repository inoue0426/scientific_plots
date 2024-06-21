import torch
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scienceplots

def plot_data(
    data,
    label,
    title="Data Visualization",
    x_label="Index",
    y_label="Value",
    figsize=(10, 6),
    marker="o",
    styles=['science', 'ieee'],
    linewidth=1,
    fontsize_title=16,
    fontsize_labels=14,
    fontsize_legend=12,
    legend_facecolor='white',
    legend_edgecolor='black',
    grid=True
):

    """
    Function to plot data.
    You can specify parameters such as 'linewidth', etc.
    """
    plt.style.use(styles)
    plt.figure(figsize=figsize)

    # Select appropriate plotting method based on data type and automatically change markers
    markers = ['o', 's', '^', 'D', '*', 'x', 'p', 'h', '+', '>', '<', '|', '_']  # Expanded list of available markers
    if isinstance(data, pd.DataFrame):
        for idx, (column, lbl) in enumerate(zip(data.columns, label)):
            plt.plot(data.index, data[column], marker=markers[idx % len(markers)], label=f"{lbl} - {column}", linewidth=linewidth)
    elif isinstance(data, np.ndarray):
        if data.ndim == 1:
            plt.plot(data, marker=markers[0], label=label, linewidth=linewidth)
        elif data.ndim == 2:
            for i, lbl in enumerate(label):
                plt.plot(data[:, i], marker=markers[i % len(markers)], label=lbl, linewidth=linewidth)
    else:  # Assuming this is a list of lists (Array of Arrays)
        for idx, (sub_data, lbl) in enumerate(zip(data, label)):
            plt.plot(sub_data, marker=markers[idx % len(markers)], label=lbl, linewidth=linewidth)

    plt.title(title, fontsize=fontsize_title)
    plt.xlabel(x_label, fontsize=fontsize_labels)
    plt.ylabel(y_label, fontsize=fontsize_labels)
    legend = plt.legend(fontsize=fontsize_legend)
    legend.get_frame().set_facecolor(legend_facecolor)
    legend.get_frame().set_edgecolor(legend_edgecolor)
    plt.grid(grid)
    plt.show()
