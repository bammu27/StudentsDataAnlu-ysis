import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np



df = pd.read_csv('Students data.csv')

st.title("Students Data:")
df = df.drop(columns =['from1','from2','from3','from4','y'])

st.table(df.head(10))

st.title("Basic Stats:")
st.write(df.iloc[:,4:10].describe())

st.title("Get Stats of any column:")
option = st.selectbox(
    'select column',
     df.iloc[:,4:10].columns.tolist())

st.write(df[option].describe())

st.title("Student data Distribution:")
option = st.selectbox(
    'select colum for ploting',
     df.iloc[:,4:10].columns.tolist()
)

fig, axes = plt.subplots(2, 2, figsize=(15, 10))
fig.suptitle('Students Data Analysis')

# Plot the first subplot (Histogram)
sns.histplot(ax=axes[0,0], x=df[option])
axes[0,0].set_title('Histogram')

# Plot the second subplot (Kernel Density Estimation - KDE)
sns.kdeplot(ax=axes[0,1], x=df[option])
axes[0,1].set_title('KDE')

sns.violinplot(data = df,ax = axes[1,0],x = option)
axes[1,0].set_title('violin plot')

sns.boxplot(ax = axes[1,1],x =df[option])
axes[1,1].set_title('BOX plot')

# Display the figure using Streamlit
st.pyplot(fig)


#male and female distributio


st.title("Male/Female Data distribution")


option = st.selectbox(
    'select col',
     df.iloc[:,4:10].columns.tolist()
)

opstat = st.selectbox(
    'select stat measure',
    ['count','mean','max','min','std']
)








fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Group and aggregate data based on the selected statistic
if opstat == 'count':
    df_group = df.groupby('gender')[option].count()
    st.table(df_group)
    sns.barplot(ax=axes[0, 0], x=df_group.index, y=df_group.values, palette="muted")
    axes[0, 0].set_title(f'Count of {option} by Gender')
    axes[0, 0].set_ylabel('Count')
elif opstat == 'mean':
    df_group = df.groupby('gender')[option].mean()
    st.table(df_group)
    sns.barplot(ax=axes[0, 0], x=df_group.index, y=df_group.values, palette="muted")
    axes[0, 0].set_title(f'Mean {option} by Gender')
    axes[0, 0].set_ylabel('Mean Value')
elif opstat == 'max':
    df_group = df.groupby('gender')[option].max()
    st.table(df_group)
    sns.barplot(ax=axes[0, 0], x=df_group.index, y=df_group.values, palette="muted")
    axes[0, 0].set_title(f'Max {option} by Gender')
    axes[0, 0].set_ylabel('Max Value')
elif opstat == 'min':
    df_group = df.groupby('gender')[option].min()
    st.table(df_group)
    sns.barplot(ax=axes[0, 0], x=df_group.index, y=df_group.values, palette="muted")
    axes[0, 0].set_title(f'Min {option} by Gender')
    axes[0, 0].set_ylabel('Min Value')
elif opstat == 'std':
    df_group = df.groupby('gender')[option].std()
    st.table(df_group)
    sns.barplot(ax=axes[0, 0], x=df_group.index, y=df_group.values, palette="muted")
    axes[0, 0].set_title(f'Standard Deviation of {option} by Gender')
    axes[0, 0].set_ylabel('Standard Deviation')

# Customize the layout
plt.tight_layout()

# Create other plots (box, histogram, and KDE)

sns.boxplot(data=df, x='gender', y=option, ax=axes[0, 1])
axes[0, 1].set_title(f'Box Plot of {option} by Gender')
sns.histplot(data=df, x=option, hue='gender', element='step', kde=True, ax=axes[1, 0])
axes[1, 0].set_title(f'Histogram and KDE of {option} by Gender')

sns.kdeplot(data=df, x=option, hue='gender', ax=axes[1, 1], common_norm=False)
axes[1, 1].set_title(f'KDE Plot of {option} by Gender')


st.pyplot(fig)


st.title('Data Distribution class wise')
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

option1 = st.selectbox(
    'select colum by class',
     df.iloc[:,4:10].columns.tolist()
)


opstat1 = st.selectbox(
    'select stat measure by class',
    ['count','mean','max','min','std']
)
# Group and aggregate data based on the selected statistic
if opstat1 == 'count':
    df_group = df.groupby('class')[option1].count()
    st.table(df_group)
    sns.barplot(ax=axes[0, 0], x=df_group.index, y=df_group.values, palette="muted")
    axes[0, 0].set_title(f'Count of {option1} by Class')
    axes[0, 0].set_ylabel('Count')
elif opstat1 == 'mean':
    df_group = df.groupby('class')[option1].mean()
    st.table(df_group)
    sns.barplot(ax=axes[0, 0], x=df_group.index, y=df_group.values, palette="muted")
    axes[0, 0].set_title(f'Mean {option1} by class')
    axes[0, 0].set_ylabel('Mean Value')
elif opstat1 == 'max':
    df_group = df.groupby('class')[option1].max()
    st.table(df_group)
    sns.barplot(ax=axes[0, 0], x=df_group.index, y=df_group.values, palette="muted")
    axes[0, 0].set_title(f'Max {option1} by class')
    axes[0, 0].set_ylabel('Max Value')
elif opstat == 'min':
    df_group = df.groupby('class')[option1].min()
    st.table(df_group)
    sns.barplot(ax=axes[0, 0], x=df_group.index, y=df_group.values, palette="muted")
    axes[0, 0].set_title(f'Min {option1} by class')
    axes[0, 0].set_ylabel('Min Value')
elif opstat1 == 'std':
    df_group = df.groupby('class')[option].std()
    st.table(df_group)
    sns.barplot(ax=axes[0, 0], x=df_group.index, y=df_group.values, palette="muted")
    axes[0, 0].set_title(f'Standard Deviation of {option1} by class')
    axes[0, 0].set_ylabel('Standard Deviation')

# Customize the layout
plt.tight_layout()

# Create other plots (box, histogram, and KDE)

sns.boxplot(data=df, x='class', y=option1, ax=axes[0, 1])
axes[0, 1].set_title(f'Box Plot of {option1} by Gender')
sns.histplot(data=df, x=option1, hue='class', element='step', kde=True, ax=axes[1, 0])
axes[1, 0].set_title(f'Histogram and KDE of {option1} by Gender')

sns.kdeplot(data=df, x=option1, hue='class', ax=axes[1, 1], common_norm=False)
axes[1, 1].set_title(f'KDE Plot of {option1} by Gender')

st.pyplot(fig)


st.title('Correlation  between')


correlation_matrix = df.iloc[:,4:10].corr()

# Create a heatmap using Seaborn
fig ,axes = plt.subplots(1,1 ,figsize=(4,4))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5,ax=axes)
plt.title('Correlation Matrix')

st.pyplot(fig)

















