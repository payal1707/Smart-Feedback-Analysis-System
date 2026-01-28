import streamlit as st 
import pandas as pd
from textblob import TextBlob
from collections import Counter

st.set_page_config(page_title="Smart Feedback Analysis System",layout="wide")

st.title("Smart Student Feedback Analysis System (NLP)")
st.writer("Ai-powered analysis of student feedback for faculty & NAAC")

uploaded_file=st.file_uploader("Upload Student Feedback CSV",type="csv")
 
if uploaded_file:
  df=pd.read_csv(uploaded_file)
   
  st.subheader("Raw Student Feedback")
  st.dataframe(df)
   
  sentiments=[]
  keywords=[]
   
  for feedback in df['feedback']:
    
    analysis=TextBlob(feedback)
    polarity=analysis.sentiments.polarity
     
if polarity>0:
  sentiments.append("Positive")
elif polarity<0:
  sentiments.append("Negative")
else:
  sentiments.append("Neutral")
       
  keywords.extend(analysis.words.lower())

df['Sentiment']=sentiments

st.subheader("Sentiment Analysis Result")
st.dataframe(df[['feedback','Sentiment']])

sentiments_count=df['Sentiment'].value_counts()
st.bar_char(sentiments_count)

st.subheader("Common Issues / Topic Identified")
common_words=Counter(keywords).most_common(10)
issues_df=pd.DataFrame(common_words,columns=["Keywords","Frequency"])
st.dataframe(issues_df)

st.subheader("Auto Summary")
st.write(
    f"""
    - Total Feedback Analyzed: {len(df)}
    - Positive Responses: {sentiments_count.get('Positive',0)}
    - Negative Responses: {sentiments_count.get('Positive',0)}
    - Neutral Responses: {sentiments_count.get('Positive',0)}
    """
    
)

st.sunheader("Suggested Action Points (Faculty Support)")
if sentiments_count.get('Negative',0) >0:
  st.write("- Slow down teaching pace where required")
  st.write("- Add more practical examples")
  st.write("- Improve note Distribution")
  
else:
  st.write("- Continue current teaching approach")
  st.write("- Maintain student engagement")
  
