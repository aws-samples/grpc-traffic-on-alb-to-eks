# grpc-traffic-on-alb-to-eks

This repository contains an example project for deploying a gRPC service on Amazon EKS and exposing it via an Application Load Balancer (ALB).

## About this Repo

This repo is an example for deploying a gRPC service on Amazon EKS and exposing it via an Application Load Balancer (ALB). It is intended to be used as a reference for building your own gRPC service on Amazon EKS and access it via ALB. 

We welcome contributions to this repo in the form of fixes to existing examples or addition of new examples. For more information on contributing, please see [CONTRIBUTING](CONTRIBUTING.md#security-issue-notifications) for more information.

## Examples

Use the below commands to deploy the sample. Make sure you substitute the values accordingly. 

```export ECR_URL="<AccountId>.dkr.ecr.<AWS-Region>.amazonaws.com/helloworld-grpc:1.0"
export ACM_ARN="arn:aws:acm:<AWS-Region>:<AccountId>:certificate/dd12f017-7caf-410c-b30f-646fff5b3f96"
export DNS_HOSTNAME="<DNS-HostName>"
envsubst < ./kubernetes/grpc-sample.yaml | kubectl apply -f -
```

If you dont have `envsubst`, then replace the below variables placeholders in the `kubernetes/grpc-sample.yaml` file with the actual values: 

```${ECR_URL} with ECR image Uri --> "<AccountId>.dkr.ecr.<AWS-Region>.amazonaws.com/helloworld-grpc:1.0"

${ACM_ARN} with ACM ARN --> "arn:aws:acm:<AWS-Region>:<AccountId>:certificate/dd12f017-7caf-410c-b30f-646fff5b3f96"

${DNS_HOSTNAME} with a valid DNS Host Name in the following example format --> "www.example.com" or "amazon.com" 
```
## License

This library is licensed under the MIT-0 License. See the LICENSE file.

