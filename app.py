import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# --- Page Setup ---
st.set_page_config(page_title="Fluid Dynamics: The Bernoulli Principle", page_icon="💧")

# --- Developer Credit ---
st.markdown("### www.cognitivecloud.ai")
st.markdown("**Developed by Xavier Honablue M.Ed**")

st.markdown("---")

# --- Title and Intro ---
st.title("💧 The Bernoulli Principle Explorer")
st.markdown("""
Welcome! This lesson helps you **see, understand, and apply** the Bernoulli principle and its mathematical underpinnings.

---

### 📘 The Principle:
The **Bernoulli principle** is a fundamental concept in fluid dynamics which states that as the speed of a fluid increases, the pressure within the fluid decreases.

Think of a river: in a narrow section, the water flows faster and the pressure is lower. In a wide section, the water flows slower and the pressure is higher. This simple relationship explains everything from why airplanes fly to how a carburetor works.

---

### 🎯 Objective:
By the end of this lesson, you'll be able to:
- Define and explain the Bernoulli principle
- Identify real-life examples of the principle in action
- Understand the inverse relationship between fluid speed and pressure
- Relate these concepts to Common Core math standards
""")

# Common Core Standards Alignment
st.info("📚 **Common Core Alignment:** This lesson aligns with high school algebra standards including interpreting functions, creating equations in real-world contexts, and understanding graphical representations of relationships between variables.")

# Standards Dropdown
common_core_standard = st.selectbox("📋 Select a Common Core Math Standard:", [
    "HSA-CED.A.1 - Create equations and inequalities in one variable",
    "HSF-IF.B.4 - Interpret key features of graphs and tables in terms of quantities",
    "HSF-IF.C.7 - Graph functions expressed symbolically and show key features",
    "HSF-BF.A.1 - Write a function that describes a relationship between two quantities"
])

# --- User Info (Moved Up) ---
name = st.text_input("Enter your name:")
avatar = st.selectbox("Choose your avatar:", [
    "💧 Droplet", "💨 Vortex", "🌊 Wave", "🌪️ Cyclone"
])

if name:
    st.success(f"Welcome, {name} the {avatar}! Let's begin exploring fluid dynamics.")

# --- Interactive Explorer Section ---
st.header("🔍 Let's explore the relationship between fluid speed and pressure...")

# Interactive Visualization
st.header("🔟 Interactive Bernoulli Visualization")
st.markdown("Use the slider to change the fluid's speed and see the corresponding change in pressure. This is a simplified model to demonstrate the inverse relationship.")

# Create columns for the slider and the explanation
col1, col2 = st.columns([2, 1])

with col1:
    # Slider for fluid speed
    speed = st.slider("Fluid Speed (v in m/s)", 0, 10, 5)

    # Simplified model: P = C - (1/2) * rho * v^2. Here, C and rho are constants.
    # We'll use a simple linear relationship to show the inverse nature for demonstration.
    # Let's model pressure as a function of speed: f(v) = 100 - 5 * v^2
    # This is a quadratic decay, effectively showing the inverse relationship.
    
    # Generate x and y values for the plot
    x_vals = np.linspace(0, 10, 100)
    y_vals = 100 - 5 * x_vals**2
    
    # Find the corresponding pressure for the selected speed
    pressure = 100 - 5 * speed**2
    
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(x_vals, y_vals, linewidth=3, color='#1f77b4')
    ax.plot(speed, pressure, 'ro', markersize=10) # Highlight the current point
    ax.set_title("Simplified Model of Bernoulli's Principle", fontsize=14, fontweight='bold')
    ax.set_xlabel("Fluid Speed (v) [m/s]", fontsize=12)
    ax.set_ylabel("Relative Pressure (P)", fontsize=12)
    ax.set_ylim(0, 100)
    ax.grid(True, alpha=0.3)
    st.pyplot(fig)

with col2:
    st.info(f"**Explanation:** As the slider increases the fluid speed (v), the graph shows that the pressure (P) decreases. The red dot represents the current value.")
    st.write(f"**Current Speed (v):** {speed} m/s")
    st.write(f"**Corresponding Pressure (P):** {pressure:.2f} (relative units)")
    st.write("**Mathematical Expression (Simplified):** `P = 100 - 5v²`")
    st.write("This shows the inverse quadratic relationship between speed and pressure.")

st.markdown("---")

# Quick Quiz Section
st.header("🎲 Quick Understanding Check")

quiz_questions = [
    {
        "question": "According to Bernoulli's principle, what happens to pressure as fluid speed increases?",
        "options": ["It increases", "It decreases", "It stays the same", "It depends on the fluid"],
        "correct": 1,
        "explanation": "The Bernoulli principle states an inverse relationship: as speed goes up, pressure goes down."
    },
    {
        "question": "Which of these is a real-world application of Bernoulli's principle?",
        "options": ["A car's engine starting", "An airplane wing generating lift", "A ball falling to the ground", "A magnet attracting metal"],
        "correct": 1,
        "explanation": "An airplane wing is shaped so that air travels faster over the top, creating lower pressure there and 'lifting' the plane."
    },
    {
        "question": "The relationship between fluid speed and pressure in the Bernoulli equation is an example of what type of relationship?",
        "options": ["Direct", "Linear", "Inverse", "Proportional"],
        "correct": 2,
        "explanation": "An inverse relationship means as one variable increases, the other decreases."
    }
]

for i, q in enumerate(quiz_questions):
    st.write(f"**Question {i+1}:** {q['question']}")
    answer = st.radio(f"Select your answer for Q{i+1}:", q['options'], key=f"q{i}")
    
    if st.button(f"Check Answer {i+1}", key=f"check{i}"):
        if q['options'].index(answer) == q['correct']:
            st.success(f"✅ Correct! {q['explanation']}")
        else:
            st.error(f"❌ Try again! {q['explanation']}")

# Exit Reflection
st.header("🧾 Reflection")
reflection = st.text_area("What is one real-world situation where you've observed a Bernoulli-like effect? How would you describe the relationship using math concepts?")

if st.button("Submit Reflection"):
    if reflection.strip():
        st.success("✅ Excellent! You're thinking like a scientist and a mathematician.")
        st.balloons()
    else:
        st.warning("Please share your thoughts to complete the reflection.")

# Final Summary
st.header("🎓 What You've Learned")
st.markdown("""
**Congratulations!** You've explored:
- ✅ **The Bernoulli principle** and its core concept
- ✅ **Real-world examples** from aviation to household objects
- ✅ **An inverse relationship** between fluid speed and pressure
- ✅ **Mathematical representations** that make the principle come alive

**Remember:** Science and math are the language that describes how our world works! Keep an eye out for these principles in your daily life.
""")

st.markdown("---")

# Related Lessons
st.header("📚 Related Lessons & Resources")

# Common Core Strand Selection for Targeted Resources
st.subheader("🎯 Choose Your Learning Focus")
strand = st.selectbox("Select a Common Core Math Strand to customize your resources:", [
    "HSA-CED.A.1 - Create equations",
    "HSF-IF.B.4 - Interpret key features of functions",
    "HSF-IF.C.7 - Graph functions expressed symbolically",
    "HSA-REI.B.3 - Solve linear equations"
])

# Adaptive content based on strand selection
if "HSA-CED.A.1" in strand:
    st.info("🎯 **Focus: Creating Equations** - Resources emphasize building equations from real-world scenarios, like those in fluid dynamics.")
    emphasis = "equation_building"
elif "HSF-IF.B.4" in strand:
    st.info("🎯 **Focus: Interpreting Key Features** - Resources emphasize analyzing graphs to understand relationships like the inverse relationship between speed and pressure.")
    emphasis = "key_features"
elif "HSF-IF.C.7" in strand:
    st.info("🎯 **Focus: Graphing Functions** - Resources emphasize creating and reading graphs to visualize mathematical relationships.")
    emphasis = "graphing"
else:  # HSA-REI.B.3
    st.info("🎯 **Focus: Solving Equations** - Resources emphasize manipulating and solving algebraic equations related to a physical principle.")
    emphasis = "solving_equations"

# IXL recommendations based on strand
st.markdown("**🎯 Recommended Practice:**")
if emphasis == "equation_building":
    st.write("⭐ **Algebra 1 > B.4 - Write linear functions: word problems**")
    st.write("⭐ **Algebra 2 > A.1 - Domain and range of functions**")
elif emphasis == "key_features":
    st.write("⭐ **Algebra 1 > A.3 - Domain and range of functions**")
    st.write("⭐ **Algebra 1 > B.5 - Interpret the graph of a linear function**")
elif emphasis == "graphing":
    st.write("⭐ **Algebra 1 > A.5 - Graph a function**")
    st.write("⭐ **Algebra 1 > Q.3 - Graph quadratic functions**")
else:  # solving_equations
    st.write("⭐ **Algebra 1 > E.1 - Solve one-step linear equations**")
    st.write("⭐ **Algebra 1 > E.2 - Solve two-step linear equations**")

st.markdown("---")

# Outside Resources Section
st.header("🌐 Additional Learning Resources")

# Categorized external resources
resources = {
    "📺 Video Tutorials": [
        {
            "name": "Bernoulli's Principle Explained - Science in a Nutshell",
            "url": "https://www.youtube.com/watch?v=yYyI36zX-eU",
            "description": "An easy-to-understand explanation of the principle with simple demonstrations."
        },
        {
            "name": "Bernoulli Equation in Detail - Khan Academy",
            "url": "https://www.khanacademy.org/science/physics/fluids/fluid-dynamics/v/bernoullis-equation",
            "description": "A deep dive into the full Bernoulli equation and its components."
        },
        {
            "name": "How Planes Fly - The Bernoulli Principle",
            "url": "https://www.youtube.com/watch?v=kvGsIo1TmsM",
            "description": "A video that specifically visualizes the pressure difference over an airplane wing."
        }
    ],
    "💻 Interactive Tools": [
        {
            "name": "Desmos Graphing Calculator",
            "url": "https://www.desmos.com/calculator",
            "description": "Free online graphing tool to visualize the inverse relationship between speed and pressure."
        },
        {
            "name": "Wolfram Alpha",
            "url": "https://www.wolframalpha.com/",
            "description": "Computational engine for solving and analyzing the Bernoulli equation."
        }
    ],
    "📚 Study Guides & Practice": [
        {
            "name": "Paul's Online Math Notes",
            "url": "https://tutorial.math.lamar.edu/Classes/Alg/Equations.aspx",
            "description": "Comprehensive notes on solving algebraic equations."
        }
    ],
    "🕰️ History of Math & Science": [
        {
            "name": "Ancient Engineering: Water Management in the Nile",
            "url": "https://ancientengrtech.wisc.edu/ancient-egypt-water-engineering/#irrigation",
            "description": "Explore how early civilizations in Africa applied principles of fluid dynamics to build irrigation systems."
        }
    ],
    "🌐 Websites & Articles": [
        {
            "name": "PBS Learning Media: Fluid Dynamics",
            "url": "https://detroitpbs.pbslearningmedia.org/resource/npe11.sci.engin.design.fluidyn/fluid-dynamics/",
            "description": "An educational resource from Detroit PBS on the principles of fluid dynamics."
        },
        {
            "name": "FY Fluid Dynamics",
            "url": "https://fyfluiddynamics.com/",
            "description": "A comprehensive site for all things fluid dynamics, from fundamentals to advanced topics."
        }
    ]
}

# Display resources in organized tabs
resource_tabs = st.tabs(list(resources.keys()))

for i, (category, items) in enumerate(resources.items()):
    with resource_tabs[i]:
        for item in items:
            st.markdown(f"**[{item['name']}]({item['url']})**")
            st.write(f"📝 {item['description']}")
            st.write("---")

# Study Plan Generator
st.header("📅 Personalized Study Plan")
current_level = st.selectbox("What's your current comfort level with this topic?", [
    "Beginner - Just starting to learn",
    "Intermediate - Understand basics, need more practice",
    "Advanced - Ready for complex applications"
])

if st.button("Generate My Study Plan"):
    st.success("🎯 Your Personalized Study Plan:")
    if "Beginner" in current_level:
        st.markdown("""
        **Week 1-2: Foundation Building**
        - Watch the "Bernoulli's Principle Explained" video.
        - Use the interactive visualization above to get a feel for the relationship.
        - Complete IXL lessons on solving one-step equations.
        """)
    elif "Intermediate" in current_level:
        st.markdown("""
        **Week 1: Deeper Understanding**
        - Watch the Khan Academy video on the full Bernoulli equation.
        - Use Desmos to graph a more complex version of the speed-pressure relationship.
        - Focus on IXL lessons related to graphing and interpreting functions.
        """)
    else:  # Advanced
        st.markdown("""
        **Ongoing Challenge Plan:**
        - Explore the full Bernoulli equation with all its variables (height, density).
        - Research real-world engineering problems solved using the principle.
        - Use Wolfram Alpha to solve complex fluid dynamics problems.
        """)

st.markdown("---")
st.markdown(f"**🎯 Your Selected Focus:** {strand}")
st.markdown("**📍 Common Core Standards:** This lesson supports high school algebra and mathematical modeling practices.")
```
