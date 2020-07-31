# SAFE - Safe Adaptable and Flexible Education
## This solution has been brainstomred and created by technologists from Cognizant as part of IBM Code For Challenge 2020.<br>

# Authors
* J.Shree Krishna Priya<br>
* Amit Aman<br>
* Gaurang Sharma<br>
* Manish Singh<br>
* Mudita Bhatia

# Contents
1. [Overview](#Overview)<br>
2. [The Idea](#The-Idea)<br>
3. [How it works technically?](#How-it-workstechnically?)<br>
4. [How SAFE application works?](#How-SAFE-application-works?)<br>
4. [Architecture Diagrams](#Architecture-Diagrams)<br>
5. [Documents](#Documents)<br>
6. [Technology](#Technology)<br>
7. [Upcoming Features](#Upcoming-Features)<br>

# Overview 

## What is the problem?

**COVID -19** has **presented us** with **multiple opportunities to explore the technology arena**, especially to **continue education**.<br> Being in a state of **indefinite lock down and social distancing** to be maintained, **we cannot reach our educational institutions**. Hence, we have to take steps to **ensure** that the **education reaches all**, because 
**“Education is the passport to the future, for tomorrow belongs to those who prepare for today”**. Be it professional or personal, **online mode of learning is now an inevitable part of our lifestyle**. We all explore a pleothera of online portals. <br>

**Most of the courses and educational videos** are provided **in English and in selective international languages**. Many people find it **difficult to pursue courses to completion.** With constant need to upgrade professional skills on various skill sets, people find it **difficult to pursue courses to completion!!!**.<br> 

**With SAFE we break the language barriers. Safe Adaptable and Flexible Education, is a universal solution to solve the problems of many seeking education with an intent of inclusion.**<br>

# The Idea
We did a survey among our circle of friends to see what they look for in an online portal. We found that majority of Folks are struggling to understand the concepts, since the videos provided to them are recorded in English. While we came across a lot of features, the most sought after feature was **"learning in native language."** <br>

**A feature that keeps the interest alive, connects with the learner and help them grasp the concept.**<br>
* SAFE is a **bridge between the Learners and online learning platform.**<br>
* **Overcomes language barrier instantly.**<br>
* Can be **integrated with 9 out of 10 online platforms and deliver courses in 125 different languages with as is architecture**.

# How it works technically?

SAFE does this by **using Google APIs – speech to text and text to speech**, which is powered by Google’s unmatched number of training data available through Google platform.
This solution can be **integrated with any learning platform or** can be used as a **stand-alone application**, where we can **upload a video and get output video in the desired language**. The application is **hosted in IBM Cloud for seameless performance**. 

# How SAFE application works? 
* SAFE is **a web based application**.<br>
* Allows User to **browse and select a video file**.<br>
* Allows User to **select a language in which the output is desired**.<br>
* Post request submission, **video is then downloaded and played in selected language**.<br>

# Diagram
![Architecture Diagaram](https://github.com/singhmanish1212/call_for_code2020/blob/dev/SAFEArchitecture_v7.jpg)

## How it works internally?

 * **Upload video in SAFE application, hosted by IBM cloud Foundry**.<br>
 * **Transcript is created from the video using Google Speech-To-text (English Speech to English text) API**.<br>
 * **Target language transcript is created from the English Transcript**.<br>
 * **Audio translation of Target language is created from the converted Language transcript using Google text to Speech API**.<br>
 * **Target language subtitles are created using Python**.<br>
 * **The translated audio, original video and the translated subtitles are combined to form a single video using MoviPy**.<br>
 * **The output is provided to the learner**.

# Documents

1. [Click here to read detailed application FAQ's](../SAFEApplicationFAQ.txt)

# Technology

* **IBM Cloud Services**<br>
**SAFE being an universal solution, IBM Cloud Foundry provides an option to deploy the application anywhere in the world and help us scale up without worrying about the same**. The **ease to run the app locally** and then **hosting in IBM cloud is one of the greatest features** that **helped us to validate the solution locally** and then going for the **hosting in the cloud**. The **fault tolerance and scalability are the two factors, why we considered IBM Cloud Foundry** and by far is the **best solution for our application when we scale SAFE to more languages and locations**.

* **Google API**<br>
SAFE uses **Google APIs Text to speech and speech to text**, as a major part of the architecture. **Google Cloud Text-to-Speech enables SAFE to synthesize natural-sounding speech with 100+ voices, available in multiple languages and variants**. It **applies DeepMind’s groundbreaking research in WaveNet and Google’s powerful neural networks to deliver the highest fidelity possible**. The **Speech to text API will help SAFE Support global user base with Speech-to-Text’s extensive language support in over 125 languages and variants**.

# Upcoming Features
While SAFE web application is handling one National language and one international language for now, it is **scalable to 125 languages with our current architecture, as is**.
We strive to achieve **enhanced accuracy** in future as we continue to train our model. SAFE will be **available as a mobile application too**, since the user base for the hand-held devices is more compared to the personal devices like laptops and desktops. Adding **LIVE streaming events like online classes, conferences will also be a future enhancement**.
SAFE can also be scaled to **monitor user behaviour** while taking the courses or attending the classes and **suggest some recreational or refreshing activities**. 
It will also be able to **suggest exercises and physical activity**, if the user is taking the course for more than particular time.

SAFE is a **universal, all-inclusive platform, breaking the language barrier** ready to take the education system by storm. 
**Because, for team SAFE, All Lives Matter!!**
