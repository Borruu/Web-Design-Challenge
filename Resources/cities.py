import pandas as pd
df = pd.read_csv("Resources/cities.csv")
text_file = open("data.html", "w")
text_file.write(df.to_html())
text_file.close()
