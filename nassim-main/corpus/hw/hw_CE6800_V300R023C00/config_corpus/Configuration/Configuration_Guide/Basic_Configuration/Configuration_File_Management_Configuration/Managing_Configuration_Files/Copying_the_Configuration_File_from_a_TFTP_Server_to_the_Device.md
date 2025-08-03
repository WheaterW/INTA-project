Copying the Configuration File from a TFTP Server to the Device
===============================================================

Copying the Configuration File from a TFTP Server to the Device

#### Prerequisites

Before copying the configuration file from a TFTP server to the device, you have completed the following tasks:

* Ensure that the device has been connected to the TFTP server. For details, see "Configuring a Device as a TFTP Client" in Configuration Guide > Basic Configuration.

* The weak security algorithm/protocol feature package (WEAKEA) has been installed using the **install feature-software WEAKEA** command.

#### Context

If functions do not operate properly due to incorrect configurations, you can copy the backup configuration file from the TFTP server to the device to restore the functions.

![](public_sys-resources/note_3.0-en-us.png) 

Restoring the configuration file through TFTP is a simple process, which however may pose security risks. In scenarios featuring high security requirements, SFTP and SCP are recommended for configuration file restoration.

In FIPS mode, TFTP cannot be used to restore configuration files.



#### Procedure

1. Copy the configuration file from the TFTP server to the device.
   
   
   ```
   [tftp](cmdqueryname=tftp) [ ipv6 ] hostname-ip get source-filename [ destination-filename ]
   ```

#### Verifying the Configuration

Run the [**dir**](cmdqueryname=dir) command on the device to check whether the configuration file has been successfully copied from the TFTP server to the device.