import pandas as pd
import plotly.graph_objects as pg
import plotly.express as px

# Reading The CSV
df = pd.read_csv('data.csv')

# !! I HAVE DONE THIS IN TWO WAYS !!

# Practiced This
figure = px.scatter(df, x="student_id", y="level",
                    size="attempt", color="attempt")
figure.show()


# Also Practiced This
# This means that i am telling this program by writing this df.groupby("level")["attempt"] is that group only the level coloumn and find the mean of the attempt column
# If i wouldnt have written the attempt in the square brackets then it will find the mean of the rest columns except the level column (we are specifying that which column to find the mean of)

# !! UNCOMMENT THIS CODE TO SEE THE OUTPUT !!

# meanData = df.groupby("level", as_index=False)["attempt"].mean()

# figure = pg.Figure(pg.Scatter(
#     x=meanData, y=["level 1", "level 2", "level 3", "level 4"], line=dict(width=5, color="#00b894", shape="spline"), marker=dict(size=25, color="#ff7675")))
# figure.show()
