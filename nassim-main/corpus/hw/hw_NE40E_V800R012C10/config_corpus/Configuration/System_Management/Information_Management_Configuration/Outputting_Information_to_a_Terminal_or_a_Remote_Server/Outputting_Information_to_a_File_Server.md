Outputting Information to a File Server
=======================================

By outputting information to a file server, you can learn about the device operation.

#### Context

Due to the limited detection scope and security inspection capability, a device cannot identify whether the OS has been compromised. When a security event occurs, logs need to be analyzed manually, which is slow and inefficient. To address this issue, you can configure the device to periodically output logs to a file server. By viewing the logs on the file server, you can monitor the device running status and promptly diagnose network faults.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this section, information refers to OS logs.



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Configure the device to output logs to a specified file server. Only one file server is supported.
   1. On an IPv4 network, run [**info-center file-server**](cmdqueryname=info-center+file-server) **ipv4** *ipv4-addr* [ **vpn-instance** *vpn-instance-name* ] [**transport-type sftp**](cmdqueryname=transport-type+sftp) [ **port** *port-number* ] **username** *user-name* **password** *pass\_word* [ **path** *destination-path* ] [**file-type os**](cmdqueryname=file-type+os)
      
      
      
      The device is configured to output logs to the specified file server using SFTP.
   2. On an IPv6 network, run [**info-center file-server**](cmdqueryname=info-center+file-server) **ipv6** *ipv6-addr* [ **vpn-instance** *vpn-instance-name* ] [**transport-type sftp**](cmdqueryname=transport-type+sftp) [ **port** *port-number* ] **username** *user-name* **password** *pass\_word* [ **path** *destination-path* ] [**file-type os**](cmdqueryname=file-type+os)
      
      
      
      The device is configured to output logs to the specified file server using SFTP.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.