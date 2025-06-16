import streamlit as st
import pandas as pd
import time
from streamlit_option_menu import option_menu

st.set_page_config(page_title="AI Protection Console", layout="wide")

# Custom CSS for colorful background and neon sidebar
st.markdown("""
    <style>
    body, .stApp, .block-container {
        background: linear-gradient(135deg, #ff69b4, #ffcc00, #00ffcc, #cc00ff);
        background-size: 1000% 1000%;
        animation: gradientBG 15s ease infinite;
    }

    @keyframes gradientBG {
        0% {background-position: 0% 70%;}
        50% {background-position: 100% 70%;}
        100% {background-position: 0% 70%;}
    }

    .neon-box {
        border: 2px solid #39FF14;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 0 10px #39FF14, 0 0 20px #39FF14;
        margin-bottom: 25px;
        background-color: rgba(0,0,0,0.3);
        color: white;
    }

    .css-1d391kg .css-ng1t4o {
        width: 500px;  /* Smaller sidebar */
    }

    /* Updated sidebar background and neon effect */
    .css-1d391kg {
        background-color: silver !important;
        box-shadow: 0 0 10px #39FF14, 0 0 25px #39FF14, 0 0 40px #39FF14;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar Navigation
with st.sidebar:
    selected = option_menu(
        menu_title="AI Console",
        options=["Home", "Live Feed", "Heatmap", "Alerts", "Rule Builder", "Logs", "Analytics"],
        icons=["house", "activity", "globe", "bell", "tools", "list", "bar-chart"],
        menu_icon="cpu", default_index=0,
        styles={
            "container": {
                "background-color": "#85F7ECEF",  # Silver background
                "padding": "5px 0px",
                "width": "280px",  # Smaller sidebar
                "box-shadow": "0 0 50px #39FF14"
            },
            "icon": {"color": "white", "font-size": "22px"},
            "nav-link": {
                "color": "white",
                "font-size": "16px",
                "text-align": "left",
                "padding": "8px 16px"
            },
            "nav-link-selected": {
                "background-color": "#39FF14",
                "color": "black",
                "font-weight": "bold"
            }
        }
    )

# Home Page
if selected == "Home":
    st.title("🚀 AI Protection Console")
    st.markdown("### Your centralized control for real-time AI threat monitoring and response")
    st.markdown("""
    <div class='neon-box'>
        <h3>👁️‍🗨️ Real-Time Monitoring & Visualization</h3>
        <ul>
            <li>Live AI Output Feed</li>
            <li>Threat Heatmap</li>
            <li>Threat-Level Timeline</li>
        </ul>
    </div>
    <div class='neon-box'>
        <h3>⚙️ Automated Detection & Analysis</h3>
        <ul>
            <li>Rule-Engine Builder</li>
            <li>Sentiment & Toxicity Scoring</li>
            <li>Multi-Model Comparison</li>
        </ul>
    </div>
    <div class='neon-box'>
        <h3>🚨 Alerting & Escalation</h3>
        <ul>
            <li>Alert Center</li>
            <li>Escalation Workflow</li>
            <li>Acknowledge & Comment</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# Live Feed Page
elif selected == "Live Feed":
    st.header("📡 Live AI Output Feed")
    with st.container():
        placeholder = st.empty()
        for i in range(10):
            with placeholder.container():
                st.markdown(f"<div class='neon-box'>🔴 Suspicious activity detected at 12:{10+i} PM</div>", unsafe_allow_html=True)
                time.sleep(0.5)

# Heatmap Page
elif selected == "Heatmap":
    st.header("🗺️ Threat Heatmap")
    st.map(pd.DataFrame({
        'lat': [28.7041, 37.7749, 51.5074],
        'lon': [77.1025, -122.4194, -0.1278]
    }))

# Alerts Page
elif selected == "Alerts":
    st.header("📨 Alert Center")
    df = pd.DataFrame({
        "Time": ["12:05 PM", "12:15 PM"],
        "Severity": ["High", "Medium"],
        "Message": ["Toxic comment flagged", "Sentiment drop"]
    })
    st.dataframe(df)

# Rule Builder Page
elif selected == "Rule Builder":
    st.header("🛠️ Rule Engine Builder")
    keyword = st.text_input("Keyword to Flag:")
    severity = st.selectbox("Severity Level", ["Low", "Medium", "High"])
    if st.button("Add Rule"):
        st.success(f"Rule for '{keyword}' with severity '{severity}' added.")

# Logs Page
elif selected == "Logs":
    st.header("📋 Interaction Logs")
    log_data = pd.DataFrame({
        "Timestamp": ["2025-06-15 12:10:00", "2025-06-15 12:20:00"],
        "Event": ["Alert Acknowledged", "Rule Added"]
    })
    st.dataframe(log_data)

# Analytics Page
elif selected == "Analytics":
    st.header("📊 API Call Analytics")
    chart_data = pd.DataFrame(
        {
            "Calls": [100, 120, 140, 130, 160],
            "Errors": [2, 3, 5, 4, 6]
        },
        index=pd.date_range("2025-06-10", periods=5)
    )
    st.line_chart(chart_data)
    st.bar_chart(chart_data["Calls"])
    st.success("✅ Daily/Weekly Reports Available")
