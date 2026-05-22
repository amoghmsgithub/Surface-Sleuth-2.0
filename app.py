import streamlit as st
import tempfile
import os
from main import build_database, match_fingerprint

st.set_page_config(page_title="Surface Sleuth 2.0", layout="centered")

st.title("🔍 Surface Sleuth 2.0")
st.subheader("Forensic Fingerprint Matching System")

# -----------------------------
# BUILD DATABASE SECTION
# -----------------------------
st.markdown("### 🔐 Step 1: Build Fingerprint Database")

if st.button("🔐 Build Encrypted Fingerprint Database"):
    msg = build_database()
    st.success(msg)

st.divider()

# -----------------------------
# UPLOAD TEST IMAGE
# -----------------------------
st.markdown("### 📤 Step 2: Upload Test Fingerprint")

uploaded_file = st.file_uploader(
    "Upload Fingerprint (Laser / Latent / Clean)",
    type=["jpg", "png", "jpeg"]
)

if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded Test Fingerprint", use_container_width=True)

    # Save uploaded file temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp:
        tmp.write(uploaded_file.read())
        temp_path = tmp.name

    st.divider()

    # -----------------------------
    # MATCH BUTTON
    # -----------------------------
    if st.button("🚀 Match Fingerprint"):
        with st.spinner("Matching fingerprint..."):
            results = match_fingerprint(temp_path)

        st.divider()

        # -----------------------------
        # RESULTS DISPLAY
        # -----------------------------
        if results:
            st.subheader("🔎 Matching Results")

            for name, score in results[:5]:
                if score > 70:
                    st.success(f"✅ {name} → {score:.2f}% match")
                elif score > 50:
                    st.warning(f"⚠️ {name} → {score:.2f}% (Possible match)")
                else:
                    st.error(f"❌ {name} → {score:.2f}% (Low match)")

            # Best match
            best_match, best_score = results[0]

            st.markdown("### 🏆 Best Match")
            st.info(f"**{best_match}** with confidence **{best_score:.2f}%**")

        else:
            st.error("❌ No matches found.\n\n👉 Please:\n- Build database first\n- Add training images\n- Try a clearer fingerprint")

        # Cleanup temp file
        os.remove(temp_path)

# -----------------------------
# FOOTER
# -----------------------------
st.divider()
st.caption("Surface Sleuth 2.0 • Hybrid Fingerprint Matching • Secure & Intelligent")