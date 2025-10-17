from dotenv import load_dotenv
import os
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient


def main():
    try:
        # Get Configuration Settings
        load_dotenv()
        ai_endpoint = os.getenv('AI_SERVICE_ENDPOINT') # previously defined
        ai_key = os.getenv('AI_SERVICE_KEY') # previously defined
        project_name = os.getenv('PROJECT') # project defined to deploy the trainning model
        deployment_name = os.getenv('DEPLOYMENT') # model itself

        # Create client using endpoint and key
        credential = AzureKeyCredential(ai_key)
        ai_client = TextAnalyticsClient(endpoint=ai_endpoint, credential=credential)


        # Read each text file in the articles folder
        batchedDocuments = []
        articles_folder = 'articles'
        files = os.listdir(articles_folder)
        for file_name in files:
            # Read the file contents
            text = open(os.path.join(articles_folder, file_name), encoding='utf8').read()
            batchedDocuments.append(text)

        # Get Classifications
        operations = ai_client.begin_single_label_classify(
            batchedDocuments, # Documents used for classification
            project_name=project_name, 
            deployment_name=deployment_name
        )

        results = operations.result()

        for doc, classification_result in zip(files, results):
            if classification_result.kind == "CustomDocumentClassification":
                classification = classification_result.classifications[0]
                print("{} was classified as '{}' with confidence score {}.".format(
                    doc, classification.category, classification.confidence_score)
                )
            elif classification_result.is_error is True:
                print("{} has an error with code '{}' and message '{}'".format(
                    doc, classification_result.error.code, classification_result.error.message)
                )

    except Exception as ex:
        print(ex)


if __name__ == "__main__":
    main()