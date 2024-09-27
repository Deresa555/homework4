# import packages  
import streamlit as st  
import pandas as pd  
import matplotlib.pyplot as plt  
import seaborn as sns  
sns.set()  
  
# show the title  
st.title('Titanic App by Xinran Feng')  
  
# try to read csv and show the dataframe  
try:  
    df_train = pd.read_csv('train.csv')  
    st.dataframe(df_train)  
except FileNotFoundError:  
    st.error("The file 'train.csv' was not found. Please check the file path.")  
    exit()  
  
# function to create and display the boxplots  
def plot_fare_by_pclass(df):  
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))  
      
    for i, pclass in enumerate([1, 2, 3]):  
        subset = df[df['Pclass'] == pclass]  
        subset.boxplot(column='Fare', ax=axes[i])  
        axes[i].set_xlabel(f'PClass = {pclass}')  
        axes[i].set_ylabel('Fare')  
        axes[i].set_title(f'Fare Distribution for PClass {pclass}')  
      
    plt.tight_layout()  
    return fig  
  
# create and display the figure  
fig = plot_fare_by_pclass(df_train)  
st.pyplot(fig)