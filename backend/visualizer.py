import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def generate_visualizations(df, max_charts=5):
    plots = []
    sns.set(style="darkgrid")

    # Categorical columns → Bar charts
    cat_cols = df.select_dtypes(include=['object', 'category']).columns.tolist()
    for col in cat_cols[:max_charts]:
        fig, ax = plt.subplots()
        df[col].value_counts().head(10).plot(kind='bar', ax=ax, color='skyblue')
        ax.set_title(f'🔤 Top Categories in "{col}"')
        ax.set_ylabel('Count')
        ax.set_xlabel(col)
        plt.xticks(rotation=45)
        plots.append(fig)

    # Numerical columns → Histograms
    num_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
    for col in num_cols[:max_charts]:
        fig, ax = plt.subplots()
        sns.histplot(df[col].dropna(), kde=True, ax=ax, color='salmon')
        ax.set_title(f'📊 Distribution of "{col}"')
        ax.set_xlabel(col)
        plots.append(fig)

    # Datetime columns → Line plots (optional)
    date_cols = df.select_dtypes(include=['datetime64']).columns.tolist()
    for col in date_cols[:max_charts]:
        fig, ax = plt.subplots()
        df[col].value_counts().sort_index().plot(ax=ax, color='limegreen')
        ax.set_title(f'🕒 Time Series of "{col}"')
        ax.set_ylabel('Frequency')
        ax.set_xlabel('Date')
        plots.append(fig)

    return plots

