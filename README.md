# Minio-OW-Tester

### Requirementes
 - nodejs
 - pipenv
 - python3

# Setup
1. install [serverless framework](https://www.serverless.com/framework/docs/getting-started/)
2. run `npm install`
3. run `sls deploy`

# Usage 
 `sls invoke -f tester -p '{"address":"","port":"","key":"","secret":"",}'`

 If you get an error use 
 `wsk activation logs -l` to see what happend if minio is reachable you'll see: 
 ``` 
{
    "mTest": true,
    "pTest": true
}
 ```

 pTest is a simple ping test to the host/port and mTest uses the minio client to list all avalible dicrectories.

 # Cleanup
 1. run `sls remove`
 2. run `rm -rf node_modules` - if you want to remove unassesary files

