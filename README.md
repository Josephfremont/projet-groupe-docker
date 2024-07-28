# TP-Groupe-Kubernetes

## Prérequis

- Docker
- Kubertes


## Ajout de la base de donnée et son volume (attendre 10 sec entre chaques commandes)
`kubectl apply -f db.yaml`<br>
`kubectl apply -f dbVolume.yaml`

## Lancement du service (attendre 10 sec entre chaques commandes)

`kubectl apply -f djangoservice.yml`

## Déploiement (attendre 10 sec entre chaques commandes)

`kubectl apply -f djangoapppoddeploy.yml`

## Accéder au déploiement
### Retourne l'adresse ip et le port du site web {127.0.0.1:port}
`minikube service externaldjangoapp -n projet-groupe`

## Accéder au phpmyadmin
### Retourne l'adresse ip et le port de phpmyadmin {127.0.0.1:port} (les identifiants sont root et root)
`minikube service phpmyadmin -n projet-groupe`

## Création des jobs

`kubectl apply -f job.yaml`<br>
`kubectl apply -f cronjob.yaml`

## Vérification des fichiers SQL créés par les jobs

### Vérification de l'existence des jobs et cronjobs

`kubectl get jobs -n projet-groupe`<br>
`kubectl get cronjobs -n projet-groupe`

### Création d'un pod temporaire pour check le volume

`kubectl apply -f pod_check_backup.yaml`

### Vérification du contenu du volume

`kubectl exec -it volume-inspect -n projet-groupe -- sh`<br>
`cd /data`<br>
`ls -l`

### Suppression du pod temporaire

`kubectl delete -f pod_check_backup.yaml`

## Accès

- Le site : http://127.0.0.1:{port}/
- Le panel d'adminitration : http://127.0.0.1:{port}/admin/
- L'API : http://127.0.0.1:{port}/api/
- La documentation : http://127.0.0.1:{port}/api/redoc/
- Le Swagger : http://127.0.0.1:{port}/api/schema/

