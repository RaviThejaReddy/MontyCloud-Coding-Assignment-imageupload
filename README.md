# MontyCloud-Coding-Assignment-imageupload

You are developing the service layer of an application like Instagram. You are working
on a module which is responsible for supporting image upload and storage in the
Cloud. Along with the image, its metadata must be persisted in a NoSQL storage.

Multiple users are going to use this service at the same time. For this reason, the
service should be scalable.

The team currently uses API Gateway, Lambda Functions, S3 and DynamoDB services.
Language: Python3.7+

Tasks:
1. Create APIs for:
1. Uploading image with metadata
2. List all images, support at least two filters to search
3. View/download image
4. Delete an image
2. Write unit tests to cover all scenarios
3. API documentation and usage instructions

Development Environment
Use LocalStack to create a local development environment. If you are new to
LocalStack, refer to the below articles:
• How to use LocalStack with Docker compose
• How to use AWS CLI with LocalStack
• What is LocalStack?


# how to use this code
to install localstack -> install docker as a prerequirements
```pip3 install --upgrade localstack```

run below command to start the localstack
```sh start_local_stack.sh```

to deploy stack run below command
```sh delpoy_stack.sh```


import it and use it to make calls
get rest-api-id from localstack and update it in postman collection  -> ImageStorageApiGateway.postman_collection.json