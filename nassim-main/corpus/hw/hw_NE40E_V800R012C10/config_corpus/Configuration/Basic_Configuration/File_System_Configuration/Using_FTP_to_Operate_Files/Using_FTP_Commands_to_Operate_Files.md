Using FTP Commands to Operate Files
===================================

After logging in to a device that functions as an FTP server by using FTP, you can upload files to or download files from the device, and manage device directories.

#### Context

[Table 1](#EN-US_TASK_0172359924__tab_dc_vrp_vfm_cfg_001301) describes FTP file attributes.

**Table 1** FTP file attributes
| File Attribute | Description |
| --- | --- |
| FTP file type | * ASCII type A file is transmitted in ASCII characters. In this type, the **Enter** key cannot be used to separate lines.  * Binary type |
| FTP data connection mode | The following data connection mode can be set for the FTP server:  * ACTIVE mode: The server proactively connects clients during connection establishment. * PASV mode: The server waits to be connected by clients during connection establishment.  During connection establishment, the FTP client determines the data connection mode. |



#### Procedure

1. Perform either of the following steps on the client based on the type of the server's IP address:
   
   
   * Run the [**ftp**](cmdqueryname=ftp) [ [ **-a** *source-ip-address* | **-i** { *interface-type interface-number* | *interface-name* } ] *host-ip* [ *port-number* ] [ **vpn-instance** *vpn-instance-name* ] | **public-net** ] command to configure the device to use an IPv4 address to establish a connection to the FTP server and enter the FTP client view.
   * Run the [**ftp**](cmdqueryname=ftp) **ipv6** [ **-a** *source-ip6* ] *host-ipv6-address* [ [ **vpn-instance** *ipv6-vpn-instance-name* ] | **public-net** ] [ **-oi** { *interface-type interface-number* | *interface-name* } ] [ *port-number* ] command to configure the device to use an IPv6 address to establish a connection to the FTP server and enter the FTP client view.
2. Perform one or more operations described in [Table 2](#EN-US_TASK_0172359924__tab_dc_vrp_vfm_cfg_001302).
   
   
   
   **Table 2** File operations
   | File Operation | | Description |
   | --- | --- | --- |
   | Managing files | Configuring the file type | * Run the [**ascii**](cmdqueryname=ascii) command to set the file type to ASCII. * Run the [**binary**](cmdqueryname=binary) command to set the file type to binary. The FTP file type is determined by the client. By default, the ASCII type is used. |
   | Configuring the data connection mode | * Run the [**passive**](cmdqueryname=passive) command to set the data connection mode to PASV. * Run the [**undo passive**](cmdqueryname=undo+passive) command to set the data connection mode to ACTIVE. |
   | Uploading files | * Run the [**put**](cmdqueryname=put) *local-filename* [ *remote-filename* ] command to upload a file from the local device to the remote server. * Run the [**mput**](cmdqueryname=mput) *local-filenames* command to upload files from the local device to a remote server. NOTE: You can also run either of the following commands in the user view to upload the local file to the FTP server:   + On an IPv4 network:  Run the [**ftp client-transfile**](cmdqueryname=ftp+client-transfile) **put** [ **-a** *source-ipv4* | **-i** { *interface-type interface-number* | interface-name } ] **host-ip** *ipv4-address* [ **port** *portnumber* ] [ **vpn-instance** *vpn-instancename* | **public-net** ] **username** *user-name* **sourcefile** *localfilename* [ **destination** *remotefilename* ] command.   + On an IPv6 network:  Run the [**ftp client-transfile**](cmdqueryname=ftp+client-transfile) **put** **ipv6** [ **-a** *source-ipv6* ] **host-ip** *ipv6-address* [ [ **vpn-instance** *ipv6-vpn-name* ] | **public-net** ] [ **port** *port-number* ] **username** *username* **sourcefile** *local-filename* [ **destination** *remote-filename* ] command. |
   | Downloading files | * Run the [**get**](cmdqueryname=get) *remote-filename* [ *local-filename* ] command to download a file from the remote server and save the file on the local device. * Run the [**mget**](cmdqueryname=mget) *remote-filenames* command to download files from a remote server and save the files on the local device. NOTE: You can also run either of the following commands in the user view to download files from the FTP server to the local device:   + On an IPv4 network:  Run the [**ftp client-transfile**](cmdqueryname=ftp+client-transfile) **get** [ **-a** *source-ipv4* | **-i** { *interface-type interface-number* | interface-name } ] **host-ip** *ipv4-address* [ **port** *portnumber* ] [ **vpn-instance** *vpn-instancename* | **public-net** ] **username** *user-name* **sourcefile** *localfilename* [ **destination** *remotefilename* ] command.   + On an IPv6 network:  Run the [**ftp client-transfile**](cmdqueryname=ftp+client-transfile) **get** **ipv6** [ **-a** *source-ipv6* ] **host-ip** *ipv6-address* [ [ **vpn-instance** *ipv6-vpn-name* ] | **public-net** ] [ **port** *port-number* ] **username** *username* **sourcefile** *local-filename* [ **destination** *remote-filename* ] command. |
   | Enabling the file transfer notification function | * If the [**prompt**](cmdqueryname=prompt) command is run in the FTP client view to enable the file transfer notification function, the system prompts you to confirm the upload or download operation before file upload or download. * If the [**prompt**](cmdqueryname=prompt) command is run again in the FTP client view, the file transfer notification function is disabled. NOTE:  The [**prompt**](cmdqueryname=prompt) command applies when the [**mput**](cmdqueryname=mput) or [**mget**](cmdqueryname=mget) command is used to upload or download files. If the local device has the files to be downloaded by running the [**mget**](cmdqueryname=mget) command, the system prompts you to replace the existing ones regardless of whether the file transfer notification function is enabled. |
   | Enabling the FTP verbose function | Run the [**verbose**](cmdqueryname=verbose) command.  After the verbose function is enabled, all FTP response information is displayed. After file transfer is complete, statistics about the transmission rate are displayed. |
   | Enabling the function of appending the local file contents to the file on the FTP server | Run the [**append**](cmdqueryname=append) *local-filename* [ *remote-filename* ] command.  If the file specified by *remote-filename* does not exist on the FTP server, the file is automatically created on the FTP server, and the local file contents are automatically appended to the end of the created file. |
   | Deleting files | Run the [**delete**](cmdqueryname=delete) *remote-filename* command. |
   | Managing directories | Changing the working path of a remote FTP server | Run the [**cd**](cmdqueryname=cd) *pathname* command. |
   | Changing the working path of an FTP server to the parent directory | Run the [**cdup**](cmdqueryname=cdup) command. |
   | Displaying the working path of an FTP server | Run the [**pwd**](cmdqueryname=pwd) command. |
   | Displaying files in a directory and the list of sub-directories | Run the [**dir**](cmdqueryname=dir) [ *remote-directory* [ *local-filename* ] ] command.  If no path name is specified for a specified remote file, the system searches an authorized directory for a specified file. |
   | Displaying a specified remote directory or file on an FTP server | Run the [**ls**](cmdqueryname=ls) [ *remote-directory* [ *local-filename* ] ] command. |
   | Displaying or changing the working path of an FTP client | Run the [**lcd**](cmdqueryname=lcd) [ *directory* ] command.  The [**lcd**](cmdqueryname=lcd) [ *directory* ] command displays the local working path of the FTP client, whereas the [**pwd**](cmdqueryname=pwd) command displays the working path of the remote FTP server. |
   | Creating a directory on an FTP server | Run the [**mkdir**](cmdqueryname=mkdir) *remote-directory* command.  The directory can be a combination of letters and digits and must not contain special characters, such as less than (<), greater than (>), question marks (?), backslashes (\), and colons (:). |
   | Deleting a directory from an FTP server | Run the [**rmdir**](cmdqueryname=rmdir) *remote-directory* command. |
   | Displaying online help for an FTP command | | Run the [**remotehelp**](cmdqueryname=remotehelp) [ *command* ] command. |
   | Changing an FTP user | | Run the [**user**](cmdqueryname=user) *username* [ *password* ] command. |
3. Perform either of the following operations as needed to end an FTP connection.
   
   
   * Run the [**bye/quit**](cmdqueryname=bye%2Fquit) command to end the connection to the FTP server and return to the user view.
   * Run the [**close/disconnect**](cmdqueryname=close%2Fdisconnect) command to end both the connection to the FTP server and the FTP session and remain in the FTP client view.
4. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.