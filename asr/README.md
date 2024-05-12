# Introduction
The automatic speech recognition (ASR) model solves the problem of converting spoken language into text. The ASR model is trained on a large dataset of labeled audio files, where the input is the audio signal and the output is the corresponding text transcription.

In this project, we will build an ASR model using Whisper. Whisper is a general-purpose speech recognition model. It is trained on a large dataset of diverse audio and is also a multitasking model that can perform multilingual speech recognition, speech translation, and language identification.

# Usage
```
python asr.py <audio_file> 
```
- audio_file: Path to the input audio file

# Training
To train the Whiser model, you need a large dataset of labeled audio files.

In this project, we will train the Whisper model on the custom dataset which isn't available in Hugging Face Datasets.
## Data Preparation
You need to prepare the dataset in the following format:
```
.
├── audio
│   ├── audio1.wav
│   ├── audio2.wav
├── audio_paths.txt
├── transcriptions.txt
```
where `audio_paths.txt` contains the paths to the audio files:
```
<unique-id> <absolute path to the audio file-1>
<unique-id> <absolute path to the audio file-2>
...
<unique-id> <absolute path to the audio file-N>
```
and `transcriptions.txt` contains the transcriptions for each audio file:
```
<unique-id> <Transcription (ground truth) corresponding to the audio file-1>
<unique-id> <Transcription (ground truth) corresponding to the audio file-2>
...
<unique-id> <Transcription (ground truth) corresponding to the audio file-N>
```
then you can use the `data_prep.py` script to prepare the data for training:
```
python data_prep.py \
--source_data_dir source_data_directory \
--output_data_dir output_data_directory
```
- source_data_dir: Path to the source data directory which contains the `audio_paths.txt` and `transcriptions.txt` files

- output_data_dir: Path to the output data directory where the processed data will be saved