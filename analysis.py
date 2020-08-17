'''
File to perform data analysis
'''

# import clean_data --> need to figure out how to access the dataframe from
# the other file
import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt


def plot_problem_1():
    df = pd.read_csv('/Users/sahana/Desktop/github/cse163-final-project/'
                     'data/Racial_and_Social_Equity_Composite_Index.csv') 
    df = df.dropna()
    data = df[['PCT_ADULTMENTALHEALTHNOTGOOD', 'RACE_ELL_ORIGINS_PERCENTILE',
               'SOCIOECONOMIC_PERCENTILE', 'PCT_ENGLISH_LESSTHAN_VERY_WELL',
               'PCT_LESS_BACHELOR_DEGREE', 'ACRES_TOTAL', 'COMPOSITE_QUINTILE',
               'NAME10']]    
    # race vs.poor mental health  
    sns.relplot(x = 'RACE_ELL_ORIGINS_PERCENTILE',
                y = 'PCT_ADULTMENTALHEALTHNOTGOOD',
                kind = 'scatter', data = data) 
    plt.savefig('racevsmentalhealth.png')

    # socioeconomic vs poor mental health 
    sns.relplot(x = 'SOCIOECONOMIC_PERCENTILE',
                y = 'PCT_ADULTMENTALHEALTHNOTGOOD',
                kind = 'scatter', data = data) 
    plt.savefig('racevsmentalhealth.png') 
    #plots not saving need to figure that out :) 



def main():
    plot_problem_1()


if __name__ == '__main__':
    main()