# OLA driver partner churn prediction using ensemble models : 

## Problem Statement : 

Recruiting and retaining drivers is seen by industry watchers as a tough battle for Ola. Churn among drivers is high and it’s very easy for drivers to stop working for the service on the fly or jump to Uber depending on the rates.

As the companies get bigger, the high churn could become a bigger problem. To find new drivers, Ola is casting a wide net, including people who don’t have cars for jobs. But this acquisition is really costly. Losing drivers frequently impacts the morale of the organization and acquiring new drivers is more expensive than retaining existing ones.

 ## Objective : 

 To help the business to identify / predict whether the cab driving partner will churn to other company or not based on different attributes.

 ## Approach : 

 Bought the data into a proper structure  

 Performed data analysis 

 Tried different Ensemble Machine Learning models , performed hyper-parameter tuning and compared performance metrics of different models.

 Picked the best model

 Made a demo using streamlit for Poc.

## Streamlit demo : 
 
[OLA_ensemble_driver_churn.webm](https://github.com/user-attachments/assets/dc60f1d8-39dd-4e64-8c0e-c8e3f36c040c)

Future updates : Flask Api + docker +  deploy on AWS....

Created a flask api and tested it on POSTMAN
.

![ola_flask_post](https://github.com/user-attachments/assets/129c2c4f-b5d4-4a1c-9c85-510171e61508)


since it is a small-scale app and I'm managing everything manually on a single EC2 instance, cloning from GitHub and setting up the environment manually usually works but if I'm working production level scale I nned an isolated docker container. 

## AWS-Ec2 instance : 

Steps :

Login into AWS and create EC2 - t2.micro (this is enoughm for now) instance and get .pem file

Then connect EC2 via SSH using -->   ssh -i /path/to/key.pem ec2-user@instance-ip-address

sudo apt-get update

sudo apt install git curl unzip tar make sudo vim wget -y

git clone https://github.com/mahikshith/Ola_ensemble_learning.git 

touch .env

vi .env , exit :wq and then install pip --> sudo apt install python3-pip -->> pip3 install -r  requirements.txt --break-system-packages

and finally run -->> ola_flask.py to check if it running 

Update the esecurity group for a inbound rule with port  5000 , save it 

## ec2 : https://54.198.248.170/predict  [stopped the instance]

Don't let the instance run indefinitely
