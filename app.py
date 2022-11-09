# import des differents modules

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import streamlit as st
import pickle

pickle_in = open("modelRid.pkl", "rb")
model = pickle.load(pickle_in)

# Titre de mon fichier

st.title("L'immobilier du conté de King vu par Immotep")
st.subheader("Ich fahre mein auto wunderschön da nacht")

# Creation des differentes listes pour les selectbox

zipcode = [
        "98001", "98002", "98003", "98004", "98005", "98006", "98007", "98008", "98010", "98011", "98014", "98019",
        "98022", "98023", "98024", "98027", "98028", "98029", "98030", "98031", "98032", "98033", "98034", "98038",
        "98039", "98040", "98042", "98045", "98052", "98053", "98055", "98056", "98058", "98059", "98065", "98070",
        "98072", "98074", "98075", "98077", "98092", "98102", "98103", "98105", "98106", "98107", "98108", "98109",
        "98112", "98115", "98116", "98117", "98118", "98119", "98122", "98125", "98126", "98133", "98136", "98144",
        "98146", "98148", "98155", "98166", "98168", "98177", "98178", "98188", "98198", "98199"
]

cp = st.selectbox("Veuillez entrez le code postal",zipcode)
bedrooms = st.number_input("nb des chambres",min_value=0,max_value=11)
bathrooms = st.number_input("baths",min_value=0.00,max_value=8.00)
floors = st.number_input("floors",min_value=1.,max_value=4.,step=0.5)
waterfront = st.radio("waterfront",("yes","no"))
if waterfront == "yes":
    waterfront =1
else:
    waterfront=0

# selectbox et slidebar pour que l'utilisateur effectue ses choix

view = st.number_input("view",min_value=0,max_value=4)
conditions = st.number_input("conditions",min_value=0,max_value=5)
grade = st.number_input("grade",min_value=3,max_value=13)
yr_built = st.number_input('year construction', min_value=1900, max_value=2015)
yr_renovated = st.number_input('year renovation', min_value=0, max_value=2015)
surface_lot = st.number_input("surface_lot",min_value=0.000000, max_value=130000.000000)
surface_base = st.number_input("surface_base",min_value=0.000000, max_value=130000.000000)
surface_above = st.number_input("surface_above",min_value=0.000000, max_value=130000.000000)
surface_liv = st.number_input("habitable surface",min_value=0.000000, max_value=130000.000000)


# Affichage du bouton Validay
if st.sidebar.button("Attention vous êtes sûr, non mais vraiment sûr ?"):
    point_en_cours = {
        "Chambres": bedrooms,
        'Salle_de_bains': bathrooms,
        "etages": floors,
        "vue_mer": waterfront,
        "vu": view,
        "condition":conditions,
        "grade": grade,
        "annee_cons": yr_built,
        "annee_renov": yr_renovated,
        "surface": surface_liv,
        'm2_parcelle': surface_lot,
        'm2_cave': surface_base,
        'rdc': surface_above,
    }

    for code in zipcode: 
        point_en_cours[code]=0

    point_en_cours[cp]=1
    point_en_cours = [point_en_cours[cle] for cle in point_en_cours]
    st.success(model.predict([point_en_cours]))

# Bouton pour afficher la carte

df = pd.read_csv("df.csv")

if st.sidebar.button("Clique dessus pour afficher la carte lo !"):
    st.map(df)


# Promis c'est pas du troll

if st.sidebar.button("Clique dessus tu ne vas pas t'en remettre promis juré craché"):
    st.video("https://youtu.be/Et_sv6uk4Rk")

if st.sidebar.button("Clique ici c'est safe ?"):
    st.image('https://media1.tenor.com/images/72633f9c12ef5004d873d9cc6556ae4d/tenor.gif?itemid=5034006')
    for i in range(10):
        st.balloons()
        st.snow()

if st.sidebar.button("Je serais vous je ne cliquerais pas dessus wallah c'est une surprise"):
    st.error("Pardon je n'ai pas compris votre demande, veuillez tenter votre chance une autre fois, merci de votre comprehension")
    st.button ("Trop bien ouhya")

    for i in range (10):
        st.snow()
        st.balloons()


