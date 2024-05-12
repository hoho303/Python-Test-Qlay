# 1. Installation
```
git clone 
cd 
pip install -r requirements.txt
```

# 2. Usage
## 2.1. Voice Seperation
```
python voice_seperation.py <input_url> --num-speakers --out-file <output_file>
```
- input_url: Youtube url of the input audio file, default is None
- num-speakers: Number of speakers in the audio file, default is 1
- output_file: Path to save the results, default is out.json

Example:
```
python voice_seperation.py https://www.youtube.com/watch?v=54AYOd5S7uo --num-speakers 2 --out-file output.json
```

## 2.2 Score Accent
```
python score_accent.py <input_file> --num-speakers --out-file <output_file>
```

# 3. Training
You can see the details of the training process for each model in the corresponding folder:
- [Speaker Diarization](spkd/README.md)
- [Audio Speech Recognition](asr/README.md)
- [Grammar Correction](grammar/README.md)

