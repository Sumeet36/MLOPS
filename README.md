# ML-Devops Integration project
##Project description:

1.	Create a container image that has Python3 and Keras or numpy installed in it using a Dockerfile. 

2.	When we launch this image, it should automatically start training the model in the container.

3.	We need to create a job chain of job1, job2, job3, job4 and job5 using build pipeline plugin in Jenkins. 

4.	 Job1 : Pull the Github repo automatically when a developer pushes a repository to the Github.

5.	 Job2 : By looking at the code or program file, Jenkins should automatically start the respective machine learning software interpreter installed in image container to deploy code  and start training( for example:If code uses CNN, then Jenkins should start the container that has already installed all the softwares required for the cnn processing).

7.	Job3 : if metrics accuracy is less than 98%  , then tweak the machine learning model architecture and retrain it.

8.	Job4: Notify that the best model is created.

9.	Create one extra job job5 for monitoring - In case the model was not trained due to some reason then it will be trained again.

## Steps :

Step 1: Upload your Machine learning code to gitHub by commiting to local git and also create a hook to automatically push it to github while commiting.

![](https://github.com/Sumeet36/MLOPS/blob/master/images1/pc.png)

Step 2: Create a docker-file and install all the required programs in the machine you are using as server.

![](https://github.com/Sumeet36/MLOPS/blob/master/images1/df.png)

Step 3: Now start your jenkins and create jobs according to the requirements.
#### note: Jenkins by default uses port 8080.

## Jobs  

### Job 1 :
The function of thuis job is to pull the code from github as soon as it is uploaded and then copy it to the specified directory.

![](https://github.com/Sumeet36/MLOPS/blob/master/images1/j1.png)

![](https://github.com/Sumeet36/MLOPS/blob/master/images1/j1_2.png)

![](https://github.com/Sumeet36/MLOPS/blob/master/images1/j1_3.png)

![](https://github.com/Sumeet36/MLOPS/blob/master/images1/j1_4.png)


### Job 2 : 

This job should run after job 1 is finished successfully.

By looking at the uploaded code, Jenkins should automatically start the respective dockerfile and start training the model.

![](https://github.com/Sumeet36/MLOPS/blob/master/images1/j2_1.png)


![](https://github.com/Sumeet36/MLOPS/blob/master/images1/j2_2.png)


![](https://github.com/Sumeet36/MLOPS/blob/master/images1/j2_3.png)

### Job 3 :

The objective of this job is to check the final accuracy. If the accuracy is found less than required accuracy ( in our case 98% ), it will make some changes and then retrain the model.

![](https://github.com/Sumeet36/MLOPS/blob/master/images1/j3_1.png)

![](https://github.com/Sumeet36/MLOPS/blob/master/images1/j3_2.png)


if the accuracy is above required accuracy the output will look like this: 

![](https://github.com/Sumeet36/MLOPS/blob/master/images1/j3_3.png)

### Job 4 :

job 4 is supposed to send a mail to notify that the mmodel has been trained succesfully.

![](https://github.com/Sumeet36/MLOPS/blob/master/images1/j4_2.png)

### Job 5:
Finally job 5 will search if mnist_LeNet_correct.h5 file is present or not , if it is present it means the model was trained successfully and if not then it will retrain it.

![](https://github.com/Sumeet36/MLOPS/blob/master/images1/j5_1.png)

![](https://github.com/Sumeet36/MLOPS/blob/master/images1/j5_2.png)

![](https://github.com/Sumeet36/MLOPS/blob/master/images1/j5_3.png)
