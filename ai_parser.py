from static import Static
import re

class AIParser:
    def __init__(self):
        self.llm = Static.load_api()
    
    def parse_audio_input(self, transcribed_text):
        """Parse transcribed audio to extract question, location, and language using AI"""
        
        prompt = f"""
        Analisis teks berikut yang merupakan pertanyaan sejarah dari user:
        "{transcribed_text}"
        
        Ekstrak informasi berikut dalam format JSON:
        1. question: pertanyaan sejarah utama
        2. location: lokasi yang disebutkan (jika ada), kosongkan jika tidak ada
        3. language: bahasa yang diminta untuk jawaban (default: indonesian jika tidak disebutkan)
        
        Contoh output:
        {{
            "question": "Ceritakan tentang Perang Diponegoro",
            "location": "Yogyakarta", 
            "language": "indonesian"
        }}
        
        Jika tidak ada lokasi yang disebutkan, biarkan location kosong "".
        Jika tidak ada bahasa yang disebutkan, gunakan "indonesian" sebagai default.
        
        Berikan hanya JSON tanpa penjelasan tambahan.
        """
        
        try:
            response = self.llm.predict(prompt)
            
            # Simple regex parsing as fallback
            import json
            try:
                parsed = json.loads(response)
                return {
                    'question': parsed.get('question', transcribed_text),
                    'location': parsed.get('location', ''),
                    'language': parsed.get('language', 'indonesian')
                }
            except:
                # Fallback simple parsing
                return self._simple_parse(transcribed_text)
                
        except Exception as e:
            print(f"Error in AI parsing: {e}")
            return self._simple_parse(transcribed_text)
    
    def _simple_parse(self, text):
        """Simple fallback parsing without AI"""
        # Simple keyword detection for location
        location = ""
        common_locations = ["jakarta", "yogyakarta", "surabaya", "bandung", "medan", "bali", "jawa", "sumatra"]
        for loc in common_locations:
            if loc in text.lower():
                location = loc.title()
                break
        
        # Simple language detection
        language = "indonesian"
        if "english" in text.lower() or "inggris" in text.lower():
            language = "english"
        elif "arab" in text.lower() or "arabic" in text.lower():
            language = "arabic"
            
        return {
            'question': text,
            'location': location,
            'language': language
        }
