import sys
from TTS.api import TTS

def synthesize(text, output_path):
    try:
        tts = TTS(model_name="tts_models/en/vctk/vits", 
                  progress_bar=False, 
                  gpu=False)
        tts.tts_to_file(
            text=text,
            speaker="p236",
            file_path=output_path
        )
        print("SUCCESS")
    except Exception as e:
        print(f"ERROR: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("ERROR: Usage: python coqui_tts.py <text> <output_path>")
        sys.exit(1)
    synthesize(sys.argv[1], sys.argv[2])
