# Introduction
The speaker diarization model solves the problem of identifying "who spoke when" in an audio file. This is a crucial step in many speech processing applications, such as automatic speech recognition, speaker identification, and speaker verification. The speaker diarization model is trained on a large dataset of labeled audio files, where each speaker is identified by a unique label.

In this project, i used pyannote-audio, an open-source toolkit for speaker diarization, to build a speaker diarization model.

# Usage
```
python speaker_diarization.py <audio_file> --outfile <output_file> --num-speakers <n_speakers>
```
- audio_file: Path to the input audio file
- output_file: Path to save the results, default is out.rttm
- n_speakers: Number of speakers in audio file, default is 1

# Training
To train the speaker diarization model, you need a large dataset of labeled audio files.

## Data Preparation
The first step is to prepare the data for training. You need to create a pyannote database, which is a YAML file that contains the paths to the audio files and the corresponding speaker labels.

Here is an example of a pyannote database:
```yaml
Databases:
  MyDatabase: 
    - /path/to/audio/{uri}.wav
    - /path/to/audio/{uri}.mp3

Protocols:
  MyDatabase:
    SpeakerDiarization:
      MyProtocol:
        train:
            uri: /path/to/train.lst
            annotation: /path/to/train.rttm
            annotated: /path/to/train.uem
```
where /path/to/train.lst contains the list of identifiers of the files in the training set:
```
# /path/to/train.lst
filename1
filename2
...
```
/path/to/train.rttm contains the reference speaker diarization using RTTM format:
```
# /path/to/reference.rttm
SPEAKER filename1 1 3.168 0.800 <NA> <NA> speaker_A <NA> <NA>
SPEAKER filename1 1 5.463 0.640 <NA> <NA> speaker_A <NA> <NA>
SPEAKER filename1 1 5.496 0.574 <NA> <NA> speaker_B <NA> <NA>
SPEAKER filename1 1 10.454 0.499 <NA> <NA> speaker_B <NA> <NA>
SPEAKER filename2 1 2.977 0.391 <NA> <NA> speaker_C <NA> <NA>
SPEAKER filename2 1 18.705 0.964 <NA> <NA> speaker_C <NA> <NA>
SPEAKER filename2 1 22.269 0.457 <NA> <NA> speaker_A <NA> <NA>
SPEAKER filename2 1 28.474 1.526 <NA> <NA> speaker_A <NA> <NA>
```
/path/to/train.uem contains the reference speaker diarization using UEM format:
```
filename1 NA 0.000 30.000
filename2 NA 0.000 30.000
filename2 NA 40.000 70.000
```

The dataset directory should have the following structure:
```
.
├── database.yml
├── audio
|   ├── filename1.wav
|   ├── filename2.wav
├── lists
|   └── train.lst
├── rttms
|   └── filename1.rttm
|   └── filename2.rttm
└── uems
    ├── filename1.uem
    └── filename2.uem
```
