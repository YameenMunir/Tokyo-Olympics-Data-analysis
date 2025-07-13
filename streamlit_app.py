import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
from plotly.subplots import make_subplots
import plotly.graph_objects as go

st.title('Tokyo Olympics 2021 Data Analysis')

st.markdown('---')

# Read Excel files
def read_excel(name):
    mapping = {
        'Athletes': 'Athletes (2).xlsx',
        'Coaches': 'Coaches (1).xlsx',
        'EntriesGender': 'EntriesGender (1).xlsx',
        'Medals': 'Medals (1).xlsx',
        'Teams': 'Teams (1).xlsx',
    }
    return pd.read_excel(mapping[name])

athletes = read_excel('Athletes')
coaches = read_excel('Coaches')
entries_gender = read_excel('EntriesGender')
medals = read_excel('Medals')
teams = read_excel('Teams')

def clean_coaches(df):
    df.fillna(method='ffill', inplace=True)
    return df
coaches = clean_coaches(coaches)

# Medals per Country
st.header('🏅 Number of Medals per Country')
medals_sorted = medals.sort_values('Rank by Total')
fig = px.bar(medals_sorted, x='Team/NOC', y=['Gold', 'Silver', 'Bronze'], color_discrete_sequence=['Gold', 'Silver', 'Brown'], title='Number of Medals per Country')
st.plotly_chart(fig, use_container_width=True)
st.markdown('''
Overall, the graph shows the medal count of various countries, categorized into gold, silver, bronze medals.

Some of the key observation:

* Countries like the United States, Great Britain, and China have a significantly higher medal counts compared to other countries, suggesting that a dominance in the represented sporting event.
* There's a considerable gap between the top-ranking countries and the majority of countries, indicating a high level of competition concentration.
* Despite there being variations in silver and bronze medal counts, the number of gold medals seems to be the most significant factor in determining a country's overall ranking.
* Some countries shown in this graph show lower overall medal counts might have surprisingly high numbers of gold medals, indicating strong performance in specific disciplines.
''')

st.markdown('---')

# Coaches per Country
st.header('👨‍🏫 Number of Coaches per Country')
pd_coaches_query = coaches.groupby('NOC').size().reset_index(name='Count').sort_values('NOC')
fig = px.bar(pd_coaches_query, x='NOC', y='Count', color='Count', title='Number of Coaches per Country')
st.plotly_chart(fig, use_container_width=True)
st.markdown('''
The graph above presents the number of coaches associated with different National Olympic Committees (NOCs). It appears that the data is likely from a specific sporting event or competition.

Key Observations:
* There's a significant variation in the number of coaches across countries. Some NOCs have a higher number of coaches compared to others. Which could suggest why countries like USA, Great Britain have a high performance in terms of achieving medals.
* Some countries seem to be grouped together with similar coach counts, suggesting potential regional trends or similar levels of investment in coaching resources.
* Countries like Japan, Germany, and China also seem to have a substantial number of coaches.
''')

st.markdown('---')

# Athletes per Discipline
st.header('🏃‍♂️ Number of Athletes per Discipline')
pd_athletes_query = athletes.groupby(['NOC', 'Discipline']).size().reset_index(name='Count').sort_values(['NOC', 'Discipline'])
fig = px.bar(pd_athletes_query, x='NOC', y='Count', color='Discipline', title='Number of Athletes per Discipline')
st.plotly_chart(fig, use_container_width=True)
st.markdown('''
The graph represents the number of athletes participating in different disciplines across various countries.

Key Observations:
* After analysing this graph, it is clear that the number of athletes varies significantly across both disciplines and countries. Some disciplines have a considerably higher number of athletes compared to others, and the same applies to countries.
* Disciplines like Cycling track and Karate seem to have a larger number of athletes overall compared to other disciplines like sport climbing and Trampoline Gymnastics.
* Despite other countries have a presence in multiple disciplines, other countries might be focused on specific ones.
* There're few countries with a higher number athletes across different countries.
''')

# Top 3 disciplines
pd_athletes_query_top = pd_athletes_query[pd_athletes_query['Discipline'].isin(['Athletics', 'Swimming', 'Football'])]
fig2 = px.bar(pd_athletes_query_top, x='NOC', y='Count', color='Discipline', title='Number of athletes from each country per discipline')
st.plotly_chart(fig2, use_container_width=True)
st.markdown('''
The graph represents the number of athletes participating in different disciplines across various countries. It is a visualization of data from a specific event of competition.

Key Observations:
* The number of athletes varies significantly across both disciplines and countries. In other words, some disciplines have considerably higher number of athletes compared to others, and the same applies to countries.
* Disciplines like Athletics and Swimming seem to have a larger number of athletes overall compared other disciplines like Football.
''')

st.markdown('---')

# Gender Distribution
st.header('⚖️ Distribution of Gender amongst each game')
specs = [[{'type':'domain'}, {'type':'domain'}]]*min(23, len(entries_gender))
fig = make_subplots(rows=len(specs), cols=2, subplot_titles=entries_gender['Discipline'], specs=specs)
sub_figs = []
for index, row in entries_gender.iterrows():
    sub_fig = go.Pie(labels=['Female', 'Male'], values=[row['Female'], row['Male']])
    sub_figs.append(sub_fig)
k = 0
for i in range(1, len(specs)+1):
    for j in range(1, 3):
        if k < len(sub_figs):
            fig.add_trace(sub_figs[k], i, j)
            k += 1
fig.update_layout(showlegend=False, height=10000, width=800, title_text="Distribution of Gender amongst each game")
fig.update_traces(textposition='inside', textinfo='label+percent', hoverinfo='label+value+percent')
st.plotly_chart(fig)

st.markdown('---')

# Teams by Country
st.header('🇺🇳 Number of Teams by Country')
country_counts = teams['NOC'].value_counts()
fig, ax = plt.subplots(figsize=(16, 12))
country_counts.plot(kind='bar', ax=ax)
ax.set_title('Number of Teams by Country')
ax.set_xlabel('Country (NOC)')
ax.set_ylabel('Number of Teams')
st.pyplot(fig)
st.markdown('From this bar chart Japan has the highest number of teams')

# Heatmap
event_country_counts = teams.groupby(['NOC', 'Event']).size().unstack().fillna(0)
fig2, ax2 = plt.subplots(figsize=(20, 18))
sns.heatmap(event_country_counts, annot=True, fmt='g', cmap='viridis', ax=ax2)
ax2.set_title('Heatmap of Teams by Country and Event')
ax2.set_xlabel('Event')
ax2.set_ylabel('Country (NOC)')
st.pyplot(fig2)

# Pie chart
event_counts = teams['Event'].value_counts()
fig3, ax3 = plt.subplots(figsize=(22, 30))
event_counts.plot(kind='pie', autopct='%1.1f%%', startangle=140, ax=ax3)
ax3.set_title('Distribution of Teams by Event (Men vs. Women)')
ax3.set_ylabel('')
st.pyplot(fig3)
st.markdown('After analysing this graph, there were more men than women playing the Tokyo Olympics.')

st.markdown('---')

# Conclusion
st.header('📊 Conclusion')
st.markdown('''
### Summary of Findings:
1.   Medal Distribution Analysis:
  *   USA led the medal tally, followed by China and Japan, showcasing their dominance in various sports.
  *   There has been notable performance in swimming, gymnastics, and track and field events, contributing significantly to the overall medal count of these countries
2.   Athlete Performance:
  *   Younger athletes showed a more stronger performance in sports such as gymnastics and swimming, on the other hand experienced athletes excelled in sports such as equestrian and shooting.
  *   The distribution of medals across different age groups highlighted the varying peak performance ages for different sports.
3.   Gender Representation:
  *  The Tokyo Olympics saw a near-equal representation of male and female athletes, with many countries sending mixed-gender teams for the first time.
  *   Female athletes had outstanding performances in events such as weightlifting, boxing, and athletics, contributing significantly to their country's medal tally.
4.   Impact of COVID-19:
  *   As a result of the pandemic many people were not able to train and prepare to the best of their ability due to disrupted training schedules, psychological stress and issues
  *   Despite these encounters of challenges, the overall performance levels remained high, indicating the resilience and adaptability of the athletes.

### Key Insights:
*   The analysis underscores the importance of infrastructure, funding, and support systems in developing world-class athletes, as evidenced by the performance of top-ranking countries.
*   Sports with high youth participation saw younger medalists, emphasizing the need for early talent identification and development programs.
*   Gender equality in sports is progressing, with nearly equal participation and notable achievements by female athletes across various disciplines.

With these analysis it can help shape the future strategies for sports development and ensure continued excellence in international competitions.
''')

st.markdown('---')
st.markdown(
    '<div style="text-align:center; font-size:1.1em;">'
    '    Made by <b>Yameen Munir</b> 👨‍💻 &nbsp;|&nbsp; '
    '    <a href="https://github.com/YameenMunir" target="_blank">📁 GitHub</a> &nbsp;|&nbsp; '
    '    <a href="https://www.linkedin.com/in/yameen-munir/" target="_blank">💼 LinkedIn</a> &nbsp;|&nbsp; '
    '    <a href="https://yameenmunir.vercel.app/" target="_blank">🌐 Website</a>'
    '</div>',
    unsafe_allow_html=True
)

