import streamlit as st
from PIL import Image
import pandas as pd
from vader_sent import get_sentiments

def launch_sentiment_analysis_ui():
    """
      User Interface for Sentiment Analysis
    """

    # Page Setup
    st.set_page_config(
    page_title='Sentiment Analysis',
    page_icon='./static/emoji.png',
    layout="centered",
    initial_sidebar_state="auto")
        
    # Image
    logo_image = Image.open('./static/emoticons.png')


    # Remove Streamlit Footer
    st.markdown('<style> #MainMenu {visibility: hidden;} footer {visibility: hidden;}</style>',
                unsafe_allow_html=True)

    # Load Application Name
    st.markdown('<h3 style="background-color:#03306E; text-align:center; font-family:arial;color:white">SENTIMENT ANALYSIS</h3>', unsafe_allow_html=True)


    st.markdown('<h3 style=text-align:left; font-family:arial;color:black">Add a sentence for sentiment analysis</h3>', unsafe_allow_html=True)

    user_input = st.text_area(label='')
    
    if st.button('Submit'):
        sentiment_polarity, score =  get_sentiments(user_input)
        
        if sentiment_polarity == 'Positive Sentiment':
            st.success(sentiment_polarity)
        elif sentiment_polarity == 'Neutral Sentiment':
            st.warning(sentiment_polarity)
        else:
            st.error(sentiment_polarity)

        st.write(pd.DataFrame({'Sentiment_Metric':list(score.keys()), 'Score' : list(score.values())}))

if __name__ == "__main__":
    
    launch_sentiment_analysis_ui()

