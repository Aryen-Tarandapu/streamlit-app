import streamlit as st
# Judul Aplikasi
st.title("Kelompok 5")
# Menampilkan daftar nama anggota kelompok
st.subheader("Daftar Anggota Kelompok 5:")
nama_kelompok = [
    "1. Veri",
    "2. Aryen",
    "3. Rizal",
]
for nama in nama_kelompok:
    st.write(nama)
# Input nama
user_input = st.text_input("Masukkan Nama Anda:")
# Input tambahan untuk hobi, warna favorit, dan studi
user_hobby = st.text_input("Apa hobi Anda?")
favorite_color = st.color_picker("Pilih warna favorit Anda:")
user_study = st.text_input("Apa bidang studi Anda?")
# Menampilkan data yang diinput pengguna
if user_input:
    st.write(f"Hallo, {user_input}! Selamat datang di website ini.")
    if user_hobby:
        st.write(f"Hobi Anda adalah {user_hobby}.")
    if favorite_color:
        st.write(f"Warna favorit Anda adalah {favorite_color}.")
    if user_study:
        st.write(f"Anda sedang belajar di bidang {user_study}.")