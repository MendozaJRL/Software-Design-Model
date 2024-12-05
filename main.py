import streamlit as st

# Streamlit app
def main():
    st.title("Ol'west Crafting: Raw Materials Calculator")
    st.write("This calculator will display the cumulative raw materials needed to craft each item. This is made by Renzo and tested by Cons, and Lazy.")

    # Provide options for users to choose from
    option = st.selectbox("Select which item to craft", ["Spring", "Nail" , "Scrap Metal", 
                                                         "Silver Ingot", "Gold Ingot", "Diamond Ingot", "Void Ingot",
                                                         "Silver Crafting Rune", "Amethyst Crafting Rune", "Gold Crafting Rune",
                                                         "Rusty Plank", "Normal Plank", "Reinforced Plank", "Fossil Plank", "Diamond Plank",
                                                         "Rope", "Sewing Kit",
                                                         "Broken Stock", "Broken Body", "Broken Barrel",
                                                         "Normal Stock", "Normal Body", "Normal Barrel",
                                                         "Good Stock", "Good Body", "Good Barrel",
                                                         "Advanced Stock", "Advanced Body", "Advanced Barrel",
                                                         "Morano", "Silver Morano", "Gold Morano", "Diamond Morano"
                                                        ])
    multiplier = st.number_input("Quantity", min_value=1, max_value=100, value=1, step=1)
    if st.button("Calculate Materials"):
        # Display the calculated materials in a more organized way using Markdown
        st.markdown("### Materials Required:")
        st.write("Weapons that has prerequisites (e.g., Gold Morano requires Silver Morano), will only calculate the total materials from one tier to the other.")
        st.write("For instance, selecting Gold Morano will show the total raw materials needed assuming you already have Silver Morano. It would not include the materials in making Silver Morano. This is to avoid confusion to the people with high-tier weapons.")
        st.write("The rule above doesnt apply on normal crafting items such as chance runes, and gun's body parts")
        categories = {
            'Minerals': ['iron', 'lead', 'coal', 'silver', 'gold', 'ruby', 'diamond'],
            'Logs': ['aspen', 'acacia', 'evergreen', 'spikey', 'fossil', 'crystal'],
            'Pyramid Loots': ['normal_feather', 'spider_web', 'snake_skin'],
            'Rune Fragments': ['common_rune', 'epic_rune', 'void'],
            'Recipes': ['rare_recipe', 'epic_recipe', 'legendary_recipe'],
            'Other': ['horseshoe']
        }

        for category, items in categories.items():
            # Check if any item in the category has a positive quantity
            any_positive = any(materials[item] > 0 for item in items)
            if any_positive:
                st.write(f"#### {category}")
                for item in items:
                    if materials[item] > 0:
                        st.write(f"<div style='margin-left: 20px;'>{item.replace('_', ' ').title()}: {materials[item]}</div>", unsafe_allow_html=True)
    
    st.write("")
    st.write("Are there any inaccuracies, bugs or suggestions here is my discord:  renzomisago")
                    
# Run the app
if __name__ == '__main__':
    main()
