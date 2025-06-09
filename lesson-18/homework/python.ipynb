import pandas as pd

# Load data
df = pd.read_csv('task\\stackoverflow_qa.csv', parse_dates=['creationdate'])

# 1. Questions created before 2014
before_2014 = df[df['creationdate'] < '2014-01-01']
print("Questions before 2014:\n", before_2014)

# 2. Questions with score > 50
score_gt_50 = df[df['score'] > 50]
print("\nQuestions with score > 50:\n", score_gt_50)

# 3. Questions with score between 50 and 100
score_50_100 = df[df['score'].between(50, 100)]
print("\nScore between 50 and 100:\n", score_50_100)

# 4. Questions answered by Scott Boston
answered_by_scott = df[df['ans_name'] == 'Scott Boston']
print("\nAnswered by Scott Boston:\n", answered_by_scott)

# 5. Questions answered by 5 specific users
users = ['Scott Boston', 'Unutbu', 'Mike Pennington', 'unutbu', 'DSM']
answered_by_5 = df[df['ans_name'].isin(users)]
print("\nAnswered by 5 specific users:\n", answered_by_5)

# 6. Questions created between March and October 2014, answered by Unutbu, score < 5
unubtu_low_score = df[
    (df['creationdate'] >= '2014-03-01') & 
    (df['creationdate'] <= '2014-10-31') & 
    (df['ans_name'].str.lower() == 'unutbu') &
    (df['score'] < 5)
]
print("\nUnutbu's answers between March and October 2014 with score < 5:\n", unubtu_low_score)

# 7. Score between 5 and 10 OR viewcount > 10000
score_or_views = df[(df['score'].between(5, 10)) | (df['viewcount'] > 10000)]
print("\nScore 5-10 OR views > 10,000:\n", score_or_views)

# 8. Questions NOT answered by Scott Boston
not_scott = df[df['ans_name'] != 'Scott Boston']
print("\nNot answered by Scott Boston:\n", not_scott)
 Homework 3: Titanic Dataset Queries

# Load Titanic data
titanic_df = pd.read_csv("task\\titanic.csv")

# 1. Female passengers in Class 1 aged 20–30
females_class1_20_30 = titanic_df[(titanic_df['Sex'] == 'female') & 
                                  (titanic_df['Pclass'] == 1) & 
                                  (titanic_df['Age'].between(20, 30))]
print("\nFemales in Class 1 aged 20-30:\n", females_class1_20_30)

# 2. Passengers who paid > $100
fare_gt_100 = titanic_df[titanic_df['Fare'] > 100]
print("\nFare > $100:\n", fare_gt_100)

# 3. Survived & alone (SibSp + Parch == 0)
survived_alone = titanic_df[(titanic_df['Survived'] == 1) & 
                            (titanic_df['SibSp'] == 0) & 
                            (titanic_df['Parch'] == 0)]
print("\nSurvived and alone:\n", survived_alone)

# 4. Embarked from 'C' and paid > $50
embarked_c_gt_50 = titanic_df[(titanic_df['Embarked'] == 'C') & 
                              (titanic_df['Fare'] > 50)]
print("\nEmbarked C & fare > $50:\n", embarked_c_gt_50)

 5. Passengers with both siblings/spouses AND parents/children
has_family = titanic_df[(titanic_df['SibSp'] > 0) & (titanic_df['Parch'] > 0)]
print("\nPassengers with SibSp and Parch:\n", has_family)

# 6. Age ≤ 15 and did not survive
kids_didnt_survive = titanic_df[(titanic_df['Age'] <= 15) & 
                                (titanic_df['Survived'] == 0)]
print("\nKids who did not survive:\n", kids_didnt_survive)

# 7. Has Cabin and Fare > $200
cabin_and_fare_gt_200 = titanic_df[titanic_df['Cabin'].notna() & 
                                   (titanic_df['Fare'] > 200)]
print("\nCabin present and fare > $200:\n", cabin_and_fare_gt_200)

# 8. Odd-numbered PassengerId
odd_passenger_ids = titanic_df[titanic_df['PassengerId'] % 2 == 1]
print("\nOdd-numbered Passenger IDs:\n", odd_passenger_ids)

# 9. Passengers with unique ticket numbers
unique_tickets = titanic_df[titanic_df.duplicated('Ticket', keep=False) == False]
print("\nUnique ticket numbers:\n", unique_tickets)

# 10. 'Miss' in name, female, Class 1
miss_class1_female = titanic_df[(titanic_df['Sex'] == 'female') & 
                                (titanic_df['Pclass'] == 1) & 
                                (titanic_df['Name'].str.contains('Miss'))]
print("\nMiss in name, female, Class 1:\n", miss_class1_female)
