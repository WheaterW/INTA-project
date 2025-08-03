Understanding OAS
=================

Understanding OAS

#### System Architecture

[Figure 1](#EN-US_CONCEPT_0000001563766133__fig18360103414218) shows the system architecture of a device with the OAS function. The service software of the device and the OAS run on the basic hardware and operating system of the device.

**Figure 1** System architecture of a device with the OAS function  
![](figure/en-us_image_0000001563766145.png)

* APP
  
  The applications created in the OAS can provide the functions of third-party application software for users.
* Application Manager (APPM)
  
  An application management system, which is used to manage virtualized applications, including application resource management and lifecycle management.

* Application resource management
  
  Allocates, monitors, and schedules CPU, memory, storage, and other resources used by applications.
* Application lifecycle management
  
  Implements operations on applications, such as creating, starting, stopping, and deleting them.

The OAS supports the installation and management of third-party applications through container engines. The following describes the concepts related to containers and container engine.


#### OAS Based on the iSulad Container Engine

Container is a lightweight virtualization technology. A container packs the code and all the dependencies required for running an application, so that the application can be reliably and quickly copied from one computing environment to another. All containers share the same operating system kernel and are isolated from each other. Typical container management applications include Docker, iSulad, and LXC. The OAS integrates iSulad and allows users to run third-party container applications developed based on iSulad or Docker.

iSulad is an open-source container engine. It allows developers to uniformly integrate their applications and dependency packages into a portable image and then release the image to any server where the iSulad or Docker container engine is installed.

* Image: An Open Container Initiative (OCI) image is a special file system. In addition to providing the files required for running a container, such as programs, libraries, resources, and configuration files, an image also contains some configuration parameters that are prepared for running. An image does not contain any dynamic data, and its content will not be changed after being compiled. An image can be used to create an iSulad or Docker container. You can use an existing image on the device to deploy multiple iSulad or Docker containers of the same class.
* Container: A container is the entity of a running image. Containers can be created, started, stopped, deleted, and more. Each iSulad or Docker container runs only one application and implements only one service function. An application is embedded in the image of a container when the image is created. After the container is installed, you can manage the application by operating the container. You do not need to install or configure the application on the device.

[Figure 2](#EN-US_CONCEPT_0000001563766133__fig1277213281790) shows the architecture of an OAS in [Figure 1](#EN-US_CONCEPT_0000001563766133__fig18360103414218) based on the iSulad container engine.

**Figure 2** Architecture of an OAS based on the iSulad container engine  
![](figure/en-us_image_0000001563885781.png)

* APPM
  
  Implements application resource management and application lifecycle management based on the iSulad container engine.
* Container
  
  A container created using an image created based on the OCI standard.
* App
  
  Application software that implements service functions required by users in a container.
* Bin/Libs
  
  Environment dependencies required for application running.

Each container contains an application required by users to implement service functions and running dependencies of the application. You can manage the application by performing operations on a container.

![](public_sys-resources/note_3.0-en-us.png) 

In the OAS development guide, an application refers to a container.