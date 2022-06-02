  ```
  24  docker service ls 
   25  docker service ps my_web_2
   26  docker node ls 
   27  docker node inspect 2t6nezs718bhqn8fpadfxek68
   28  docker node ls 
   29  docker node update --label-add env=prod 2t6nezs718bhqn8fpadfxek68 
   30  docker node update --label-add env=prod rwe866sdeqqymxkpafnamq50i
   31  docker node update --label-add env=uat szgpnumgv5j4kanxts38ksaml
   32  docker node inspect 2t6nezs718bhqn8fpadfxek68
   33  docker node ls 
   34  docker node inspect szgpnumgv5j4kanxts38ksaml
   35  history 
   36  docker service create --name my_web_prod --replicas 3 --publish published=8005,target=8081 --constraint node.labels.env==prod amitvashist7/python-web-app
   37  docker service create --name my_web_prod --replicas 3 --publish published=8006,target=8081 --constraint node.labels.env==prod amitvashist7/python-web-app
   38  docker service ls 
   39  docker service ps my_web_prod
   40  docker node ls  
   41  docker service create --name my_web_uat --replicas 3 --publish published=8007,target=8081 --constraint node.labels.env==uat amitvashist7/python-web-app
   42  docker service ls 
   43  docker service ps my_web_uat
   44  docker service scale my_web_uat=5
   45  docker service ps my_web_uat
   46  docker service rm my_web_uat
   47  docker service rm my_web_prod
   48  docker service rm --all
   49  docker service rm --help
   50  docker service ls
   51  docker service rm my_web_2 my_web
   52  docker service ls
   53  ls
   54  cd 04-DockerSwarm/
   55  ls
   56  mkdir 05-Labels
   57  history > 05-Labels/README.md
```
