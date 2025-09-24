import streamlit as st
from static import Static
from crews import Crews
from audio_utils import AudioProcessor
# from audio_fallback import SimpleAudioRecorder, show_manual_input_fallback

def main():
    
    Static.config()
    Static.styling()
    Static.logo('gema.png')
    Static.title('HISTORIAN GPT')
    
    # Initialize audio processor
    audio_processor = AudioProcessor()
    
    st.markdown("### 🎤 Tanyakan pertanyaan sejarah dengan suara Anda!")
    st.markdown("**Contoh:** *Ceritakan tentang Perang Diponegoro di Yogyakarta dalam bahasa Indonesia*")
    
    # Audio recording section with fallbacks
    transcribed_text = None
    
    # Try streamlit-mic-recorder first
    try:
        audio_data = audio_processor.record_audio()
        
        if audio_data is not None:
            st.success("Audio berhasil direkam!")
            
            # Convert audio to text
            with st.spinner("Memproses audio..."):
                transcribed_text = audio_processor.audio_to_text(audio_data)
                
    except Exception as e:
        st.warning(f"Mic recorder error: {e}")
        audio_data = None
    
    # Fallback 1: PyAudio recorder
    # if audio_data is None and transcribed_text is None:
    #     st.markdown("---")
    #     st.markdown("### 🎙️ Alternatif: Recording dengan durasi tetap")
        
    #     col1, col2 = st.columns([1, 1])
    #     with col1:
    #         duration = st.selectbox("Durasi recording (detik):", [3, 5, 10], index=1)
    #     with col2:
    #         if st.button("🎤 Record Audio", type="primary"):
    #             fallback_recorder = SimpleAudioRecorder()
                
    #             try:
    #                 audio_file = fallback_recorder.record_with_pyaudio(duration)
    #                 if audio_file:
    #                     st.success("Recording selesai!")
    #                     with st.spinner("Memproses audio..."):
    #                         transcribed_text = fallback_recorder.audio_file_to_text(audio_file)
    #             except Exception as e:
    #                 st.error(f"Fallback recorder error: {e}")
    
    # Fallback 2: Manual text input
    # if transcribed_text is None:
    #     st.markdown("---")
    #     transcribed_text = show_manual_input_fallback()
    
    # Process the question if we have transcribed text
    if transcribed_text:
            st.write(f"**Pertanyaan yang didengar:** {transcribed_text}")
            
            # Extract question components using AI or simple parsing
            parsed_input = audio_processor.extract_question_location_language(transcribed_text)
            question = parsed_input['question']
            location = parsed_input['location']
            language = "Bahasa Indonesia"
            
            Static.load_api()
            
            inputs = {'question': question, 'location': location, 'language': language}
            
            crew = Crews(question=question, location=location, language=language)
            
            with st.spinner("Memvalidasi pertanyaan..."):               
                validation_result = crew.validate_crew().kickoff(inputs=inputs)
                
            if str(validation_result).lower().strip() == "yes":
                
                st.success("Validasi berhasil! Sedang meneliti...")
                
                with st.spinner("Mencari informasi sejarah..."):
                    crew_output = crew.main_crew().kickoff()
                
                st.markdown("### 📜 Jawaban Sejarah:")
                st.markdown(f"{crew_output}")
                
                # Convert answer to speech
                st.markdown("### 🔊 Mendengarkan Jawaban:")
                with st.spinner("Mengkonversi ke suara..."):
                    audio_processor.text_to_speech(str(crew_output), language='en')
                    
            else:
                st.error("Validasi gagal. Silakan tanyakan pertanyaan sejarah yang valid.")
        
if __name__ == "__main__":
    main()
