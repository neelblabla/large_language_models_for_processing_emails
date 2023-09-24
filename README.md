## Fine-tuning Llama2-7b llm for categorising emails for Deutsche Bahn

Hi Welcome!

In this repo, we perform parameter efficient fine tuning on Meta's Llama2-7b large language model using Enron email corpus to demonstrate a proof of concept around email classification for Deutsche Bahn.

Following is the workflow:
1. Enron email corpus is an open dataset of more than 500,000 raw emails. We work on a subest of ~1700 pre-labeled emails available here - https://data.world/brianray/enron-email-dataset
2. We narrowed down to lables in one layer i.e. we only consider 'Cat_1_level_1'and 'Cat_1_level_2' exclusively for our purpose. The original (layered) labeling methodology is explained in detail here - https://datascience.stackexchange.com/questions/92341/how-to-read-the-labeled-enron-dataset-categories/92737#92737
3. 'Regular Expressions' methods are used to clean the heavily unstructured email bodies in the labeled dataset. Dataset is split into training (~1400) and testing (~300) subsets. Final training dataset is hosted here - https://huggingface.co/datasets/neelblabla/enron_labeled_email-llama2-7b_finetuning
4. Prompts are templated on the final training dataset and parameter efficient finetuning is performed on Llama2-7b using this dataset. The parameters of the models are merged and the final fine-tuned model is hosted in the following repo - https://huggingface.co/neelblabla/email-classification-llama2-7b-peft
5. Model is finally evaluated on the testing dataset (maximum length of input test-prompts restricted to 100) - 65% of model-generated responses match the human labels of the emails.
6. Model's performance degrades if the maximum length of input test-prompts are increased to 180, 200, 300, etc.
7. All the fine-tuning and evaluation computations are performed using T4 GPUs on Google Collab notebooks.

*******

PEFT Fine-Tuned Model - https://huggingface.co/neelblabla/email-classification-llama2-7b-peft

Labeled Enron Dataset for Fine-Tuning - https://huggingface.co/datasets/neelblabla/enron_labeled_email-llama2-7b_finetuning

*******
