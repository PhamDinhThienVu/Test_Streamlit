import streamlit as st
import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Manage page link - nav bar to move on another pages

with st.sidebar:

  st.header('Outline', divider='rainbow')

  st.page_link(page = "pages/Problems.py", 
             label="Problems")

  st.page_link(page = "pages/AboutData.py", 
             label="About Data")

  st.page_link(page = "pages/AnalysData.py", 
             label="Data Analysis")
  
  st.page_link(page = "pages/TestYourHealth.py", 
             label="Test Your Health")
  
  
data = pd.read_csv("./data/HepatitisCdata.csv")  
st.title("Phân tích và xem xét bộ dữ liệu")
st.write(data)

column_to_drop = 'Unnamed: 0'
data = data.drop(column_to_drop, axis=1)
data = data.dropna(subset=['ALB', 'ALT', 'PROT','ALP','CHOL'])

df_binary = data.copy()
df_binary['Sex'] = df_binary['Sex'].map({'m': 1, 'f': 0})
df_binary['Category'] = df_binary['Category'].map({'0=Blood Donor': 0,
                                         '0s=suspect Blood Donor': 0,
                                         "1=Hepatitis" : 1,
                                         "2=Fibrosis" : 1, 
                                         "3=Cirrhosis" : 1})


df_multi = data.copy()
df_multi['Sex'] = df_multi['Sex'].map({'m': 1, 'f': 0})

df_multi['Category'] = df_multi['Category'].map({'0=Blood Donor': 0,
                                         '0s=suspect Blood Donor': 0,
                                         "1=Hepatitis" : 1,
                                         "2=Fibrosis" : 2, 
                                         "3=Cirrhosis" : 3})


st.subheader("Người bệnh và không bệnh")
st.text('Số lượng người bình thường: {} '.format(df_binary.Category.value_counts()[0]))
st.text('Số lượng người bị Viêm gan C: {} '.format(df_binary.Category.value_counts()[1]))
fig, ax = plt.subplots(figsize=(8,8))
plt.pie(x=df_binary["Category"].value_counts(), 
        colors=["red","yellow"], 
        labels=["Khỏe mạnh", "Viêm gan C"], 
        )
st.pyplot(fig)



st.subheader("Số lượng nam và nữ trong tập dữ liệu")
st.text ('Nữ : {} '.format(df_binary.Sex.value_counts()[0]))
st.text ('Nam : {} '.format(df_binary.Sex.value_counts()[1]))
fig, ax = plt.subplots(figsize=(8,8))

plt.pie(x=df_binary["Sex"].value_counts(), 
        colors=["blue","pink"], 
        labels=["Nam","Nữ"], 
        )

st.pyplot(fig)

fig, ax = plt.subplots()
sns.countplot(x="Sex", data=data, ax=ax)
st.pyplot(fig)





st.subheader("Số lượng bệnh giữa nam và nữ")

# Group data and get disease counts
grouped_data = df_binary.groupby(['Category', 'Sex'])
disease_gender_counts = grouped_data.size().unstack()

# Create a Matplotlib figure and plot the bar chart
fig, ax = plt.subplots()
disease_gender_counts.plot(kind='bar', stacked=False, ax=ax)

# Customize the plot
plt.xlabel("Loại bệnh")
plt.ylabel("Số người")
plt.title("Số người không bị viêm gan và bị viêm gan")
plt.legend(title="Giới tính")
plt.xticks(rotation=0)  # Rotate x-axis labels for readability
plt.tight_layout()

# Display the plot in Streamlit
st.pyplot(fig)



# Group data and get disease counts
grouped_data = df_multi.groupby(['Category', 'Sex'])
disease_gender_counts = grouped_data.size().unstack()

# Create a Matplotlib figure and plot the bar chart
fig, ax = plt.subplots()
disease_gender_counts.plot(kind='bar', stacked=False, ax=ax)

# Customize the plot
plt.xlabel("Loại bệnh")
plt.ylabel("Số người")
plt.title("Số người không bị viêm gan và bị viêm gan")
plt.legend(title="Giới tính")
plt.xticks(rotation=0)  # Rotate x-axis labels for readability
plt.tight_layout()

# Display the plot in Streamlit
st.pyplot(fig)




def plot_count(df, columns, n_cols, hue):
  """
  Function to generate countplot with Streamlit integration

  Args:
      df: Total data (pandas DataFrame)
      columns: Category variables (list)
      n_cols: Number of columns for subplot (int)
      hue: Hue variable for coloring (optional, string)
  """
  n_rows = (len(columns) - 1) // n_cols + 1
  fig, ax = plt.subplots(n_rows, n_cols, figsize=(17, 4 * n_rows))
  ax = ax.flatten()

  for i, column in enumerate(columns):
    sns.countplot(data=df, x=column, ax=ax[i], hue=hue)

    # Titles
    ax[i].set_title(f'{column} Counts', fontsize=18)
    ax[i].set_xlabel(None, fontsize=16)
    ax[i].set_ylabel(None, fontsize=16)
    ax[i].tick_params(axis='x', rotation=10)

    for p in ax[i].patches:
      value = int(p.get_height())
      ax[i].annotate(f'{value:.0f}', (p.get_x() + p.get_width() / 2, p.get_height()),
                     ha='center', va='bottom', fontsize=9)

    ylim_top = ax[i].get_ylim()[1]
    ax[i].set_ylim(top=ylim_top * 1.1)
  for i in range(len(columns), len(ax)):
    ax[i].axis('off')

  # No suptitle needed in Streamlit
  plt.tight_layout()
  st.pyplot(fig)

# Call the function with desired arguments
plot_count(df_multi, ["Sex"], 2, "Category")



st.subheader("Mắc bệnh theo độ tuổi")
fig, ax = plt.subplots()
sns.countplot(x="Category", hue="Age", data=df_binary, ax = ax)
st.pyplot(fig)

fig, ax = plt.subplots()
sns.countplot(x="Category", hue="Age", data=df_multi, ax = ax)
st.pyplot(fig)



st.subheader("Các biểu đồ đặc trưng của dữ liệu")
fig, axes = plt.subplots(5, 2, figsize=(20, 25))
axes = axes.flatten()
columns = ["Age", "ALB", "ALP", "ALT", "AST", "BIL", "CHE", "CHOL", "CREA", "GGT"]
for i, col in enumerate(columns):
    sns.histplot(x=df_binary[col], hue=df_binary["Category"], kde=True, palette="magma", ax=axes[i])
    axes[i].set_xlabel(col, fontsize=16)  
    axes[i].set_ylabel("Count", fontsize=16)  
    axes[i].set_title(f"Histogram of {col}", fontsize=18)  

    fig.suptitle("Biểu đồ Histogram của các đặc trưng cho trường hợp khỏe mạnh và bị viêm gan", fontsize=24)
st.pyplot(fig)




def plot_pair(df_train, num_var, target, plotname):
  """
  Function to generate pairplot with Streamlit integration

  Args:
      df_train: Total data (pandas DataFrame)
      num_var: List of numeric variables (list)
      target: Target variable (string)
      plotname: Plot title (string)
  """
  g = sns.pairplot(data=df_train, x_vars=num_var, y_vars=num_var, hue=target, corner=True)
  g._legend.set_bbox_to_anchor((0.8, 0.7))
  g._legend.set_title(target)
  g._legend.loc = 'upper center'
  g._legend.get_title().set_fontsize(14)
  for item in g._legend.get_texts():
    item.set_fontsize(14)

  # No suptitle needed in Streamlit
  plt.tight_layout()
  st.pyplot(fig=g.fig)  # Pass the figure object to Streamlit

# Get numeric variables
num_var = [column for column in df_multi.columns if df_multi[column].nunique() > 10]

# Call the function with desired arguments
plot_pair(df_multi, num_var, "Category", plotname="Biểu đồ điểm dữ liệu với biến mục tiêu")

#Colerration check.

plt.style.use('fivethirtyeight')  # Set the style
fig, ax = plt.subplots(figsize=(12, 12))  # Create figure and axis

# Generate heatmap with annotations and formatting
sns.heatmap(df_binary.corr(), annot=True, fmt=".2f", cmap='viridis', ax=ax)

# No title needed in Streamlit
plt.tight_layout()
st.pyplot(fig)