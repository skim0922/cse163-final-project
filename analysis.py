'''
File to perform data analysis
'''

from clean_data import filter_data
import seaborn as sns
import matplotlib.pyplot as plt


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
    clean_data = filter_data()
    plot_problem_1(clean_data)
    plot_question_three(clean_data)


if __name__ == '__main__':
    main()
