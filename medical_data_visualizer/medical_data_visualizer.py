import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

#load data.
medical_df = pd.read_csv("data/medical_examination.csv")

#Add 'overweight' column.
medical_df['overweight'] = (medical_df['weight'] / (medical_df['height'] / 100) ** 2 > 25).astype(int)

medical_df['cholesterol'] = (medical_df['cholesterol'] > 1).astype(int)
medical_df['gluc'] = (medical_df['gluc'] > 1).astype(int)

def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke',
    # 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(medical_df, id_vars=['cardio'],
                     value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename
    # one of the collumns for the catplot to work correctly.
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index()
    df_cat = df_cat.rename(columns={0: 'total'})

    # Draw the catplot with 'sns.catplot()'
    graph = sns.catplot(data=df_cat, kind="bar", x="variable", y="total", hue="value", col="cardio")
    fig = graph.fig

    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig

def draw_heat_map():
    # Clean the data
    df_heat = medical_df[(medical_df['ap_lo'] <= medical_df['ap_hi']) &
                 (medical_df['height'] >= medical_df['height'].quantile(0.025)) &
                 (medical_df['height'] <= medical_df['height'].quantile(0.975)) &
                 (medical_df['weight'] >= medical_df['weight'].quantile(0.025)) &
                 (medical_df['weight'] <= medical_df['weight'].quantile(0.975))
                 ]

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(16, 9))

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(corr, mask=mask, square=True, linewidths=0.5, annot=True, fmt="0.1f")

    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig