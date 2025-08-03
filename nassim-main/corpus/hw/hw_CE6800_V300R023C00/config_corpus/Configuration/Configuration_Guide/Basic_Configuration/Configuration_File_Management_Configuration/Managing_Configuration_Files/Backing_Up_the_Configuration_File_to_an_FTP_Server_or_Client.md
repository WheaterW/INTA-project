Backing Up the Configuration File to an FTP Server or Client
============================================================

Backing Up the Configuration File to an FTP Server or Client

#### Prerequisites

Before backing up the configuration file to an FTP server or client, you have completed the following tasks:

* If the device functions as an FTP client, connect it to an FTP server. For details, see "Configuring a Device as an FTP Client" in Configuration Guide > Basic Configuration.
* If the device functions as an FTP server, connect it to an FTP client. For details, see "Configuring a Device as an FTP Server" in Configuration Guide > Basic Configuration.
* The weak security algorithm/protocol feature package (WEAKEA) has been installed using the **install feature-software WEAKEA** command.


#### Context

If the device is unexpectedly damaged, the configuration file cannot be restored. In this case, a backup configuration file is required for restoring the device configurations. You can back up the configuration file through FTP using either of the following methods:

* If the device functions as an FTP client, back up the configuration file to an FTP server.
* If the device functions as an FTP server, back up the configuration file to an FTP client.

Select one method as required.

![](public_sys-resources/note_3.0-en-us.png) 

Backing up the configuration file through FTP is a simple process, which however may pose security risks. In scenarios featuring high security requirements, SFTP and SCP are recommended for configuration file backup.

In FIPS mode, FTP cannot be used to back up configuration files.



#### Procedure

* Back up the configuration file to the FTP server when the device functions as an FTP client.
  1. Set up an FTP connection with the FTP server.
     
     
     ```
     [ftp](cmdqueryname=ftp) [ ipv6 ] host-ip
     ```
  2. Transfer the configuration file.
     
     
     
     On the device, run the [**put**](cmdqueryname=put) command to upload the configuration file to the specified path on the PC that functions as an FTP server.
     
     ```
     [put](cmdqueryname=put) local-filename [ remote-filename ]
     ```
* Back up the configuration file to the FTP client when the device functions as an FTP server.
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
     
     
     
     On the PC, run the **get** command to download the configuration file to the specified path on the PC.
     
     ```
     ftp> get remote-filename [ local-filename ]
     ```

#### Verifying the Configuration

The configuration file is saved to the working directory of the FTP user, and the size of the configuration file on the device is the same as that on the FTP server or client.