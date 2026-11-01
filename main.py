import streamlit as st
from checker import analyze_password
from crypto_utils import generate_hash, encrypt_message, decrypt_message

st.set_page_config(page_title="KeyGuard - Security Suite", page_icon="🔐")

st.title("🔐 KeyGuard: AI & Security Suite")
st.caption("İstinye Üniversitesi - Açık Kaynak İşletim Sistemleri Vize Projesi")

tab1, tab2 = st.tabs(["🛡️ Parola Analizi", "🔒 Metin Şifreleme (AES)"])

with tab1:
    st.header("Parola Güvenlik Analizi")
    pwd = st.text_input("Analiz edilecek parolayı girin:", type="password")
    
    if st.button("Analiz Et"):
        score, feedback = analyze_password(pwd)
        st.write(f"**Güvenlik Skoru:** %{score}")
        st.progress(score / 100)
        
        if score == 100:
            st.success("Harika! Parolanız son derece güçlü.")
        else:
            st.warning("Öneriler:")
            for f in feedback:
                st.write(f"- {f}")

with tab2:
    st.header("AES-256 Metin Şifreleme & Çözme")
    msg = st.text_area("Gizli Mesaj:")
    key = st.text_input("Gizli Anahtar (Passphrase):", type="password")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Şifrele"):
            if msg and key:
                enc = encrypt_message(msg, key)
                st.code(enc, language="text")
                st.info(f"SHA-256 Hash: {generate_hash(msg)}")
            else:
                st.error("Lütfen mesaj ve anahtar girin.")
    with col2:
        if st.button("Çöz"):
            if msg and key:
                dec = decrypt_message(msg, key)
                st.success(f"Çözülen Mesaj: {dec}")