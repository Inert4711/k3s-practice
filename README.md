# k3s-practice
Практика развертывания микросервисов в кластере k3s: манифесты Deployment и ClusterIP для веб-приложения на базе Nginx

## Что выполнено:
- Сборка оптимизированного Docker-образа через многоступенчатую сборку
- Настройка локального реестра для хранения образов
- Развёртывание приложения через Deployment + Service
- Интеграция конфигурации через ConfigMap
- Хранение секретов через Secret
- Настройка проб здоровья (livenessProbe, readinessProbe)
- Масштабирование через `kubectl scale`
- Rolling updates без простоя

## Ключевые команды:
```bash
# Сборка и пуш образа
docker build -t localhost:5001/flask-app:1.0.0 .
docker push localhost:5001/flask-app:1.0.0

# Развёртывание
kubectl apply -f app-manifest.yaml

# Масштабирование
kubectl scale deployment myapp --replicas=5

# Обновление
kubectl rollout status deployment myapp
kubectl rollout undo deployment myapp
```

## Проблемы и решения:
1. Ошибка ErrImageNeverPull → Использовать локальный реестр вместо imagePullPolicy: Never
