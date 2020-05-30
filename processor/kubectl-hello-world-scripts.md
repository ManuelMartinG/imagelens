### Kubernetes Hello World Scripts
**source**: https://kubernetes.io/es/docs/tutorials/hello-minikube/

##### Crear un deployment
````bash
minikube start

kubectl create deployment hello-node --image=k8s.gcr.io/echoserver:1.4

kubectl get deployments
kubectl get pods
kubectl get events
kubectl config view
````
> **¿Qué es un deployment y qué es un pod?**: Un pod es un grupo de 1 o más contenedores Docker 
>con una red  o sistema de almacenamiento compartido. Comparten también una especificación
>de cómo se ejecutan estos contenedores.

##### Crear un Service
Por defecto, el pod es accedido por su dirección IP
interna dentro del clúster de Kubernetes. Para hacer que sea accesible
desde fuera de la red virtual de kubernetes, se debe exponer
el pod como un service de kubernetes.
````bash
 kubectl expose deployment hello-node --type=LoadBalancer --port=8080
service/hello-node exposed

kubectl get services
````

#### Eliminar el servicio
````bash
kubectl delete service hello-node
kubectl delete deployment hello-node
minikube stop
minikube delete
````


## Kubernetes with Python
**source**: https://kubernetes.io/blog/2019/07/23/get-started-with-kubernetes-using-python/
1. Create Dockerfile
2. Build docker image:
````bash
docker build -f Dockerfile -t hello-python:latest .
docker run -p 50002:5000 hello-python
# -p {Puerto localhost: Puerto Docker Container}
````

3. We add the file `deployment.yml` and run `kubectl config use-context docker-for-desktop`
4. Run the following to start up the cluster of nodes:
````bash
kubectl config use-context docker-for-desktop # Remember to got to Docker for Desktop an "Enable Kubernetes"
kubectl apply -f deployment.yml
kubectl get pods

# you will see something like:
NAME                            READY   STATUS    RESTARTS   AGE
hello-python-5477d55974-8679k   1/1     Running   0          27s
hello-python-5477d55974-f2lhc   1/1     Running   0          27s
hello-python-5477d55974-hcrm8   1/1     Running   0          27s
hello-python-5477d55974-w4nk4   1/1     Running   0          27s

````

#### Cómo eliminar todo
```bash
kubectl delete daemonsets,replicasets,services,deployments,pods,rc --all
```
Para parar todos los controladores de kubernetes, hay que quitar el tick de "Enable" kubernetes
en Docker Desktop.