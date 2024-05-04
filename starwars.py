import streamlit as st
import os

def watch_Order(name):
    st.title(name + " Order") #1st New Method
    if name == "Numerical":
        st.header("I, II, III, IV, V, VI, VII, VII, IX")
    elif name == "Release":
        st.header("IV, V, VI, I, II, III, VII, VIII, IX")
    elif name == "Rinster":
        st.header("IV, V, I, II, III, VI, VII, VIII, IX")
    elif name == "Machete":
        st.header("IV, V, II, III, VI, VII, VIII, IX")
    elif name == "Bonus":
        st.header("Solo, Rouge One, IV, V, I, II, III, VI, VII, VIII, IX")

    image_filename = os.path.join(name.lower() + ".jpg")
    st.image(image_filename, use_column_width=True)
    st.header("Moives:")

    if name == "Numerical":
        st.write("Star Wars: The Phantom Menace (Episode I)")
        st.write("Star Wars: Attack of the Clones (Episode II)")
        st.write("Star Wars: Revenge of the Sith (Episode III)")
        st.write("Star Wars: A New Hope (Episode IV)")
        st.write("Star Wars: The Empire Strikes Back (Episode V)")
        st.write("Star Wars: Return of the Jedi (Episode VI)")
        st.write("Star Wars: The Force Awakens (Episode VII)")
        st.write("Star Wars: The Last Jedi (Episode VIII)")
        st.write("Star Wars: The Rise of Skywalker (Episode IX)")
    elif name == "Release":
        st.write("Star Wars: A New Hope (Episode IV)")
        st.write("Star Wars: The Empire Strikes Back (Episode V)")
        st.write("Star Wars: Return of the Jedi (Episode VI)")
        st.write("Star Wars: The Phantom Menace (Episode I)")
        st.write("Star Wars: Attack of the Clones (Episode II)")
        st.write("Star Wars: Revenge of the Sith (Episode III)")
        st.write("Star Wars: The Force Awakens (Episode VII)")
        st.write("Star Wars: The Last Jedi (Episode VIII)")
        st.write("Star Wars: The Rise of Skywalker (Episode IX)")
    elif name == "Rinster":
        st.write("Star Wars: A New Hope (Episode IV)")
        st.write("Star Wars: The Empire Strikes Back (Episode V)")
        st.write("Star Wars: The Phantom Menace (Episode I)")
        st.write("Star Wars: Attack of the Clones (Episode II)")
        st.write("Star Wars: Revenge of the Sith (Episode III)")
        st.write("Star Wars: Return of the Jedi (Episode VI)")
        st.write("Star Wars: The Force Awakens (Episode VII)")
        st.write("Star Wars: The Last Jedi (Episode VIII)")
        st.write("Star Wars: The Rise of Skywalker (Episode IX)")
    elif name == "Machete":
        st.write("Star Wars: A New Hope (Episode IV)")
        st.write("Star Wars: The Empire Strikes Back (Episode V)")
        st.write("Star Wars: Attack of the Clones (Episode II)")
        st.write("Star Wars: Revenge of the Sith (Episode III)")
        st.write("Star Wars: Return of the Jedi (Episode VI)")
        st.write("Star Wars: The Force Awakens (Episode VII)")
        st.write("Star Wars: The Last Jedi (Episode VIII)")
        st.write("Star Wars: The Rise of Skywalker (Episode IX)")
    elif name == "Bonus":
        st.write("Solo")
        st.write("Rouge One")
        st.write("Star Wars: A New Hope (Episode IV)")
        st.write("Star Wars: The Empire Strikes Back (Episode V)")
        st.write("Star Wars: Attack of the Clones (Episode II)")
        st.write("Star Wars: Revenge of the Sith (Episode III)")
        st.write("Star Wars: Return of the Jedi (Episode VI)")
        st.write("Star Wars: The Force Awakens (Episode VII)")
        st.write("Star Wars: The Last Jedi (Episode VIII)")
        st.write("Star Wars: The Rise of Skywalker (Episode IX)")
    st.header("Reasoning:")
    if name == "Numerical":
        st.write("By watching it in numerical order, you get to see the rise and fall of Anikin Skywalker through the whole sage. You get to see each character develop as time moves on.")
        st.write("")
        st.write("Enjoy watching!")
    elif name == "Release":
        st.write("By watching it in release order, you get to experience the story of Star Wars like you were growing up with it. You get to see the intendent story arc of the story.")
        st.write("")
        st.write("Enjoy watching!")
    elif name == "Rinster":
        st.write("By watching it in the Rinster order, you get build the suspense and leave the twist of Darth Vader at the end of the first six movies that you watch.")
        st.write("")
        st.write("Enjoy watching!")
    elif name == "Machete":
        st.write("By watching it in Machete order, you get the suspense of Darth Vader at the end, but skip Episode I which has been seen as pointless by many fans.")
        st.write("")
        st.write("Enjoy watching!")
    elif name == "Bonus":
        st.write("Here is the bonus order with Solo and Rouge One included. It fills in more context about some events for you.")
        st.write("")
        st.write("Enjoy watching!")

st.sidebar.title("Movie Orders")
order = st.sidebar.radio("Select a watch order", ["Numerical", "Release", "Rinster", "Machete"],)#2nd New Method
on = st.sidebar.toggle("Bonus") #3rd New Method
if on:
    watch_Order("Bonus")

if order == "Numerical":
    watch_Order("Numerical")
elif order == "Release":
    watch_Order("Release")
elif order == "Rinster":
    watch_Order("Rinster")
elif order == "Machete":
    watch_Order("Machete")
