import streamlit as st
from datetime import datetime
import random

# Page configuration
st.set_page_config(
    page_title="StellarWellness - Recovery Coaching & Life Support",
    page_icon="⭐",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #14b8a6, #10b981, #06b6d4);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 3.5rem;
        font-weight: bold;
        text-align: center;
        margin-bottom: 0;
    }
    .sub-header {
        text-align: center;
        color: #9ca3af;
        font-size: 1.25rem;
        margin-bottom: 2rem;
    }
    .stat-card {
        background-color: #1f2937;
        border-radius: 10px;
        padding: 20px;
        text-align: center;
        border: 1px solid #374151;
    }
    .stat-number {
        font-size: 2rem;
        font-weight: bold;
    }
    .service-card {
        background-color: #1f2937;
        border-radius: 12px;
        padding: 20px;
        border: 1px solid #374151;
        margin-bottom: 10px;
    }
    .testimonial-card {
        background-color: #1f2937;
        border-radius: 12px;
        padding: 20px;
        border: 1px solid #374151;
    }
    .chat-user {
        background-color: #0d9488;
        color: white;
        padding: 10px 15px;
        border-radius: 15px;
        margin: 5px 0;
        max-width: 80%;
        margin-left: auto;
        text-align: right;
    }
    .chat-coach {
        background-color: #374151;
        color: #f3f4f6;
        padding: 10px 15px;
        border-radius: 15px;
        margin: 5px 0;
        max-width: 80%;
    }
    .goal-item {
        background-color: #1f2937;
        border-radius: 8px;
        padding: 10px 15px;
        margin: 5px 0;
        border: 1px solid #374151;
    }
    .category-recovery { color: #a855f7; }
    .category-health { color: #22c55e; }
    .category-personal { color: #3b82f6; }
    .category-social { color: #f97316; }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'chat_messages' not in st.session_state:
    st.session_state.chat_messages = [
        {"role": "coach", "content": "Hello! I'm your personal AI wellness coach. I'm here to support you on your recovery journey and help you achieve your daily goals. How are you feeling today?", "timestamp": datetime.now()}
    ]

if 'goals' not in st.session_state:
    st.session_state.goals = [
        {"id": 1, "text": "Attend morning meditation session", "completed": False, "category": "recovery"},
        {"id": 2, "text": "Take a 30-minute walk outside", "completed": False, "category": "health"},
        {"id": 3, "text": "Journal about feelings and progress", "completed": True, "category": "personal"},
        {"id": 4, "text": "Call a supportive friend or family member", "completed": False, "category": "social"},
        {"id": 5, "text": "Practice deep breathing exercises", "completed": False, "category": "recovery"},
    ]

if 'goal_counter' not in st.session_state:
    st.session_state.goal_counter = 6

# Coach responses
coach_responses = [
    "That's a great step forward! Remember, recovery is about progress, not perfection. What small action can you take today to support your wellbeing?",
    "I hear you. It's completely normal to have challenging days. Let's focus on what you CAN control right now. Have you tried any of your coping strategies today?",
    "Wonderful! Celebrating small wins is so important in recovery. Each positive choice builds momentum. What are you most proud of this week?",
    "Thank you for sharing that with me. Your honesty takes courage. Remember, setbacks don't define you - they're opportunities to learn and grow stronger.",
    "That sounds like a meaningful goal. Let's break it down into smaller, manageable steps. What would be the first thing you could do today?",
    "Self-compassion is key to lasting recovery. How would you speak to a friend going through the same thing? Try offering yourself that same kindness.",
    "I'm so glad you're here and committed to your journey. Every day is a new opportunity. What's one thing you're grateful for right now?",
    "Building healthy routines takes time. Be patient with yourself. What small habit would make the biggest positive impact on your daily life?",
]

# Category colors and labels
category_colors = {
    "recovery": "#a855f7",
    "health": "#22c55e",
    "personal": "#3b82f6",
    "social": "#f97316"
}

category_labels = {
    "recovery": "Recovery",
    "health": "Health & Wellness",
    "personal": "Personal Growth",
    "social": "Social Connection"
}

# ================== HERO SECTION ==================
st.markdown('<p style="text-align: center; color: #14b8a6; font-size: 0.875rem; margin-bottom: 0.5rem;">⭐ Your Journey to Wellness Starts Here</p>', unsafe_allow_html=True)
st.markdown('<h1 class="main-header">StellarWellness</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Life Coaching for Recovery & Personal Growth</p>', unsafe_allow_html=True)

st.markdown("""
<p style="text-align: center; color: #9ca3af; max-width: 800px; margin: 0 auto 2rem auto;">
Empowering individuals on their journey to overcome addiction and build a fulfilling life.
With personalized AI coaching, daily goal tracking, and compassionate support every step of the way.
</p>
""", unsafe_allow_html=True)

# ================== STATS SECTION ==================
st.divider()
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown('<div class="stat-card"><p class="stat-number" style="color: #14b8a6;">24/7</p><p style="color: #9ca3af; font-size: 0.875rem;">AI Coach Support</p></div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="stat-card"><p class="stat-number" style="color: #10b981;">100%</p><p style="color: #9ca3af; font-size: 0.875rem;">Confidential</p></div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="stat-card"><p class="stat-number" style="color: #06b6d4;">Daily</p><p style="color: #9ca3af; font-size: 0.875rem;">Goal Tracking</p></div>', unsafe_allow_html=True)

with col4:
    st.markdown('<div class="stat-card"><p class="stat-number" style="color: #a855f7;">1000+</p><p style="color: #9ca3af; font-size: 0.875rem;">Lives Transformed</p></div>', unsafe_allow_html=True)

st.divider()

# ================== ABOUT SECTION ==================
st.header("Recovery is a Journey, Not a Destination")

col_about1, col_about2 = st.columns([3, 2])

with col_about1:
    st.markdown("""
    At StellarWellness, we understand that overcoming addiction and building a healthier life
    requires more than willpower alone. It requires compassionate guidance, practical tools,
    and unwavering support.

    Our approach combines evidence-based recovery techniques with modern AI technology to provide
    you with personalized coaching that adapts to your unique needs, challenges, and goals.

    **What we offer:**
    - ✅ Personalized recovery plans tailored to your journey
    - ✅ 24/7 AI coaching support when you need it most
    - ✅ Daily goal tracking to celebrate every milestone
    """)

with col_about2:
    st.info("""
    💜 **StellarWellness Philosophy**

    *"Every step forward, no matter how small, is progress worth celebrating."*
    """)

# ================== SERVICES SECTION ==================
st.header("Our Services")
st.markdown("Comprehensive support designed to help you thrive in every aspect of your recovery journey")

col_s1, col_s2, col_s3 = st.columns(3)

with col_s1:
    with st.container():
        st.subheader("💬 AI Recovery Coach")
        st.markdown("24/7 access to our intelligent AI coach that provides personalized guidance, coping strategies, and emotional support whenever you need it.")

    with st.container():
        st.subheader("💜 Mindfulness & Meditation")
        st.markdown("Guided meditation sessions and mindfulness exercises to help manage stress, cravings, and emotional challenges.")

with col_s2:
    with st.container():
        st.subheader("📋 Goal & Task Tracking")
        st.markdown("Set daily, weekly, and milestone goals. Track your progress and celebrate achievements as you build healthy habits and routines.")

    with st.container():
        st.subheader("👥 Community Support")
        st.markdown("Connect with others on similar journeys. Share experiences, find encouragement, and build a supportive network.")

with col_s3:
    with st.container():
        st.subheader("📚 Recovery Resources")
        st.markdown("Access a curated library of articles, exercises, and techniques based on evidence-based recovery methodologies.")

    with st.container():
        st.subheader("📊 Progress Analytics")
        st.markdown("Visualize your recovery journey with insights and analytics that show how far you've come and inspire continued growth.")

st.divider()

# ================== INTERACTIVE TOOLS SECTION ==================
st.header("Your Recovery Toolkit")
st.markdown("Interactive tools designed to support your daily wellness journey")

tool_tab1, tool_tab2 = st.tabs(["💬 AI Wellness Coach", "📋 Daily Goal Tracker"])

# ================== AI COACH TAB ==================
with tool_tab1:
    st.subheader("Stellar AI Coach")
    st.caption("Your personal recovery companion • 🟢 Online")

    # Chat display
    chat_container = st.container()
    with chat_container:
        for msg in st.session_state.chat_messages:
            if msg["role"] == "coach":
                st.markdown(f'<div class="chat-coach">{msg["content"]}<br><small style="color: #6b7280;">{msg["timestamp"].strftime("%I:%M %p")}</small></div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="chat-user">{msg["content"]}<br><small style="color: #99f6e4;">{msg["timestamp"].strftime("%I:%M %p")}</small></div>', unsafe_allow_html=True)

    # Chat input
    with st.form(key="chat_form", clear_on_submit=True):
        user_input = st.text_input("Share what's on your mind...", key="user_message", label_visibility="collapsed", placeholder="Share what's on your mind...")
        submit_chat = st.form_submit_button("Send", use_container_width=True)

        if submit_chat and user_input:
            # Add user message
            st.session_state.chat_messages.append({
                "role": "user",
                "content": user_input,
                "timestamp": datetime.now()
            })

            # Add coach response
            response = random.choice(coach_responses)
            st.session_state.chat_messages.append({
                "role": "coach",
                "content": response,
                "timestamp": datetime.now()
            })
            st.rerun()

    st.caption("🔒 Your conversations are private and secure")

# ================== GOAL TRACKER TAB ==================
with tool_tab2:
    st.subheader("Daily Goals & Tasks")
    st.caption("Track your recovery milestones")

    # Progress display
    completed_count = sum(1 for g in st.session_state.goals if g["completed"])
    total_count = len(st.session_state.goals)
    progress_pct = (completed_count / total_count * 100) if total_count > 0 else 0

    col_prog1, col_prog2 = st.columns([3, 1])
    with col_prog1:
        st.progress(progress_pct / 100)
    with col_prog2:
        st.metric("Progress", f"{int(progress_pct)}%", f"{completed_count}/{total_count} complete")

    # Add new goal
    with st.form(key="goal_form", clear_on_submit=True):
        col_g1, col_g2, col_g3 = st.columns([3, 1, 1])
        with col_g1:
            new_goal_text = st.text_input("Add a new goal...", key="new_goal", label_visibility="collapsed", placeholder="Add a new goal...")
        with col_g2:
            new_goal_category = st.selectbox("Category", options=list(category_labels.keys()), format_func=lambda x: category_labels[x], label_visibility="collapsed")
        with col_g3:
            submit_goal = st.form_submit_button("Add", use_container_width=True)

        if submit_goal and new_goal_text:
            st.session_state.goals.insert(0, {
                "id": st.session_state.goal_counter,
                "text": new_goal_text,
                "completed": False,
                "category": new_goal_category
            })
            st.session_state.goal_counter += 1
            st.rerun()

    # Filter tabs
    filter_options = ["All"] + list(category_labels.values())
    selected_filter = st.radio("Filter by category:", filter_options, horizontal=True, label_visibility="collapsed")

    # Display goals
    for goal in st.session_state.goals:
        # Apply filter
        if selected_filter != "All" and category_labels[goal["category"]] != selected_filter:
            continue

        col_check, col_cat, col_text, col_delete = st.columns([0.5, 0.5, 8, 1])

        with col_check:
            completed = st.checkbox("", value=goal["completed"], key=f"goal_{goal['id']}", label_visibility="collapsed")
            if completed != goal["completed"]:
                goal["completed"] = completed
                st.rerun()

        with col_cat:
            cat_color = category_colors[goal["category"]]
            st.markdown(f'<span style="color: {cat_color}; font-size: 1.5rem;">●</span>', unsafe_allow_html=True)

        with col_text:
            if goal["completed"]:
                st.markdown(f'<span style="text-decoration: line-through; color: #6b7280;">{goal["text"]}</span>', unsafe_allow_html=True)
            else:
                st.markdown(goal["text"])

        with col_delete:
            if st.button("✕", key=f"delete_{goal['id']}"):
                st.session_state.goals = [g for g in st.session_state.goals if g["id"] != goal["id"]]
                st.rerun()

st.divider()

# ================== CTA SECTION ==================
st.markdown("""
<div style="background: linear-gradient(90deg, rgba(20, 184, 166, 0.2), rgba(16, 185, 129, 0.2), rgba(6, 182, 212, 0.2)); border-radius: 15px; padding: 40px; text-align: center; border: 1px solid #374151;">
    <h2 style="color: white;">Begin Your Transformation Today</h2>
    <p style="color: #d1d5db; max-width: 600px; margin: 0 auto 20px auto;">
        Every journey begins with a single step. Take yours today and discover the support,
        tools, and guidance you need to build the life you deserve.
    </p>
    <p style="color: #6b7280; font-size: 0.875rem;">
        Free to start. No credit card required. Your privacy is our priority.
    </p>
</div>
""", unsafe_allow_html=True)

st.divider()

# ================== TESTIMONIALS SECTION ==================
st.header("Stories of Hope")
st.markdown("Real people, real transformations. Your story could be next.")

col_t1, col_t2, col_t3 = st.columns(3)

with col_t1:
    st.markdown("""
    <div class="testimonial-card">
        <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 10px;">
            <div style="width: 40px; height: 40px; background-color: rgba(20, 184, 166, 0.3); border-radius: 50%; display: flex; align-items: center; justify-content: center; color: #14b8a6; font-weight: bold;">M</div>
            <div>
                <p style="margin: 0; font-weight: 600; color: white;">Michael R.</p>
                <p style="margin: 0; color: #9ca3af; font-size: 0.875rem;">18 months sober</p>
            </div>
        </div>
        <p style="color: #d1d5db; font-style: italic;">"The AI coach was there for me at 3 AM when I felt like giving up. It helped me get through my darkest moments. Today, I'm stronger than ever."</p>
    </div>
    """, unsafe_allow_html=True)

with col_t2:
    st.markdown("""
    <div class="testimonial-card">
        <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 10px;">
            <div style="width: 40px; height: 40px; background-color: rgba(16, 185, 129, 0.3); border-radius: 50%; display: flex; align-items: center; justify-content: center; color: #10b981; font-weight: bold;">S</div>
            <div>
                <p style="margin: 0; font-weight: 600; color: white;">Sarah K.</p>
                <p style="margin: 0; color: #9ca3af; font-size: 0.875rem;">2 years in recovery</p>
            </div>
        </div>
        <p style="color: #d1d5db; font-style: italic;">"The daily goal tracker changed everything. Small wins add up, and seeing my progress visualized kept me motivated every single day."</p>
    </div>
    """, unsafe_allow_html=True)

with col_t3:
    st.markdown("""
    <div class="testimonial-card">
        <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 10px;">
            <div style="width: 40px; height: 40px; background-color: rgba(168, 85, 247, 0.3); border-radius: 50%; display: flex; align-items: center; justify-content: center; color: #a855f7; font-weight: bold;">J</div>
            <div>
                <p style="margin: 0; font-weight: 600; color: white;">James T.</p>
                <p style="margin: 0; color: #9ca3af; font-size: 0.875rem;">1 year clean</p>
            </div>
        </div>
        <p style="color: #d1d5db; font-style: italic;">"I was skeptical about AI coaching, but it felt like talking to someone who truly understood. It's been a game-changer for my recovery."</p>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.divider()
st.markdown("""
<p style="text-align: center; color: #6b7280;">
    © 2024 StellarWellness | Contact: hello@stellarwellness.com
</p>
""", unsafe_allow_html=True)
