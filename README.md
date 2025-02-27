Download eksctl in your local using below commands:
```
wget https://github.com/weaveworks/eksctl/releases/latest/download/eksctl_Linux_amd64.tar.gz -O eksctl.tar.gz
tar -xzf eksctl.tar.gz
sudo mv eksctl /usr/local/bin
eksctl version
```
Download kubectl in your local using below commands:

```
curl -LO "https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl
chmod +x ./kubectl
sudo mv ./kubectl /usr/local/bin/kubectl
kubectl version --client
```

--------------------------------------------------------------
eksctl create cluster --name demo-cluster --region us-east-1 --fargate

eksctl create fargateprofile \
    --cluster demo-cluster \
    --region us-east-1 \
    --name alb-sample-app \
    --namespace game-2048

kubectl apply -f https://raw.githubusercontent.com/kubernetes-sigs/aws-load-balancer-controller/v2.5.4/docs/examples/2048/2048_full.yaml

export cluster_name=demo-cluster

oidc_id=$(aws eks describe-cluster --name $cluster_name --query "cluster.identity.oidc.issuer" --output text | cut -d '/' -f 5) 

eksctl utils associate-iam-oidc-provider --cluster $cluster_name --approve

curl -O https://raw.githubusercontent.com/kubernetes-sigs/aws-load-balancer-controller/v2.11.0/docs/install/iam_policy.json


aws iam create-policy \
    --policy-name AWSLoadBalancerControllerIAMPolicy \
    --policy-document file://iam_policy.json

aws iam attach-role-policy \
    --policy-arn arn:aws:iam::aws:policy/AmazonEKSALBIngressControllerPolicy \
    --role-name AmazonEKSLoadBalancerControllerRole

kubectl rollout restart deployment aws-load-balancer-controller -n kube-system


eksctl create iamserviceaccount \
  --cluster=<your-cluster-name> \
  --namespace=kube-system \
  --name=aws-load-balancer-controller \
  --role-name AmazonEKSLoadBalancerControllerRole \
  --attach-policy-arn=arn:aws:iam::<your-aws-account-id>:policy/AWSLoadBalancerControllerIAMPolicy \
  --approve


helm repo add eks https://aws.github.io/eks-charts

helm repo update eks

helm install aws-load-balancer-controller eks/aws-load-balancer-controller \            
  -n kube-system \
  --set clusterName=<your-cluster-name> \
  --set serviceAccount.create=false \
  --set serviceAccount.name=aws-load-balancer-controller \
  --set region=<region> \
  --set vpcId=<your-vpc-id>

kubectl get deployment -n kube-system aws-load-balancer-controller

eksctl delete cluster --name demo-cluster --region us-east-1

--------------------------------------------------------------------

eksctl create cluster --name my-cluster --region us-west-2 --nodegroup-name linux-nodes --node-type t3.medium --nodes 3 --nodes-min 1 --nodes-max 4 --managed

aws eks --region us-west-2 update-kubeconfig --name my-cluster

```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-deployment
spec:
  replicas: 3
  selector:
    matchLabels:
      app: my-app
  template:
    metadata:
      labels:
        app: my-app
    spec:
      containers:
      - name: my-container
        image: <your-ecr-repo-url>:<tag>
        ports:
        - containerPort: 80
```

kubectl apply -f deployment.yaml

```
apiVersion: v1
kind: Service
metadata:
  name: my-service
spec:
  type: LoadBalancer
  selector:
    app: my-app
  ports:
  - protocol: TCP
    port: 80
    targetPort: 80
```

kubectl apply -f service.yaml

kubectl get deployments

kubectl get services
