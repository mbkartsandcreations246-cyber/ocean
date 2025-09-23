# species_data.py

# Otolith species list
otolith_species = [
    {"name": "Carcharhinus sorrah", "shape_index": 0.87, "growth_rings": 12, "confidence": 92},
    {"name": "Scomberomorus commerson", "shape_index": 0.75, "growth_rings": 8, "confidence": 88},
    {"name": "Thunnus albacares", "shape_index": 0.92, "growth_rings": 5, "confidence": 95},
    {"name": "Lutjanus fulviflamma", "shape_index": 0.80, "growth_rings": 6, "confidence": 90},
    {"name": "Epinephelus coioides", "shape_index": 0.78, "growth_rings": 7, "confidence": 85},
]

# eDNA species list with simulated sequences
edna_species = [
    {
        "name": "Salmo salar (Atlantic Salmon)",
        "sequence": "ATCGTAGCTAGCTAGCATGACTAGCTAGCATGACTAGCTAGCATGCTAGCTAGCTAGC",
        "biodiversity_index": 3.45,
        "rare": True,
        "confidence": 88
    },
    {
        "name": "Oncorhynchus mykiss (Rainbow Trout)",
        "sequence": "GCTAGCATCGATCGTACGATCGTAGCTAGCTACGATCGTAGCTAGCTACGATCGT",
        "biodiversity_index": 3.12,
        "rare": False,
        "confidence": 91
    },
    {
        "name": "Thunnus albacares (Yellowfin Tuna)",
        "sequence": "CGTAGCTAGCATGCTAGCTAGCTAGCATGACGATCGTAGCTAGCATGCTAGCTAGC",
        "biodiversity_index": 3.60,
        "rare": False,
        "confidence": 89
    },
    {
        "name": "Chelonodon patoca (Milk-spotted Puffer)",
        "sequence": "TAGCTAGCATGCTAGCTAGCATGACTAGCTAGCATGCTAGCTAGCATGCTAGC",
        "biodiversity_index": 3.30,
        "rare": True,
        "confidence": 87
    },
    {
        "name": "Sphyraena barracuda (Great Barracuda)",
        "sequence": "GATCGTAGCTAGCTACGATCGTAGCTAGCTACGATCGTAGCTAGCTAGCATG",
        "biodiversity_index": 3.50,
        "rare": False,
        "confidence": 92
    }
]
