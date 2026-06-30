import streamlit as st

# Custom styling hook to make media layout blend perfectly with Dark Mode
st.markdown(
    """
    <style>
    .stVideo {
        border-radius: 10px;
        box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.3);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ─── SIDEBAR / MAIN VIDEO EMBED ───
st.sidebar.markdown("### 🔬 Laboratory Hardware Link")
st.sidebar.video(
    "lab_simulation.mp4", 
    format="video/mp4", 
    start_time=0,
    loop=True,
    autoplay=True,
    muted=True
)


import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import io

# Set browser tab configuration
st.set_page_config(page_title="2D Superconductor Analyzer", layout="wide", page_icon="🔬")

st.title("🔬 Micro-Engineered 2D Superconductor Analyzer Dashboard")
st.markdown("""
This application models the thermodynamic phase stability of the breakthrough **ultrathin cuprate superconductor films** grown on nanostructured templates. 
""")

# ==========================================
# 🎛️ SIDEBAR CONTROL PANEL
# ==========================================
st.sidebar.header("🎛️ Global Environment Controls")
live_j_load = st.sidebar.slider("Active Electric Current Load ($J$)", 0.0, 0.8, 0.20, 0.05)

st.sidebar.header("🤖 ML Classifier Tuning")
num_samples = st.sidebar.slider("Lab Sample Volume Size", 100, 1200, 600, 50)

st.sidebar.header("📈 Gradient Descent Target")
op_temp = st.sidebar.slider("Operating Temperature ($T / T_c$)", 0.05, 1.20, 0.40, 0.05)
ambient_b = st.sidebar.slider("Ambient Magnetic Field ($B$)", 0.00, 0.80, 0.15, 0.05)

# ==========================================
# 📊 DATA SIMULATION CORE
# ==========================================
T_range = np.linspace(0.01, 1.4, 100)
B_range = np.linspace(0.0, 1.0, 100)
T_mesh, B_mesh = np.meshgrid(T_range, B_range)

dx = (1.4 - 0.01) / 100
dy = (1.0 - 0.0) / 100

curr_supp_base = live_j_load ** 2
curr_supp_eng = curr_supp_base * 0.70

Z_base = np.clip(1.0 - T_mesh - B_mesh - curr_supp_base, 0, None)
Z_eng = np.clip(1.15 - (T_mesh / 1.15) - (B_mesh * 0.5) - curr_supp_eng, 0, None)

vol_base = np.sum(Z_base) * dx * dy
vol_eng = np.sum(Z_eng) * dx * dy

# ==========================================
# 🏛️ TABS LAYOUT FOR USER INTERFACE
# ==========================================
tab1, tab2, tab3 = st.tabs(["📊 3D Phase Mapping & Data Export", "🤖 AI Phase Classifier", "📈 Gradient Descent Optimizer"])

# ------------------------------------------
# TAB 1: 3D SURFACE & CSV GENERATOR
# ------------------------------------------
with tab1:
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("3D Phase Profile Map")
        fig1 = plt.figure(figsize=(10, 6))
        ax1 = fig1.add_subplot(111, projection='3d')
        
        ax1.plot_surface(T_mesh, B_mesh, Z_base, color='red', alpha=0.15, linewidth=0, antialiased=True)
        surf = ax1.plot_surface(T_mesh, B_mesh, Z_eng, cmap='plasma', alpha=0.65, linewidth=0, antialiased=True)
        
        ax1.set_xlabel('Normalized Temp ($T / T_c$)')
        ax1.set_ylabel('Magnetic Field ($B$)')
        ax1.set_zlabel('Cooper Pair Density ($|\\psi|^2$)')
        ax1.view_init(elev=22, azim=38)
        
        fake_base = plt.Rectangle((0,0),1,1,fc="red", alpha=0.25)
        fake_eng = plt.Rectangle((0,0),1,1,fc="#bc3754", alpha=0.7)
        ax1.legend([fake_base, fake_eng], ['Standard Thin Film Baseline', 'Nanostructured Substrate Film'], loc='upper right')
        st.pyplot(fig1)

    with col2:
        st.subheader("📊 Live Volumetric Analytics")
        st.metric(label="Standard Thin Film Volume", value=f"{vol_base:.4f} units³")
        st.metric(label="Nanostructured Film Volume", value=f"{vol_eng:.4f} units³")
        
        if vol_base > 0:
            gain = ((vol_eng - vol_base) / vol_base) * 100
            st.success(f"🚀 Stability Window Expanded by **{gain:.1f}%**")
        else:
            st.error("⚠️ CRITICAL COLLAPSE: Standard baseline circuit has failed completely!")

        # Automated CSV Generator
        st.subheader("💾 Export Laboratory Sweep Data")
        current_sweep = np.linspace(0.0, 0.8, 10)
        sweep_records = []
        for J in current_sweep:
            zb = np.clip(1.0 - T_mesh - B_mesh - (J**2), 0, None)
            ze = np.clip(1.15 - (T_mesh / 1.15) - (B_mesh * 0.5) - ((J**2)*0.70), 0, None)
            vb = np.sum(zb) * dx * dy
            ve = np.sum(ze) * dx * dy
            sweep_records.append({
                "current_load_J": round(J, 2),
                "standard_film_volume": round(vb, 4),
                "nanostructured_film_volume": round(ve, 4),
                "stability_advantage": f"+{((ve-vb)/vb)*100:.1f}%" if vb > 0 else "COLLAPSED"
            })
        df_export = pd.DataFrame(sweep_records)
        
        # Streamlit Native Download Button
        csv = df_export.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📥 Download Data Spreadsheet (CSV)",
            data=csv,
            file_name="superconductor_stress_analysis.csv",
            mime="text/csv"
        )

# ------------------------------------------
# TAB 2: AI PHASING K-MEANS ENGINE
# ------------------------------------------
with tab2:
    st.subheader("🤖 Unsupervised Machine Learning Profiler")
    np.random.seed(42)
    T_sim = np.random.uniform(0.05, 1.4, num_samples)
    B_sim = np.random.uniform(0.0, 1.0, num_samples)
    J_sim = np.random.uniform(0.0, 0.8, num_samples)
    
    psi_squared = np.clip(1.15 - (T_sim / 1.15) - (B_sim * 0.5) - ((J_sim**2)*0.70), 0, None)
    data_matrix = np.column_stack((T_sim, B_sim, J_sim, psi_squared))
    
    scaled_features = StandardScaler().fit_transform(data_matrix)
    kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
    cluster_labels = kmeans.fit_predict(scaled_features)
    
    cluster_means = [data_matrix[cluster_labels == i, 3].mean() for i in range(3)]
    sorted_indices = np.argsort(cluster_means)
    label_mapping = {sorted_indices[0]: 0, sorted_indices[1]: 1, sorted_indices[2]: 2}
    final_labels = np.array([label_mapping[label] for label in cluster_labels])
    
    fig2 = plt.figure(figsize=(10, 5.5))
    ax2 = fig2.add_subplot(111, projection='3d')
    colors = {0: '#ff4d4d', 1: '#ffd11a', 2: '#2ecc71'}
    labels_text = {0: 'Critical Phase Collapse', 1: 'Marginal Stability Zone', 2: 'Optimal Performance'}
    
    for i in range(3):
        mask = (final_labels == i)
        ax2.scatter(T_sim[mask], B_sim[mask], J_sim[mask], c=colors[i], label=labels_text[i], alpha=0.6, s=25)
        
    ax2.set_xlabel('Temperature ($T / T_c$)')
    ax2.set_ylabel('Magnetic Field ($B$)')
    ax2.set_zlabel('Current ($J$)')
    ax2.view_init(elev=25, azim=135)
    ax2.legend()
    st.pyplot(fig2)

# ------------------------------------------
# TAB 3: GRADIENT DESCENT SYSTEM OPTIMIZER
# ------------------------------------------
with tab3:
    st.subheader("📈 Real-Time Threshold Tracking Optimization")
    j_history = []
    psi_history = []
    J_current = 0.01
    
    for i in range(40):
        suppression = (J_current ** 2) * 0.70
        psi_sq = 1.15 - (op_temp / 1.15) - (ambient_b * 0.5) - suppression
        j_history.append(J_current)
        psi_history.append(np.clip(psi_sq, 0, None))
        
        if psi_sq <= 0.01:
            break
        gradient_step = 0.05 * psi_sq
        J_current = J_current + (0.1 * gradient_step)
        if J_current > 1.5:
            J_current = 1.5
            break

    J_max = j_history[-1]
    
    col_opt1, col_opt2 = st.columns([2, 1])
    with col_opt1:
        fig3, ax3 = plt.subplots(figsize=(8, 4.5))
        ax3.plot(range(len(j_history)), j_history, 'b-o', linewidth=2, label=r'Current Load ($J$)')
        ax3.plot(range(len(psi_history)), psi_history, 'g--s', linewidth=1.5, label=r'Quantum Density ($|\psi|^2$)')
        ax3.set_xlabel('Optimization Iteration Steps')
        ax3.set_ylabel('Normalized Scale Value')
        ax3.grid(True, linestyle='--', alpha=0.5)
        ax3.legend()
        st.pyplot(fig3)
        
    with col_opt2:
        st.info("### 📈 Optimization Extraction Logs")
        st.markdown(f"**Target Temperature:** `{op_temp:.2f} T/Tc`")
        st.markdown(f"**Target Magnetic Field:** `{ambient_b:.2f} B`")
        st.markdown(f"💥 **Calculated $J_{{max}}$ Threshold:** `{J_max:.3f}`")
        st.warning(f"🔒 **Safe Operating Circuit Layout Ceiling (20% Buffer):** `{J_max*0.8:.3f} J`")
