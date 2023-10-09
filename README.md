## Fine-tuning Llama2-7b, BERT base, XLNet base llm(s) for classifying emails for Deutsche Bahn

Hi, welcome!

In this repo, we perform parameter efficient fine tuning on Meta's Llama2-7b, BERT base and XLNet base large language models using Enron email corpus to demonstrate a proof of concept around email classification for Deutsche Bahn.

Following is the workflow:
1. Enron email corpus is an open dataset of more than 500,000 raw emails. We work on a subest of ~1700 pre-labeled emails available here - https://data.world/brianray/enron-email-dataset and another subset of chat GPT3.5 labelled ~12000.
2. We narrowed down to lables in one layer i.e. we only consider 'Cat_1_level_1'and 'Cat_1_level_2' exclusively for our purpose. The original (layered) labeling methodology is explained in detail here - https://datascience.stackexchange.com/questions/92341/how-to-read-the-labeled-enron-dataset-categories/92737#92737
3. 'Regular Expressions' methods are used to clean the heavily unstructured email bodies in the labeled dataset along with lemmatization of email subject and body. ( Dataset is split into training (~1400) and testing (~300) subsets. Final training dataset is hosted on huggingface here - https://huggingface.co/datasets/neelblabla/enron_labeled_email-llama2-7b_finetuning )
4. Following models and methodologies are used further:

### Llama2-7b
1. Prompts are generated on the final training dataset and parameter efficient finetuning is performed on Llama2-7b using this dataset. The parameters of the models are merged and the final fine-tuned model is hosted in the following huggingface repo - https://huggingface.co/neelblabla/email-classification-llama2-7b-peft
2. Model is finally evaluated on the testing dataset (maximum length of input test-prompts restricted to 100) - 65% of model-generated responses have strong indicative signals in the responses matching the human labels of the emails.
3. It is observed that model's performance degrades if the maximum length of input test-prompts are increased to 180, 200, 300, etc.

### BERT_base_uncased-100m
1. We employ a pre-trained BERT base model containing 110 million parameters.
2. The email content is tokenized using BERT's pre-trained tokenizer.
3. To enhance training efficiency, we freeze the first 8 layers of the model, focusing our fine-tuning efforts exclusively on the remaining 4 layers using our training data.
4. For comprehensive regularization and optimization, you can refer to the specific methods and hyperparameters detailed in the accompanying code.
5. Additionally, we introduce a classifier layer atop the BERT model, tailored to the number of output classes required for the task at hand.

### XLNet_base-110m
Similar workflow as BERT

*******

PEFT Fine-Tuned Llama2-7b Model - https://huggingface.co/neelblabla/email-classification-llama2-7b-peft

( Labeled Enron Dataset for Fine-Tuning on Llama2-7b - https://huggingface.co/datasets/neelblabla/enron_labeled_email-llama2-7b_finetuning )

*******
