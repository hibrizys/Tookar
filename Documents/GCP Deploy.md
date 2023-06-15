# Deploying to Google Cloud Platform

Here are the steps to manually deploy our back-end to Google Cloud Platform.

GCP Services used:

- App Engine
- CLoud SQL
- Vertex AI
- CLoud Storage

## App Engine

- Create Application on App Engine

![AppEngine1](https://github.com/hibrizys/imageDocsTookar/blob/main/appengine1.png)

- Configure Application and select region asia-southeast2

![AppEngine2](https://github.com/hibrizys/imageDocsTookar/blob/main/appengine2.png)

- Configure the Resources with language Node.js

![AppEngine3](https://github.com/hibrizys/imageDocsTookar/blob/main/appengine3.png)

- dont forget put app.yaml to your folder API in GCP

![AppEngine4](https://github.com/hibrizys/imageDocsTookar/blob/main/appengine4.png)

- run " gcloud app deploy " on terminal

![AppEngine5](https://github.com/hibrizys/imageDocsTookar/blob/main/appengine5.png)

- and then u can see the output

![AppEngine6](https://github.com/hibrizys/imageDocsTookar/blob/main/appengine6.png)

