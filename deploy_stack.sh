
sh prepare_env.sh
# pip3 install -r python-module-layers/requirements.txt -t ./python-module-layers/python/
sam package -t template.yaml --s3-bucket localstack-resources-bucket --s3-prefix imageupload --output-template-file package.yaml --profile localstack
sam deploy -t package.yaml   --s3-bucket localstack-resources-bucket --s3-prefix imageupload --stack-name imageupload --capabilities CAPABILITY_IAM CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND --parameter-overrides Environment=dev --profile localstack