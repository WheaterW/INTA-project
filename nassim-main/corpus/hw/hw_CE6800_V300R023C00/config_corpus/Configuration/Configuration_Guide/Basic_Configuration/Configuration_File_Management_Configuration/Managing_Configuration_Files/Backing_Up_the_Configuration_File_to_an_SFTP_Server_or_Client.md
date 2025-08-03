Backing Up the Configuration File to an SFTP Server or Client
=============================================================

Backing Up the Configuration File to an SFTP Server or Client

#### Prerequisites

Before backing up the configuration file to an SFTP server or client, you have completed the following tasks:

* If the device functions as an SFTP client, connect it to an SFTP server. For details, see "Configuring a Device as an SFTP Client" in Configuration Guide > Basic Configuration.
* If the device functions as an SFTP server, connect it to an SFTP client. For details, see "Configuring a Device as an SFTP Server" in Configuration Guide > Basic Configuration.


#### Context

If the device is unexpectedly damaged, the configuration file cannot be restored. In this case, a backup configuration file is required for restoring the device configurations. You can back up the configuration file through SFTP using either of the following methods:

* If the device functions as an SFTP client, back up the configuration file to an SFTP server.
* If the device functions as an SFTP server, back up the configuration file to an SFTP client.

Select one method as required.

![](public_sys-resources/note_3.0-en-us.png) 

Backing up the configuration file through FTP or TFTP is a simple process, which however may pose security risks. In scenarios featuring high security requirements, SFTP and SCP are recommended for configuration file backup.



#### Procedure

* Back up the configuration file to the SFTP server when the device functions as an SFTP client.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view) 
     ```
  2. Set up an SFTP connection with the SFTP server.
     
     
     ```
     [sftp](cmdqueryname=sftp) [ ipv6 ] host-ip
     ```
  3. Transfer the configuration file.
     
     
     
     On the device, run the [**put**](cmdqueryname=put) command to upload the configuration file to the specified path on the PC that functions as an SFTP server.
     
     ```
     [put](cmdqueryname=put) local-filename [ remote-filename ]
     ```
* Back up the configuration file to the SFTP client when the device functions as an SFTP server.
  1. On the PC that functions as an SFTP client, initiate an SFTP connection with the device.
     
     
     
     The following information is for reference only.
     
     ```
     C:/Documents and Settings/Administrator> sftp client001@10.136.23.4
     Connecting to 10.136.23.4...
     The authenticity of host "10.136.23.4 (10.136.23.4)" can't be established.
     DSA key fingerprint is 0d:48:82:fd:2f:52:1c:f0:c4:22:70:80:8f:7b:fd:78.
     Are you sure you want to continue connecting (yes/no)? yes
     Warning: Permanently added "10.136.23.4" (DSA) to the list of known hosts.
     client001@10.136.23.4's password:
     sftp>
     ```
  2. Transfer the configuration file.
     
     
     
     On the PC, run the **get** command to transfer the configuration file to the specified path on the PC.
     
     ```
     sftp> get remote-filename [ local-filename ]
     ```

#### Verifying the Configuration

The configuration file is saved to the working directory of the SFTP user, and the size of the configuration file on the device is the same as that on the SFTP server or client.