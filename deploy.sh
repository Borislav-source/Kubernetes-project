docker build -t abadoom/worker1:latest -t abadoom/worker1:$SHA -f ./Prime/Dockerfile ./Prime
docker build -t abadoom/worker2:latest -t abadoom/worker2:$SHA -f ./Fibonacci/Dockerfile ./Fibonacci
docker build -t abadoom/router:latest -t abadoom/router:$SHA -f ./Router/Dockerfile ./Router
docker push abadoom/worker1:latest
docker push abadoom/worker2:latest
docker push abadoom/router:latest
docker push abadoom/worker1:$SHA
docker push abadoom/worker2:$SHA
docker push abadoom/router:$SHA
kubectl apply -f k8s
kubectl set image deployments/worker1-deployment server=abadoom/worker1:$SHA
kubectl set image deployments/worker2-deployment server=abadoom/worker2:$SHA
kubectl set image deployments/router-deployment server=abadoom/router:$SHA