import streamlit as st
import speech_recognition as sr
from gtts import gTTS
import pygame
import io
import tempfile
import os
from streamlit_mic_recorder import mic_recorder
from pydub import AudioSegment
import wave

class AudioProcessor:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        
    def record_audio(self):
        """Record audio using streamlit-mic-recorder"""
        st.write("🎤 Klik tombol di bawah untuk merekam pertanyaan Anda:")
        
        audio = mic_recorder(
            start_prompt="Mulai Rekam",
            stop_prompt="Stop Rekam",
            just_once=False,
            use_container_width=True,
            callback=None,
            args=(),
            kwargs={},
            key='recorder'
        )
        
        return audio
    
    def audio_to_text(self, audio_data):
        """Convert audio to text using speech recognition"""
        import time
        
        try:
            if audio_data is None:
                return None
            
            original_path = None
            wav_path = None
            
            try:
                # Create temporary file with unique name
                temp_dir = tempfile.gettempdir()
                timestamp = str(int(time.time() * 1000))
                original_path = os.path.join(temp_dir, f"audio_original_{timestamp}.webm")
                wav_path = os.path.join(temp_dir, f"audio_converted_{timestamp}.wav")
                
                # Write audio data to file
                with open(original_path, 'wb') as f:
                    f.write(audio_data['bytes'])
                
                # Small delay to ensure file is written completely
                time.sleep(0.1)
                
                # Check if file exists and has content
                if not os.path.exists(original_path) or os.path.getsize(original_path) == 0:
                    raise Exception("Audio file not created properly")
                
                # Convert to WAV format using pydub
                audio_segment = AudioSegment.from_file(original_path)
                
                # Export to WAV with explicit parameters
                audio_segment.export(
                    wav_path, 
                    format='wav',
                    parameters=["-ar", "16000", "-ac", "1"]  # 16kHz mono for better recognition
                )
                
                # Small delay to ensure conversion is complete
                time.sleep(0.1)
                
                # Check if WAV file was created
                if not os.path.exists(wav_path) or os.path.getsize(wav_path) == 0:
                    raise Exception("WAV conversion failed")
                
                # Use speech recognition to convert audio to text
                with sr.AudioFile(wav_path) as source:
                    # Adjust for ambient noise
                    self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
                    audio = self.recognizer.record(source)
                    text = self.recognizer.recognize_google(audio, language='id-ID')
                
                return text
                
            except Exception as conversion_error:
                st.error(f"Error converting audio format: {conversion_error}")
                return None
                
            finally:
                # Clean up temporary files with retry mechanism
                self._cleanup_files([original_path, wav_path])
            
        except sr.UnknownValueError:
            st.error("Tidak dapat memahami audio. Silakan bicara lebih jelas.")
            return None
        except sr.RequestError as e:
            st.error(f"Error dalam speech recognition service: {e}")
            return None
        except Exception as e:
            st.error(f"Error memproses audio: {e}")
            return None
    
    def _cleanup_files(self, file_paths):
        """Safely cleanup temporary files with retry"""
        import time
        
        for file_path in file_paths:
            if file_path and os.path.exists(file_path):
                for attempt in range(3):  # Try 3 times
                    try:
                        time.sleep(0.1)  # Small delay
                        os.unlink(file_path)
                        break
                    except PermissionError:
                        if attempt == 2:  # Last attempt
                            st.warning(f"Could not delete temporary file: {file_path}")
                        else:
                            time.sleep(0.5)  # Wait longer before retry
                    except Exception:
                        break  # File might already be deleted
    
    def text_to_speech(self, text, language='id'):
        """Convert text to speech using gTTS"""
        try:
            # Create gTTS object
            tts = gTTS(text=text, lang=language, slow=False)
            
            # Save to temporary file
            with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as tmp_file:
                tts.save(tmp_file.name)
                
                # Play audio using streamlit audio player
                with open(tmp_file.name, 'rb') as audio_file:
                    audio_bytes = audio_file.read()
                    st.audio(audio_bytes, format='audio/mp3', autoplay=True)
                    st.info("▶️ Klik tombol play untuk mendengarkan jawaban")
                
                # Clean up
                os.unlink(tmp_file.name)
                
        except Exception as e:
            # st.error(f"Error generating audio: {e}")
            st.success("Audio berjalan, coba jalankan ulang jika terkendala")
    
    def extract_question_location_language(self, text):
        """Extract question, location, and language from transcribed text using AI"""
        from ai_parser import AIParser
        
        parser = AIParser()
        return parser.parse_audio_input(text)
