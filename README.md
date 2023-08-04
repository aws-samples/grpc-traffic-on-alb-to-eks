## grpc-traffic-on-alb-to-eks

Use the below commands to deploy the sample. Make sure you substitute the values accordingly. 

export EcrUrl="<AccountId>.dkr.ecr.<AWS-Region>.amazonaws.com/helloworld-grpc:1.0"
export AcmArn="arn:aws:acm:<AWS-Region>:<AccountId>:certificate/dd12f017-7caf-410c-b30f-646fff5b3f96"
export DnsHostName="<DNS-HostName>"
envsubst < ./kubernetes/grpc-sample.yaml | kubectl apply -f -

If you dont have `envsubst`, then replace the below variables placeholders in the `kubernetes/grpc-sample.yaml` file with the actual values: 

${EcrUrl} with ECR image Uri --> "<AccountId>.dkr.ecr.<AWS-Region>.amazonaws.com/helloworld-grpc:1.0"

${AcmArn} with ACM ARN --> "arn:aws:acm:<AWS-Region>:<AccountId>:certificate/dd12f017-7caf-410c-b30f-646fff5b3f96"

${DnsHostName} with a valid DNS Host Name in the following example format --> "www.example.com" or "amazon.com" 

## Security

See [CONTRIBUTING](CONTRIBUTING.md#security-issue-notifications) for more information.

## License

This library is licensed under the MIT-0 License. See the LICENSE file.

