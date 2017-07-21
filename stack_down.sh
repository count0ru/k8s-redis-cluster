NAMESPACE=$1
if [[ ! -z "$NAMESPACE" ]]; then
  NAMESPACE='--namespace='$NAMESPACE
fi
kubectl delete -f redis-sentinel-controller.yaml $NAMESPACE 
kubectl delete -f redis-controller.yaml $NAMESPACE 
kubectl delete -f redis-sentinel-service.yaml $NAMESPACE
kubectl delete -f redis-master.yaml $NAMESPACE

