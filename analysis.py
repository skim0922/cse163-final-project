'''
File to perform data analysis
'''

from clean_data import filter_data
import seaborn as sns
import matplotlib.pyplot as plt


def plot_problem_one(clean_data):
    # race vs.poor mental health
    sns.relplot(x='RACE_ELL_ORIGINS_PERCENTILE',
                y='PCT_ADULTMENTALHEALTHNOTGOOD',
                kind='scatter', data=clean_data)
    plt.xlabel('Race, ELL, and Origins Index Percentile')
    plt.ylabel('Percentage of Adults Without Good Mental Health')
    plt.title('Race, English Language Learners(ELL), and Origins Index'
              'Percentile vs Percentage of Adults Without Good Mental Health')
    plt.savefig('race_vs_mentalhealth.png', bbox_inches='tight')


def plot_problem_two(clean_data):
    # socioeconomic vs poor mental health
    sns.relplot(x='SOCIOECONOMIC_PERCENTILE',
                y='PCT_ADULTMENTALHEALTHNOTGOOD',
                kind='scatter', data=clean_data)
    plt.xlabel('Socioeconomic Disadvantage Index Percentile')
    plt.ylabel('Percentage of Adults Without Good Mental Health')
    plt.title('Socioeconomic Disadvantage Index'
              'Percentile vs Percentage of Adults Without Good Mental Health')
    plt.savefig('socioecon_vs_mentalhealth.png', bbox_inches='tight')


def plot_question_three(clean_data):
    # total acres vs. index quintile
    # grouped = data.groupby('COMPOSITE_QUINTILE')['ACRES_TOTAL'].mean()
    sns.catplot(x='ACRES_TOTAL',
                y='COMPOSITE_QUINTILE',
                data=clean_data,
                kind='bar')

    plt.xlabel('Acres Total')
    plt.ylabel('Composite Index Quintile')
    plt.title('Total Neighborhood Acres by Composite Index Quintile')
    plt.savefig('size_vs_quintile.png', bbox_inches='tight')


def main():
    clean_data = filter_data()
    plot_problem_one(clean_data)
    plot_problem_two(clean_data)
    plot_question_three(clean_data)


if __name__ == '__main__':
    main()
