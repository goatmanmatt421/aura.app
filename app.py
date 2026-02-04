import streamlit as st
import datetime
import random

# --- CONFIGURATION & PAGE SETUP ---
st.set_page_config(
    page_title="Aura: AI Astrology & Numerology Coach",
    page_icon="🔮",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CSS STYLING ---
st.markdown("""
<style>
    .main {
        background-color: #0e1117;
        color: #fafafa;
    }
    .stButton>button {
        width: 100%;
        border-radius: 20px;
        background-color: #FF4B4B; 
        color: white; 
    }
    .metric-card {
        background-color: #262730;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #41424C;
        text-align: center;
    }
    h1, h2, h3 {
        font-family: 'Helvetica Neue', sans-serif;
    }
</style>
""", unsafe_allow_html=True)

# --- LOGIC: NUMEROLOGY ---
def calculate_life_path(birthdate):
    # Sum of digits calculation (recursive reduction)
    nums = [int(d) for d in birthdate.strftime("%Y%m%d")]
    total = sum(nums)
    while total > 9 and total not in [11, 22, 33]: # Master numbers check
        total = sum(int(d) for d in str(total))
    return total

def calculate_name_number(name, method="destiny"):
    # Pythagorean System
    mapping = {
        'a':1, 'j':1, 's':1,
        'b':2, 'k':2, 't':2,
        'c':3, 'l':3, 'u':3,
        'd':4, 'm':4, 'v':4,
        'e':5, 'n':5, 'w':5,
        'f':6, 'o':6, 'x':6,
        'g':7, 'p':7, 'y':7,
        'h':8, 'q':8, 'z':8
    }
    name = name.lower().replace(" ", "")
    total = 0
    vowels = "aeiou"
    
    for char in name:
        if char not in mapping: continue
        val = mapping[char]
        
        if method == "destiny": # All letters
            total += val
        elif method == "soul" and char in vowels: # Soul Urge (Vowels)
            total += val
        elif method == "personality" and char not in vowels: # Personality (Consonants)
            total += val
            
    while total > 9 and total not in [11, 22, 33]:
        total = sum(int(d) for d in str(total))
    return total

# --- LOGIC: ASTROLOGY ---
def get_zodiac_sign(day, month):
    zodiac_dates = [
        (120, 'Capricorn'), (218, 'Aquarius'), (320, 'Pisces'), (420, 'Aries'),
        (521, 'Taurus'), (621, 'Gemini'), (722, 'Cancer'), (823, 'Leo'),
        (923, 'Virgo'), (1023, 'Libra'), (1122, 'Scorpio'), (1222, 'Sagittarius'), (1231, 'Capricorn')
    ]
    date_num = month * 100 + day
    for z_date, sign in zodiac_dates:
        if date_num <= z_date:
            return sign
    return 'Capricorn'

# --- LOGIC: AI COACH (SIMULATED & REAL) ---
def get_ai_insight(api_key, context_data, prompt_type="daily"):
    """
    If an API key is provided, this would call OpenAI/Gemini.
    Otherwise, it returns a high-quality deterministic simulation.
    """
    
    # SIMULATION MODE (No API Key)
    sign = context_data['sign']
    lp = context_data['life_path']
    
    insights = [
        f"As a {sign} with Life Path {lp}, your energy today is focused on alignment. The universe asks you to pause before acting.",
        f"Your {sign} nature might feel restless, but your Life Path {lp} grounding helps you navigate the storm. Seek stillness.",
        f"Today is a power day for {sign}. Use the vibratory power of {lp} to manifest specific goals in your career."
    ]
    
    recovery_tips = {
        "Fire": "Burn off excess energy with high-intensity cardio or creative expression.",
        "Earth": "Ground yourself. Walk barefoot on grass or organize your physical space.",
        "Air": "Clear the mental clutter. Journaling or breathwork is essential today.",
        "Water": "Emotional release is needed. A salt bath or meditation by water will restore you."
    }
    
    element_map = {
        "Aries": "Fire", "Leo": "Fire", "Sagittarius": "Fire",
        "Taurus": "Earth", "Virgo": "Earth", "Capricorn": "Earth",
        "Gemini": "Air", "Libra": "Air", "Aquarius": "Air",
        "Cancer": "Water", "Scorpio": "Water", "Pisces": "Water"
    }
    
    element = element_map.get(sign, "Earth")
    
    if prompt_type == "daily":
        return random.choice(insights)
    elif prompt_type == "recovery":
        return f"**Recovery Protocol:** {recovery_tips[element]}\n\n**Mantra:** I am aligned with my higher purpose."

# --- SIDEBAR: USER INPUT ---
with st.sidebar:
    st.header("👤 Your Profile")
    name = st.text_input("Full Name", "Alex Doe")
    dob = st.date_input("Date of Birth", datetime.date(2000, 1, 1))
    
    st.markdown("---")
    st.header("⚙️ AI Configuration")
    api_key = st.text_input("OpenAI/Gemini API Key (Optional)", type="password")
    st.caption("Leave blank to use the built-in offline engine.")
    
    if st.button("Generate Profile"):
        st.session_state['generated'] = True

# --- MAIN APP ---
st.title("🔮 Aura: Energy & Recovery System")
st.markdown("### Your daily metaphysical dashboard.")

if 'generated' in st.session_state:
    
    # 1. CALCULATE DATA
    life_path = calculate_life_path(dob)
    destiny = calculate_name_number(name, "destiny")
    soul_urge = calculate_name_number(name, "soul")
    zodiac = get_zodiac_sign(dob.day, dob.month)
    
    context = {
        "name": name,
        "sign": zodiac,
        "life_path": life_path,
        "destiny": destiny
    }

    # 2. DISPLAY DASHBOARD
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(f"<div class='metric-card'><h3>☀️ {zodiac}</h3><p>Sun Sign</p></div>", unsafe_allow_html=True)
    with col2:
        st.markdown(f"<div class='metric-card'><h3>🛣️ {life_path}</h3><p>Life Path</p></div>", unsafe_allow_html=True)
    with col3:
        st.markdown(f"<div class='metric-card'><h3>🌟 {destiny}</h3><p>Destiny</p></div>", unsafe_allow_html=True)
    with col4:
        st.markdown(f"<div class='metric-card'><h3>❤️ {soul_urge}</h3><p>Soul Urge</p></div>", unsafe_allow_html=True)

    st.markdown("---")

    # 3. TABS FOR INSIGHTS
    tab1, tab2, tab3 = st.tabs(["Daily Download", "Energy Recovery", "Ask the Coach"])

    with tab1:
        st.subheader(f"📅 Daily Horoscope for {datetime.date.today().strftime('%B %d, %Y')}")
        insight = get_ai_insight(api_key, context, "daily")
        st.info(insight)
        
        st.markdown("### Numerological Vibration of the Day")
        # Universal Day Number = Sum of today's date
        today_num = calculate_life_path(datetime.date.today())
        st.write(f"Today is a **Universal {today_num} Day**. This influences the collective energy.")

    with tab2:
        st.subheader("🔋 Personalized Energy Recovery")
        st.write("Based on your elemental makeup and numerology, here is your recharge plan:")
        recovery = get_ai_insight(api_key, context, "recovery")
        st.success(recovery)
        
        st.progress(random.randint(40, 90), text="Current Energy Alignment Score")

    with tab3:
        st.subheader("💬 AI Spiritual Coach")
        user_q = st.text_input("Ask a question about your chart or current situation:")
        if user_q:
            # Simple simulation of a chat response
            st.write("🤖 **Coach Aura:**")
            if api_key:
                st.write("*(API Connection would trigger here - returning simulated response for demo)*")
            st.write(f"Reflecting on your Life Path {life_path}, consider how '{user_q}' relates to your core lesson of independence and leadership. Trust your intuition, {name}.")

else:
    st.info("👈 Please enter your details in the sidebar to reveal your energetic profile.")
