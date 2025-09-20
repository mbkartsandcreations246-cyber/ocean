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
    
    option = st.radio("Choose Data Source:", ["Upload My Data", "Use stored Data"])
    
    if option == "Upload My Data":
        uploaded = st.file_uploader("Upload Oceanographic Biodiversity CSV", type=["csv"])
        if uploaded:
            df = pd.read_csv(uploaded)
    else:
        # Replace with your own GitHub raw CSV link
        sample_url = "https://raw.githubusercontent.com/mbkartsandcreations246-cyber/ocean/refs/heads/main/oceanographic_biodiversity.csv"
        df = pd.read_csv(sample_url)
        st.success("✅ Loaded sample data from GitHub!")

    if 'df' in locals():
        st.dataframe(df.head())
        
        # Line plot: temperature vs species count
        if {"Temperature", "Species_Count"}.issubset(df.columns):
            fig = px.line(df, x="Temperature", y="Species_Count",
                          title="Temperature vs Species Count", markers=True)
            st.plotly_chart(fig, use_container_width=True)
         # Scatter: Salinity vs Species Diversity
        if {"Salinity", "Species_Diversity"}.issubset(df.columns):
            fig2 = px.scatter(df, x="Salinity", y="Species_Diversity",
                              color="Region", title="Salinity vs Species Diversity", markers=True)
            st.plotly_chart(fig2, use_container_width=True) 
       

    #----map-----        
    st.title("🌍 Species Distribution Map")
    st.write("This map shows demo distribution of selected species along Indian coastline.")

     # Dummy data with species & coordinates
    demo_map_data = pd.DataFrame({
        "Species": ["Yellowfin Tuna", "Indian Oil Sardine", "Skipjack Tuna"],
        "Latitude": [8.5, 10.0, 15.5],
        "Longitude": [76.5, 78.5, 73.0]
    })
       
    fig = px.scatter_mapbox(
        demo_map_data,
        lat="Latitude",
        lon="Longitude",
        hover_name="Species",
        zoom=4,
        height=600,
        size=[20, 20, 20],
    )
    fig.update_layout(mapbox_style="open-street-map")  # free base map
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

    st.plotly_chart(fig, use_container_width=True)

    st.dataframe(demo_map_data)
# ---------------- Taxonomy Explorer ----------------
elif choice == "Taxonomy Explorer":
    st.title("🧬 Taxonomy Explorer")

    st.write("Browse through taxonomy levels:")

    taxonomy = {
        "Chordata": {
            "Chondrichthyes": {
                "Carcharhiniformes": {
                    "Carcharhinidae": ["Carcharhinus sorrah (Spot-tail shark)"],
                },
                "Carcharhiniformes_2": {
                    "Scoliodonidae": ["Scoliodon laticaudus (Spadenose shark)"],
                },
            },
            "Actinopterygii": {
                "Clupeiformes": {
                    "Clupeidae": ["Sardinella longiceps (Indian oil sardine)", "Stolephorus indicus (Indian anchovy)"],
                },
                "Perciformes": {
                    "Carangidae": ["Rastrelliger kanagurta (Indian mackerel)"],
                    "Lutjanidae": ["Lutjanus johnii (Spotted snapper)"],
                },
                "Pleuronectiformes": {
                  "Cynoglossidae": ["Cynoglossus semifasciatus (Malabar sole)"],
                },
             },
          }
      }

    phylum = st.selectbox("Select Phylum", list(taxonomy.keys()))
    cls = st.selectbox("Select Class", list(taxonomy[phylum].keys()))
    order = st.selectbox("Select Order", list(taxonomy[phylum][cls].keys()))
    family = st.selectbox("Select Family", list(taxonomy[phylum][cls][order].keys()))
    species = st.selectbox("Select Species", taxonomy[phylum][cls][order][family])

    st.success(f"📌 Selected Species: {species}")
    st.write("🔎 Useful Information about the species will appear here (description, image, habitat, importance, etc.)")

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

# ---------------- User Guide ----------------
elif choice == "User Guide":
    st.title("📖 User Manual")
    st.markdown("""
    **Steps to Use Platform**  
    1. Upload your dataset (TSV or GeoParquet).  
    2. Explore biodiversity & ocean trends in Visualization tab.  
    3. Browse taxonomy classification.  
    4. Upload otolith image or DNA sequence for demo analysis.  
    
    **Future Scope**  
    - Real-time data ingestion pipelines  
    - AI models for taxonomy & eDNA  
    - Integration with global marine databases  
    """)

