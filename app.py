import streamlit as st

st.set_page_config(page_title="Priya Kitchen – Telugu Ruchulu")

st.title("🍛 Priya Kitchen – Telugu Ruchulu")
st.write("మన ఇంటి రుచులు – మీ దగ్గర ఉన్న వాటితో వంట!")

lang = st.selectbox("Language / భాష", ["English", "Telugu"])


def ai_recipe(items, lang):

    veg = items.lower()

    # -------- BIRYANI LOGIC --------
    if "rice" in veg and ("briyani" in veg or "biryani" in veg or "spices" in veg):

        if lang == "English":

            text = "Dish Name: Simple Veg Biryani (Home Style)\n\n"
            text += "Ingredients:\n"
            text += "- 1 cup rice\n"
            text += "- " + veg + "\n"
            text += "- 2 onions sliced\n"
            text += "- 1 tomato\n"
            text += "- 2 tsp biryani masala\n"
            text += "- 1 tsp ginger garlic paste\n"
            text += "- salt as needed\n\n"

            text += "Steps:\n"
            text += "1. Wash rice and soak 15 minutes\n"
            text += "2. Fry onions till golden\n"
            text += "3. Add tomato and ginger garlic\n"
            text += "4. Add vegetables and masala\n"
            text += "5. Add rice with 2 cups water\n"
            text += "6. Cook 15 minutes on low flame\n\n"

            text += "Time: 25 minutes\n\n"
            text += "Amma Tip: Add little ghee for nice aroma 💚"

            return text

        else:

            text = "వంటకం పేరు: సింపుల్ వెజ్ బిర్యానీ\n\n"
            text += "కావలసినవి:\n"
            text += "- 1 కప్పు బియ్యం\n"
            text += "- " + veg + "\n"
            text += "- 2 ఉల్లిపాయలు\n"
            text += "- 1 టమాటా\n"
            text += "- బిర్యానీ మసాలా\n\n"

            text += "తయారీ విధానం:\n"
            text += "1. బియ్యం 15 నిమిషాలు నానబెట్టండి\n"
            text += "2. ఉల్లి వేయించండి\n"
            text += "3. టమాటా వేసండి\n"
            text += "4. కూరగాయలు + మసాలా\n"
            text += "5. బియ్యం + నీరు\n"
            text += "6. 15 నిమిషాలు మగ్గించండి\n\n"

            text += "పట్టే సమయం: 25 నిమిషాలు\n\n"
            text += "అమ్మ చిట్కా: చివరగా నెయ్యి వేస్తే సూపర్ 💚"

            return text


    # -------- NORMAL CURRY --------

    if lang == "English":

        text = "Dish Name: " + veg.title() + " Curry\n\n"
        text += "Ingredients:\n"
        text += "- " + veg + "\n"
        text += "- onion, tomato\n"
        text += "- salt, chilli, turmeric\n\n"

        text += "Steps:\n"
        text += "1. Fry onion tomato\n"
        text += "2. Add masala\n"
        text += "3. Add " + veg + "\n"
        text += "4. Cook 10 minutes\n\n"

        text += "Time: 15 minutes\n"
        text += "Tip: Add little water 💚"

        return text

    else:

        text = "వంటకం పేరు: " + veg + " కర్రీ\n\n"
        text += "కావలసినవి:\n"
        text += "- " + veg + "\n"
        text += "- ఉల్లి, టమాటా\n"
        text += "- ఉప్పు, కారం, పసుపు\n\n"

        text += "విధానం:\n"
        text += "1. ఉల్లి టమాటా వేయించండి\n"
        text += "2. మసాలా వేయండి\n"
        text += "3. " + veg + " కలపండి\n"
        text += "4. 10 నిమిషాలు\n\n"

        text += "చిట్కా: కొద్దిగా నీరు వేయండి 💚"

        return text



# -------- APP MENU --------

menu = st.sidebar.selectbox(
    "Menu",
    ["Cook With Ingredients",
     "Priya Specials",
     "Healthy Tips"]
)


if menu == "Cook With Ingredients":

    items = st.text_area("Ingredients / పదార్థాలు")

    if st.button("Suggest Recipe"):

        if items.strip() == "":
            st.write("Please enter ingredients 😊")
        else:
            st.write(ai_recipe(items, lang))


elif menu == "Priya Specials":

    st.subheader("Priya Specials 💖")

    st.write("""
• Gulab Jamun Ice Cream  
• Veg Biryani  
• Methi Chaman  
• Mango Dal  
• Coconut Pickle  
""")


elif menu == "Healthy Tips":

    st.write("""
• ఎక్కువ నూనె వద్దు  
• రోజూ ఒక ఆకు కూర  
• ఇంటి భోజనం ఆరోగ్యం 💚  
""")
