# HEIGHT_DETECTION
## Artificial Intelligence Course Project

> The project is based on height detection of humans from an image dataset and thereby extending the possibilities to live detection of height through a video camera of known focal length!

## DESCRIPTION
This is a course project done for the course of Artificial Intelligence under the instructor **Yashasvi Verma**. The objective of the project is to work on an idea in which at least one of the components involve AI. Posing any real world problem as a search problem and trying to come-up with some unique solution was one of the prerequisites. So, the project chosen by the writer, Ankit Bhardwaj, was **Height detection using computation techniques**. <br/>

We have used the [Mask R-CNN model](https://arxiv.org/pdf/1703.06870.pdf), and trained it on the [Penn-Fudan database](https://www.cis.upenn.edu/~jshi/ped_html/). Firstly, the [human images](https://www.cis.upenn.edu/~jshi/ped_html/pageshow1.html) are segmented from the background. The mask image generated is then progressed through post-image processing to find the contours of the image. The difference between the topmost and the bottommost y-coordinates gives us the height of the person in pixel units. This can be converted to SI Units using some corelations between the camera's focal length, distance of the human from the camera and the height of the camera. <br/>
Thereafter, we look at the possibility of real-time height detection through this method by the use of web camera. The video is processed in a frame-by-frame manner, and the height of the person in front of the camera is calculated and printed (in pixels). <br/>
One of the typical approach somewhat similar to ours taken in the past is [described](http://ij3c.ncuteecs.org/volume/paperfile/4-3/IJ3C_6.pdf).

A fixed laser point and triangular distance measurement (FLPTDM) constructs a non-contact height measurement scheme. We calculate the distance between the laser beam projection image and the image’s center to obtain the measured length. In hardware, a laser beam is used for signal emission, and a digital camera is used as the signal detection. The distance between the laser beam projection image and the center of the image is calculated to get the measured length. On the other hand, an offset compensation data is used to calibrate the error and increase the measurement precision. We simply use a laser pointer and a camera associated with image detection techniques to obtain a precise human height measurement.


## VISUALS
> We attach some descriptive images here in order to describe the step-by-step progress.

![Image](https://github.com/AnkitAnkitR/HEIGHT_DETECTION_AI/blob/main/Images/1.jpeg?raw=true)
![Image](https://github.com/AnkitAnkitR/HEIGHT_DETECTION_AI/blob/main/Images/2.jpeg?raw=true)
![Image](https://github.com/AnkitAnkitR/HEIGHT_DETECTION_AI/blob/main/Images/3.jpeg?raw=true)
![Image](https://github.com/AnkitAnkitR/HEIGHT_DETECTION_AI/blob/main/Images/4.jpeg?raw=true)




## INSTALLATION_REQUIREMENTS
There are some python packages that were essential for the completion of this project. All these packages and other requirements have been mentioned in [requirements.txt]()
