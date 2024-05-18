
5.1 Problem Statement: Explore the potential of Large Language Models(LLMs) and Generative AI models like GPT for Natural Language Processing tasks, such as Text Generation, Summarization, or Question -Answering

As Provided dataset (https://huggingface.co/datasets/viewer/?dataset=json) is not working so i have choosen this Dataset called Extreme Summarization (XSum) Dataset with the T5 Text-To-Text Transfer Transformer from Hugging Face.

The dataset consists of BBC articles and accompanying single sentence summaries. Specifically, each article is prefaced with an introductory sentence (aka summary) which is professionally written, typically by the author of the article. There are two features in this dataset: (1) document: Input news article. (2) summary: One sentence summary of the article.

The idea is to generate a short, one-sentence news summary answering the question ”What is the article about?”.

There are in total 226k samples: 204,045 samples for training data, 11,332 samples for validation data and 11,334 samples for test data.

The average number of words in a document is 431.07 (19.77 sentences) and The average number of words in a summary is 23.26.

T5 is a state-of-the-art language model developed by Google Research that can perform various NLP tasks, such as translation, summarization, and text generation. In this , we will explore how to fine-tune T5 for text generation and demonstrate the results with a few examples. We will also discuss some best practices and considerations when fine-tuning T5 for text generation

Text Generation with HuggingFace - GPT2
In this notebook, I will explore text generation using a GPT-2 model, which was trained to predict next words on 40GB of Internet text data. 
