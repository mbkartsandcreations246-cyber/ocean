# file: app.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import random

# --------------------------
# 1. TITLE & SIDEBAR
# --------------------------
st.set_page_config(page_title="Marine Data Prototype", layout="wide")
st.title("🌊 Unified Ocean & Biodiversity Data Platform (Prototype)")
st.markdown("AI-driven dashboard for oceanography, fisheries & biodiversity data")

menu = st.sidebar.radio("Navigation", ["Home", "Ocean Data", "Biodiversity", "AI Demo","About"])

# --------------------------
# 2. HOME PAGE
# --------------------------
if menu == "Home":
    st.header("📌 About this Prototype")
    st.write("""
    This is a prototype for integrating **oceanographic, fisheries, taxonomy & molecular biology data**.  
    Built with **Python + Streamlit**, ready to scale into a full platform.
    
    Features included:
    - Ocean Data Visualization
    - Biodiversity Records
    - AI Demo (Mockup for Otolith / eDNA recognition)
    """)

# --------------------------
# 3. OCEAN DATA PAGE
# --------------------------
elif menu == "Ocean Data":
    st.header("🌍 Oceanographic Parameters")
    # Sample dataset
    data = {
        "Location": ["Bay of Bengal", "Arabian Sea", "Indian Ocean", "Andaman Sea"],
        "Temperature (°C)": [28.5, 26.3, 24.8, 27.6],
        "Salinity (PSU)": [35, 36, 34, 33],
        "Oxygen (mg/L)": [5.2, 4.8, 5.5, 5.0]
    }
    df = pd.DataFrame(data)

    st.dataframe(df)

    st.subheader("📊 Visualization")
    fig, ax = plt.subplots()
    sns.barplot(x="Location", y="Temperature (°C)", data=df, ax=ax)
    plt.xticks(rotation=30)
    st.pyplot(fig)

# --------------------------
# 4. BIODIVERSITY PAGE
# --------------------------
elif menu == "Biodiversity":
    st.header("🐟 Biodiversity Records (Sample)")
    biodata = {
        "Species": ["Sardinella longiceps", "Thunnus albacares", "Lutjanus argentimaculatus"],
        "Family": ["Clupeidae", "Scombridae", "Lutjanidae"],
        "Common Name": ["Oil Sardine", "Yellowfin Tuna", "Mangrove Red Snapper"],
        "Region": ["Kerala", "Tamil Nadu", "Andaman"]
    }
    bio_df = pd.DataFrame(biodata)
    st.table(bio_df)

    st.subheader("Biodiversity Heatmap (Mock Data)")
    heatmap_data = pd.DataFrame({
        "Region": ["Kerala", "Tamil Nadu", "Andaman", "Goa", "Gujarat"],
        "Species Count": [120, 90, 75, 60, 45]
    })
    fig, ax = plt.subplots()
    sns.barplot(x="Region", y="Species Count", data=heatmap_data, ax=ax)
    st.pyplot(fig)

# --------------------------
# 5. AI DEMO PAGE (Mockup)
# --------------------------
elif menu == "AI Demo":
    st.header("🤖 AI Demo (Prototype)")
    option = st.radio("Choose AI Tool", ["Otolith Recognition", "eDNA Matching"])

    if option == "Otolith Recognition":
        st.subheader("Upload Otolith Image")
        uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png"])
        if uploaded_file:
            st.image(uploaded_file, caption="Uploaded Otolith", width=300)
            st.success("✅ Predicted Species: " + random.choice(
                ["Sardinella longiceps", "Thunnus albacares", "Lutjanus argentimaculatus"]
            ))

    elif option == "eDNA Matching":
        st.subheader("Enter DNA Sequence")
        seq = st.text_area("Paste a short DNA sequence")
        if st.button("Match Sequence"):
            if seq:
                st.success("✅ Closest Match: " + random.choice(
                    ["Sardinella longiceps", "Thunnus albacares", "Lutjanus argentimaculatus"]
                ))
            else:
                st.warning("Please enter a DNA sequence first!")
elif menu == "About":
    st.header("ℹ️ About this Prototype")
    st.write("""
    - Developed as a **conceptual prototype** for CMLRE.  
    - Built using **Python, Streamlit, Pandas**.  
    - Designed for integration with **cloud databases, APIs, AI models** in the future.  
    """)
