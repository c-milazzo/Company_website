import streamlit as st
import pandas

st.set_page_config(layout="wide")

st.title("EcoSynergy Innovations")
st.write("""The epitome of modern excellence and sustainable ingenuity. As 
an industry trailblazer, EcoSynergy Innovations seamlessly melds 
cutting-edge technology with an unwavering commitment to environmental 
harmony. Renowned for its visionary leadership, the company has created an 
unparalleled portfolio of groundbreaking solutions that redefine the very 
essence of progress. With a culture of innovation woven into its DNA, 
EcoSynergy consistently shatters the boundaries of what's possible, 
propelling society towards a brighter, greener future. Meticulously 
handpicked teams of brilliant minds converge within their state-of-the-art 
headquarters, each member fueled by an unwavering passion to catalyze 
positive change. From awe-inspiring architectural marvels that generate 
energy from thin air to AI-driven reforestation initiatives that restore 
ecosystems at an unprecedented scale, EcoSynergy's influence radiates 
globally, inspiring all to believe in the boundless potential of 
human-driven ecological transformation.""" )

st.header("Our Team")

col1, empty_col, col2, empty_col2, col3 = st.columns([1.5, 0.5, 1.5, 0.5, 1.5])

df = pandas.read_csv('data.csv')

with col1:
    for index, row in df[:4].iterrows():
        st.subheader(f"{row['first name'].title()} {row['last name'].title()}")
        st.write(row['role'])
        st.image('images/' + row['image'])

with col2:
    for index, row in df[4:8].iterrows():
        st.subheader(f"{row['first name'].title()} {row['last name'].title()}")
        st.write(row['role'])
        st.image('images/' + row['image'])

with col3:
    for index, row in df[8:].iterrows():
        st.subheader(f"{row['first name'].title()} {row['last name'].title()}")
        st.write(row['role'])
        st.image('images/' + row['image'])
