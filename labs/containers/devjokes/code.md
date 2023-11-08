# 1. Build container image inside Minikube
minikube image build -t devjokes .

# 2. Run container (create Pod)
kubectl run devjokes --image devjokes --image-pull-policy IfNotPresent

# 3. Expose pod to our local network
kubectl port-forward devjokes 8000

# 4. Open browser 
Open browser at http://localhost:8080
