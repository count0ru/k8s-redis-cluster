NAMESPACE=$1
if [[ ! -z "$NAMESPACE" ]]; then
  NAMESPACE='--namespace='$NAMESPACE
fi
kubectl create -f redis-master.yaml $NAMESPACE
sleep 20
kubectl create -f redis-sentinel-service.yaml $NAMESPACE
sleep 20
kubectl create -f redis-controller.yaml $NAMESPACE 
sleep 20
kubectl create -f redis-sentinel-controller.yaml $NAMESPACE 
sleep 20
kubectl scale rc redis --replicas=3 $NAMESPACE
kubectl scale rc redis-sentinel --replicas=3 $NAMESPACE
sleep 20
kubectl delete pods redis-master $NAMESPACE
