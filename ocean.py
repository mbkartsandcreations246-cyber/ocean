import streamlit as st
import pandas as pd
import plotly.express as px
import geopandas as gpd

st.set_page_config(page_title="AI-Driven Marine Data Platform", layout="wide")

# Sidebar Navigation
menu = [
    "Home", 
    "Upload Data", 
    "Visualization", 
    "Taxonomy Explorer", 
    "Otolith & Morphology", 
    "eDNA Module", 
    "API Docs", 
    "User Guide"
]
choice = st.sidebar.radio("Navigate", menu)

# ---------------- Home ----------------
if choice == "Home":
    st.title("🌊 AI-Driven Unified Data Platform for Marine Biodiversity")
    st.markdown("""
    ### About CMLRE  
    The Centre for Marine Living Resources & Ecology (CMLRE), Kochi, focuses on 
    sustainable management of India’s marine biodiversity.  

    ### Why this platform?  
    - Integrates oceanographic, fisheries, taxonomy, and molecular (eDNA) data  
    - Provides visualization tools for researchers and policymakers  
    - Supports sustainable fisheries & blue economy initiatives  
    """)

# ---------------- Upload Data ----------------
elif choice == "Upload Data":
    st.title("📂 Upload Marine Data")
    uploaded_file = st.file_uploader("Upload TSV or GeoParquet", type=["tsv", "parquet"])
    if uploaded_file:
        if uploaded_file.name.endswith(".tsv"):
            df = pd.read_csv(uploaded_file, sep="\t")
        else:
            df = pd.read_parquet(uploaded_file)
        st.success("✅ Data Uploaded Successfully!")
        st.dataframe(df.head(20))

# ---------------- Visualization ----------------
elif choice == "Visualization":
    st.title("📊 Visualize Oceanographic & Biodiversity Trends")
    st.info("Upload data first in 'Upload Data' tab.")
    # Example Demo Data
    demo = pd.DataFrame({
        "Year": [2018, 2019, 2020, 2021, 2022],
        "Fish Diversity Index": [120, 135, 160, 140, 170],
        "Sea Temp (°C)": [28.1, 28.3, 28.6, 29.0, 28.7]
    })
    fig = px.line(demo, x="Year", y=["Fish Diversity Index", "Sea Temp (°C)"], markers=True)
    st.plotly_chart(fig, use_container_width=True)

# ---------------- Taxonomy Explorer ----------------
elif choice == "Taxonomy Explorer":
    st.title("🧬 Taxonomy Explorer")
    st.write("Explore species hierarchy (Dummy Example):")
    st.markdown("""
    - Kingdom: Animalia  
      - Phylum: Chordata  
        - Class: Actinopterygii (Ray-finned fishes)  
          - Order: Perciformes  
            - Family: Scombridae  
              - Genus: *Thunnus*  
                - Species: *Thunnus albacares* (Yellowfin Tuna)  
    """)

# ---------------- Otolith ----------------
elif choice == "Otolith & Morphology":
    st.title("🐟 Otolith & Morphology Module")
    st.write("Upload otolith image for visualization (Prototype Demo).")
    img = st.file_uploader("Upload Otolith Image", type=["jpg","png"])
    if img:
        st.image(img, caption="Uploaded Otolith Image", use_container_width=True)
        st.success("Future AI model will analyze shape & classify species.")

# ---------------- eDNA ----------------
elif choice == "eDNA Module":
    st.title("🧬 eDNA Analysis")
    dna = st.text_area("Paste DNA sequence:")
    if st.button("Analyze DNA"):
        if dna:
            st.success("Matched Species: *Sardinella longiceps* (Demo)")
        else:
            st.warning("Please paste DNA sequence.")

# ---------------- API Docs ----------------
elif choice == "API Docs":
    st.title("🔗 API Documentation")
    st.markdown("""
    Example Endpoints (Future Ready):
    - `/get_species_data?species=Thunnus` → Returns species info  
    - `/upload_data` → Upload new biodiversity dataset  
    - `/edna_match` → Match DNA sequence to species  
    """)

# ---------------- User Guide ----------------
elif choice == "User Guide":
    st.title("📖 User Manual")
    st.markdown("""
    **Steps to Use Platform**  
    1. Upload your dataset (TSV or GeoParquet).  
    2. Explore biodiversity & ocean trends in Visualization tab.  
    3. Browse taxonomy classification.  
    4. Upload otolith image or DNA sequence for demo analysis.  
    5. Use API endpoints for programmatic access.  

    **Future Scope**  
    - Real-time data ingestion pipelines  
    - AI models for taxonomy & eDNA  
    - Integration with global marine databases  
    """)

