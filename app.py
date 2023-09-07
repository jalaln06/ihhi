# Импортируем необходимые библиотеки
import streamlit as st
import speech_recognition as sr

    

# Основная функция приложения
def main():
    st.title("Аудио в текст")
    uploaded_file = st.file_uploader("Загрузите ваш аудиофайл", type=["wav"])

    # Если файл был загружен
    if uploaded_file is not None:
        with st.spinner('Преобразование аудио в текст...'):
            # Используем библиотеку speech_recognition для распознавания речи
            r = sr.Recognizer()
            with sr.AudioFile(uploaded_file) as source:
                audio_data = r.record(source)
                try:
                    text = r.recognize_google(audio_data, language='ru-RU')
                    st.write(f"Распознанный текст: {text}")
                except sr.UnknownValueError:
                    st.write("Google Speech Recognition не смог распознать аудио")
                except sr.RequestError:
                    st.write("Не удалось запросить результаты из Google Speech Recognition")

if __name__ == "__main__":
    main()
