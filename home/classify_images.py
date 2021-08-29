#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/classify_images.py
#                                                                             
# PROGRAMMER: KETAN N.
# DATE CREATED: MAY 23rd, 2021                          
# REVISED DATE: MAY 31st, 2021
# PURPOSE: Create a function classify_images that uses the classifier function 
#          to create the classifier labels and then compares the classifier 
#          labels to the pet image labels. This function inputs:
#            -The Image Folder as image_dir within classify_images and function 
#             and as in_arg.dir for function call within main. 
#            -The results dictionary as results_dic within classify_images 
#             function and results for the functin call within main.
#            -The CNN model architecture as model wihtin classify_images function
#             and in_arg.arch for the function call within main. 
#           This function uses the extend function to add items to the list 
#           that's the 'value' of the results dictionary. You will be adding the
#           classifier label as the item at index 1 of the list and the comparison 
#           of the pet and classifier labels as the item at index 2 of the list.
#
##
# Imports classifier function for using CNN to classify images 
from classifier import classifier 

def classify_images(images_dir, results_dic, model):
    """
    Creates classifier labels with classifier function, compares pet labels to 
    the classifier labels, and adds the classifier label and the comparison of 
    the labels to the results dictionary using the extend function. Be sure to
    format the classifier labels so that they will match your pet image labels.
    The format will include putting the classifier labels in all lower case 
    letters and strip the leading and trailing whitespace characters from them.
    For example, the Classifier function returns = 'Maltese dog, Maltese terrier, Maltese' 
    so the classifier label = 'maltese dog, maltese terrier, maltese'.
    Recall that dog names from the classifier function can be a string of dog 
    names separated by commas when a particular breed of dog has multiple dog 
    names associated with that breed. For example, you will find pet images of
    a 'dalmatian'(pet label) and it will match to the classifier label 
    'dalmatian, coach dog, carriage dog' if the classifier function correctly 
    classified the pet images of dalmatians.
     PLEASE NOTE: This function uses the classifier() function defined in 
     classifier.py within this function. The proper use of this function is
     in test_classifier.py Please refer to this program prior to using the 
     classifier() function to classify images within this function 
     Parameters: 
      images_dir - The (full) path to the folder of images that are to be
                   classified by the classifier function (string)
      results_dic - Results Dictionary with 'key' as image filename and 'value'
                    as a List. Where the list will contain the following items: 
                  index 0 = pet image label (string)
                --- where index 1 & index 2 are added by this function ---
                  NEW - index 1 = classifier label (string)
                  NEW - index 2 = 1/0 (int)  where 1 = match between pet image
                    and classifer labels and 0 = no match between labels
      model - Indicates which CNN model architecture will be used by the 
              classifier function to classify the pet images,
              values must be either: resnet alexnet vgg (string)
     Returns:
           None - results_dic is mutable data type so no return needed.         
    """
    
    for key, values in results_dic.items():
        
        # Use classifier() function to classify images based on a particular model
        # Image classification raw will hold the label of each file classified
        # after converting string into all lower case and
        # strip the leading and trailing whitespace characters
        classifier_label = images_dir+key
        image_classification = classifier(classifier_label, model).lower().strip()
        
        # commented to use method chaining.
        # convert string into all lower case
        #image_classification_lower = image_classification_raw.lower()
        
        # commented to use method chaining.
        # strip the leading and trailing whitespace characters
        #image_classification = image_classification_lower.strip()
        
        #print(type(image_classification))
        #image_classification_list = list(image_classification.split(','))
        
        # fetch the pet label from dictionary 
        pet_label = results_dic[key][0]
        
        #values.append(image_classification)
        #print('Value being evaluated', value)
        
        # Check if pet label is in image classification label string or not
        # If match is found then set image classification as index 1 and value 1 in the index 2 
        # Else set value of immage classification as index 1 and value 0 in the index 2 
        # List Index 1 = represent image classification from classifier function 
        # List Index 2 = represent the value 1 (match) or 0 (non-match) if pet label in image classiciation label
        if pet_label in image_classification:
            results_dic[key].extend((image_classification, 1))
        else:
            results_dic[key].extend((image_classification, 0))
            
        #print(key, values)
    None 