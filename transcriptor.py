import torch
from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline
from transformers.utils import is_flash_attn_2_available
from pytube import YouTube
import os

USE_GPU = True
LANGUAGES = [
    "spanish",
    "english"
]
SELECTED_LANG = 0
YT_VIDEO = 'https://www.youtube.com/watch?v=81VnO4puNkg"'

def get_device():
    device = torch.device("cpu")
    if USE_GPU and torch.backends.mps.is_available():
        torch.mps.empty_cache()
        device = torch.device("mps")
    elif USE_GPU and torch.cuda.is_available():
        torch.cuda.empty_cache()
        device = torch.device("cuda:0")
    return device

def get_torch_dtype():
    if USE_GPU and (torch.backends.mps.is_available() or torch.cuda.is_available()):
        return torch.float16
    return torch.float32

def create_model(model_id, device):
    torch_dtype = get_torch_dtype()
    model = AutoModelForSpeechSeq2Seq.from_pretrained(
        model_id, torch_dtype=torch_dtype, low_cpu_mem_usage=True, use_safetensors=True
    )
    model.to(device)
    processor = AutoProcessor.from_pretrained(model_id)

    return model, processor

def create_pipeline(model, processor, device):
    pipe = pipeline(
        "automatic-speech-recognition",
        model=model,
        tokenizer=processor.tokenizer,
        feature_extractor=processor.feature_extractor,
        chunk_length_s=30,
        batch_size=24,
        torch_dtype=model.config.torch_dtype,
        device=device,
        model_kwargs={"attn_implementation": "flash_attention_2"} if is_flash_attn_2_available() else {"attn_implementation": "sdpa"},
    )
    return pipe

def download_audio_from_youtube(url):
    try:
        yt = YouTube(url)
        audio_stream = yt.streams.filter(only_audio=True).first()
        audio_file = audio_stream.download()
        return audio_file
    except Exception as e:
        print(f"Error al descargar el audio de YouTube: {e}")

def transcript(pipe, audio):
    print("----- Comienza la transcripción -----")
    result = pipe(audio, generate_kwargs={"language": LANGUAGES[SELECTED_LANG]})
    print(f"Transcription: {result['text']}")

def main():
    model_id = "openai/whisper-large-v3"
    device = get_device()

    model, processor = create_model(model_id, device)
    pipe = create_pipeline(model, processor, device)
    audio_file_path = download_audio_from_youtube(YT_VIDEO)
    if audio_file_path:
        transcript(pipe, audio_file_path)
        os.remove(audio_file_path)

if __name__ == "__main__":
    main()