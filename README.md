# Image
**Image recognition using Convolutional Neural Networks(Tensorflow)**
The idea is to recognize apples in an image.The model has been trained on 120 pictures of red apples.
Because there is only only one class here,there needs to be a class with negative samples which represents "Not Apples".
The classes are as follows
  * Class 0- 100x100 pictures of different fruits which are not apples.
  * Class 1-100x100 pictures of red apples in various orientations.
  
 ## Dataset properties ##

Training set size: 240 images.

Validation set size: 20 images.

Number of classes: 2

Image size: 100x100 pixels.

## How to run ##

Use the generate_data.py script to generate the train-00000-of-00001 and validation-00000-of-00001 tfrecords file which are needed for the train and test scripts. In the generate_data.py file you can modify the path to the dataset as well as the location where the tfrecords are saved.

Run the train.py to train the network - currently the network runs for 10 iterations and saves the network state every 8 steps. This will generate the models/ folder where the network parameters are saved.
After completing the training, run the test.py file to evaluate the accuracy.

The network.py file contains the network definition as well as parameters used for building the network like the weights, biases, learning rate etc.

## Result using ReLu ##
``` Predicted 50 out of 50; partial accuracy 1.0000 ```
