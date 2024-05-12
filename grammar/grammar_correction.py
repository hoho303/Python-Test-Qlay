from happytransformer import HappyTextToText, TTSettings
import argparse

def load_grammar_model():
    happy_tt = HappyTextToText("T5", "vennify/t5-base-grammar-correction")
    args = TTSettings(num_beams=5, min_length=1)

    return happy_tt, args

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'text', type=str, help='Text to correct.')
    return parser.parse_args()

def main():
    args = parse_args()
    text = args.text

    happy_tt, args = load_grammar_model()
    corrected_text = happy_tt.generate_text(text, args)
    print(corrected_text)

if __name__ == '__main__':
    main()