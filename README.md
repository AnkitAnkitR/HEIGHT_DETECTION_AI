# HEIGHT_DETECTION
## Artificial Intelligence Course Project

> The project is based on height detection of humans from an image dataset and thereby extending the possibilities to live detection of height through a video camera of known focal length!

## DESCRIPTION
This is a course project done for the course of Artificial Intelligence under the instructor **Yashasvi Verma**. The objective of the project is to work on an idea in which at least one of the components involve AI. Posing any real world problem as a search problem and trying to come-up with some unique solution was one of the prerequisites. So, the project **Height detection using computation techniques** was chosen. <br/>

We have used the [Mask R-CNN model](https://arxiv.org/pdf/1703.06870.pdf), and trained it on the [Penn-Fudan database](https://www.cis.upenn.edu/~jshi/ped_html/). Firstly, the [human images](https://www.cis.upenn.edu/~jshi/ped_html/pageshow1.html) are segmented from the background. The mask image generated is then progressed through post-image processing to find the contours of the image. The difference between the topmost and the bottommost y-coordinates gives us the height of the person in pixel units. This can be converted to SI Units using some corelations between the camera's focal length, distance of the human from the camera and the height of the camera. <br/>

We can calculate the height of a person in our preferred metric by comparing the dimensions (in pixels) of a reference object of known size with that of the human. PPI stands for Pixels Per Inch and is a metric typically used to describe the pixel density, and that could be useful to convert the height into SI units. Mathematically,
 pixels_per_metric = object_width/known_width <br/>


Thereafter, we look at the possibility of real-time height detection through this method by the use of web camera. The video is processed in a frame-by-frame manner, and the height of the person in front of the camera is calculated and printed (in pixels). <br/>

One approach taken in the past somewhat similar to ours is [described](http://ij3c.ncuteecs.org/volume/paperfile/4-3/IJ3C_6.pdf).

## VISUALS
> We attach some descriptive images here in order to describe the step-by-step progress of height detection of images in the dataset.

![Image](https://github.com/AnkitAnkitR/HEIGHT_DETECTION_AI/blob/main/Images/1.jpeg?raw=true)
![Image](https://github.com/AnkitAnkitR/HEIGHT_DETECTION_AI/blob/main/Images/2.jpeg?raw=true)
![Image](https://github.com/AnkitAnkitR/HEIGHT_DETECTION_AI/blob/main/Images/3.jpeg?raw=true)
![Image](https://github.com/AnkitAnkitR/HEIGHT_DETECTION_AI/blob/main/Images/4.jpeg?raw=true)


## DEMONSTRATION
> A video for the demonstration of the ultimate goal of the project, i.e., live height detection through the use of webcamera, is attached [here](https://drive.google.com/file/d/1ycx6WSUFdXFMj7C-MmESCZM8N7Bvallj/view?usp=sharing) for reference of code implementation.


## INSTALLATION_REQUIREMENTS
There are some python packages that were essential for the completion of this project. All these packages and other requirements have been mentioned in [requirements.txt](https://github.com/AnkitAnkitR/HEIGHT_DETECTION_AI/blob/main/requirements.txt)

## PROJET STATUS AND CHALLENGES FACED

Most real-world applications require blazingly fast inference time, varying anywhere from a few milliseconds to one second. As noticed from the demonstrations, there is some lag between the real time media captured by the webcam and the output window showing the mask image. This is because the processing power requirements of the program are higher than the user’s machine. As a result of the lag, some of the input frames get skipped.  <br/>

It is not possible to calculate the number of pixels per metric unless the distance to the object and camera is known. Even though we may be pointing the camera straight to the human figure, the distance from the camera to the person changes as the incident angle changes, thus, every given point on the body is at a different distance from the camera. This variation in distance needs to be taken care of by taking the help of some complex trigonometry. 
