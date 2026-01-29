# Age\_Predict

## This repo is for age predict projection mission using ML model, which combine with GUI.

This program allow users predict the age using their own face image.
In UI, you can also choose with different model to estimate.


### Example 

### Environment Setup
This program development on the environment below : 

Hardware : 

1. Nvidia RTX 5060
2. AMD I7 350

Attention. If your GPU is not the Nvidia Blackwell Gen, then you don’t have to follow the software requests below.
Just find the Tensorflow 2.10.0, which is the last version support GPU on windows directly, and everything can still work out.

Software : 

1. WSL2 with Ubuntu 24.04
2. Image : Nvidia NGC Tensorflow container 
3. Container : Docker desktop
4. Container Tool : Dev container in VS code
5. Requirement.txt with all ML tool you want to build in this container, include …… .
6. Docker file 
7. Devcontainer.json