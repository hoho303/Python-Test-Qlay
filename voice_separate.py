import argparse
from pydub import AudioSegment
from utils import download_audio_youtube, export_file
from asr.whisper import load_asr_model
from spkd.speaker_diarization import load_speaker_diarization_model
import os

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'url', type=str, help='Youtube video URL.')
    parser.add_argument(
        '--num-speakers',
        type=int,
        default=1,
        help='Number of speakers to diarize. Default is 1.')
    parser.add_argument(
        '--out-file',
        type=str,
        default='out.json',
        help='Output file path. Default is out.json.'
    )
    return parser.parse_args()

def main():
    args = parse_args()
    url = args.url
    num_speakers = args.num_speakers

    audio_file = download_audio_youtube(url)
    audio = AudioSegment.from_file(audio_file)

    asr_model = load_asr_model()

    results = []

    if num_speakers > 1:
        diarization_model = load_speaker_diarization_model()
        diarization = diarization_model(audio_file, num_speakers=num_speakers)
        diarization = diarization.rename_labels(generator='string')

        for turn, _, speaker in diarization.itertracks(yield_label=True):
            segment = audio[turn.start * 1000:turn.end * 1000]
            segment.export('temp.wav', format='wav')

            text = asr_model('temp.wav', return_timestamps=False)['text']
            
            results.append(
                {
                    'id': 0,
                    'speaker': speaker,
                    'text': text,
                    'start': turn.start * 1000,
                    'end': turn.end * 1000
                }
            )
        os.remove('temp.wav')

    else:
        result = asr_model(audio_file, return_timestamps=True)['chunks']
        for res in result:
            results.append(
                {
                    'id': 0,
                    'speaker': 'A',
                    'text': res['text'],
                    'start': int(res['timestamp'][0] * 1000),
                    'end': int(res['timestamp'][1] * 1000)
                }
            )
    
    export_file(results, args.out_file)

if __name__ == '__main__':
    main()