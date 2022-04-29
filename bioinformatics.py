import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from PIL import Image

image = Image.open("dna-logo.jpeg")
st.image(image)

st.write("""
#DNA Nucleotide Count Web App

This app counts the nucleotide composition of query DNA

***
    """)

st.header("Enter DNA Sequence")
sequence_input = ">DNA Query 2\nGAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT"

sequence = st.text_area("Sequence Input", sequence_input, height= 250)
splitted_sequence = sequence.splitlines()
sequence = splitted_sequence[1:]

new_sequence = ''.join(sequence)

st.write("""
***
    """)

st.header("INPUT (DNA Query)")
print(sequence)
st.header("OUTPUT (DNA Nucleotide Counter)")

st.subheader("1. Print Dictionary")

def dna_nucleotide_count(sequence):
    dna_dictionary = dict([
        ("A", sequence.count("A")),
        ("T", sequence.count("T")),
        ("G", sequence.count("G")),
        ("C", sequence.count("C"))
    ])
    return dna_dictionary

x = dna_nucleotide_count(sequence_input)
x_label = list(x)
x_values = list(x.values())

x

st.header("2. Text")
st.write(f"There are " + str(x["A"]) + " Adenines (A)")
st.write(f"There are " + str(x["G"]) + " Guanines (G)")
st.write(f"There are " + str(x["T"]) + " Thymines (T)")
st.write(f"There are " + str(x["C"]) + " Cytosines (C)")

st.subheader("3. Display the Dataframe")
dataframe = pd.DataFrame({
    "Nucleotide": [i for i in x.keys()],
    "Count": [i for i in x.values()]
})
dataframe

st.subheader("4. Display Bar Chart")

plt.bar([i for i in x.keys()], [i for i in x.values()])
plt.title("DNA Count Graph")
plt.xlabel("Nucleobases")
plt.ylabel("Amount")
plt.show()