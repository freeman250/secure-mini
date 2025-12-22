# ECS Service Deployment with Application Load Balancer

The SecureMe Mini Flask application was deployed using AWS ECS (Fargate)
with an Application Load Balancer.

Due to IAM restrictions in the lab environment, Elastic Beanstalk could
not be used. ECS with ALB was selected as an equivalent and valid
deployment option.

## Deployment details
- Cluster: secureme-mini-cluster
- Task definition: secureme-mini-task
- Service: AN-flask-app-svc
- Load balancer: an-flask-app-lb
- Container port: 5000
- Public access via ALB DNS

The application is accessible through the ALB URL and serves all
three application pages.

