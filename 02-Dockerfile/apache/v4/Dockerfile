# Base Image
FROM ubuntu:16.04

# Owner of IMAGE
MAINTAINER Amit Vashist <amitvashist7@gmail.com>

# Update the APT-Repo
RUN apt-get update 


# Install Apache Packages 
RUN apt-get install apache2 -y 


# Deploy custom Index Page.
COPY index.html  /var/www/html/

# Port Info.
EXPOSE 80 
EXPOSE 8080 
EXPOSE 8081 

# Run Apache Server
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]
