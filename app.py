import streamlit as st
from streamlit_option_menu import option_menu
from datetime import datetime
import time

st.set_page_config(page_title="AI Protection Console", layout="wide")

# --- Sidebar Navigation ---
with st.sidebar:
    selected = option_menu(
        menu_title="Main Menu",
        options=["Home", "Monitoring Dashboard", "Logs", "Settings"],
        icons=["house", "activity", "file-earmark-text", "gear"],
        menu_icon="cast",
        default_index=0,
        styles={
            "container": {"padding": "5!important", "background-color": "#181818"},
            "icon": {"color": "lime", "font-size": "25px"},
            "nav-link": {
                "font-size": "16px",
                "text-align": "left",
                "margin": "0px",
                "--hover-color": "#00FFC6",
            },
            "nav-link-selected": {"background-color": "#00FFC6", "color": "black"},
        },
    )

# --- Home Page ---
if selected == "Home":
    st.markdown("""
        <style>
            .neon-box {
                padding: 20px;
                border-radius: 12px;
                margin-bottom: 20px;
                text-align: center;
                box-shadow: 0 0 15px #00ffc6, 0 0 30px #00ffc6;
            }

            .neon-title-green {
                color: #39FF14;
                font-size: 38px;
                font-weight: bold;
                background-color: #111;
                border: 2px solid #39FF14;
                box-shadow: 0 0 15px #39FF14, 0 0 30px #39FF14;
            }

            .neon-title-blue {
                color: #00D9FF;
                font-size: 28px;
                background-color: #111;
                border: 2px solid #00D9FF;
                box-shadow: 0 0 10px #00D9FF, 0 0 20px #00D9FF;
            }

            .neon-paragraph {
                color: #BBB;
                font-size: 16px;
                margin-top: 20px;
            }

            .neon-status {
                background-color: #222;
                padding: 10px;
                border-radius: 8px;
                color: #00FF00;
                font-weight: bold;
                box-shadow: 0 0 10px #00FF00;
            }
        </style>

        <div class="neon-box neon-title-green">🚨 AI Protection Console</div>
        <div class="neon-box neon-title-blue">Real-Time Monitoring & Automated Flagging</div>

        <div style="margin-top: 20px; background-color: #00BFFF; padding: 15px; border-radius: 8px;">
        <p style="color:#CCFF00; margin: 0;">Scan AI-generated outputs to detect harmful or unsafe behavior including threats, harassment, and biases.</p>
         <span style="color:#CCFF00; display: block; margin-top: 8px;">✅ System is currently active and monitoring 24/7.</span>
        </div>

    """, unsafe_allow_html=True)


# --- Monitoring Dashboard ---
elif selected == "Monitoring Dashboard":
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Flags Detected", "12")
    with col2:
        st.metric("Threat Level", "Medium", delta="+2", delta_color="inverse")
    with col3:
        st.metric("Interactions", "2387")

    tabs = st.tabs(["Live Feed", "Analytics"])
    with tabs[0]:
        st.subheader("Live Output Feed")
        feed_data = [
            {"time": "12:01", "model": "GPT-5", "text": "I will find you..."},
            {"time": "12:02", "model": "Gemini", "text": "You are worthless"},
        ]
        for msg in feed_data:
            st.markdown(
                f"""
                <div style='padding:10px; background:#222; color:#DDD; margin-bottom:8px; border-left: 5px solid red;'>
                    <b>[{msg['time']}] {msg['model']}:</b> '{msg['text']}'
                </div>
                """,
                unsafe_allow_html=True,
            )

# --- Logs ---
elif selected == "Logs":
    st.title("🔍 Interaction Logs")
    st.dataframe([
        {"Timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "Model": "GPT-5", "Severity": "High", "Snippet": "...I will find you..."},
        {"Timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "Model": "Gemini", "Severity": "High", "Snippet": "...You are worthless..."}
    ])

# --- Settings ---
elif selected == "Settings":
    st.title("⚙️ Settings & Configuration")
    sensitivity = st.slider("Detection Sensitivity", 0, 100, 50)
    dark_mode = st.toggle("Dark Mode")
    st.text_input("Notification Email", "admin@example.com")
    st.selectbox("User Role", ["Admin", "Analyst", "Viewer"])
    st.button("Save Changes")
