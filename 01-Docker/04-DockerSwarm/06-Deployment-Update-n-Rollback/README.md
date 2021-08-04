    1  docker service create --name tiny-web --replicas 3 --publish published=8001,target=80 amitvashist7/k8s-tiny-web:latest
    2  docker service ls 
    3  docker service ps tiny-web
    4  docker service --help
    5  docker service inspect tiny-web
    6  docker service scale tiny-web=20
    7  docker service ps tiny-web
    8  docker service update tiny-web --image amitvashist7/k8s-tiny-web:2
    9  docker service ps tiny-web
   10  docker service scale tiny-web=3
   11  docker service ps tiny-web
   12  docker service update tiny-web --image amitvashist7/k8s-tiny-web:3
   13  docker service ps tiny-web
   14  docker service update --rollback --update-delay 0s tiny-web
   15  docker service ps tiny-web
   16  ls
   17  cd 04-DockerSwarm/ls
   18  cd 04-DockerSwarm/
   19  ls
   20  mkdir 06-Deployment-Update-&-Rollback
   21  mkdir 06-Deployment-Update-n-Rollback
   22  ls
   23  rm -rf 06-Deployment-Update-
   24  ls
   25  history 
   26  history  > 06-Deployment-Update-n-Rollback/README.md
