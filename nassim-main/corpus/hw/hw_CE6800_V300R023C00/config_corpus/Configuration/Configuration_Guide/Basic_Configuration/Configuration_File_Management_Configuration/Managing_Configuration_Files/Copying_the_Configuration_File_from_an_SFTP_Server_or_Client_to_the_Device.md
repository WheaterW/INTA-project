Copying the Configuration File from an SFTP Server or Client to the Device
==========================================================================

Copying the Configuration File from an SFTP Server or Client to the Device

#### Prerequisites

Before copying the configuration file from an SFTP server or client to the device, you have completed the following tasks:

* If the device functions as an SFTP client, connect it to an SFTP server. For details, see "Configuring a Device as an SFTP Client" in Configuration Guide > Basic Configuration.
* If the device functions as an SFTP server, connect it to an SFTP client. For details, see "Configuring a Device as an SFTP Server" in Configuration Guide > Basic Configuration.


#### Context

If functions do not operate properly due to incorrect configurations, you can copy the backup configuration file of the device from an SFTP server or client to restore the configuration file using either of the following methods:

* If the device functions as an SFTP client, copy the configuration file from an SFTP server to the device.
* If the device functions as an SFTP server, copy the configuration file from an SFTP client to the device.

Select one method as required.


#### Procedure

* Copy the configuration file from the SFTP server when the device functions as an SFTP client.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Set up an SFTP connection with the SFTP server.
     
     
     ```
     [sftp](cmdqueryname=sftp) [ ipv6 ] host-ip
     ```
  3. Transfer the configuration file.
     
     
     
     On the device, run the [**get**](cmdqueryname=get) command to copy the configuration file from the PC that functions as an SFTP server to the specified path on the device.
     
     ```
     [get](cmdqueryname=get) remote-filename [ local-filename ]
     ```
* Copy the configuration file from the SFTP client when the device functions as an SFTP server.
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
     
     
     
     On the PC that functions as an SFTP client, run the **put** command to copy the configuration file from the PC to the specified path on the device.
     
     ```
     sftp> put local-filename [ remote-filename ]
     ```

#### Verifying the Configuration

Run the [**dir**](cmdqueryname=dir) command on the device to check whether the configuration file has been successfully copied from the PC to the device.