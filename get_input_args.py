#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# get_input_args.py
#                                                                             
# PROGRAMMER: Aaron Ma
# DATE CREATED: 5/16/2020                       
# REVISED DATE: 5/16/2020
# PURPOSE: Create a function that retrieves the following 3 command line inputs 
#          from the user using the Argparse Python module. If the user fails to 
#          provide some or all of the 3 inputs, then the default values are
#          used for the missing inputs. Command Line Arguments:
#     1. Image Folder as --dir with default value 'pet_images'
#     2. CNN Model Architecture as --arch with default value 'vgg'
#     3. Text File with Dog Names as --dogfile with default value 'dognames.txt'
#
##
# Imports python modules
import argparse

# Returns the parsed argument collection
# 
def get_input_args():
    """
    Retrieves and parses the 3 command line arguments provided by the user when
    they run the program from a terminal window. This function uses Python's 
    argparse module to created and defined these 3 command line arguments. If 
    the user fails to provide some or all of the 3 arguments, then the default 
    values are used for the missing arguments. 
    Command Line Arguments:
      1. Image Folder as --dir with default value 'pet_images'
      2. CNN Model Architecture as --arch with default value 'vgg'
      3. Text File with Dog Names as --dogfile with default value 'dognames.txt'
    This function returns these arguments as an ArgumentParser object.
    Parameters:
     None - simply using argparse module to create & store command line arguments
    Returns:
     parse_args() - data structure that stores the command line arguments object  
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--dir", type = str, default = "pet_images/", help = "Path to the directory where the pet images are")
    parser.add_argument("--arch", type = str, default = "vgg", help = "Path to the model architecture")
    parser.add_argument("--dogfile", type = str, default = "dognames.txt", help = "Path to the dog labels")
    
    parsed_args = parser.parse_args()
    data_dir = parsed_args.dir
    model_arch = parsed_args.arch
    labels = parsed_args.dogfile
    
    sep = "=" * 50
    
    print(sep)
    print("Summary of your chosen parameters:")
    print(sep)
    print(f"Data directory: {data_dir}")
    print(f"Model architecture: {model_arch}")
    print(f"Training labels: {labels}")
    print(sep)
    
    return parsed_args
