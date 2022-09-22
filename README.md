Automatic segmentation and recognition of anatomical lung
			structures from high-resolution chest X-Ray images

			ASADEL TECH


OBJECTIVE- 

1. Detect Lung in the X Ray
2. Perform segmentation of the lungs

INTRODUCTION-

The report demonstrates the work done and the results obtained for the lung recognition and segmentation project undertaken during December,2018 for ASADEL TECH.

APPROACH 1-

Segmentation using OpenCV (CCA)

The approach used to segment the images is Connected Component Analysis. Connected regions wil imply that all the connected pixels belong
to the same object. A pixel is said to be connected to another if they both have the same value and are adjacent to each other.

X Ray Image -> Grayscale Image -> Binary Image -> Applying CCA to get connected regions -> Detect lungs out of all connected regions


Otsu’s binarization is used to convert a grayscale image into a binary image. 
The following explains in detail the process of binarization which was integrl in segmenting the images.

OTSU’S BINARIZATION-

In image analysis, we often need an automatic, data-driven way to distinguish two types of relatively homogenous things, like land vs. water, forest vs. grass or foreground vs. background. For single-band images that have a bimodal pixel distribution, a two-class segmentation can be performed by finding a single threshold that separates the two classes.

Otsu’s method is a means of automatically finding an optimal threshold based on the observed distribution of pixel values (Otsu. 1979).

First, let’s define optimal as Otsu did: whatever partition of the data that maximizes inter-class variance (equivalently, minimizes the sum of intra-class variances). Define inter-class variance as BSS/p, where BSS (between-sum-of-squares) is







In our case, there are two classes so p=2. Here we’re using the between-sum-of-squares (BSS) terminology to indicate that this is a general method to describe the variance structure of a dataset.

We’re looking for that threshold that maximizes the BSS.
We’re not going to search exhaustively. We’re just going to search over the thresholds that are represented by the bins in a histogram. The advantage of that approach is that it only requires a single pass over the data. At each bin of the histogram, define class k as the pixels in that bin and lower. Class k+1 is everything else. 
The function looks at every possible partition of the input data defined by the bins of the histogram, then returns the mean associated with the bin that maximizes the BSS. This works better when you strategically choose the region for which the histogram is generated. A rudimentary mask is obtained by this with the two components being the sure foreground and the sure background region. 

The resulting mask is then inverted so that the characters are distinctly visible over the background.

Now, the output of the  binarization is used as input for Connected Component Analysis which is explained below.

CONNECTED COMPONENT ANALYSIS-

Connected components labeling scans an image and groups its pixels into components based on pixel connectivity, i.e. all pixels in a connected component share similar pixel intensity values and are in some way connected with each other. Once all groups have been determined, each pixel is labeled with a graylevel or a color (color labeling) according to the component it was assigned to. 
Extracting and labeling of various disjoint and connected components in an image is central to many automated image analysis applications. 
Connected component labeling works on binary or graylevel images and different measures of connectivity are possible. However, for the following we assume binary input images and 8-connectivity. The connected components labeling operator scans the image by moving along a row until it comes to a point p (where p denotes the pixel to be labeled at any stage in the scanning process) for which V={1}. When this is true, it examines the four neighbors of p which have already been encountered in the scan (i.e. the neighbors (i) to the left of p, (ii) above it, and (iii and iv) the two upper diagonal terms). Based on this information, the labeling of p occurs as follows: 
    • If all four neighbors are 0, assign a new label to p, else 
    • if only one neighbor has V={1}, assign its label to p, else 
    • if more than one of the neighbors have V={1}, assign one of the labels to p and make a note of the equivalences. 
After completing the scan, the equivalent label pairs are sorted into equivalence classes and a unique label is assigned to each class. As a final step, a second scan is made through the image, during which each label is replaced by the label assigned to its equivalence classes. For display, the labels might be different graylevels or colors. 

Result- The resultant output fell well short of expectations due to inherent problems with the algorithm which resulted in disparate regions getting connected together.

Approach 2-
Segmentation using OpenCV (Watershed Algorithm)

Binarization was again performed on the image using Otsu’s algorithm as explained above.
Afterwards, using the thresholding created by binarization, watershed algorithm was applied.
Result- This method proved unsuccessful too since the segmentation tended to include the surface on which the X Ray was kept too due to similar colouring.

Approach 3-
Segmentation using Neural Network 
The only approach left now was to go for the neural network.
Two different architectures seemed viable for this purpose, namely Mask R-CNN and UNet.
Firstly, I implemented the Mask R-CNN architecture since it is currently the best object detection network available. The only problem was that despite some promising results, it proved to be very expensive computationally and thus was infeasible for the project.
UNet is currently the state of the art architecture for biomedical image segmentation since it is faster than Mask R-CNN and uses an innovative method of upsampling which helps to segment images using the corresponding downsampled feature mappings.  The model created for the project with details on the indiviual convolution layers has been given below:
 
The results obtained by this method were highly encouraging since even with a very small training set, a dice score of 82.7 was obtained. Further increase in performance can be achieved by using a larger dataset and by better preprocessing in order to remove the erroneous samples from the training model.

A part of the output has been given below:

Here, the first column contains the preprocessed images, the second one is the superimposition of the predicted segment against the actual segmentation done by hand. The third column shows the predicted masks for each sample and the last column contains a graphical representation of the difference between the predicted valus and the optimum value.

Improvements to be made in the future:
 
In the future, the number of neural layers in the network will be increased further to see how it affects the accuracy. Nextly, a substantially larger dataset will be taken to avoid the problems of ovrfitting. At last, Mask R-CNN will also be used to implement the model using a GPU so that the work can be taken ahead further.
