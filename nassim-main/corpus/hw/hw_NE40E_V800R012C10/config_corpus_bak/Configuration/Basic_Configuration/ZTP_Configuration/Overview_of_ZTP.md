Overview of ZTP
===============

Overview_of_ZTP

#### Definition

ZTP enables a device with default configurations to automatically load version files (including the system software, configuration file, and patch file) when the device starts.


#### Purpose

In conventional network device deployment, network administrators are required to perform manual onsite configuration and software commissioning on each device after hardware installation is complete. Therefore, deploying a large number of geographically scattered devices is inefficient and incurs high labor costs.

A ZTP-enabled device can automatically obtain and load version files from a file server without requiring onsite configuration or deployment, reducing labor costs and improving deployment efficiency.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Although ZTP can automatically obtain and load version files from a file server, it is vulnerable to security risks (for example, the username and password are not encrypted or the server is forged). Therefore, you are advised to implement ZTP in a secure networking environment and shut down the peer file server as soon as ZTP is implemented.



#### Benefits

ZTP eliminates the need for onsite device configuration and deployment, reducing labor costs and improving deployment efficiency.