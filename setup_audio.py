"""
Setup script for audio dependencies on Windows
Run this if you encounter audio-related errors
"""

import subprocess
import sys
import os

def install_ffmpeg():
    """Install FFmpeg which is required for pydub"""
    try:
        print("🔧 Installing FFmpeg...")
        
        # Check if ffmpeg is already available
        result = subprocess.run(['ffmpeg', '-version'], 
                              capture_output=True, text=True)
        if result.returncode == 0:
            print("✅ FFmpeg already installed!")
            return True
            
    except FileNotFoundError:
        print("❌ FFmpeg not found. Please install FFmpeg manually:")
        print("1. Download from: https://ffmpeg.org/download.html")
        print("2. Extract to C:\\ffmpeg")
        print("3. Add C:\\ffmpeg\\bin to your PATH environment variable")
        print("4. Restart your terminal/IDE")
        print("\nAlternatively, install via chocolatey:")
        print("choco install ffmpeg")
        return False
    
    return True

def check_audio_dependencies():
    """Check if all audio dependencies are working"""
    print("🔍 Checking audio dependencies...")
    
    # Check speech_recognition
    try:
        import speech_recognition as sr
        print("✅ speech_recognition: OK")
    except ImportError:
        print("❌ speech_recognition: MISSING")
        return False
    
    # Check pydub
    try:
        import pydub
        print("✅ pydub: OK")
    except ImportError:
        print("❌ pydub: MISSING")
        return False
    
    # Check gTTS
    try:
        import gtts
        print("✅ gTTS: OK")
    except ImportError:
        print("❌ gTTS: MISSING")
        return False
    
    # Check streamlit-mic-recorder
    try:
        import streamlit_mic_recorder
        print("✅ streamlit-mic-recorder: OK")
    except ImportError:
        print("❌ streamlit-mic-recorder: MISSING")
        return False
    
    return True

def main():
    print("🎤 Audio Setup Checker for HISTORIAN GPT")
    print("=" * 50)
    
    # Check dependencies
    if not check_audio_dependencies():
        print("\n❌ Some dependencies are missing!")
        print("Run: pip install -r req.txt")
        return
    
    # Check FFmpeg
    if not install_ffmpeg():
        print("\n⚠️  FFmpeg installation required for audio conversion")
        return
    
    print("\n✅ All audio dependencies are ready!")
    print("You can now run the HISTORIAN GPT with audio features!")

if __name__ == "__main__":
    main()
