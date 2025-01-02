Добрий день 

Я ТЗ виконав на двох віртуалках, з локальними ІР 192.168.65.127 та 192.168.65.128) 

Архів 1.tar  (192.168.65.127) 
  містить 
    docker-compose.yml
    grafana.conf  -  nginx config - потрібно буде внести ваші правки на IP
    prometheus.conf  - nginx config - потрібно буде внести ваші правки на IP
    jenkins.conf - nginx config - потрібно буде внести ваші правки на IP 
    jenkins.crt - само підпистини сертифікат для https 
    jenkins_home - волюми для  jenkins
    jenkins.key - само підпистини сертифікат для https  
    prometeus+grafana - тут  prometeus та grafana яка теж працює з 65.127 
      alert_rules.yml - когфіги для prometeus та  grafana 
      docker-compose.yml - prometeus та grafana
      grafana_data - волюми 
      prometheus_data  - волюми 
      prometheus.yml - когфіги для prometeus та  grafana 

Архів 2.tar  (192.168.65.128)  
  містить 
   for_metrik  - когфіги для prometeus та  grafana 
      docker-compose.yml  -  prometeus grafana - їхні налаштування для збору метрик 
   nginx-selfsigned.crt - само підпистини сертифікат для https 
   nginx-selfsigned.key  - само підпистини сертифікат для https 
   panda-jenkins-site - сам сайт , який викачується з гіта - та сам все робить завдяки скрипту  update_site.sh - від запускається через Jenkins 
   panda-site.conf -  nginx config - потрібно буде внести ваші правки на IP
   remoting - волюми 
   update_site.sh - скрипт , який білдить проект який написаний на flack ( репозиторі в гіта відкритий ) 

   в себе локально на ПК потрно пропистаи локальні домена в host 
   
готовий показати все в себе на своїй інфраструктурі ТГ seventist 
https://drive.google.com/drive/folders/1ADC-Y7k7ALc3WbupiPkbn4ld_r76BylE?usp=drive_link - тут проект 
