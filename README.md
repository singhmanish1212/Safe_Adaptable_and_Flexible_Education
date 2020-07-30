
#Quick Intro to SAFE
> SAFE is a bridge between the Learners and online learning platform. 
> Overcomes language barrier instantly.
> Can be integrated with 9 out of 10 online platforms and deliver courses in 125 different languages with as is architecture. 

#SAFE OverView
>SAFE Application UI is both desktop and UI compatible.
>User must browse and select a video file. 
>User must select the language in which the output is desired. 
>User submits the request.
>Video is then played in the selected language with 80 to 90% accuracy. 

#Technicality Behind

#Known Issues

#Upcoming Features
>Integration of AI
>Inetegration of other skilled activities to keep the Learner engaged during breaks.
>Add features for differently skilled individuals. 

### Frontend UI

### Frontend UI Development
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
