'''
File to clean and sort data
'''

import pandas as pd

def filter_data():
    # creating master dataframe with everything in it 
    # Sahana's path: df = pd.read_csv('/Users/sahana/Desktop/github/cse163-final-project/'
    #                 'data/Racial_and_Social_Equity_Composite_Index.csv')
    # Stella's path: 
    df = pd.read_csv('/Users/stella/Desktop/cse163-final-project/'
                     'data/Racial_and_Social_Equity_Composite_Index.csv')
    df = df.dropna()

    data = df[['PCT_ADULTMENTALHEALTHNOTGOOD', 'RACE_ELL_ORIGINS_PERCENTILE',
               'SOCIOECONOMIC_PERCENTILE', 'PCT_ENGLISH_LESSTHAN_VERY_WELL',
               'PCT_LESS_BACHELOR_DEGREE', 'ACRES_TOTAL', 'COMPOSITE_QUINTILE',
              'NAME10']] 

def main():
    filter_data()


if __name__ == '__main__':
    main()