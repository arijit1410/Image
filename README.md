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

## Result using ArcTan Custom Activation Function ##
``` time: 390.3867 step: 1 loss: 3.8274 accuracy: 0.0000 ```

``` time: 226.9772 step: 8 loss: 1.1998 accuracy: 0.4200 ```

``` time: 239.9261 step: 16 loss: 0.7230 accuracy: 0.5400 ```

``` time: 254.3470 step: 24 loss: 0.7081 accuracy: 0.4400 ```

``` time: 235.8235 step: 32 loss: 0.6672 accuracy: 0.6400 ```

``` time: 243.3578 step: 40 loss: 0.6987 accuracy: 0.5600 ```

``` time: 223.6025 step: 48 loss: 0.6977 accuracy: 0.5200 ```

``` time: 217.2507 step: 56 loss: 0.6961 accuracy: 0.5200 ```

``` time: 227.9983 step: 64 loss: 0.6997 accuracy: 0.5200 ```

``` time: 236.2819 step: 72 loss: 0.7255 accuracy: 0.3600 ```

``` time: 225.5156 step: 88 loss: 0.6872 accuracy: 0.6800 ```

``` time: 240.2957 step: 96 loss: 0.6657 accuracy: 0.6200 ```

``` Predicted 27 out of 50; partial accuracy 0.5400 ```


