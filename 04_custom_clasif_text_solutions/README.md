# SUMMARY
+ Understand types of classification projects.
+ Build a custom text classification project.
+ Tag data, train, and deploy a model.
+ Submit classification tasks from your own app.

## LABELING DATA
+ Single Label
+ Multiple Label

## EVALUATING AND IMPROVING THE MODEL
+ False positive: model predicts x but the file is not labeled x.
+ False negative: model does not predict label x but in fact the file is x
    ### Metrics
    + Recall: 
    Of all the actual labels, how many were identified; the ratio of true positives to all that was labeled.
    **Recall = #True_Positive / (#True_Positive + #False_Negatives)**

    + Precision: 
    How many of the predicted labels are correct; the ratio of true positives to all identified positives.
    **Precision = #True_Positive / (#True_Positive + #False_Positive)**

    + F1 Score : 
    A function of recall and precision, intended to provide a single score to maximize for a balance of each component
    **F1 Score = 2 * Precision * Recall / (Precision + Recall)**

Evaluation metrics documentation: https://learn.microsoft.com/en-us/azure/ai-services/language-service/custom-text-classification/concepts/evaluation-metrics?azure-portal=true
