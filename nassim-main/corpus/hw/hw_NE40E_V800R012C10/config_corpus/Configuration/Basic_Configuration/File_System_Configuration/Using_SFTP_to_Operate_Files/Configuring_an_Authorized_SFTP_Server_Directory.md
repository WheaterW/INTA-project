Configuring an Authorized SFTP Server Directory
===============================================

This topic describes how to configure an authorized SFTP server directory for SSH users.

#### Context

When you run the [**ssh user**](cmdqueryname=ssh+user) *username* **sftp-directory** *directoryname* command, if the username specified using *username* does not exist, an SSH user with the specified *username* is created, and the configured directory is used as the authorized SFTP service directory. In this case, you can also use the username specified in the [**local-user**](cmdqueryname=local-user) *user-name* **ftp-directory** *directory* command for authorization. If neither the configured authorized directory nor the default authorized directory exists, an SFTP client fails to connect to the corresponding SFTP server.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Configure an authorized SFTP server directory for SSH users as required.
   
   
   * Run the [**ssh user**](cmdqueryname=ssh+user) *user-name* **sftp-directory** *directoryname* command to configure an authorized SFTP server directory for a specified SSH user.
   * Run the [**sftp server default-directory**](cmdqueryname=sftp+server+default-directory) *sftpdir* command to configure a default authorized SFTP server directory.![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * Of the two preceding commands, the [**ssh user**](cmdqueryname=ssh+user) *username* **sftp-directory** *directoryname* command has a higher priority but takes effect only for a specified SSH user.
   * If the information is stored in different directories, run the [**ssh user**](cmdqueryname=ssh+user) *username* **sftp-directory** *directoryname* command to change the authorized SFTP server directory for a specified SSH user.
   * Of the two preceding commands, the [**sftp server default-directory**](cmdqueryname=sftp+server+default-directory) *sftpdir* command has a lower priority but takes effect for all SSH users.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.