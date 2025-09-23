import streamlit as st
import pandas as pd
import plotly.express as px
import geopandas as gpd
from taxonomy_data import taxonomy 
import time
import random
from oto_edna import otolithh_species, edna_species

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
    
    option = st.radio("Choose Data Source:", ["Upload My Data", "Use stored Data"])
    
    if option == "Upload My Data":
        uploaded = st.file_uploader("Upload Oceanographic Biodiversity CSV", type=["csv"])
        if uploaded:
            df = pd.read_csv(uploaded)
    else:
        # Replace with your own GitHub raw CSV link
        sample_url = "https://raw.githubusercontent.com/mbkartsandcreations246-cyber/ocean/refs/heads/main/oceanographic_biodiversity.csv"
        df = pd.read_csv(sample_url)

    if 'df' in locals():
        st.dataframe(df.head())
        df.columns = df.columns.str.strip().str.lower().str.replace("_", " ")
        col1, col2 = st.columns(2)
        # Line plot: temperature vs species count
        if {"temperature", "region"}.issubset(df.columns):
            fig = px.bar(df,x="region",y="temperature",
                         title="Average Temperature by Region")
        with col1:   
            st.plotly_chart(fig, use_container_width=True)
        # Scatter: Salinity vs pH
        if {"salinity", "ph","species count"}.issubset(df.columns):
            fig2 = px.scatter(df, x="salinity", y="ph",
                              color="region",size="species count",title="Salinity vs pH")
        with col2:
            st.plotly_chart(fig2, use_container_width=True) 
           

    #----map-----        
    st.title("🌍 Species Distribution Map")
    st.write("This map shows demo distribution of selected species along Indian coastline.")

     # Dummy data with species & coordinates
    sample_url = "https://raw.githubusercontent.com/mbkartsandcreations246-cyber/ocean/refs/heads/main/biodiversity.csv"
    dff = pd.read_csv(sample_url)
    st.dataframe(dff.head())
    dff.columns = dff.columns.str.strip().str.lower().str.replace("_", " ")
    if {"latitude", "longitude", "species"}.issubset(dff.columns):   
        fig = px.scatter_mapbox(
            dff,
            lat="latitude", 
            lon="longitude", 
            hover_name="species",
            zoom=4,                   
            height=600,
        )
        fig.update_layout(mapbox_style="open-street-map")  # free base map
        fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
        fig.update_traces(marker=dict(size=25, opacity=0.6))
  
        st.plotly_chart(fig, use_container_width=True)
        
# ---------------- Taxonomy Explorer ----------------
elif choice == "Taxonomy Explorer":
    st.title("🧬 Taxonomy Explorer")

    st.write("Browse through taxonomy levels:")
    phylum = st.selectbox("Select Phylum", list(taxonomy.keys()))
    cls = st.selectbox("Select Class", list(taxonomy[phylum].keys()))
    order = st.selectbox("Select Order", list(taxonomy[phylum][cls].keys()))
    family = st.selectbox("Select Family", list(taxonomy[phylum][cls][order].keys()))
    species = st.selectbox("Select Species", list(taxonomy[phylum][cls][order][family].keys()))

    # Display species info
    info = taxonomy[phylum][cls][order][family][species]["info"]
    image_path = taxonomy[phylum][cls][order][family][species]["image"]
    st.success(f"📌 Selected Species: {species}")
    coll, colr = st.columns(2)
    with coll:
      st.image(image_path, caption=species, width=400)
    with colr:
      st.markdown(f"<p style='font-size:26px'><b>{species}:</b></p>", unsafe_allow_html=True)
      st.markdown(f"<p style='font-size:20px'>🔎 Information: {info}</p>", unsafe_allow_html=True)
    
# ---------------- Otolith ----------------
elif choice == "Otolith & Morphology":
    st.title("🐟 Otolith & Morphology Module")
    st.write("Upload otolith image for visualization (Prototype Demo).")
    img = st.file_uploader("Upload Otolith Image", type=["jpg","png"])
    if img:
        st.image(img, caption="Uploaded Otolith Image", use_container_width=True)
        with st.spinner("🔍 Analyzing otolith shape with AI..."):
            time.sleep(2)
        st.success("✅ AI Analysis Complete!")
        
        # Pick 3 random species
        selected = random.sample(otolith_species,1)
        st.markdown("**Predicted Insights (Demo):**")
        for s in selected:
            st.markdown(f"- Likely Species: *{s['name']}*  \n"
                        f"  Shape Index: {s['shape_index']}  \n"
                        f"  Growth Rings: {s['growth_rings']}  \n"
                        f"  Confidence: {s['confidence']}%  \n")
     else:
            st.warning("Please upload the species image.")

# ---------------- eDNA ----------------
elif choice == "eDNA Module":
    st.title("🧬 eDNA Analysis")
    st.write("Paste eDNA sequence")

    # User pastes the sequence
    edna_seq = st.text_area("Paste eDNA sequence here", height=150)

    if edna_seq.strip():  # make sure it's not empty
        st.code(edna_seq, language=None)  # display the sequence nicely

        with st.spinner("🔬 Running AI analysis on eDNA sequence..."):
            time.sleep(2)
        st.success("✅ AI Analysis Complete!")

        # Pick 3 random species
        selected = random.sample(edna_species, 1)
        st.markdown("**Predicted Insights (Demo):**")
        for s in selected:
            rare_text = "Yes" if s["rare"] else "No"
            st.markdown(f"- Species: *{s['name']}*  \n"
                        f"  Biodiversity Index: {s['biodiversity_index']}  \n"
                        f"  Rare Species: {rare_text}  \n"
                        f"  Confidence: {s['confidence']}%  \n")
    else:
            st.warning("Please enter the edna sequence")
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

