# UzBooksQA
End to end extractive QA model for asaxiy.uz books.

Asaxiy Books, the largest online book seller in Uzbekistan, has been lacking an innovative QA model for its users to interact with. Their current method of answering user questions mostly revolves around providing information on prices and delivery times. To solve this issue, we have developed an Open Domain QA model with a focus on providing information about books. While our model is not yet perfect, it represents a significant step forward in enhancing the user experience and facilitating access to information about books.

## Running on your machine

To run the notebooks on your own machine, first clone the repository and navigate to it:

```bash
$ git clone https://github.com/shopulatov/UzBooksQA.git
$ cd UzBooksQA
```

Next, install all the dependencies from requirements.txt:

```bash
$ pip install -r requirements.txt
```

And follow through [demo.ipynb](https://github.com/shopulatov/UzBooksQA/blob/main/demo.ipynb) notebook and the demo from Gradio will pop up.

> Disclaimer!!! You'll need a GPU. Currently, this means you cannot build locally with a CPU 😢

> Note: We are assuming you have at least 3 GB storage and a stable connection.

 ## Challenges in Open Domain QA for Asaxiy Books</h3>
 Asaxiy Books, the largest online book seller in Uzbekistan, has limited support for customer queries and relies mostly on human assistance for answering questions related to books. This approach can be inefficient and may not always provide satisfactory results to customers.
In order to improve the user experience and to provide better support, we propose an Open Domain Question Answering (QA) system for Asaxiy Books that can help customers find information about books and answer their queries in a more efficient manner.
The QA system is built using Elasticsearch as the database and Haystack as the framework for running the pipeline.

## Implementation Details
We have used pre-trained models from the Hugging Face Transformers library, specifically the SQuAD 2.0 model in order to perform extractive QA. These models have been trained on large datasets of text and can accurately extract answers to questions from text.
The Haystack framework has been used to integrate Elasticsearch with the QA system. Elasticsearch provides fast and efficient indexing and querying of large volumes of text data, making it an ideal choice for the backend of the QA system.
The QA system consists of a retriever and a reader. The retriever performs an initial search of the Elasticsearch index to identify the most relevant documents to a given question. The reader then extracts the answer from these documents using the pre-trained models.
The QA system has been integrated into a web interface, allowing customers to easily interact with the system and obtain answers to their queries.

## Conclusion and Future Work
The Open Domain QA system developed for Asaxiy Books provides an efficient and accurate method for answering customer queries related to books. This system has the potential to greatly improve the user experience and reduce the workload of customer service representatives.
Future work on this system could involve improving the accuracy of the models used for QA, as well as incorporating additional features such as question generation and summarization.

## Authors
[Abror Shopulatov](https://www.linkedin.com/in/abrorshopulatov/)
[Navfalbek Makhfuzullaev](https://www.linkedin.com/in/navfalbek/)
[Samir Irgashev](https://www.linkedin.com/in/samir-irgashev-47522717a/)
