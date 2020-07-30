# SAFE - Safe Adaptable and Flexible Education
## This solution has been brainstomred and created by technologists from Cognizant as part of IBM Code For Challenge 2020.<br>

# Authors
* J.Shree Krishna Priya<br>
* Amit Aman<br>
* Gaurang Sharma<br>
* Manish Singh<br>
* Mudita Bhatia

# Contents
1. Overview <br>
2. The Idea <br>
3. How it works<br>
4. Diagrams<br>
5. Documents<br>
6. Technology<br>
7. Getting started<br>
8. Resources<br>
9. License<br>

# Overview

<h1 style="font-size:5px;">What is the problem?</h1><br>
COVID -19 has presented us with multiple opportunities to explore the technology arena, especially to **continue education**.<br> Being in a state of indefinite lock down and social distancing to be maintained, **we cannot reach our educational institutions**. Hence, we have to take steps to **ensure** that the **education reaches all**, because 
**“Education is the passport to the future, for tomorrow belongs to those who prepare for today”**. Be it professional or personal, **online mode of learning is now an inevitable part of our lifestyle**. We all explore a pleothera of online portals. <br>

**Most of the courses and educational videos** are provided **in English and in selective international languages**. Many people find it **difficult to pursue courses to completion.** It’s ok for some time. However, with a constant need to upgrade professional skills on various skill sets, people find it **difficult to pursue courses to completion**.<br> 

**With SAFE we break the language barriers**. <br>
**Safe Adaptable and Flexible Education, is a universal solution to solve the problems of many seeking education with an intent of inclusion.**<br>

<h1 style="font-size:15px;">Salient Features</h1><br>
SAFE Application UI is both desktop and UI compatible.<br>User must browse and select a video file.<br>User must select the language in which the output is desired.
<br>User submits the request.<br>Video is then played in the selected language with 80 to 90% accuracy.<br>

<h1 style="font-size:15px;">How can technology help?</h1><br>

**to be updated**<br>

**Mobile, web, and cloud services enable rapid deployment of applications that can empower cooperation in the community. **Watson Assistant is a service on IBM Cloud that allows you to build, train, and deploy conversational interactions into any application, device, or channel.
Creating a chatbot using Watson Assistant can help you address the issues that your users may face while trying to gather the necessary information. Embedding location/routing services (like HERE) can enhance such applications, giving optimum guidance so that they are outside of their isolation location for the minimum amount of time.**

<h1 style="font-size:15px;">The Idea</h1><br>
We did a survey among our circle of friends to see what they look for in an online portal. We found that majority of Folks are struggling to understand the concepts, since the videos provided to them are recorded in English. While we came across a lot of features, the most sought after feature was **"learning in native language."** <br>

**A feature that keeps the interest alive, connects with the learner and help them grasp the concept.**<br>
SAFE is a bridge between the Learners and online learning platform.<br> Overcomes language barrier instantly.<br> Can be integrated with 9 out of 10 online platforms and deliver courses in 125 different languages with as is architecture.

<h1 style="font-size:15px;">How it works</h1><br>
SAFE does this by using Google APIs – speech to text and text to speech, which is powered by Google’s unmatched number of training data available through Google platform.
This solution can be integrated with any learning platform or can be used as a stand-alone application, where we can upload the video or paste the URL of the video in the site and get the output video in the desired language. 

<h1 style="font-size:15px;">Diagram</h1><br>
**paste architecture diagram here**

<h1 style="font-size:15px;">Documents</h1><br>
**to be updated**<br>
Trusted sources for COVID-19 Information:<br>CDC COVID-19 FAQ<br>WHO COVID-19 page<br>Johns Hopkins University Coronavirus (includes tracking map)<br>National Foundation for Infectious Diseases

<h1 style="font-size:15px;">Technology</h1><br>
**to be updated**<br>
IBM Cloud Services<br>Google API

**How-to**<br>
<h1 style="font-size:15px;">Technology</h1><br>
**to be updated**<br>
Create a machine learning powered web app to answer questions
Learning path: Getting started with Watson Assistant
Train a speech-to-text model
Enhance customer helpdesks with Smart Document Understanding using webhooks in Watson Assistant
Watson Voice Agent
Getting Started with Watson Voice Agent
Making Programmatic Calls from Watson Assistant
IBM Cloud Voice Agent with Twilio
Build a Chatbot For Your Mobile App
Build a cross-platform mobile app using React Native
Building successful mobile apps article series
Chat Bot Slack Integration
Chat Bot Slack deployment
Node-RED Slack integration

**HERE Technologies**<br>
**to be updated**<br>

HERE.com API Key
HERE Maps
HERE Routing
Integrate interactive maps and location features into your application

<h1 style="font-size:15px;">Getting started</h1><br>

**to be updated**<br>
**Prerequisites**<br>
Register for an IBM Cloud account.
Install and configure IBM Cloud CLI.
Register for a HERE account.
Install React Native CLI dependencies. See the React Native documentation for the exact steps and requirements based on your Operating System and Target OS. For example: 
iOS on macOS 
Node.js
Watchman
Xcode
CocoaPods
Android on Windows 
Node.js
Python 2
Java Development Kit
Android Studio - add Android 9 (Pie) SDK & configure ANDROID_HOME
Create an Android Virtual Device (AVD) - with Pie image (API Level 28)
Clone the repository.
**Steps**
Set up an instance of Watson Assistant.
Provision a CouchDB instance using Cloudant.
Generate an API Key from the HERE Developer Portal.
Run the server.
**Run the mobile application.**
**to be updated**
1. Set up an instance of Watson Assistant
Log in to IBM Cloud and provision a Watson Assistant instance.
Provision an instance of Watson Assistant from the IBM Cloud catalog.
Launch the Watson Assistant service.
Create an Assistant.
Add a dialog skill to the Assistant by importing the starter-kit-cooperation-dialog-skill.json file.
Go back to All Assistants page, open Settings from the action menu ( ⋮ ) and click on API Details.
Note the Assistant ID, API Key, and Assistant URL. For Assistant URL, make note of the base URL/domain (e.g., https://api.us-south.assistant.watson.cloud.ibm.com or https://api.eu-gb.assistant.watson.cloud.ibm.com) and not the full directory/path. You will need all three of these values in Step 4 below.
Go to Preview Link to get a link to test and verify the dialog skill.
2: Provision a CouchDB instance using Cloudant
Log into the IBM Cloud and provision a CouchDB instance using Cloudant.
From the catalog, select Databases and then the Cloudant panel.
Once selected, you can choose your Cloudant plan -- there is a free tier for simple testing that is sufficient to run this CIR example. You should choose an appropriate region, give the service a name, and it is recommended you choose Use only IAM under Available authentication methods. You can leave the other settings with their defaults. Click the blue Create button when ready.
Once your Cloudant instance has been created, you need to create a service credential that the CIR API Server can use to communicate with it. By selecting your running Cloudant instance, you can choose Service credentials from the left-hand menu. Create a new service credential and give it a name (it doesn't matter what you call it).
Once created, you can display the credentials by selecting view service credentials, and then copy the credential, so you are ready to paste it into the code of the API server in Step 4.
3. Generate an API Key from the HERE Developer Portal
The application uses HERE Location Services for maps, searching, and routing.
To access these services, you'll need an API key. Follow the instructions outlined in the HERE Developer Portal to generate a JavaScript API key.
4. Run the server
To set up and launch the server application:
Go to the starter-kit/server-app directory of the cloned repo.
Copy the .env.example file in the starter-kit/server-app directory, and create a new file named .env.
Edit the newly created .env file and update the ASSISTANT_URL, ASSISTANT_ID, and ASSISTANT_IAM_APIKEY with the values from the dialog skill's API Detail page in Watson Assistant, from Step 1. Also, update the CLOUDANT_ID and CLOUDANT_IAM_APIKEY with the values from the service credential you created in Step 2. (Note that the username from the credential is what should be used for the CLOUDANT_ID.)
Edit the name value in the manifest.yml file to your application name (for example, my-app-name).
From a terminal: 
Go to the starter-kit/server-app directory of the cloned repo.
Install the dependencies: npm install.
Launch the server application locally or deploy to IBM Cloud: 
To run locally: 
Start the application: npm start.
The server can be accessed at http://localhost:3000.
To deploy to IBM Cloud: 
Log in to your IBM Cloud account using the IBM Cloud CLI: ibmcloud login.
Target a Cloud Foundry org and space: ibmcloud target --cf.
Push the app to IBM Cloud: ibmcloud app push.
The server can be accessed at a URL using the name given in the manifest.yml file (for example, https://my-app-name.bluemix.net).
5. Run the mobile application
To run the mobile application (using the Xcode iOS Simulator or Android Studio Emulator):
Go to the starter-kit/mobile-app directory of the cloned repo.
Copy the .env.example file in the starter-kit/mobile-app directory, and create a file named .env.
Edit the newly created .env file: 
Update the STARTER_KIT_SERVER_URL with the URL to the server app launched in the previous step. 
Note: If you are running the server locally and testing with the Android Emulator set the STARTER_KIT_SERVER_URL using the local machine's URL (e.g., http://10.0.2.2:3000) instead of localhost
Update the HERE_APIKEY with the API key generated in the HERE Developer Portal.
From a terminal: 
Go to the starter-kit/mobile-app directory.
Install the dependencies: npm install.
iOS only: Go to the ios directory: cd ios.
iOS only: Install pod dependencies: pod install.
iOS only: Return to the mobile-app directory: cd ../.
Launch the app in the simulator/emulator: 
iOS only: npm run ios 
Note: You should be running at least iOS 13.0. The first time you launch the simulator, you should ensure that you set a Location in the Features menu.
Android only: npm run android 
Note: Your Android Studio needs to have the Android 9 (Pie) SDK and a Pie API Level 28 virtual device
With the application running in the simulator/emulator, you should be able to navigate through the various screens:
 
<h1 style="font-size:15px;">Resources</h1><br>
**to be updated**<br>
IBM Cloud
Watson Assistant
IBM Cloudant
HERE Location Services
Node.js
React Native
IBM Blockchain for Developers
License
This solution starter is made available under the Apache 2 License.

<h1 style="font-size:15px;">Licenses</h1><br>
**to be updated**<br>

<h1 style="font-size:15px;">Technicality Behind</h1><br>
**to be updated**<br>


<h1 style="font-size:15px;">Known Issues</h1><br>
**to be updated**

<h1 style="font-size:15px;">Upcoming Features</h1><br>
While SAFE web application is handling one National language and one international language for now, it is **scalable to 125 languages with our current architecture, as is**.
We strive to achieve **enhanced accuracy** in future as we continue to train our model. SAFE will be **available as a mobile application too**, since the user base for the hand-held devices is more compared to the personal devices like laptops and desktops. Adding **LIVE streaming events like online classes, conferences will also be a future enhancement**.
SAFE can also be scaled to **monitor user behaviour** while taking the courses or attending the classes and **suggest some recreational or refreshing activities**. 
It will also be able to **suggest exercises and physical activity**, if the user is taking the course for more than particular time.

SAFE is a **universal, all-inclusive platform, breaking the language barrier** ready to take the education system by storm. 
**Because, for team SAFE, All Lives Matter!!**

**to be updated**
*>Integration of AI*>Inetegration of other skilled activities to keep the Learner engaged during breaks.*>Add features for differently skilled individuals.


**--------------------------------------------------------------------------------------------------------------------------------------------------------**<br>
**--------------------------------------------------------------------------------------------------------------------------------------------------------**<br>
**--------------------------------------------------------------------------------------------------------------------------------------------------------**<br>
**--------------------------------------------------------------------------------------------------------------------------------------------------------**<br>
**--------------------------------------------------------------------------------------------------------------------------------------------------------**<br>
**--------------------------------------------------------------------------------------------------------------------------------------------------------**<br>
**--------------------------------------------------------------------------------------------------------------------------------------------------------**<br>
**--------------------------------------------------------------------------------------------------------------------------------------------------------**<br>
**--------------------------------------------------------------------------------------------------------------------------------------------------------**<br>
**--------------------------------------------------------------------------------------------------------------------------------------------------------**<br>
**--------------------------------------------------------------------------------------------------------------------------------------------------------**<br>
**--------------------------------------------------------------------------------------------------------------------------------------------------------**<br>

**Revalidate if the below content needs to be retained**


**Frontend UI**
**to be updated**

**Frontend UI Development**
**to be updated**
1. If you have not done so already, install [`Node.js`](https://nodejs.org) and [`Yarn`](https://classic.yarnpkg.com/en/docs/install/).
2. In a new terminal, change to the `frontend` directory from the project root and install the dependencies:
    ```bash 
    cd frontend
    yarn install
    ```  
3. Launch the frontend application:  
    **Compiles and hot-reloads for development**
    ```bash
    yarn serve
    ```
    **Compiles and minifies for production**
    ```bash
    yarn build
   ```
    **Lints and fixes files**
    ```bash
    yarn lint
    ```
The frontend UI is now running at `http://localhost:8080/` in your browser. 

## 5. Language Translator Extension

This tutorial shows you how to create a Watson Language Translator service and write the necessary server side code to translate video transcriptions. The front-end UI implementation is left as an extension for you to implement yourself. Hint - inspecting the `upload_video` function in `server/routes/index.py`, you can see that the server side expects a `source` and a `target` language as part of the POST request form data to `/upload_video`. Supported language models are provided at [https://localhost:3000/language_models](http://localhost:3000/language_models) once your server is running.
## 6. Deploy the app

The following instructions apply to deploying the Python Flask server. To deploy the frontend UI, follow the [Node.js build and deploy tutorial](https://developer.ibm.com/node/getting-started-node-js-ibm-cloud/).
### Deploying to IBM Cloud

You can [deploy this application to IBM Cloud](https://cloud.ibm.com/developer/appservice/starter-kits/python-flask-app) or [build it locally](#building-locally) by cloning the repo first. Once your app is live, you can access the `/health` endpoint to build out your cloud native application.

Use the button below to deploy this same application to IBM Cloud. This option creates a deployment pipeline, complete with a hosted GitLab project and DevOps toolchain. You will have the option of deploying to either Cloud Foundry or a Kubernetes cluster. [IBM Cloud DevOps](https://www.ibm.com/cloud/devops) services provide toolchains as a set of tool integrations that support development, deployment, and operations tasks inside IBM Cloud. 
<p align="center">
    <a href="https://cloud.ibm.com/developer/appservice/starter-kits/python-flask-app">
    <img src="https://cloud.ibm.com/devops/setup/deploy/button_x2.png" alt="Deploy to IBM Cloud">
    </a>
</p>
### Building locally
To get started building this application locally, you can either run the application natively or use the [IBM Cloud Developer Tools](https://cloud.ibm.com/docs/cli?topic=cloud-cli-getting-started) for containerization and easy deployment to IBM Cloud.
#### Native application development
Native application development was covered in step 4 above when you installed and ran the app. Your server is running at: `http://localhost:3000/` in your browser.
There are two different options for debugging a Flask project:
1. Run `python manage.py runserver` to start a native Flask development server. This comes with the Werkzeug stack-trace debugger, which will present runtime failure stack-traces in-browser with the ability to inspect objects at any point in the trace. For more information, see [Werkzeug documentation](http://werkzeug.pocoo.org/).

2. Run `python manage.py debug` to run a Flask development server with debug exposed, but the native debugger/reloader turned off. This grants access for an IDE to attach itself to the process (that is, in PyCharm, use `Run` -> `Attach to Local Process`).
You can also verify the state of your locally running application using the Selenium UI test script included in the `scripts` directory.
> **Note for Windows users:** `gunicorn` is not supported on Windows. You can start the server with `python manage.py run` on your local machine or build and start the Dockerfile.

#### IBM Cloud Developer Tools

# Node.js getting started application
The Getting Started tutorial for Node.js uses this sample application to provide you with a sample workflow for working with any Node.js app on IBM Cloud or in IBM Cloud Private; you set up a development environment, deploy an app locally and on the cloud, and then integrate a IBM Cloud database service in your app.

The Node.js app uses [Express Framework](https://expressjs.com) and [Cloudant noSQL DB service](https://console.bluemix.net/catalog/services/cloudant-nosql-db) or the [MongoDB Service](http://mongodb.github.io/node-mongodb-native/) to add information to a database and then return information from a database to the UI. To learn more about how the app connects to Cloudant, see the [Cloudant library for Node.js](https://www.npmjs.com/package/cloudant).

<p align="center">
  <img src="https://raw.githubusercontent.com/IBM-Cloud/get-started-java/master/docs/GettingStarted.gif" width="300" alt="Gif of the sample app contains a title that says, Welcome, a prompt asking the user to enter their name, and a list of the database contents which are the names Joe, Jane, and Bob. The user enters the name, Mary and the screen refreshes to display, Hello, Mary, I've added you to the database. The database contents listed are now Mary, Joe, Jane, and Bob.">
</p>

## Before you begin

You'll need a [IBM Cloud account](https://console.ng.bluemix.net/registration/), [Git](https://git-scm.com/downloads), [Cloud Foundry CLI](https://github.com/cloudfoundry/cli#downloads), and [Node](https://nodejs.org/en/) installed. If you use [IBM Cloud Private](https://www.ibm.com/cloud-computing/products/ibm-cloud-private/), you need access to the [IBM Cloud Private Cloud Foundry](https://www.ibm.com/support/knowledgecenter/en/SSBS6K_2.1.0/cloud_foundry/overview.html) environment.

## Instructions

**IBM Cloud Cloud Foundry**: [Getting started tutorial for Node.js](https://console.bluemix.net/docs/runtimes/nodejs/getting-started.html).


**IBM Cloud Kubernetes Service**: [README-kubernetes.md](README-kubernetes.md)

**IBM Cloud Private**: The starter application for IBM Cloud Private guides you through a similar process. However, instead of hosting both your service and application in the same cloud environment, you use a user-provided service. This guide shows you how to deploy your application to IBM Cloud Private and bind it to a Cloudant Database in IBM Cloud. For the complete procedure, see [Working with user-provided services and the Node.js starter app](https://www.ibm.com/support/knowledgecenter/SSBS6K_2.1.0/cloud_foundry/buildpacks/buildpacks_using_nodejsapp.html).









# Node.js getting started application
The Getting Started tutorial for Node.js uses this sample application to provide you with a sample workflow for working with any Node.js app on IBM Cloud or in IBM Cloud Private; you set up a development environment, deploy an app locally and on the cloud, and then integrate a IBM Cloud database service in your app.

The Node.js app uses [Express Framework](https://expressjs.com) and [Cloudant noSQL DB service](https://console.bluemix.net/catalog/services/cloudant-nosql-db) or the [MongoDB Service](http://mongodb.github.io/node-mongodb-native/) to add information to a database and then return information from a database to the UI. To learn more about how the app connects to Cloudant, see the [Cloudant library for Node.js](https://www.npmjs.com/package/cloudant).

<p align="center">
  <img src="https://raw.githubusercontent.com/IBM-Cloud/get-started-java/master/docs/GettingStarted.gif" width="300" alt="Gif of the sample app contains a title that says, Welcome, a prompt asking the user to enter their name, and a list of the database contents which are the names Joe, Jane, and Bob. The user enters the name, Mary and the screen refreshes to display, Hello, Mary, I've added you to the database. The database contents listed are now Mary, Joe, Jane, and Bob.">
</p>

## Before you begin

You'll need a [IBM Cloud account](https://console.ng.bluemix.net/registration/), [Git](https://git-scm.com/downloads), [Cloud Foundry CLI](https://github.com/cloudfoundry/cli#downloads), and [Node](https://nodejs.org/en/) installed. If you use [IBM Cloud Private](https://www.ibm.com/cloud-computing/products/ibm-cloud-private/), you need access to the [IBM Cloud Private Cloud Foundry](https://www.ibm.com/support/knowledgecenter/en/SSBS6K_2.1.0/cloud_foundry/overview.html) environment.

## Instructions

**IBM Cloud Cloud Foundry**: [Getting started tutorial for Node.js](https://console.bluemix.net/docs/runtimes/nodejs/getting-started.html).


**IBM Cloud Kubernetes Service**: [README-kubernetes.md](README-kubernetes.md)

**IBM Cloud Private**: The starter application for IBM Cloud Private guides you through a similar process. However, instead of hosting both your service and application in the same cloud environment, you use a user-provided service. This guide shows you how to deploy your application to IBM Cloud Private and bind it to a Cloudant Database in IBM Cloud. For the complete procedure, see [Working with user-provided services and the Node.js starter app](https://www.ibm.com/support/knowledgecenter/SSBS6K_2.1.0/cloud_foundry/buildpacks/buildpacks_using_nodejsapp.html).
