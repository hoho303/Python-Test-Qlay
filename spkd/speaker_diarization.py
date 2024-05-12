from pyannote.audio import Pipeline
import torch
from argparse import ArgumentParser
from utils import download_audio_youtube

HF_TOKEN = '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'
HF_MODEL = 'pyannote/speaker-diarization-3.1'

device = 'cuda' if torch.cuda.is_available() else 'cpu'

def load_speaker_diarization_model():
    pipeline = Pipeline.from_pretrained(HF_MODEL, use_auth_token=HF_TOKEN)
    pipeline.to(torch.device(device))
    return pipeline

def parse_args():
    parser = ArgumentParser()
    parser.add_argument(
        'input', type=str, help='Input audio file.')
    parser.add_argument(
        '--out-file',
        type=str,
        default='out.rttm',
        help='Output file path. Default is out.rttm.')
    parser.add_argument(
        '--num-speakers',
        type=int,
        default=2,
        help='Number of speakers to diarize. Default is 2.')
    return parser.parse_args()

def main():
    args = parse_args()
    audio_file = args.input
    out_file = args.out_file
    num_speakers = args.num_speakers

    spd_model = load_speaker_diarization_model()
    
    # run the pipeline on an audio file
    diarization = spd_model(audio_file, num_speakers=num_speakers)

    # dump the diarization output to disk using RTTM format
    with open(out_file, "w") as rttm:
        diarization.write_rttm(rttm)



