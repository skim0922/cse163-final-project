'''
File to perform data analysis
'''

from clean_data import filter_data
import seaborn as sns
import matplotlib.pyplot as plt


<<<<<<< Updated upstream
def plot_problem_1(clean_data):
    # race vs.poor mental health
    sns.relplot(x='RACE_ELL_ORIGINS_PERCENTILE',
                y='PCT_ADULTMENTALHEALTHNOTGOOD',
                kind='scatter', data=clean_data)
    plt.savefig('race_vs_mentalhealth.png')

    # socioeconomic vs poor mental health
    sns.relplot(x='SOCIOECONOMIC_PERCENTILE',
                y='PCT_ADULTMENTALHEALTHNOTGOOD',
                kind='scatter', data=clean_data)
    plt.savefig('socioecon_vs_mentalhealth.png')

=======
def plot_problem_one(data):
    # race vs.poor mental health
    sns.relplot(x = 'RACE_ELL_ORIGINS_PERCENTILE',
                y = 'PCT_ADULTMENTALHEALTHNOTGOOD',
                kind = 'scatter', data=data) 
    plt.xlabel('Race, ELL, and Origins Index Percentile')
    plt.ylabel('Percentage of Adults Without Good Mental Health') 
    plt.tile('Race, English Language Learners(ELL), and Origins Index'
             'Percentile vs Percentage of Adults Without Good Mental Health')
    plt.savefig('race_vs_mentalhealth.png', bbox_inches='tight')


def plot_problem_two(data): 
    # socioeconomic vs poor mental health
    sns.relplot(x = 'SOCIOECONOMIC_PERCENTILE',
                y = 'PCT_ADULTMENTALHEALTHNOTGOOD',
                kind = 'scatter', data = data) 
    plt.xlabel('Socioeconomic Disadvantage Index Percentile')
    plt.ylabel('Percentage of Adults Without Good Mental Health') 
    plt.tile('Socioeconomic Disadvantage Index'
             'Percentile vs Percentage of Adults Without Good Mental Health')
    plt.savefig('socioecon_vs_mentalhealth.png', bbox_inches='tight') 
    
>>>>>>> Stashed changes

def plot_question_three(clean_data):
    # total acres vs. index quintile
    # grouped = data.groupby('COMPOSITE_QUINTILE')['ACRES_TOTAL'].mean()
    sns.catplot(x='COMPOSITE_QUINTILE',
                y='ACRES_TOTAL',
                data=clean_data,
                kind='bar')
    plt.xlabel('Composite Quintile')
    plt.ylabel('Acres Total')
    plt.title('Total Neighborhood Acres by Composite Index Quintile')
    plt.savefig('size_vs_quintile.png')


def main():
<<<<<<< Updated upstream
    clean_data = filter_data()
    plot_problem_1(clean_data)
    plot_question_three(clean_data)
=======
    # Sahana's path:
     df = pd.read_csv('/Users/sahana/Desktop/github/cse163-final-project/'
                   'data/Racial_and_Social_Equity_Composite_Index.csv') 
    # Stella's path:
    # df = pd.read_csv('/Users/stella/Desktop/cse163-final-project/data/
    # Racial_and_Social_Equity_Composite_Index.csv')

    df = df.dropna()
    data = df[['PCT_ADULTMENTALHEALTHNOTGOOD', 'RACE_ELL_ORIGINS_PERCENTILE',
               'SOCIOECONOMIC_PERCENTILE', 'PCT_ENGLISH_LESSTHAN_VERY_WELL',
               'PCT_LESS_BACHELOR_DEGREE', 'ACRES_TOTAL', 'COMPOSITE_QUINTILE',
               'NAME10']]   
    plot_problem_one(data)
    plot_problem_two(data)
    plot_question_three(data)
>>>>>>> Stashed changes


if __name__ == '__main__':
    main()
