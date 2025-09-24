import streamlit as st
import pandas as pd
import plotly.express as px
import geopandas as gpd
from taxonomy_data import taxonomy 
import time
import random
from oto_edna import otolith_species, edna_species

st.set_page_config(page_title="AI-Driven Marine Data Platform", layout="wide")

st.markdown("""
    <style>
    [data-testid="stHeader"] {
        background-color: #001F3F;
    }
    [data-testid="stHeader"] * {
        color: white !important;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar Navigation
menu = [
    "Home", 
    "Visualization", 
    "Taxonomy Explorer", 
    "Otolith & Morphology", 
    "eDNA Module",  
    "User Guide"
]


with st.container():
    choice=st.sidebar.radio("**navigation**",menu)
    st.markdown(
    """
    <style>
    /* Container background */
    div[data-baseweb="radio"] > div {
        background-color: #4CAF50;
        border-radius: 8px;
        padding: 5px;
        display: flex;
        justify-content: space-around; /* spread buttons */
        width: 100%;
    }

    /* Unselected buttons */
    div[data-baseweb="radio"] span[data-baseweb="radio-button"] label {
        background-color: #388E3C;
        color: white;
        font-weight: bold;
        padding: 8px 12px;
        border-radius: 5px;
        margin: 2px;
        cursor: pointer;
    }

    /* Selected button */
    div[data-baseweb="radio"] span[data-baseweb="radio-button"] input:checked + label {
        background-color: #1B5E20;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)
    
# ---------------- Home ----------------
if choice == "Home":
    st.title("🌊 AI-Driven Unified Data Platform for Marine Biodiversity")
    st.markdown("""
    ### About CMLRE  
    The Centre for Marine Living Resources & Ecology (CMLRE) is a research institution under India's Ministry of Earth Sciences. Its core mission is to manage, conserve, and sustainably utilize marine living resources in India's waters.

    ### CMLRE was established in Kochi in 1998 with the mandate to:

    - Develop management strategies for marine living resources by monitoring and modeling marine ecosystems.
    - Coordinate and implement national research and development (R&D) programs related to marine biodiversity and ecology.
    - Store and disseminate data on marine living resources to researchers and end-users.
    - Coordinate national programs concerning living resources in the Southern Ocean (Antarctic marine life).

    ### Why this platform?  
    - Integrates oceanographic, fisheries, taxonomy, and molecular (eDNA) data  
    - Provides visualization tools for researchers and policymakers  
    - Supports sustainable fisheries & blue economy initiatives  
    """)

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
    st.write("This map shows distribution of selected species along Indian coastline.")

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
            color="species",
            zoom=4,                   
            height=600,
        )
        fig.update_layout(
    mapbox_style="open-street-map",
    legend=dict(
        orientation="h",
        yanchor="bottom", y=-0.2,   # push legend below map
        xanchor="center", x=0.5,
        font=dict(size=12)
    )
)
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
    st.write("##")
    coll, colr = st.columns(2)
    with coll:
      st.image(image_path, caption=species, use_container_width=True)
    with colr:
      st.markdown(f"<p style='font-size:26px'><b>{species}:</b></p>", unsafe_allow_html=True)
      st.markdown(f"<p style='font-size:17px'>🔎 Information: {info}</p>", unsafe_allow_html=True)
    
# ---------------- Otolith ----------------
elif choice == "Otolith & Morphology":
    st.title("🐟 Otolith & Morphology Module")
    img = st.file_uploader("Upload Otolith Image", type=["jpg","png"])
    if img:
        st.image(img, caption="Uploaded Otolith Image", use_container_width=True)
        with st.spinner("🔍 Analyzing otolith shape with AI..."):
            time.sleep(2)
        st.success("✅ AI Analysis Complete!")
        
        # Pick 3 random species
        selected = random.sample(otolith_species,1)
        st.markdown("<p style='font-size:26px'><b>Predicted Insights (Demo):</b></p>", unsafe_allow_html=True)
        for s in selected:
            st.markdown(f" <p style='font-size:17px; line-height:1.2;'> Likely Species: {s['name']}</p>   \n"
                        f" <p style='font-size:17px; line-height:1.2;'> Shape Index: {s['shape_index']}</p>  \n"
                        f" <p style='font-size:17px; line-height:1.2;'> Growth Rings: {s['growth_rings']}</p>  \n"
                        f" <p style='font-size:17px; line-height:1.2;'> Confidence: {s['confidence']}%</p>  \n", unsafe_allow_html=True)
    else:
        st.warning("Please upload the species image.")

# ---------------- eDNA ----------------
elif choice == "eDNA Module":
    st.title("🧬 eDNA Analysis")
    # User pastes the sequence
    edna_seq = st.text_area("Paste eDNA sequence here", height=10)

    if edna_seq.strip():  # make sure it's not empty
    
        with st.spinner("🔬 Running AI analysis on eDNA sequence..."):
            time.sleep(2)
        st.success("✅ AI Analysis Complete!")

        # Pick 3 random species
        selected = random.sample(edna_species, 1)
        st.markdown("<p style='font-size:26px'><b> Predicted Insights:</b></p>", unsafe_allow_html=True)
        for s in selected:
            rare_text = "Yes" if s["rare"] else "No"
            st.markdown(f" <p style='font-size:17px; line-height:1.2;'><b> Species: {s['name']}</b></p>  \n"
                        f" <p style='font-size:17px; line-height:1.2;'> EDNA: {s['sequence']}</p>  \n"
                        f" <p style='font-size:17px; line-height:1.2;'> Biodiversity Index: {s['biodiversity_index']}</p>  \n"
                        f" <p style='font-size:17px; line-height:1.2;'> Rare Species: {rare_text}</p>  \n"
                        f" <p style='font-size:17px; line-height:1.2;'> Confidence: {s['confidence']}%</p>  \n", unsafe_allow_html=True)
    else:
        st.warning("Please enter the edna sequence")
# ---------------- User Guide ----------------
elif choice == "User Guide":
    st.title("📖 User Manual")
    st.markdown("""
    **Steps to Use Platform**  
    1. Explore biodiversity & ocean trends in Visualization tab.  
    2. Browse taxonomy classification.  
    3. Upload otolith image or eDNA sequence for analysis.  
    
    **Future Scope**  
    - Real-time data ingestion pipelines  
    - AI models for taxonomy & eDNA  
    - Integration with global marine databases  
    """)

