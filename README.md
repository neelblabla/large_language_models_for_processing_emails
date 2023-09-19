# large_language_models_for_processing_emails


### llama2-7b for categorising emails for Deutsche Bahn

1. Implement an annotation tool to annotate a subset of the mails in categories. We use doccano (python based), but feel free to use whatever you want
2. Upload a subset of the mails (selection is your choice) to the annotation tool (in doccano you can easily upload the mails as text as provided by the Enron corpus). I suggest to annotate as first step between 500 and 1.000 mails
3. Annotate the 500 - 1.000 mails into categories. I suggest between 20 and 30 categories. The choice of the categories is up to you, e.g. you can use “Summary of a meeting”, “mail to customer” or whatever seems reasonable to you after having got a feeling for the mails included in the dataset
4. Feed the annotated mail in a LLM
5. Select a test sample and apply the LLM to the test sample to get the categories for the mails included in the test sample from what the LLM has learned in step 4)
6. Compare the results in step 5) with the categories you would have annotated manually to get a measure for the quality of your results
7. If results are bad either change the LLM or increase the training sample
