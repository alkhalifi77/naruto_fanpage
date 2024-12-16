import streamlit as st
from typing import Dict, List
from dataclasses import dataclass

@dataclass
class Character:
    """Class to store character information"""
    description: str
    moves: List[str]
    weapons: List[str]

# Data for Naruto characters using a more structured approach
CHARACTERS: Dict[str, Character] = {
    "Naruto Uzumaki": Character(
        description="Naruto Uzumaki is a ninja from the Hidden Leaf Village. He is the Jinchuriki of the Nine-Tails and aspires to become Hokage.",
        moves=["Rasengan", "Shadow Clone Jutsu", "Sage Mode"],
        weapons=["Kunai", "Shuriken"]
    ),
    "Sasuke Uchiha": Character(
        description="Sasuke Uchiha is one of the last surviving members of the Uchiha clan. He wields the Sharingan and seeks vengeance for his clan.",
        moves=["Chidori", "Amaterasu", "Susano'o"],
        weapons=["Kusanagi Sword", "Shuriken"]
    ),
    # ... Add other characters similarly
}

def initialize_session_state() -> None:
    """Initialize session state variables"""
    if "current_character" not in st.session_state:
        st.session_state.current_character = None

def show_character_details(character: Character) -> None:
    """Displays detailed information about the selected character"""
    st.write(character.description)
    
    st.markdown("**Moves:**")
    st.write(", ".join(character.moves))
    
    st.markdown("**Weapons:**")
    st.write(", ".join(character.weapons))

def create_layout():
    """Creates the main layout of the application"""
    st.set_page_config(
        page_title="Naruto Characters",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    st.title("Naruto Characters")
    st.write("Click on a character to learn more about them!")

def main():
    """Main application function"""
    create_layout()
    initialize_session_state()

    # Sidebar navigation
    with st.sidebar:
        st.title("Select a Character")
        selected_character = st.radio(
            "Characters:",
            options=list(CHARACTERS.keys()),
            key="character_selector"
        )
        # Update current_character when radio selection changes
        st.session_state.current_character = selected_character


    # Main content layout
    col1, col2 = st.columns([3, 2])

    with col1:
        st.header("Main Page")
        for char_name in CHARACTERS:
            if st.button(f"About {char_name}", key=f"btn_{char_name}"):
                st.session_state.current_character = char_name

    with col2:
        st.markdown("### Character Details")
        if st.session_state.current_character:
            st.markdown(f"### {st.session_state.current_character}")
            show_character_details(CHARACTERS[st.session_state.current_character])
        else:
            st.info("Select a character to view details.")

if __name__ == "__main__":
    main()
