# Introduction
Grammar correction is the task of automatically correcting the grammatical errors in a given text. The grammar correction model is trained on a large dataset of labeled sentences, where the input is the sentence and the output is the corrected sentence.

In this project, we will build a grammar correction model using Happy Transformer with T5 model which currently outperforms the human baseline on the General Language Understanding Evaluation (GLUE) benchmark – making it one of the most powerful NLP models in existence.

# Usage
```
python grammar_correction.py <input_sentence> 
```

- input_sentence: The sentence to be corrected

# Training
## Data Preparation
The dataset should be a csv file with two columns: `sentence` and `corrections`. The `sentence` column contains the sentences with grammatical errors and the `corrections` column contains the corrected sentences.

You can see an example of the dataset from: https://huggingface.co/datasets/jhu-clsp/jfleg

