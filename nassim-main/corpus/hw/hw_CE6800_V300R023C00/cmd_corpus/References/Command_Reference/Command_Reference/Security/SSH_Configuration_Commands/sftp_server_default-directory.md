sftp server default-directory
=============================

sftp server default-directory

Function
--------



The **sftp server default-directory** command configures a default authorized SFTP server directory.

The **undo sftp server default-directory** command cancels the configuration of the default authorized SFTP server directory.



By default, no authorized SFTP server directory is available.


Format
------

**sftp server default-directory** *sftpdir*

**undo sftp server default-directory** [ *sftpdir* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *sftpdir* | Specifies a default SFTP server directory. | The value is a string of 1 to 255 characters. |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

* When a user accesses the server through SFTP, the user can access only the authorized directory on the SFTP server. You can use any of the following methods to configure the SFTP server to access the authorized directory:
  1. Run the ssh user <user-name> sftp-directory <sftp-dir-path> command in the system view to configure an authorized SFTP service directory for a specified user.
  2. Run the local-user <user-name> ftp-directory <directory> command in the AAA view to configure the authorized FTP server directory for a specified user.
  3. Run the sftp server default-directory <sftpdir> command in the system view to configure the global default authorized SFTP server directory.
* The **ssh user sftp-directory** command has the highest priority and takes effect only for specified SSH users. The sftp server default-directory command has the lowest priority and takes effect for all SSH users.
* When you run the **ssh authorization-type default** command to set the authorization type of the SSH connection to AAA or run the **ssh user authentication-type** command to set the user authentication mode to password authentication, the authentication is determined by AAA.In this case, the default authorized directories of the SFTP server are listed in descending order of priority:
  1. Directory configured by running the ssh user <user-name> sftp-directory <sftp-dir-path> command.
  2. Directory configured by running the local-user <user-name> ftp-directory <directory> command.
  3. Directory configured by running the sftp server default-directory <sftpdir> command.
* When the **ssh authorization-type default** command is run to set the authorization type of the SSH connection to Root and the **ssh user authentication-type** command is run to set the user authentication mode to public key authentication or certificate authentication, the authentication is determined by SSH.In this case, the directory configured by running the local-user <user-name> ftp-directory <directory> command does not take effect on the SFTP server.The default authorized directories of the SFTP server are listed in descending order of priority:
  1. Directory configured by running the ssh user <user-name> sftp-directory <sftp-dir-path> command.
  2. Directory configured by running the sftp server default-directory <sftpdir> command.

**Precautions**

* Files cannot be uploaded to the logfile/security directory through SFTP due to permission control.
* This command takes effect for both IPv4 and IPv6.

Example
-------

# Configure a default authorized SFTP server directory for SSH users.
```
<HUAWEI> system-view
[~HUAWEI] sftp server default-directory flash:

```