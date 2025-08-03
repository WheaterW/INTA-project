Uploading Performance Statistics Files
======================================

Uploading Performance Statistics Files

#### Context

The system generates performance statistics files based on the collected performance statistics at a specified interval. To view the performance statistics on a PM server, upload the performance statistics files to the PM server.

The device uses FTP or SFTP to upload statistics files to a remote PM server in either of the following modes:

* Automatic mode: The system periodically generates performance statistics files and automatically uploads them to the PM server.
* Manual mode: The system periodically generates performance statistics files, and the files can only be manually uploaded to the PM server.

![](public_sys-resources/note_3.0-en-us.png) 

Using FTP to upload performance statistics files is not secure. Therefore, using SFTP is recommended.

In FIPS mode, files cannot be uploaded in FTP mode.



#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the PM view.
   
   
   ```
   [pm](cmdqueryname=pm)
   ```
3. Create a PM server process and enter its view.
   
   
   ```
   [pm-server](cmdqueryname=pm-server) server-name
   ```
4. Configure the parameters of the PM server to which performance statistics files will be uploaded.
   
   
   * Configure the protocol, IP address, and port number used for uploading performance statistics files to the PM server.
     ```
     [protocol](cmdqueryname=protocol) { ftp | sftp } ip-address ip-address [ port port-number | { net-manager-vpn | vpn-instance vpn-instance-name } | { [client-source interface](cmdqueryname=client-source+interface) { interface-name | interface-type interface-number } | [client-source ipv6](cmdqueryname=client-source+ipv6) IPV6ADDR } ] *
     ```
     
     The default port number of the PM server is 21 (using FTP) or 22 (using SFTP).
     
     If the IP address of the PM server is a private address, configure **net-manager-vpn** to specify a network management VPN for uploading the performance statistics files, or configure **vpn-instance** *vpn-instance-name* to specify a VPN instance for uploading the performance statistics files.
   * Configure a username and password for logging in to the PM server.
     ```
     [username](cmdqueryname=username) user-name password [ password ] 
     ```
     ![](public_sys-resources/note_3.0-en-us.png) 
     
     For security purposes, change the password periodically.
   * Configure the destination path for saving performance statistics files on the PM server.
     ```
     [path](cmdqueryname=path) destination-path
     ```
   * Configure the maximum number of retransmissions for a performance statistics file.
     ```
     [retry](cmdqueryname=retry) retry-times
     ```
5. Return to the PM view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
6. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```
7. Create a request for uploading performance statistics files to a specified PM server.
   
   
   ```
   [upload-config](cmdqueryname=upload-config) request-name server server-name
   ```
8. Enable the device to upload performance statistics files to the PM server.
   
   
   * Automatic mode
     1. Enter the performance statistics task view.
        ```
        [statistics-task](cmdqueryname=statistics-task) task-name
        ```
     2. Enable the device to automatically upload performance statistics files to the PM server.
        ```
        [upload auto](cmdqueryname=upload+auto) request-name
        ```
   * Manual mode
     1. View the list of generated statistics files.
        ```
        [display pm statistics-file](cmdqueryname=display+pm+statistics-file) [ task-name ]
        ```
     2. Configure the device to upload performance statistics files to the PM server.
        ```
        [upload](cmdqueryname=upload) request-name file { filename } &<1-16>
        ```
9. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```