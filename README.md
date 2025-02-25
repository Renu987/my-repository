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
