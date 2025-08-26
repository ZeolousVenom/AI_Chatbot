def apply_theme(theme):
    """Apply light or dark theme with custom styles"""
    if theme == "dark":
        primary_color = "#FF4B4B"
        background_color = "#0E1117"
        secondary_background_color = "#262730"
        text_color = "#FAFAFA"
    else:
        primary_color = "#FF4B4B"
        background_color = "#FFFFFF"
        secondary_background_color = "#F0F2F6"
        text_color = "#31333F"
    
    theme_config = f"""
    <style>
        :root {{
            --primary-color: {primary_color};
            --background-color: {background_color};
            --secondary-background-color: {secondary_background_color};
            --text-color: {text_color};
        }}
        
        .stApp {{
            background-color: var(--background-color);
            color: var(--text-color);
        }}
        
        .stChatInput textarea {{
            color: var(--text-color) !important;
        }}
        
        /* Add more custom styles as needed */
    </style>
    """
    return theme_config