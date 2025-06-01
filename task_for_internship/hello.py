import pandas as pd
import plotly.express as px
import preswald


df = pd.read_csv('data/Fitness_Tracker_Data.csv')

df["Date"] = pd.to_datetime(df["Date"])


heart_rate_plot = px.histogram(
    df,
    x="Heart_Rate_avg",
    nbins=30,
    color="User_ID",
    title="Distribution of Average Heart Rate"
)



workout_plot = px.histogram(
    df,
    x="Workout_Type",
    color="User_ID",
    title="Workout Type Distribution",
    barmode="group"
)

# --- Display with Preswald ---
preswald.text("# Fitness Tracker Data Analysis")



preswald.text("## Heart Rate Distribution")
preswald.text("Figure 1 displays the distribution of average heart rates, potentially highlighting differences in cardiovascular fitness or activity intensity.")
preswald.plotly(heart_rate_plot)



preswald.text("## Workout Preferences")
preswald.text("Figure 2 compares workout types among users. This helps identify training patterns or exercise diversity.")
preswald.plotly(workout_plot)




fig2 = px.scatter(
    df,
    x="Heart_Rate_avg",
    y="Calories_Burned",
    color="Workout_Type",
    hover_name="User_ID",
    title="Heart Rate vs. Calories Burned"
)


calories_per_workout = df.groupby("Workout_Type")["Calories_Burned"].mean().reset_index()
fig3 = px.bar(
    calories_per_workout,
    x="Workout_Type",
    y="Calories_Burned",
    title="Average Calories Burned per Workout Type"
)


fig4 = px.box(
    df,
    x="Workout_Type",
    y="Steps",
    title="Distribution of Steps by Workout Type"
)

fig5 = px.line(
    df,
    x="Date",
    y="Heart_Rate_avg",
    color="Workout_Type",
    title="Heart Rate Trend Over Time by Workout Type"
)




preswald.text("## Cardiovascular Intensity Assessment")
preswald.text("Figure 2 explores the relationship between heart rate and calories burned. It helps in identifying workout intensities and their effectiveness in burning calories.")
preswald.plotly(fig2)

preswald.text("## Caloric Expenditure by Workout Type")
preswald.text("Figure 3 shows the average calories burned for each workout type. This analysis provides insight into the efficiency of different exercise categories.")
preswald.plotly(fig3)

preswald.text("## Step Count Variability")
preswald.text("Figure 4 displays the distribution of steps taken across workout types using box plots. It reveals the variability and intensity of user effort.")
preswald.plotly(fig4)


