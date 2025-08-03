Copying the Configuration File from an FTP Server or Client to the Device
=========================================================================

Copying the Configuration File from an FTP Server or Client to the Device

#### Prerequisites

Before copying the configuration file from an FTP server or client to the device, you have completed the following tasks:

* If the device functions as an FTP client, connect it to an FTP server. For details, see "Configuring a Device as an FTP Client" in Configuration Guide > Basic Configuration.
* If the device functions as an FTP server, connect it to an FTP client. For details, see "Configuring a Device as an FTP Server" in Configuration Guide > Basic Configuration.
* The weak security algorithm/protocol feature package (WEAKEA) has been installed using the **install feature-software WEAKEA** command.


#### Context

If functions do not operate properly due to incorrect configurations, you can copy the backup configuration file of the device from an FTP server or client to restore the configuration file using either of the following methods:

* If the device functions as an FTP client, copy the configuration file from an FTP server to the device.
* If the device functions as an FTP server, copy the configuration file from an FTP client to the device.

Select one method as required.

![](public_sys-resources/note_3.0-en-us.png) 

Restoring the configuration file through FTP is a simple process, which however may pose security risks. In scenarios featuring high security requirements, SFTP and SCP are recommended for configuration file restoration.

In FIPS mode, FTP cannot be used to restore configuration files.



#### Procedure

* Copy the configuration file from the FTP server when the device functions as an FTP client.
  1. Set up an FTP connection with the FTP server.
     
     
     ```
     [ftp](cmdqueryname=ftp) [ ipv6 ] host-ip
     ```
  2. Transfer the configuration file.
     
     
     
     On the device, run the [**get**](cmdqueryname=get) command to copy the configuration file from the PC that functions as an FTP server to the specified path on the device.
     
     ```
     [get](cmdqueryname=get) remote-filename [ local-filename ]
     ```
* Copy the configuration file from the FTP client when the device functions as an FTP server.
  1. On the PC that functions as an FTP client, initiate an FTP connection with the device.
     
     
     
     In this example, the IP address of the device is 10.110.24.254, the FTP user name created on the device is **huawei**, and the password of the FTP user is **YsHsjx\_202206**.
     
     ```
     C:\Documents and Setting\Administrator> ftp 10.110.24.254
     Connected to 10.110.24.254.
     220 FTP service ready.
     User (10.110.24.254:(none)): huawei
     331 Password required for huawei.
     Password:
     230 User logged in.
     ```
  2. Transfer the configuration file.
     
     
     
     On the PC that functions as an FTP client, run the **put** command to copy the configuration file from the PC to the specified path on the device.
     
     ```
     ftp> put local-filename [ remote-filename ]
     ```

#### Verifying the Configuration

Run the [**dir**](cmdqueryname=dir) command on the device to check whether the configuration file has been successfully copied from the PC to the device.