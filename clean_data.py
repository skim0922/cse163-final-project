'''
File to clean and sort data
'''

import pandas as pd


def main():
    # creating master dataframe with everything in it 
    df = pd.read_csv('/Users/sahana/Desktop/github/cse163-final-project/'
                     'data/Racial_and_Social_Equity_Composite_Index.csv')

    data = df[['PCT_ADULTMENTALHEALTHNOTGOOD', 'RACE_ELL_ORIGINS_PERCENTILE',
               'SOCIOECONOMIC_PERCENTILE', 'PCT_ENGLISH_LESSTHAN_VERY_WELL',
               'PCT_LESS_BACHELOR_DEGREE', 'ACRES_TOTAL', 'COMPOSITE_QUINTILE',
              'NAME10']] 


if __name__ == '__main__':
    main()