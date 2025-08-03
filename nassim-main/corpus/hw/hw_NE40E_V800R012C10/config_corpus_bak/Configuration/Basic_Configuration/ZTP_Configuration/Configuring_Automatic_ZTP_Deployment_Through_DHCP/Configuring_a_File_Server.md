Configuring a File Server
=========================

Configuring_a_File_Server

#### Context

A file server stores the files to be downloaded to unconfigured devices, including the intermediate file and version files. A router can be configured to provide the file server functionality. A file server consumes device storage resources. Therefore, ensure that the router has sufficient space to store files before deploying a file server on the router. If the router does not have sufficient space, you can deploy a third-party server to store files. For details about configuring a third-party server, see the corresponding operation guide of the third-party server.

The version file server and intermediate file server can be the same server. A file server can be a TFTP, FTP, or SFTP server.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Ensure that reachable routes are deployed between the file server and unconfigured device.



#### Follow-up Procedure

After the file server is configured, save the intermediate file and version files to the file server.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

To ensure security of the file server, configure a unique user name for the file server and assign read-only permission to the user to prevent unauthorized modification to the files. After the ZTP process is complete, disable the file server function.