docker rm -f blog1.2
docker run -d --restart=unless-stopped --name blog1.2 -v /home/zhuxi/blog/:/app/blog -p:8080:8080 docker_blog:1.2
