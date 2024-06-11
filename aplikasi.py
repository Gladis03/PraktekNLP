import streamlit as st
import datetime

# Fungsi untuk mengatur pesan chatbot
def chatbot_response(user_input):
    response = ""
    if "halo" in user_input.lower() or "hai" in user_input.lower():
        response = "Halo! Ada yang bisa saya bantu?"
    elif "pesan tiket" in user_input.lower():
        response = "Tentu! Untuk memesan tiket, silakan masukkan detail penerbangan Anda."
    elif "terima kasih" in user_input.lower():
        response = "Sama-sama! Senang bisa membantu."
    else:
        response = "Maaf, saya tidak mengerti. Bisa Anda ulangi?"

    return response

# Fungsi utama aplikasi
def main():
    st.title("Chatbot Pemesanan Tiket Pesawat")
    st.write("Selamat datang di layanan pemesanan tiket pesawat. Silakan bertanya untuk memulai!")

    # Simpan riwayat percakapan
    if 'conversation' not in st.session_state:
        st.session_state['conversation'] = []

    user_input = st.text_input("Anda: ")

    if st.button("Kirim"):
        if user_input:
            st.session_state['conversation'].append({"role": "user", "text": user_input})
            response = chatbot_response(user_input)
            st.session_state['conversation'].append({"role": "bot", "text": response})

    # Tampilkan riwayat percakapan
    for chat in st.session_state['conversation']:
        if chat['role'] == 'user':
            st.write(f"**Anda:** {chat['text']}")
        else:
            st.write(f"**Bot:** {chat['text']}")

    # Form untuk pemesanan tiket
    st.subheader("Formulir Pemesanan Tiket")
    with st.form(key='booking_form'):
        name = st.text_input("Nama Lengkap")
        email = st.text_input("Email")
        origin = st.text_input("Kota Asal")
        destination = st.text_input("Kota Tujuan")
        departure_date = st.date_input("Tanggal Keberangkatan", datetime.date.today())
        return_date = st.date_input("Tanggal Kembali", datetime.date.today())
        submit_button = st.form_submit_button(label='Pesan Tiket')

        if submit_button:
            st.success(f"Tiket berhasil dipesan untuk {name} dari {origin} ke {destination} pada tanggal {departure_date}.")

if __name__ == "__main__":
    main()
