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
    # Example Demo Data
    demo = pd.DataFrame({
        "Year": [2018, 2019, 2020, 2021, 2022],
        "Fish Diversity Index": [120, 135, 160, 140, 170],
        "Sea Temp (°C)": [28.1, 28.3, 28.6, 29.0, 28.7]
    })
    fig = px.line(demo, x="Year", y=["Fish Diversity Index", "Sea Temp (°C)"], markers=True)
    st.plotly_chart(fig, use_container_width=True)
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
        height=600
    )
    fig.update_layout(mapbox_style="open-street-map")  # free base map
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

    st.plotly_chart(fig, use_container_width=True)

    st.dataframe(demo_map_data)

  
# ---------------- Taxonomy Explorer ----------------
elif choice == "Taxonomy Explorer":
    st.title("🧬 Taxonomy Explorer")

    st.write("Browse through taxonomy levels:")

    # Dummy taxonomy data with extra info
    taxonomy = {
        "Chordata": {
            "Actinopterygii (Ray-finned fishes)": {
                "Thunnus albacares (Yellowfin Tuna)": {
                    "image": "https://upload.img.freepik.com/premium-photo/yellowfin-tuna-thunnus-albacares-swimming-blue-water-hunting-ocean-wildlife_174533-100935.jpg",
                    "info": "Yellowfin tuna is found in pelagic waters of tropical and subtropical oceans worldwide."
                },
                "Sardinella longiceps (Indian Oil Sardine)": {
                    "image": "https://upload.wikimedia.org/wikipedia/commons/6/6a/Sardinella_longiceps.png",
                    "info": "A key commercial fish along the Indian coast, commonly used in local diets."
                },
                "Katsuwonus pelamis (Skipjack Tuna)": {
                    "image": "https://upload.wikimedia.org/wikipedia/commons/e/e5/Katsuwonus_pelamis.png",
                    "info": "Widely distributed species important for tuna canning industry."
                }
            },
            "Elasmobranchii (Sharks & Rays)": {
                "Carcharhinus limbatus (Blacktip Shark)": {
                    "image": "https://upload.wikimedia.org/wikipedia/commons/d/d4/Carcharhinus_limbatus.png",
                    "info": "Common shark species inhabiting coastal tropical and subtropical waters."
                },
                "Mobula birostris (Manta Ray)": {
                    "image": "https://upload.wikimedia.org/wikipedia/commons/f/f0/Manta_birostris-Thailand.png",
                    "info": "The largest species of ray, found in tropical waters, filter-feeding on plankton."
                }
            }
        }
    }

    # Dropdowns
    phylum = st.selectbox("Select Phylum", list(taxonomy.keys()))

    if phylum:
        class_choice = st.selectbox("Select Class", list(taxonomy[phylum].keys()))

        if class_choice:
            species = st.selectbox("Select Species", list(taxonomy[phylum][class_choice].keys()))
            if species:
                st.success(f"✅ You selected: {species}")
                st.image(taxonomy[phylum][class_choice][species]["image"], width=400)
                st.info(taxonomy[phylum][class_choice][species]["info"])

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

