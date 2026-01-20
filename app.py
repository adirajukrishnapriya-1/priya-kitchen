import streamlit as st

st.set_page_config(page_title="Priya Kitchen – Telugu Ruchulu")

st.title("🍛 Priya Kitchen – Telugu Ruchulu")
st.write("మన ఇంటి రుచులు – మీ దగ్గర ఉన్న వాటితో వంట!")

lang = st.selectbox("Language / భాష", ["English", "Telugu"])

menu = st.sidebar.selectbox("Menu",
    ["Cook With Ingredients",
     "Priya Specials",
     "Meal Idea",
     "Healthy Tips"])

if menu == "Cook With Ingredients":

    items = st.text_area("Ingredients / పదార్థాలు")

    if st.button("Suggest Recipe"):

        if lang == "English":
            st.write(f"""
You have: {items}

👉 Simple Home Style Curry

1. Heat oil  
2. Add onion & tomato  
3. Add salt, chilli, turmeric  
4. Add vegetables  
5. Cook 10 minutes  
6. Add coriander with love 💚
""")
        else:
            st.write(f"""
మీ దగ్గర ఉన్నవి: {items}

👉 సింపుల్ కర్రీ

1. నూనె వేడి  
2. ఉల్లి టమాటా  
3. ఉప్పు కారం పసుపు  
4. కూరగాయలు  
5. 10 నిమిషాలు  
6. కొత్తిమీర – ప్రేమతో 💚
""")

elif menu == "Priya Specials":
    st.subheader("Priya Specials 💖")
    st.write("""
• Gulab Jamun Ice Cream  
• Veg Biryani  
• Methi Chaman  
• Mango Dal  
• Coconut Pickle
""")

elif menu == "Meal Idea":
    st.write("Lemon rice + aloo fry + curd")

elif menu == "Healthy Tips":
    st.write("రోజూ ఇంటి భోజనం – ఆరోగ్యం 💚")
