Configuring a File Server
=========================

Configuring a File Server

#### Prerequisites

There must be reachable routes between the file server and the device with factory configurations.


#### Context

A file server stores the files to be downloaded to devices with factory configurations, including intermediate files and deployment files. If a device is configured as the file server, those files will occupy a significant amount of device storage resources. To ensure the device performance, a third-party file server is typically used on a ZTP network. For details about how to configure a third-party file server, see the third-party server operation guide.

The intermediate file server and deployment file server can be the same file server. The file server must be an SFTP, HTTP, TFTP, or FTP file server. Currently, the device uses the SHA2 algorithm by default. The file server must also support the SHA2 algorithm. You can run the [**display this include-default**](cmdqueryname=display+this+include-default) | **include ssh** command to check the algorithms used by the client and server. At least one algorithm supported by the file server must be the same as that supported by the device.


#### Procedure

1. Configure the file server. SFTP and HTTPS file servers are recommended because they are more secure than TFTP, FTP, and HTTP file servers.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   * If a Huawei device is used, see [Configuring a Device as an SFTP Server](vrp_file_cfg_0014.html) in the Configuration Guide > Basic Configuration > File System Management Configuration.
   * If a third-party device is used as the file server, see the operation guide of the third-party SFTP or HTTPS file server.
   * The file server used for SZTP must have the HTTPS server capability, but Huawei devices do not provide the capability. Therefore, a third-party server needs to be deployed. For details about how to configure a third-party server, see the third-party server operation guide.
2. Place the intermediate file and deployment files to the working directory of the file server.
   
   
   
   The HTTPS deployment file server has certain requirements on the length of the deployment file name. Ensure that the following requirements are met:
   
   * System software: 4 to 124 characters
   * Configuration file: 5 to 64 characters
   * Patch file: 5 to 63 characters
   * Intermediate file: 5 to 64 characters
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   To ensure security of the file server, configure a unique user name for the file server and assign the read-only permission to the user to prevent unauthorized modification of the files. After the ZTP process is complete, disable the file server function.