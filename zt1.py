
"""
4/19/2022
Author: Zach Tunstall
Purpose: To generate data visualizations, and provide relavent statistics for global greenhouse gas with agricultural data to use in technical interview for WattTime.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
import colorcet as cc


# Import excel files and cast to dataframes
dfCH4_0 = pd.read_excel("ch4_2015-2021.xlsx")
dfEmis_0 = pd.read_excel("emissions_csv_fao_emiss_csv_ch4_fao_2015_2019_tonnes.xlsx")
dfHarv_0 = pd.read_excel("harvest_2015-2021.xlsx")

# Remove Null Columns
dfEmis2 = dfEmis_0.dropna(axis=1)

# Remove bottom row containing 'Totals'.
dfEmis = dfEmis2.drop(23)
dfHarv1 = dfHarv_0.drop(23)
dfCH41 = dfCH4_0.drop(23)

# Remove ISO country code names.
dfCH4 = dfCH41.iloc[:, 1:]
dfHarv = dfHarv1.iloc[:, 1:]

# Set color palette for plotting.
clr23 = sb.color_palette(cc.glasbey, n_colors=50)

# Transpose dataframes for plotting over time.
dfEmis_t = dfEmis.set_index('country_fao').T  
dfCH4_t = dfCH4.set_index('country_name').T
dfHarv_t = dfHarv.set_index('country_name').T

# Give Name to dataframes.
dfEmis_t.name = dfEmis.name = 'GHG Emissions'
dfCH4_t = dfCH4.name = 'Methane Emissions'
dfHarv_t = dfHarv.name = 'Harvested Area (Ha)'

# Print data types and details of columns. 
def print_info(df):
    return df.info()

# Get descriptive statistics for each column.
def describe_data(df):
    return print(df.describe())

# Display boxplot of column values. Search for outliers.
def box_plot(df):
    return df.boxplot(vert=False, grid=False), plt.title(df.name), plt.show()

# Display histogram of column values. Search for outliers.
def hist_plot(df):
    return df.hist(bins=23), plt.title(df.name), plt.show()

# Create horizontal bar chart of country attributes per year. Use transposed dataframes.
def bar_plot(df_t):
    return (df_t.plot.barh(color=clr23), 
    plt.legend(bbox_to_anchor=(1,1), loc="upper left"), 
    plt.title(df_t.name), 
    plt.show())

# Create Heatmap of percent change between years. Use transposed dataframes.
def year_change(df_t):
    df_t_h = df_t.pct_change(axis='rows').transpose()
    return print(df_t_h), sb.heatmap(df_t_h), plt.show()

# Create line plot over time, use transposed dataframe.
def line_plot(df_t, country_name=None):
    """ country_name must be in string format. """
    if country_name == None:
        return (df_t.plot(color=clr23, x_compat=True), 
        plt.locator_params(axis='x', nbins=8), 
        plt.legend(bbox_to_anchor=(1,1), loc="upper left"), 
        plt.title(df_t.name),
        plt.show())
    else:
        return (df_t.plot(color=clr23, x_compat=True, y='{0}'.format(country_name)), 
        plt.locator_params(axis='x', nbins=8), 
        plt.legend(bbox_to_anchor=(1,1), loc="upper left"), 
        plt.title(df_t.name),
        plt.show())
