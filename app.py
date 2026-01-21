import streamlit as st

st.set_page_config(page_title="Priya Kitchen – Telugu Ruchulu")

st.title("🍛 Priya Kitchen – Telugu Ruchulu")
st.write("మన ఇంటి రుచులు – మీ దగ్గర ఉన్న వాటితో వంట!")

lang = st.selectbox("Language / భాష", ["English", "Telugu"])

dish_type = st.selectbox(
    "What do you want to cook? / ఏ వంట చేయాలనుకుంటున్నారు?",
    ["Veg Biryani", "Curry", "Rice Item", "Quick Fry"]
)


def generate_recipe(items, dish_type, lang):
    items = items.lower()

    # ---------------- BIRYANI ----------------
    if dish_type == "Veg Biryani":

        if lang == "English":
            return (
                "Dish: Simple Veg Biryani\n\n"
                "Why this dish:\n"
                "You have rice and vegetables, perfect for biryani.\n\n"
                "Ingredients:\n"
                "- 1 cup rice\n"
                "- Mixed vegetables\n"
                "- 2 onions\n"
                "- 1 tomato\n"
                "- Biryani masala\n\n"
                "Steps:\n"
                "1. Wash and soak rice for 15 minutes\n"
                "2. Fry onions till golden\n"
                "3. Add tomato and vegetables\n"
                "4. Add masala and rice\n"
                "5. Add 2 cups water and cook on low flame\n\n"
                "Amma Tip:\n"
                "Add little ghee at the end for aroma 💚"
            )
        else:
            return (
                "వంటకం: సింపుల్ వెజ్ బిర్యానీ\n\n"
                "ఈ వంట ఎందుకు:\n"
                "మీ దగ్గర బియ్యం, కూరగాయలు ఉన్నాయి – బిర్యానీకి సరిపోతాయి.\n\n"
                "కావలసినవి:\n"
                "- 1 కప్పు బియ్యం\n"
                "- కూరగాయలు\n"
                "- ఉల్లి, టమాటా\n"
                "- బిర్యానీ మసాలా\n\n"
                "తయారీ విధానం:\n"
                "1. బియ్యం 15 నిమిషాలు నానబెట్టండి\n"
                "2. ఉల్లి వేయించండి\n"
                "3. కూరగాయలు, మసాలా వేయండి\n"
                "4. బియ్యం + నీరు\n"
                "5. మగ్గించండి\n\n"
                "అమ్మ చిట్కా:\n"
                "చివరగా నెయ్యి వేస్తే వాసన బాగుంటుంది 💚"
            )

    # ---------------- CURRY ----------------
    if dish_type == "Curry":

        if lang == "English":
            return (
                "Dish: Simple Veg Curry\n\n"
                "Ingredients:\n"
                "- Vegetables\n"
                "- Onion, tomato\n"
                "- Salt, chilli, turmeric\n\n"
                "Steps:\n"
                "1. Fry onion and tomato\n"
                "2. Add masala\n"
                "3. Add vegetables\n"
                "4. Cook 10–12 minutes\n\n"
                "Tip:\n"
                "Cook on medium flame for good taste 💚"
            )
        else:
            return (
                "వంటకం: సింపుల్ వెజ్ కర్రీ\n\n"
                "కావలసినవి:\n"
                "- కూరగాయలు\n"
                "- ఉల్లి, టమాటా\n"
                "- ఉప్పు, కారం, పసుపు\n\n"
                "విధానం:\n"
                "1. ఉల్లి టమాటా వేయించండి\n"
                "2. మసాలా వేయండి\n"
                "3. కూరగాయలు వేసి ఉడికించండి\n\n"
                "చిట్కా:\n"
                "మధ్య మంటపై వండితే రుచి బాగుంటుంది 💚"
            )

    # ---------------- RICE ITEM ----------------
    if dish_type == "Rice Item":

        if lang == "English":
            return (
                "Dish: Simple Rice Item\n\n"
                "Steps:\n"
                "1. Cook rice separately\n"
                "2. Prepare tempering\n"
                "3. Mix rice with seasoning\n\n"
                "Examples:\n"
                "Lemon rice, tomato rice, curd rice\n\n"
                "Tip:\n"
                "Let rice cool before mixing 💚"
            )
        else:
            return (
                "వంటకం: సింపుల్ రైస్ ఐటమ్\n\n"
                "విధానం:\n"
                "1. అన్నం వండి చల్లార్చండి\n"
                "2. తాలింపు సిద్ధం చేయండి\n"
                "3. అన్నంలో కలపండి\n\n"
                "ఉదాహరణలు:\n"
                "లెమన్ రైస్, టమాటా రైస్, పెరుగు అన్నం\n\n"
                "చిట్కా:\n"
                "అన్నం చల్లార్చాకే కలపండి 💚"
            )

    # ---------------- QUICK FRY ----------------
    if lang == "English":
        return (
            "Dish: Quick Veg Fry\n\n"
            "Steps:\n"
            "1. Heat oil\n"
            "2. Add vegetables\n"
            "3. Add salt and chilli\n"
            "4. Fry on high flame\n\n"
            "Time:\n"
            "10 minutes\n\n"
            "Tip:\n"
            "Do not cover the pan 💚"
        )
    else:
        return (
            "వంటకం: క్విక్ వెజ్ ఫ్రై\n\n"
            "విధానం:\n"
            "1. నూనె వేడి చేయండి\n"
            "2. కూరగాయలు వేయండి\n"
            "3. ఉప్పు, కారం వేయండి\n"
            "4. వేగంగా వేయించండి\n\n"
            "పట్టే సమయం:\n"
            "10 నిమిషాలు\n\n"
            "చిట్కా:\n"
            "మూత పెట్టవద్దు 💚"
        )


menu = st.sidebar.selectbox(
    "Menu",
    ["Cook With Ingredients", "Priya Specials"]
)

if menu == "Cook With Ingredients":
    items = st.text_area("Ingredients / పదార్థాలు")

    if st.button("Suggest Recipe"):
        if items.strip():
            st.write(generate_recipe(items, dish_type, lang))
        else:
            st.warning("Please enter ingredients")

elif menu == "Priya Specials":
    st.write(
        "• Gulab Jamun Ice Cream\n"
        "• Veg Biryani\n"
        "• Methi Chaman\n"
        "• Mango Dal\n"
        "• Coconut Pickle"
    )
