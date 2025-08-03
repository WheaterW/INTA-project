(Optional) Uploading Performance Statistics Files
=================================================

The system generates performance statistics files based on the collected performance statistics at a specified interval. To view the performance statistics on a performance management (PM) server, upload performance statistics files to the PM server.

#### Context

Before uploading performance statistics files to a PM server, configure the File Transfer Protocol (FTP) or Secure File Transfer Protocol (SFTP) server functionality on the PM server, and ensure that the device on which the performance statistics are collected has been connected to the PM server.

Perform the following steps on the device:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**pm**](cmdqueryname=pm)
   
   
   
   The PM view is displayed.
3. (Optional) Run either of the following **client-source** commands to configure a global source IP address and VPN used for uploading performance statistics files to the PM server:
   
   
   * To configure a global IPv4 source address, run the **client-source** **interface** { *interface-name* | *interface-type* *interface-number* } command.![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     The device uses the IPv4 address and VPN configured on the interface for uploading performance statistics files.
     
     If no IPv4 address is configured for the interface, files may fail to be uploaded.
   * To configure a global IPv6 source address and VPN, run the **client-source** **ipv6** *IPV6ADDR* [ **vpn-instance** *vpnInstanceName* ] command.
4. Run [**pm-server**](cmdqueryname=pm-server) *server-name*
   
   
   
   A PM server process is created, and the PM server view is displayed.
5. Run the following commands to configure parameters of the PM server to which a performance statistics file will be uploaded.
   
   
   * Run the [**protocol**](cmdqueryname=protocol) { **ftp** | **sftp** } **ip-address** *ip-address* [ **port** *port-number* | { **net-manager-vpn** | **vpn-instance** *vpn-instance-name* } | { **client-source** **interface** { *interface-name* | *interface-type* *interface-number* } | **client-source** **ipv6** *IPV6ADDR* } ] \* command to configure the protocol, IPv4 or IPv6 address, and port number for uploading performance statistics files to the PM server.
     
     Using FTP to upload performance statistics files is not secure. Therefore, using SFTP is recommended.
     
     If the IP address of the PM server is a private address, use **net-manager-vpn** to specify a network management VPN or use **vpn-instance** *vpn-instance-name* to specify the name of a VPN instance for uploading performance statistics files.
     
     To specify a source IPv4 interface address or IPv6 address for the device to upload performance statistics files to a PM server, specify **client-source**. The priority of the source address configured using this way is higher than that of the global source address configured using the **client-source** command. After a source address is specified, use the matched VPN. If the corresponding VPN is not configured, use the public network.
   * To configure a username and password for logging in to the PM server, run the [**username**](cmdqueryname=username) *user-name* **password** *password* command.
   * To configure the destination path where a performance statistics file is saved on the PM server, run the [**path**](cmdqueryname=path) *destination-path* command.
   * To configure the number of retransmissions for a performance statistics file, run the [**retry**](cmdqueryname=retry) *retry-times* command.
6. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the PM view.
7. Run [**upload-config**](cmdqueryname=upload-config) *request-name* **server** *server-name*
   
   
   
   A request for uploading performance statistics files to a specified PM server is created.
8. (Optional) Run [**statistics-task**](cmdqueryname=statistics-task) *task-name*
   
   
   
   The performance statistics task view is displayed.
9. (Optional) Run [**upload auto**](cmdqueryname=upload+auto) *request-name*
   
   
   
   The device is enabled to automatically upload performance statistics files to the PM server at a specific interval.
   
   
   
   To enable the device to automatically upload performance statistics files to the PM server at a specific interval, perform this configuration.
10. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.

#### Follow-up Procedure

Run the [**upload**](cmdqueryname=upload) *request-name* **file** *filename* &<1-16> command to enable the device to upload performance statistics files to the PM server.