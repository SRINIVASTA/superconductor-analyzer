# 🔬 Micro-Engineered 2D Superconductor Analyzer Dashboard

An interactive, data-driven Streamlit dashboard designed to model and simulate the thermodynamic phase stability of ultrathin cuprate superconductor films grown on nanostructured templates. This project bridges quantum mechanics concepts with unsupervised machine learning and gradient descent optimization.

🚀 **[Click Here to Access the Live Streamlit Web Application](https://superconductor-analyzer-esmz7ncxvvohx89d8bvwlo.streamlit.app/)**

---

## ✍️ Author & Credits

This application was engineered and developed by **Srinivasta**. 

The core software architecture, data simulation layers, and predictive models were built by translating the groundbreaking, real-world scientific discoveries of the following pioneering institutions and researchers:

*   **Aalto University & The SuperC Consortium** (Pioneered by **Professor Päivi Törmä**): Utilizing AI models to pre-screen billions of material combinations and leveraging "Kagome lattices" geometry to maximize electron flat band stability.
*   **RISE Research Institutes of Sweden:** Driving advanced Nordic nanostructured technology research and ecosystem scaling.
*   **Rice University** (Led by **Professor Emilia Morosan**): Physically synthesizing structural compounds like $YRu_3B_2$ on nano-textured substrate templates.

---

## 🚀 Key Features

The application is structured into three highly functional analytical modules:

*   **📊 3D Phase Mapping & Data Export (Tab 1):** Renders dynamic 3D surface maps comparing Cooper Pair Density ($|\psi|^2$) across standard thin-film baselines and nanostructured substrate films. Includes a live automated laboratory stress data spreadsheet (CSV) generator.
*   **🤖 AI Phase Classifier (Tab 2):** Utilizes `scikit-learn` to run an unsupervised `KMeans` clustering pipeline on simulated lab samples, sorting data points into operational phases (*Critical Phase Collapse*, *Marginal Stability*, *Optimal Performance*).
*   **📈 Gradient Descent Optimizer (Tab 3):** Tracks real-time threshold limits, executing step-by-step optimization logic to calculate maximum current load capacities ($J_{max}$) with integrated safe operating limits.

---

## 🎨 Tech Stack

*   **Frontend UI:** Streamlit
*   **Data Processing:** NumPy, Pandas
*   **Machine Learning:** Scikit-Learn (KMeans, StandardScaler)
*   **Data Visualization:** Matplotlib (3D Projection Engine)

---

## 💡 Developer's Note & Call for Guidance

> [!NOTE]
> This application is a software-driven structural model created for interactive simulation and visualization purposes. 
> 
> **To the research community:** If you notice any oversimplifications or anomalies in the thermodynamic phase formulas or the gradient descent threshold parameters, please open an issue or reach out! I deeply welcome expert feedback and guidance to refine the physics engine and enhance modeling accuracy.

---

## 🛠️ Quick Start & Installation

### 1. Clone the Repository
```bash
git clone https://github.com
cd superconductor-analyzer-dashboard
```

### 2. Install Dependencies
Ensure you have Python 3.8+ installed, then run:
```bash
pip install streamlit numpy pandas matplotlib scikit-learn
```

### 3. Run the Dashboard Local Server
```bash
streamlit run app.py
```

---

## 📄 License
This project is open-source and available under the [MIT License](LICENSE).
