import streamlit as st
import pandas as pd
import pickle
import numpy as np

# Judul Aplikasi
st.title('Prediksi Tingkat Obesitas')

# Deskripsi
st.write('Aplikasi ini dapat memprediksi tingkat obesitas seseorang berdasarkan fitur-fitur tertentu.')

# Load model dan scaler yang sudah disimpan
with open('best_rf_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('scaler.pkl', 'rb') as scaler_file:
    scaler = pickle.load(scaler_file)

# Fungsi untuk melakukan prediksi
def predict_obesity(age, height, weight, fcvc, ncp, ch2o, faf, tue):

    # Normalisasi fitur
    input_data = scaler.transform([[age, height, weight, fcvc, ncp, ch2o, faf, tue]])
    
    prediction = model.predict(input_data)[0]

    # Menentukan nama tingkat obesitas
    obesitas_names = {
        0: "Insufficient Weight",
        1: "Normal Weight",
        2: "Overweight Level I",
        3: "Overweight Level II",
        4: "Obesity Type I",
        5: "Obesity Type II",
        6: "Obesity Type III"
    }

    obesitas_name = obesitas_names.get(prediction, "Tingkat Obesitas Tidak Diketahui")
    return prediction, obesitas_name

# Tampilan untuk berpindah antara profil, informasi obesitas, dan prediksi
selected_page = st.radio("Pilih Halaman:", ("Profile", "Informasi Obesitas", "Kalkulator"))

# Halaman Profil
if selected_page == "Profile":
    st.write("Ini adalah halaman profil.")
    st.subheader("Profil Mahasiswa:")
    st.write("Nama: Ari Bagus Firmansyah")
    st.write("NIM: 210411100084")
    st.write("Kelas: PSD B")

# Halaman Informasi Obesitas
if selected_page == "Informasi Obesitas":
    st.write("Ini adalah halaman informasi tentang tingkat obesitas.")

    # Tingkat Obesitas: Insufficient Weight (Kurang Berat Badan)
    st.subheader("Tingkat Obesitas: Insufficient Weight")
    st.write("Penjelasan: Anda memiliki berat badan kurang dari normal.")
    st.write("Risiko: Risiko kesehatan dapat termasuk kerentanan terhadap infeksi, gangguan pertumbuhan, dan kelemahan umum.")
    st.write("Solusi: Konsultasikan dengan dokter atau ahli gizi untuk perencanaan diet yang sehat.")
    st.write("Tips: Pertahankan pola makan yang sehat dan konsumsi makanan bernutrisi.")
    
    # Tingkat Obesitas: Normal Weight (Berat Badan Normal)
    st.subheader("Tingkat Obesitas: Normal Weight")
    st.write("Penjelasan: Berat badan Anda normal untuk tinggi badan Anda.")
    st.write("Risiko: Risiko kesehatan biasanya rendah dalam kategori ini.")
    st.write("Solusi: Pertahankan pola makan sehat dan aktivitas fisik yang konsisten.")
    st.write("Tips: Tetap aktif dan konsumsi makanan seimbang.")

    # Tingkat Obesitas: Overweight Level I (Kegemukan Tingkat I)
    st.subheader("Tingkat Obesitas: Overweight Level I")
    st.write("Penjelasan: Anda memiliki overweight tingkat I.")
    st.write("Risiko: Risiko kesehatan dapat termasuk peningkatan risiko penyakit jantung dan diabetes.")
    st.write("Solusi: Pertimbangkan diet seimbang dan rutin berolahraga.")
    st.write("Tips: Batasi makanan tinggi lemak dan gula.")

    # Tingkat Obesitas: Overweight Level II (Kegemukan Tingkat II)
    st.subheader("Tingkat Obesitas: Overweight Level II")
    st.write("Penjelasan: Anda memiliki overweight tingkat II.")
    st.write("Risiko: Risiko kesehatan yang lebih tinggi, termasuk penyakit jantung dan diabetes.")
    st.write("Solusi: Konsultasikan dengan dokter atau ahli gizi untuk perencanaan diet yang ketat dan aktifitas fisik.")
    st.write("Tips: Rutin olahraga dan pilih makanan rendah kalori.")

    # Tingkat Obesitas: Obesity Type I (Obesitas Tipe I)
    st.subheader("Tingkat Obesitas: Obesity Type I")
    st.write("Penjelasan: Anda mengalami obesitas tipe I.")
    st.write("Risiko: Risiko kesehatan yang signifikan, termasuk penyakit jantung, diabetes, dan tekanan darah tinggi.")
    st.write("Solusi: Konsultasikan dengan dokter atau ahli gizi untuk pengelolaan berat badan dan perubahan gaya hidup.")
    st.write("Tips: Kurangi porsi makan dan perbanyak aktivitas fisik.")

    # Tingkat Obesitas: Obesity Type II (Obesitas Tipe II)
    st.subheader("Tingkat Obesitas: Obesity Type II ")
    st.write("Penjelasan: Anda mengalami obesitas tipe II.")
    st.write("Risiko: Risiko kesehatan yang tinggi, termasuk penyakit jantung, diabetes, dan gangguan pernapasan.")
    st.write("Solusi: Konsultasikan dengan dokter untuk perawatan medis dan pengelolaan berat badan yang ketat.")
    st.write("Tips: Periksa kesehatan secara berkala dan konsultasikan dengan ahli gizi.")

    # Tingkat Obesitas: Obesity Type III (Obesitas Tipe III)
    st.subheader("Tingkat Obesitas: Obesity Type III")
    st.write("Penjelasan: Anda mengalami obesitas tipe III (obesitas morbid).")
    st.write("Risiko: Risiko kesehatan yang sangat tinggi, termasuk risiko kematian dini.")
    st.write("Solusi: Konsultasikan dengan dokter segera untuk perawatan medis yang mendalam dan perubahan gaya hidup yang signifikan.")
    st.write("Tips: Dukungan medis dan dukungan sosial dapat sangat penting.")

# Halaman Kalkulator
if selected_page == "Kalkulator":
    st.write("Ini adalah halaman kalkulator.")

    selected_calculator = st.radio("Pilih Kalkulator:", ("Hitung nilai NCP", "Hitung nilai FCVC"))

    if selected_calculator == "Hitung nilai NCP":
        st.write("Kalkulator untuk menghitung nilai NCP (Frekuensi Makan Buah).")
        # Fungsi untuk mengonversi pilihan skala ke nilai numerik
        def skala_ke_nilai(skala):
            if skala == "Tidak Pernah":
                return 0
            elif skala == "Kadang-kadang":
                return 1
            elif skala == "Sering":
                return 2
            elif skala == "Selalu":
                return 3
            else:
                return 0  # Nilai default jika input tidak valid

        def main():
            st.subheader("Kalkulator Nilai NCP")

            # Membuat input field untuk pengguna memilih skala FCVC
            skala_pengguna = st.selectbox("Pilih Skala NCP:", ["Tidak Pernah", "Kadang-kadang", "Sering", "Selalu"])

            # Mengonversi pilihan skala ke nilai numerik
            nilai_ncp = skala_ke_nilai(skala_pengguna)

            # Menampilkan hasil
            st.subheader("Hasil Perhitungan:")
            st.write(f"Nilai frekuensi makan buah yang dihitung: {nilai_ncp}")

        if __name__ == "__main__":
            main()

    elif selected_calculator == "Hitung nilai FCVC":
        st.write("Kalkulator untuk menghitung nilai FCVC (Frekuensi Makan Sayur).")
        # Fungsi untuk mengonversi pilihan skala ke nilai numerik
        def skala_ke_nilai(skala):
            if skala == "Tidak Pernah":
                return 0
            elif skala == "Kadang-kadang":
                return 1
            elif skala == "Sering":
                return 2
            elif skala == "Selalu":
                return 3
            else:
                return 0  # Nilai default jika input tidak valid

        def main():
            st.subheader("Kalkulator Nilai FCVC")

            # Membuat input field untuk pengguna memilih skala FCVC
            skala_pengguna = st.selectbox("Pilih Skala FCVC:", ["Tidak Pernah", "Kadang-kadang", "Sering", "Selalu"])

            # Mengonversi pilihan skala ke nilai numerik
            nilai_fcvc = skala_ke_nilai(skala_pengguna)

            # Menampilkan hasil
            st.subheader("Hasil Perhitungan:")
            st.write(f"Nilai frekuensi makan sayur yang dihitung: {nilai_fcvc}")

        if __name__ == "__main__":
            main()

# # Halaman Prediksi
# # if selected_page == "Prediksi":
st.sidebar.title('Masukkan Data Pasien')
age = st.sidebar.number_input('Usia', min_value=0)
height = st.sidebar.number_input('Tinggi (cm)', min_value=0)
weight = st.sidebar.number_input('Berat (kg)', min_value=0)
ncp = st.sidebar.number_input('Frekuensi Makan Buah [NCP]', min_value=0.0)
fcvc = st.sidebar.number_input('Frekuensi Makan Sayuran [FCVC]', min_value=0.0)
ch2o = st.sidebar.number_input('Konsumsi Air (L)', min_value=0.0)
faf = st.sidebar.number_input('Aktivitas Fisik (jam per hari)', min_value=0.0)
tue = st.sidebar.number_input('Waktu Layar (jam per hari)', min_value=0.0)

# Tombol untuk prediksi
if st.sidebar.button('Prediksi'):
    prediction = predict_obesity(age, height, weight, fcvc, ncp, ch2o, faf, tue)
    # Membuat mapping dari nilai prediksi ke tingkat obesitas
    obesitas_mapping = {
        0: "Insufficient Weight",
        1: "Normal Weight",
        2: "Overweight Level I",
        3: "Overweight Level II",
        4: "Obesity Type I",
        5: "Obesity Type II",
        6: "Obesity Type III"
    }
# Menghindari KeyError dengan memberikan nilai default "Tingkat Obesitas Tidak Dikenal"
    obesitas_prediction = obesitas_mapping.get(prediction, "")

# Hasil Prediksi
if 'prediction' in locals():
    st.title(f'Hasil Prediksi:')
    st.title(f'{prediction} - {obesitas_prediction}')
