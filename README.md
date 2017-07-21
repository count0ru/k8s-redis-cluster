#### Разворачивание redis кластера в Kubernetes

+ Развернем первоначальный под с redis мастером и sentinel
   
    ```
    kubectl create -f redis-master.yaml
    ```
* Развернем сервис, смотрящий во все sentinel поды, через который мы будем получать информацию о текущем мастере
    
    ```
    kubectl create -f redis-master.yaml
    ```
* Развернем контроллер, поддерживающий необходимое количество мастеров (для нормального функционирования необходимо не менее трех)
    
    ```
    kubectl create -f redis-controller.yaml
    ```
* Развернем контроллер для sentinel (необязательно кол-во sentinel равно кол-ву мастеров, но желательно больше трех, т.к. quorum)
    
    ```
    kubectl create -f redis-sentinel-controller.yaml
    ```
* Отмасштабируем количество реплик (в данном случае 3 - по количеству нод k8s)
    
    ```
    kubectl scale rc redis --replicas=3
    kubectl scale rc redis-sentinel --replicas=3
    ```
* Удалим первоначальный мастер (теперь он нам не нужен)
    
    ```
    kubectl delete pods redis-master
    ```

#### Остальное содержимое репозитория

| имя файла          | назначение              |
| ------------- |:-------------|
| `install_tools.sh` | устанавливает необходимы утилиты диагностики для redis внутри пода |
| `get_roles.py`     | получает с sentinel сервиса список серверов с разделением по ролям  |
| `stack_up.sh` | запускает деплой Redis кластера, в качестве аргмента может принимать namespace:   **stack_up.sh test-namespace** |
| `stack_down.sh` | **ОСТОРОЖНО** удаляет из namespace Redis кластер, в качестве аргмента может принимать namespace:   **stack_up.sh test-namespace** |
| `test_app.py` | тестовое приложение на Python, демонстрирующее процедуру подключения к Redis кластеру, посредством sentinel, а так же наполнение кластера тестовыми данными|
| `build_image` | директория, содержащая Dockerfile для сборки docker образа redis с поддержкой ролей master\sentinel|
