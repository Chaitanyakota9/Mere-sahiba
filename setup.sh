#!/bin/bash

echo "🎭 Setting up Hu Tao's MP3 Text Extractor! 🎭"
echo "Creating virtual environment..."

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

echo "Installing dependencies..."
pip install -r requirements.txt

echo "✨ Setup complete! ✨"
echo ""
echo "To use the MP3 to text converter:"
echo "1. Activate the virtual environment: source venv/bin/activate"
echo "2. Run: python sahiba.py your_audio_file.mp3"
echo ""
echo "Example: python sahiba.py audio.mp3 es-ES"

