'''
File to perform data analysis
'''

# import clean_data --> need to figure out how to access the dataframe from
# the other file
# from clean_data import filter_data: i tried this like they do in the hw but it didn't work
import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt


def plot_problem_1(data):
    # race vs.poor mental health  
    sns.relplot(x = 'RACE_ELL_ORIGINS_PERCENTILE',
                y = 'PCT_ADULTMENTALHEALTHNOTGOOD',
                kind = 'scatter', data = data) 
    plt.savefig('race_vs_mentalhealth.png')

    # socioeconomic vs poor mental health 
    sns.relplot(x = 'SOCIOECONOMIC_PERCENTILE',
                y = 'PCT_ADULTMENTALHEALTHNOTGOOD',
                kind = 'scatter', data = data) 
    plt.savefig('socioecon_vs_mentalhealth.png') 
    #plots not saving need to figure that out :) 
    # plots saved now!


def plot_question_three(data):
    # total acres vs. index quintile
    #grouped = data.groupby('COMPOSITE_QUINTILE')['ACRES_TOTAL'].mean()
    sns.catplot(x = 'COMPOSITE_QUINTILE',
                y = 'ACRES_TOTAL',
                data=data,
                kind='bar')
    plt.xlabel('Composite Quintile')
    plt.ylabel('Acres Total')
    plt.title('Total Neighborhood Acres by Composite Index Quintile')
    plt.savefig('size_vs_quintile.png', bbox_inches='tight')


def main():
    # Sahana's path: df = pd.read_csv('/Users/sahana/Desktop/github/cse163-final-project/'
    #                 'data/Racial_and_Social_Equity_Composite_Index.csv') 
    # Stella's path:
    df = pd.read_csv('/Users/stella/Desktop/cse163-final-project/data/Racial_and_Social_Equity_Composite_Index.csv')

    df = df.dropna()
    data = df[['PCT_ADULTMENTALHEALTHNOTGOOD', 'RACE_ELL_ORIGINS_PERCENTILE',
               'SOCIOECONOMIC_PERCENTILE', 'PCT_ENGLISH_LESSTHAN_VERY_WELL',
               'PCT_LESS_BACHELOR_DEGREE', 'ACRES_TOTAL', 'COMPOSITE_QUINTILE',
               'NAME10']]   
    plot_problem_1(data)
    plot_question_three(data)


if __name__ == '__main__':
    main()