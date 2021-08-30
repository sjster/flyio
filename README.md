

### Instructions

1. Initialize with flyctl init

2. Run set_secrets.sh to access the Wasabi buckets. This is not saved in the Github repository (obviously)

3. Run flyctl deploy to deploy the app. You can use a local builder or a remote builder. The remote builder uses bandwidth that will count against your quota. 

If the local builder runs out of space 
 
  docker system prune --volumes

Check the status of your app
 
 flyctl status

Check the app logs

 flyctl logs

SSH to the app

 flyctl console ssh

Destroy the app

 flyctl destroy APPNAME
