Creating an OCI Image
=====================

Creating an OCI Image

#### Prerequisites

Before creating an OCI image, you need to install Docker in the development environment and ensure that the development environment can connect to the Internet.


#### Context

Using a Dockerfile is the most common way to create a Docker image. Dockerfile is a text file. You can define the commands and descriptions required for building Docker images in a Dockerfile. [Figure Process of creating a Docker image](#EN-US_TASK_0000001513165798__fig66626252710) shows the process of creating an image using a Dockerfile.

**Figure 1** Process of creating a Docker image  
![](figure/en-us_image_0000001631716014.png)

The following describes how to use Docker to implement a simple shell script-based image. The procedure is as follows:

* Compile a hellodocker shell script.
* Create a Docker image.
* Create a local container and use the Docker tool to perform a local test.
* Save the built image.

#### Procedure

1. Compile a simple shell script to create the **hellodocker.log** file and repeatedly write **hello docker**.
   
   
   ```
   #!/bin/bash
   filePath="/var/hellodocker.log"
   if [ ! -f "$filePath" ]
   then
   touch $filePath
   echo "Create the file successfully."
   else
   echo "The file already exists."
   fi
   start=$(date +%s)
   end=$(date +%s)
   time=$(( $end - $start ))
   while (($time<120))
   do
      echo "$(date "+%Y-%m-%d %H:%M:%S") hello docker" >> $filePath
      end=$(date +%s)
      time=$(( $end - $start ))
   done
   ```
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   This script is only an example. Compile the script based on the actual function.
2. Compile the Dockerfile.
   
   
   ```
   FROM ubuntu:15.10
   RUN echo 'hello docker!'
   COPY hellodocker.sh /usr/bin/hellodocker.sh
   RUN chmod +x /usr/bin/hellodocker.sh
   CMD /usr/bin/hellodocker.sh
   ```
3. Create a Docker image named **hellodocker:1.0.0** from the Dockerfile.
   
   
   ```
   docker build -t hellodocker:1.0.0 
   ```
4. Create a local container and check whether the container works properly.
   
   
   
   # Create and run a container.
   
   ```
   docker run -d hellodocker:1.0.0
   ```
   
   # Check the container ID.
   
   ```
   docker ps
   CONTAINER ID        IMAGE               COMMAND                  CREATED                  STATUS              PORTS                       NAMES
   5bafce045b9e        hellodocker:1.0.0   "/bin/sh -c /usr/b..."   Less than a second ago   Up 5 seconds       0.0.0.0:1022->22/tcp        eloquent_albattani
   ```
   
   # Enter the container and view the generated files.
   
   ```
   docker exec -it 5bafce045b9e /bin/bash
   root@5bafce045b9e:/# cd /data
   root@5bafce045b9e:/data# cat hellodocker.log 
   2021-03-17 19:19:26 hello docker
   2021-03-17 19:19:26 hello docker
   2021-03-17 19:19:26 hello docker
   2021-03-17 19:19:26 hello docker
   2021-03-17 19:19:26 hello docker
   ...
   ```
5. Save the image and generate the **hellodocker.tar** file.
   
   
   ```
   docker save hellodocker:1.0.0 -o hellodocker.tar
   ```