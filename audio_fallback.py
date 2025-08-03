import streamlit as st
import speech_recognition as sr
import pyaudio
import wave
import tempfile
import os
from gtts import gTTS

class SimpleAudioRecorder:
    """Fallback audio recorder using pyaudio if streamlit-mic-recorder fails"""
    
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.chunk = 1024
        self.format = pyaudio.paInt16
        self.channels = 1
        self.rate = 44100
        
    def record_with_pyaudio(self, duration=5):
        """Record audio using pyaudio for specified duration"""
        try:
            p = pyaudio.PyAudio()
            
            stream = p.open(format=self.format,
                           channels=self.channels,
                           rate=self.rate,
                           input=True,
                           frames_per_buffer=self.chunk)
            
            st.info(f"🎤 Recording for {duration} seconds... Speak now!")
            
            frames = []
            for i in range(0, int(self.rate / self.chunk * duration)):
                data = stream.read(self.chunk)
                frames.append(data)
            
            stream.stop_stream()
            stream.close()
            p.terminate()
            
            # Save to temporary file
            with tempfile.NamedTemporaryFile(delete=False, suffix='.wav') as tmp_file:
                wf = wave.open(tmp_file.name, 'wb')
                wf.setnchannels(self.channels)
                wf.setsampwidth(p.get_sample_size(self.format))
                wf.setframerate(self.rate)
                wf.writeframes(b''.join(frames))
                wf.close()
                
                return tmp_file.name
                
        except Exception as e:
            st.error(f"Error recording audio: {e}")
            return None
    
    def audio_file_to_text(self, audio_file_path):
        """Convert audio file to text"""
        try:
            with sr.AudioFile(audio_file_path) as source:
                self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
                audio = self.recognizer.record(source)
                text = self.recognizer.recognize_google(audio, language='id-ID')
                
            # Clean up
            os.unlink(audio_file_path)
            return text
            
        except sr.UnknownValueError:
            st.error("Tidak dapat memahami audio. Silakan bicara lebih jelas.")
            if os.path.exists(audio_file_path):
                os.unlink(audio_file_path)
            return None
        except Exception as e:
            st.error(f"Error processing audio: {e}")
            if os.path.exists(audio_file_path):
                os.unlink(audio_file_path)
            return None

def show_manual_input_fallback():
    """Show manual text input as final fallback"""
    st.warning("⚠️ Audio recording tidak tersedia. Gunakan input teks manual:")
    
    with st.form("manual_input_form"):
        question = st.text_area(
            "Pertanyaan Sejarah", 
            placeholder="Contoh: Ceritakan tentang Perang Diponegoro di Yogyakarta dalam bahasa Indonesia",
            help="Ketik pertanyaan sejarah Anda di sini"
        )
        submit = st.form_submit_button("Tanyakan")
        
        if submit and question.strip():
            return question.strip()
    
    return None
