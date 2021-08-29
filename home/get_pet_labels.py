#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: KETAN N.
# DATE CREATED: MAY 19th, 2021                           
# REVISED DATE: MAY 31st, 2021
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir, path

def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    
    
    # Code review comments fixed to ignore hidden files or files starting with a dot
    
    # Initialize empty list called filenames
    filenames = []
    
    # Retrieve the filenames from folder while ignoring hidden files or files starting with a dot
    for files in listdir(image_dir):
        if not files.startswith('.'):
            #print("Inside dot check", files)
            filenames.append(files)
    
    # Printing filenames to see if list is captured or not - Debugging
    #print("Printing Filenames:", filenames)
    
    # Print 3 of the filenames from folder image_dir - Debugging
    #print("\nPrints 3 filenames from folder {}".format(image_dir))
    #for i in range(0, 3, 1):
    #    print("{:2d} file: {:>25}".format(i + 1, filenames[i]) )
 
    # Create and Initalize an empty list to store formatted labels
    pet_labels = []
    
    # Function call to populate pet_labels list with formatted pet labels 
    # that will be used for forming Index 0 of results_dic dictionary
    get_labels_from_filenames(filenames, pet_labels)
    
    # Creates empty dictionary named results_dic
    results_dic = dict()
    
    # Creates empty dictionary named results_dic_duplicates
    results_dic_duplicates = dict()
    
    # Number of items in dictionary
    print("\nEmpty Dictionary results_dic - n items=", len(results_dic))
    
    # Printing lists before combining into dictionary - Debugging
    #print(filenames)
    #print(pet_labels)
    
    # If filename doesn't already exist in dictionary add it and it's
    # pet label 
    for idx in range(0, len(filenames), 1):
        if filenames[idx] not in results_dic:
            results_dic[filenames[idx]] = [pet_labels[idx]]
        else:
            results_dic_duplicates[filenames[idx]] = [pet_labels[idx]]
    
    # Additional methods to prepare results_dic from list
    #for (idx, file) in enumerate(filenames):
    #    results_dic[file] = [pet_labels[idx]]
    #results_dic = {filenames[i]: [pet_labels[i]] for i in range(len(filenames))}
    #results_dic = dict(zip(filenames, pet_labels))
    
    # Debugging
    #print(results_dic)
    
    print("\n **** Filenames not considered in classification **** : \n {}".format(results_dic_duplicates))
    
    return results_dic

def get_labels_from_filenames(filenames_list, pet_labels):
    """
    Creates pet labels formatted list based on the image files from the filenames_list. 
    Parameters:
     filenames_list - The file names list from which labels to be extracted (list)
    Returns:
      pet_labels_formatted - List with pet names labels after lower case, splitting, extracting characters, 
      adding space and removing white space character from both the sides of original file name (string)
    """
    
    # Create and Initalize an empty list to store formatted labels
    #pet_labels_formatted = []
    
    # Loop to go over each elements of filenames in the filenames_list 
    for idx in range(0, len(filenames_list), 1):
        
        # Assign name_ext tuple with name and extension as seperate values from the filename 
        # so that later name can be used without their extensions 
        # hence capturing pet labels accurately in conditions when filenames 
        # have numericals or not have numericals at the end of filename
        # example 'Grizzly_Bear.jpg' or 'Grizzly_Bear_01.jpg' will resolve the pet label
        # correctly as 'grizzly bear'
        filename_ext = path.splitext(filenames_list[idx])
        
        # Sets pet_image list from filename_ext by accessing just the name part of the file 
        # convert to lower case and split words having _ character in between as different
        # list elements
        pet_image = filename_ext[0].lower().split("_")
        
        # Create pet_name starting as empty string
        pet_name = ""
        
        # Loops to check if word in pet name is only
        # alphabetic characters - if true append word
        # to pet_name separated by trailing space 
        for word in pet_image:
            #print("word", word)
            if word.isalpha():
                pet_name += word + " "
    
        # Strip off starting/trailing whitespace characters 
        pet_name = pet_name.strip()
        
        # Append final label in the list pet_labels_formatted
        pet_labels.append(pet_name)
    
    # Print 3 of the filenames from folder image_dir - Debugging
    #print("\nPrints 3 labels from filenames")
    #for i in range(0, 3, 1):
    #    print("{:2d} file: {:>25}".format(i + 1, pet_labels[i]) )
    
    None