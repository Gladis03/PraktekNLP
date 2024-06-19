import streamlit as st
import datetime

# Fungsi untuk mengatur pesan chatbot
def chatbot_response(option):
    response = ""
    if option in ["Pesan Tiket Kapal", "Pesan Tiket Kereta", "Pesan Tiket Pesawat"]:
        response = f"Tentu! Untuk memesan {option.lower()}, silakan masukkan detail perjalanan Anda."
    elif option == "Terima Kasih":
        response = "Sama-sama! Senang bisa membantu."
    else:
        response = "Maaf, saya tidak mengerti. Bisa Anda ulangi?"

    return response

# Fungsi utama aplikasi
def main():
    st.title("Chatbot Pemesanan Tiket")
    st.write("Selamat datang di layanan pemesanan tiket. Silakan pilih opsi untuk memulai!")

    # Simpan riwayat percakapan
    if 'conversation' not in st.session_state:
        st.session_state['conversation'] = []

    options = ["Pesan Tiket Kapal", "Pesan Tiket Kereta", "Pesan Tiket Pesawat"]
    option = st.selectbox("Pilih opsi:", options)

    if st.button("Kirim"):
        st.session_state['conversation'].append({"role": "user", "text": option})
        response = chatbot_response(option)
        st.session_state['conversation'].append({"role": "bot", "text": response})

    # Tampilkan riwayat percakapan
    for chat in st.session_state['conversation']:
        if chat['role'] == 'user':
            st.write(f"**Anda:** {chat['text']}")
        else:
            st.write(f"**Bot:** {chat['text']}")

    # Form untuk pemesanan tiket
    if any(option in chat['text'] for chat in st.session_state['conversation']):
        st.subheader("Formulir Pemesanan Tiket")
        with st.form(key='booking_form'):
            name = st.text_input("Nama Lengkap")
            email = st.text_input("Email")
            origin = st.text_input("Berangkat dari")
            destination = st.text_input("Tujuan ke")
            departure_date = st.date_input("Tanggal Keberangkatan", datetime.date.today())
            return_date = st.date_input("Tanggal Kembali", datetime.date.today())
            submit_button = st.form_submit_button(label='Pesan Tiket')

            if submit_button:
                st.success(f"Tiket berhasil dipesan untuk {name} dari {origin} ke {destination} pada tanggal {departure_date}.")

if __name__ == "__main__":
    main()
