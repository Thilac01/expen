import streamlit as st
import json
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime


st.set_page_config(
    page_title="Expens",
    page_icon="📈", 
    layout="centered",
    initial_sidebar_state="expanded"
)

def load_data(file_path):
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {'date': [], 'cost': [], 'category': []}
    return data

def save_data(data, file_path):
    with open(file_path, 'w') as f:
        json.dump(data, f)

def display_graph(data):
    import pandas as pd
    import matplotlib.pyplot as plt
    import streamlit as st

    df = pd.DataFrame(data)
    df['date'] = pd.to_datetime(df['date'])
    df.set_index('date', inplace=True)


    grouped_data = df.groupby(df.index).sum()

    fig, ax = plt.subplots(figsize=(10, 6))

    grouped_data.plot(ax=ax, kind='area', stacked=False, linewidth=0)

    ax.set_xlabel('Date')
    ax.set_ylabel('Cost')
    ax.set_title('Cost Tracking')
    ax.legend(loc='upper left')
    st.pyplot(fig)
def main():

    with st.sidebar:
        user_name = st.text_input('Enter your name')

        

    if user_name == 'Thilac':
        file_path = 'Thilac_cost_data.json'
        data = load_data(file_path)

        st.title(f"What's Up, {user_name}?")

       
        st.sidebar.header('Add New Cost')
        new_category = st.sidebar.selectbox('Category', ['Housing', 'Food', 'Books and Supplies','Transportation','Technology','Healthcare','Personal Expenses'])
        new_cost = st.sidebar.number_input('Cost', value=0.0)
        new_date = st.sidebar.date_input('Date', value=datetime.now())
        

        
        if st.sidebar.button('Add Cost'):
            data['date'].append(new_date.strftime('%Y-%m-%d'))
            data['cost'].append(new_cost)
            data['category'].append(new_category)
            save_data(data, file_path)
            st.success('Cost added successfully!')

        #st.sidebar.image("8878499.jpg", caption="Optional caption here", use_column_width=True)
        st.header('All Costs')
        if data['date'] and data['cost']:
            col1, col2 = st.columns(2)

            df = pd.DataFrame(data)
            with col1:
                st.write(df)
            with col2:
                st.table(pd.DataFrame(data).describe())
            display_graph(data)

        else:
            st.write('No data available.')

if __name__ == '__main__':
    main()
