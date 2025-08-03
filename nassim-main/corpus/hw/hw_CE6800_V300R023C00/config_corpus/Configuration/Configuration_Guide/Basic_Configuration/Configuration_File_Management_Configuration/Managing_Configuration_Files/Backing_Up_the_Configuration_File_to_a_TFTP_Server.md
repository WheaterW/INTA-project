Backing Up the Configuration File to a TFTP Server
==================================================

Backing Up the Configuration File to a TFTP Server

#### Prerequisites

Before backing up the configuration file to a TFTP server, you have completed the following tasks:

* Ensure that the device has been connected to the TFTP server. For details, see "Configuring a Device as a TFTP Client" in Configuration Guide > Basic Configuration.
* The weak security algorithm/protocol feature package (WEAKEA) has been installed using the **install feature-software WEAKEA** command.

#### Context

If the device is unexpectedly damaged, the configuration file cannot be restored. In this case, a backup configuration file is required for restoring the device configurations. You can back up the configuration file through TFTP.

![](public_sys-resources/note_3.0-en-us.png) 

Backing up the configuration file through TFTP is a simple process, which however may pose security risks. In scenarios featuring high security requirements, SFTP and SCP are recommended for configuration file backup.

In FIPS mode, TFTP cannot be used to back up configuration files.



#### Procedure

1. Back up the configuration file to the TFTP server.
   
   
   ```
   [tftp](cmdqueryname=tftp) [ ipv6 ] hostname-ip put sourcefilename [ destination-filename ]
   ```

#### Verifying the Configuration

The configuration file is saved to the working directory of the TFTP user, and the size of the configuration file on the device is the same as that on the TFTP server.