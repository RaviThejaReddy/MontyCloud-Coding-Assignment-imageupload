aws configure set region us-east-1 --profile localstack
aws configure set AWS_ACCESS_KEY_ID test --profile localstack
aws configure set AWS_SECRET_ACCESS_KEY test --profile localstack
aws configure set aws_session_token test --profile localstack
aws configure set aws_security_token test --profile localstack
aws configure set endpoint_url http://localhost:4566 --profile localstack
aws s3api create-bucket --bucket localstack-resources-bucket --profile localstack
aws s3 ls --profile localstack
