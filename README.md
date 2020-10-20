# HEIGHT_DETECTION
## Artificial Intelligence Course Project

> The project is based on height detection of humans from an image dataset and thereby extending the possibilities to live detection of height through a video camera of known focal length!

## DESCRIPTION
This is a course project done for the course of Artificial Intelligence under the instructor **Yashasvi Verma**. The objective of the project is to work on an idea in which at least one of the components involve AI. Posing any real world problem as a search problem and trying to come-up with some unique solution was one of the prerequisites. So, the project chosen by the writer, Ankit Bhardwaj, was **Height detection using computation techniques**. <br/>
We have used the Penn-Fudan dataset. Firstly, the human images are segmented from the background. The mask image generated is then progressed through post-image processing to find the contours of the image. The difference between the topmost and the bottommost y-coordinates gives us the height of the person in pixel units. This can be converted to SI Units using some corelations between the camera's focal length, distance of the human from the camera and the height of the camera. <br/>
Thereafter, we look at the possibility of real-time height detection through this method by the use of web camera. The video is processed in a frame-by-frame manner, and the height of the person in front of the camera is calculated and printed (in pixels).

## VISUALS
> We attach some descriptive images here in order to describe the step-by-step progress.

![Image](blob:https://web.whatsapp.com/86401782-ff66-41d6-820f-ea1cad4120bf)
