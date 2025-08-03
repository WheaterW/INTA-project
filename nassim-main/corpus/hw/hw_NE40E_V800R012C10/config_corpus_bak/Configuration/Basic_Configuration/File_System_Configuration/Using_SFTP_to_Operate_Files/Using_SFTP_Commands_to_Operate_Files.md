Using SFTP Commands to Operate Files
====================================

After logging in to the SFTP server, you can manage directories and files on the server.

#### Context

After logging in to the SFTP server, you can perform the following operations:

* Obtain command help information on the SFTP client.
* Manage directories on the SFTP server.
* Manage files on the SFTP server.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Perform either of the following operations based on the network protocol:
   
   
   * For IPv4:
     
     Run the [**sftp**](cmdqueryname=sftp) [ **-a** *source-ip-address* ] [ **-force-receive-pubkey** ] *host-ip-address* [ *port-number* ] [ [ **prefer\_kex***prefer\_kex* ] | [ **prefer\_ctos\_cipher***prefer\_ctos\_cipher* ] | [ **prefer\_stoc\_cipher** *prefer\_stoc\_cipher* ] | [ **prefer\_ctos\_hmac***prefer\_ctos\_hmac* ] | [ **prefer\_stoc\_hmac***prefer\_stoc\_hmac* ] | [ **prefer\_ctos\_compress zlib** ] | [ **prefer\_stoc\_compress zlib** ] | [ **public-net** | **-vpn-instance***vpn-instance-name* ] | [ **-ki***interval* ] | [ **-kc***count* ] | [ **identity-key***identity-key-type* ] | [ **user-identity-key***user-key* ] ] \* command to log in to the SSH server using the specified IPv4 address through SFTP and enter the SFTP client view.
   * For IPv6:
     
     Run the [**sftp ipv6**](cmdqueryname=sftp+ipv6) [ **-force-receive-pubkey** ] [ **-a** *source-ipv6-address* ] *host-ipv6-address* [ [ [ **-vpn-instance** *vpn-instance-name* ] | **public-net** ] | [ **-oi** { *interface-name* | *interface-type* *interface-number* } ] [ *port-number* ] | [ **prefer\_kex** { *prefer\_kex* } ] | [ **prefer\_ctos\_cipher** *prefer\_ctos\_cipher* ] | [ **prefer\_stoc\_cipher** *prefer\_stoc\_cipher* ] | [ **prefer\_ctos\_hmac** *prefer\_ctos\_hmac* ] | [ **prefer\_stoc\_hmac** *prefer\_stoc\_hmac* ] | [ **prefer\_ctos\_compress** **zlib** ] | [ **prefer\_stoc\_compress** **zlib** ] | [ **-ki** *interval* ] | [ **-kc** *count* ] | [ **identity-key** *identity-key-type* ] | [ **user-identity-key** *user-key* ] ]\* command to log in to the SSH server using the specified IPv6 address through SFTP and enter the SFTP client view.
3. Perform one or more operations described in [Table 1](#EN-US_TASK_0172359936__tab_dc_vrp_vfm_cfg_002001) as needed.
   
   
   
   **Table 1** File operation
   | File Operation | | Description |
   | --- | --- | --- |
   | Managing directories | Changing the current working directory | Run the [**cd**](cmdqueryname=cd) [ *path* ] command. |
   | Changing the current working directory to the parent directory | Run the [**cdup**](cmdqueryname=cdup) command. |
   | Displaying the current working directory | Run the [**pwd**](cmdqueryname=pwd) command. |
   | Displaying files in a directory and the list of sub-directories | Run the [**dir**](cmdqueryname=dir) [ *remote-filename* [ *local-filename* ] ] command. |
   | Deleting directories on the server | Run the [**rmdir**](cmdqueryname=rmdir) *directory-name* command. |
   | Creating a directory on the server | Run the [**mkdir**](cmdqueryname=mkdir) *path* command. |
   | Managing files | Renaming a file on the server | Run the [**rename**](cmdqueryname=rename) *old-name* *new-name* command. |
   | Downloading files from a remote server | Run the [**get**](cmdqueryname=get) *remote-filename* [ *local-filename* ] command. |
   | Uploading files to a remote server | Run the [**put**](cmdqueryname=put) *local-filename* [ *remote-filename* ] command. |
   | Deleting files from the server | Run the [**remove**](cmdqueryname=remove) *path* or [**delete**](cmdqueryname=delete) *file* command. |
   | Displaying command help information on the SFTP client | | Run the [**help**](cmdqueryname=help) [ *command-name* ] command. |