import streamlit as st
import pickle
import pandas as pd

# Load data from the pickle file
def load_data(filename):
    with open(filename, 'rb') as f:
        data = pickle.load(f)
    return data

def main():
    st.title('Movies Recommendation')
    
    # Load data from the pickle file
    data = load_data('data.pickle')
    
    # Create a selectbox with movie names as options
    hobby = st.selectbox("Select a movie:", data['names'].map())
 
    # Print the selected movie
    st.write("Your selected movie is:", hobby)

if __name__ == '__main__':
    main()
