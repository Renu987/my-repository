eksctl create cluster --name my-cluster --region us-west-2 --nodegroup-name linux-nodes --node-type t3.medium --nodes 3 --nodes-min 1 --nodes-max 4 --managed

aws eks --region us-west-2 update-kubeconfig --name my-cluster


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

kubectl apply -f deployment.yaml


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

kubectl apply -f service.yaml

kubectl get deployments
kubectl get services
