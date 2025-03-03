import streamlit as st
import requests

# Set Streamlit page configuration
st.set_page_config(page_title="🌠 AstroConverter", page_icon="🔁", layout="wide")

# Theme Toggle (Dark Mode)
dark_mode = st.sidebar.checkbox("🌙 Dark Mode")

# Apply Dark Mode Styles
if dark_mode:
    st.markdown(
        """
        <style>
        body { background-color: #222; color: white; }
        .stApp { background-color: #333; }
        .sidebar .sidebar-content { background-color: #111; color: white; }
        h1, h2, h3, h4 { color: #4CAF50; }
        </style>
        """,
        unsafe_allow_html=True
    )

# Sidebar with icons
categories = {
    "Weight ⚖": "Weight",
    "Temperature 🌡": "Temperature",
    "Length 📏": "Length",
    "Time ⏳": "Time",
    "Currency 💰": "Currency",
    "Area 🌍": "Area",
    "Speed 🚀": "Speed",
    "Volume 🧪": "Volume",
}

st.sidebar.title("🔁 Unit Converter")
category = st.sidebar.radio("Choose a conversion type:", list(categories.keys()))
category = categories[category]  # Remove icons for processing

# Session state for conversion history
if "history" not in st.session_state:
    st.session_state.history = []

# Display last 5 conversion history entries
st.sidebar.subheader("🕒 Conversion History")
for entry in st.session_state.history[-5:]:
    st.sidebar.write(entry)

# Clear history button
if st.sidebar.button("🗑 Clear History"):
    st.session_state.history = []
    st.sidebar.success("History cleared!")

st.markdown(f"## 🚀 {category} Conversion")

# Function to save history
def save_to_history(conversion):
    st.session_state.history.append(conversion)

# Conversion Logic
if category == "Weight":
    weight_units = {"Grams": 1, "Kilograms": 0.001, "Pounds": 0.00220462, "Ounces": 0.035274}
    value = st.number_input("Enter weight", min_value=0.0, value=1.0)
    from_unit = st.selectbox("From", weight_units)
    to_unit = st.selectbox("To", weight_units)

    result = value * (weight_units[to_unit] / weight_units[from_unit])
    conversion_text = f"{value} {from_unit} = {result:.4f} {to_unit}"

    save_to_history(conversion_text)
    st.success(conversion_text)

elif category == "Temperature":
    value = st.slider("Enter temperature", min_value=-100, max_value=100, value=25)
    from_unit = st.radio("From", ["Celsius", "Fahrenheit", "Kelvin"])
    to_unit = st.radio("To", ["Celsius", "Fahrenheit", "Kelvin"])

    conversions = {
        ("Celsius", "Fahrenheit"): lambda x: x * 9/5 + 32,
        ("Celsius", "Kelvin"): lambda x: x + 273.15,
        ("Fahrenheit", "Celsius"): lambda x: (x - 32) * 5/9,
        ("Fahrenheit", "Kelvin"): lambda x: (x - 32) * 5/9 + 273.15,
        ("Kelvin", "Celsius"): lambda x: x - 273.15,
        ("Kelvin", "Fahrenheit"): lambda x: (x - 273.15) * 9/5 + 32
    }

    result = conversions.get((from_unit, to_unit), lambda x: x)(value)
    conversion_text = f"{value} {from_unit} = {result:.2f} {to_unit}"
    
    save_to_history(conversion_text)
    st.success(conversion_text)

elif category == "Currency":
    value = st.number_input("Enter amount", min_value=0.0, value=1.0)
    currency_list = ["USD", "EUR", "GBP", "JPY", "INR", "CAD", "AUD", "CNY", "BRL"]
    from_currency = st.selectbox("From", currency_list)
    to_currency = st.selectbox("To", currency_list)

    if st.button("Convert"):
        try:
            response = requests.get(f"https://api.exchangerate-api.com/v4/latest/{from_currency}")
            data = response.json()
            rate = data["rates"].get(to_currency)

            if rate:
                result = value * rate
                conversion_text = f"{value} {from_currency} = {result:.2f} {to_currency}"
                save_to_history(conversion_text)
                st.success(conversion_text)
            else:
                st.error("Conversion rate not available.")
        except Exception:
            st.error("Error fetching currency rates! Please try again.")

elif category == "Length":
    length_units = {"Meters": 1, "Kilometers": 0.001, "Centimeters": 100, "Feet": 3.28084, "Inches": 39.3701}
    value = st.number_input("Enter length", min_value=0.0, value=1.0)
    from_unit = st.selectbox("From", length_units)
    to_unit = st.selectbox("To", length_units)

    result = value * (length_units[to_unit] / length_units[from_unit])
    conversion_text = f"{value} {from_unit} = {result:.4f} {to_unit}"
    
    save_to_history(conversion_text)
    st.success(conversion_text)

elif category == "Time":
    time_units = {"Seconds": 1, "Minutes": 1/60, "Hours": 1/3600, "Days": 1/86400}
    value = st.number_input("Enter time", min_value=0.0, value=1.0)
    from_unit = st.selectbox("From", time_units)
    to_unit = st.selectbox("To", time_units)

    result = value * (time_units[to_unit] / time_units[from_unit])
    conversion_text = f"{value} {from_unit} = {result:.4f} {to_unit}"
    
    save_to_history(conversion_text)
    st.success(conversion_text)

elif category == "Area":
    area_units = {"Square Meters": 1, "Square Kilometers": 0.000001, "Square Feet": 10.7639, "Acres": 0.000247105}
    value = st.number_input("Enter area", min_value=0.0, value=1.0)
    from_unit = st.selectbox("From", area_units)
    to_unit = st.selectbox("To", area_units)

    result = value * (area_units[to_unit] / area_units[from_unit])
    conversion_text = f"{value} {from_unit} = {result:.4f} {to_unit}"
    
    save_to_history(conversion_text)
    st.success(conversion_text)

elif category == "Speed":
    speed_units = {"Meters per second": 1, "Kilometers per hour": 3.6, "Miles per hour": 2.23694}
    value = st.number_input("Enter speed", min_value=0.0, value=1.0)
    from_unit = st.selectbox("From", speed_units)
    to_unit = st.selectbox("To", speed_units)

    result = value * (speed_units[to_unit] / speed_units[from_unit])
    conversion_text = f"{value} {from_unit} = {result:.4f} {to_unit}"
    
    save_to_history(conversion_text)
    st.success(conversion_text)

elif category == "Volume":
    volume_units = {"Liters": 1, "Milliliters": 1000, "Cubic Meters": 0.001, "Gallons": 0.264172}
    value = st.number_input("Enter volume", min_value=0.0, value=1.0)
    from_unit = st.selectbox("From", volume_units)
    to_unit = st.selectbox("To", volume_units)

    result = value * (volume_units[to_unit] / volume_units[from_unit])
    conversion_text = f"{value} {from_unit} = {result:.4f} {to_unit}"
    
    save_to_history(conversion_text)
    st.success(conversion_text)
