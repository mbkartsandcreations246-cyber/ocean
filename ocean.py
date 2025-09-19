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
        height=600,
        size=[20, 20, 20],
    )
    fig.update_layout(mapbox_style="open-street-map")  # free base map
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

    st.plotly_chart(fig, use_container_width=True)

    st.dataframe(demo_map_data)

# Taxonomy data with descriptions and images
taxonomy_data = {
    "Chordata": {
        "Chondrichthyes": {
            "Carcharhiniformes": {
                "Carcharhinidae": {
                    "Carcharhinus sorrah (Spot-tail shark)": {
                        "image": "https://upload.wikimedia.org/wikipedia/commons/2/29/Carcharhinus_sorrah_shark.jpg",
                        "desc": "Spot-tail shark is a small coastal shark found in the Indo-Pacific. Important in artisanal fisheries."
                    }
                },
                "Scoliodonidae": {
                    "Scoliodon laticaudus (Spadenose shark)": {
                        "image": "https://upload.wikimedia.org/wikipedia/commons/3/37/Scoliodon_laticudus.jpg",
                        "desc": "Spadenose shark is a small shark inhabiting shallow waters. Valued for local fisheries."
                    }
                }
            },
            "Myliobatiformes": {
                "Dasyatidae": {
                    "Himantura gerrardi (Whitespotted whipray)": {
                        "image": "https://upload.wikimedia.org/wikipedia/commons/5/56/Himantura_gerrardi.jpg",
                        "desc": "A large stingray found in Indo-Pacific coastal waters, often caught as bycatch."
                    }
                }
            },
            "Rhinobatiformes": {
                "Rhinobatidae": {
                    "Rhinobatos granulatus (Granulated shovel nose ray)": {
                        "image": "https://upload.wikimedia.org/wikipedia/commons/7/72/Rhinobatos_granulatus.jpg",
                        "desc": "A benthic ray species living on sandy bottoms, vulnerable to overfishing."
                    }
                }
            }
        },
        "Actinopterygii": {
            "Clupeiformes": {
                "Clupeidae": {
                    "Sardinella longiceps (Indian oil sardine)": {
                        "image": "https://upload.wikimedia.org/wikipedia/commons/4/47/Sardinella_longiceps.jpg",
                        "desc": "One of the most important commercial fishes of India, rich in omega-3 fatty acids."
                    },
                    "Stolephorus indicus (Indian anchovy)": {
                        "image": "https://upload.wikimedia.org/wikipedia/commons/c/c4/Stolephorus_indicus.jpg",
                        "desc": "A small schooling fish used for dried fish and fishmeal industries."
                    }
                }
            },
            "Siluriformes": {
                "Ariidae": {
                    "Osteogeneiosus militaris (Soldier catfish)": {
                        "image": "https://upload.wikimedia.org/wikipedia/commons/f/f3/Osteogeneiosus_militaris.jpg",
                        "desc": "A catfish inhabiting estuaries and coastal waters, important for artisanal fisheries."
                    }
                }
            },
            "Perciformes": {
                "Scombridae": {
                    "Rastrelliger kanagurta (Indian mackerel)": {
                        "image": "https://upload.wikimedia.org/wikipedia/commons/2/2d/Rastrelliger_kanagurta.jpg",
                        "desc": "A pelagic fish widely consumed in India. Rich in protein and omega-3 fatty acids."
                    }
                },
                "Lutjanidae": {
                    "Lutjanus johnii (Spotted snapper)": {
                        "image": "https://upload.wikimedia.org/wikipedia/commons/6/65/Lutjanus_johnii.jpg",
                        "desc": "Demersal fish found in reefs and estuaries. High commercial value as food fish."
                    }
                }
            },
            "Pleuronectiformes": {
                "Cynoglossidae": {
                    "Cynoglossus semifasciatus (Malabar sole)": {
                        "image": "https://upload.wikimedia.org/wikipedia/commons/a/aa/Cynoglossus_semifasciatus.jpg",
                        "desc": "A flatfish inhabiting sandy and muddy bottoms, valued in local markets."
                    }
                }
            },
            "Tetraodontiformes": {
                "Tetraodontidae": {
                    "Chelonodon patoca (Milk-spotted puffer)": {
                        "image": "https://upload.wikimedia.org/wikipedia/commons/4/4e/Chelonodon_patoca.jpg",
                        "desc": "A brackish water pufferfish known for its toxin. Sometimes used in ornamental fish trade."
                    }
                }
            }
        }
    }
}

st.title("Taxonomy Explorer")

# --- Hierarchical Dropdowns ---
phylum = st.selectbox("Select Phylum", list(taxonomy_data.keys()))
_class = st.selectbox("Select Class", list(taxonomy_data[phylum].keys()))
order = st.selectbox("Select Order", list(taxonomy_data[phylum][_class].keys()))
family = st.selectbox("Select Family", list(taxonomy_data[phylum][_class][order].keys()))
species = st.selectbox("Select Species", list(taxonomy_data[phylum][_class][order][family].keys()))

selected = taxonomy_data[phylum][_class][order][family][species]

# --- Display Information ---
st.success(f"You selected: {species}")
st.image(selected["image"], caption=species, use_container_width=True)
st.write(selected["desc"])

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

