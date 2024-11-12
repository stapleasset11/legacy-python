import pandas as pd


def calculate_demographic_data(print_data:True):
    
    adult_df = pd.read_csv("data/adult.data.csv")
    
    race_count = adult_df['race'].value_counts()

    average_age_men = round(adult_df[adult_df['sex'] == 'Male']['age'].dropna().mean(),1)

    percentage_bachelors  = round(adult_df[adult_df['education'] == 'Bachelors'].shape[0] / adult_df.shape[0] * 100,1)

    p1 = adult_df['education'].isin(['Bachelors','Masters','Doctorate'])
    p2 = adult_df['salary'] == '>50K'

    higher_education_rich = round((p1 & p2).sum() / p1.sum() * 100,1)
    lower_education_rich = round((~p1 & p2).sum()/(~p1).sum() * 100,1)


    min_work_hours = adult_df['hours-per-week'].min()

    q1 = adult_df['hours-per-week'] == min_work_hours

    rich_percentage = round((q1 & p2).sum() / p2.sum() * 100 ,1)

    p = ((adult_df[p2]['native-country'].value_counts() / adult_df['native-country'].value_counts() )* 100).sort_values(ascending=False)
    highest_earning_country = p.index[0]
    highest_earning_country_percentage = round(p.iloc[0],1)


    top_IN_occupation = adult_df[(adult_df['native-country'] == 'India') & (adult_df['salary'] == '>50K')]['occupation'].value_counts().index[0]

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }

calculate_demographic_data(print_data=True)