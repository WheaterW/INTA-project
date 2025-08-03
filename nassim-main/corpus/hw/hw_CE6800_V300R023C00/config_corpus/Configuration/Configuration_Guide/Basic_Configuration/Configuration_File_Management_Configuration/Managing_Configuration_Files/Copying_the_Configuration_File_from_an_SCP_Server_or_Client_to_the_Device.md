Copying the Configuration File from an SCP Server or Client to the Device
=========================================================================

Copying the Configuration File from an SCP Server or Client to the Device

#### Prerequisites

Before copying the configuration file from an SCP server or client to the device, you have completed the following tasks:

* If the device functions as an SCP client, connect it to an SCP server. For details, see "Configuring a Device as an SCP Client" in Configuration Guide > Basic Configuration.
* If the device functions as an SCP server, connect it to an SCP client. For details, see "Configuring a Device as an SCP Server" in Configuration Guide > Basic Configuration.


#### Context

If functions do not operate properly due to incorrect configurations, you can copy the backup configuration file of the device from an SCP server or client to restore the configuration file using either of the following methods:

* If the device functions as an SCP client, copy the configuration file from an SCP server to the device.
* If the device functions as an SCP server, copy the configuration file from an SCP client to the device.

Select one method as required.


#### Procedure

* Copy the configuration file from the SCP server when the device functions as an SCP client.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view) 
     ```
  2. Transfer the configuration file.
     
     
     
     On the device, run the following command to copy the configuration file from the PC that functions as an SCP server to the specified path on the device:
     
     ```
     [scp](cmdqueryname=scp) source-filename destination-filename
     ```
     
     For example, to copy the **vrpcfg.cfg** file from the SCP server at 10.1.1.1 to the device using SCP, run the following command. (The following information is for reference only.)
     
     ```
     <HUAWEI> system-view
     [~HUAWEI] scp scpuser@10.1.1.1:flash:/vrpcfg.cfg vrpcfg-backup.cfg 
     Trying 10.1.1.1...
     Press CTRL+K to abort
     Connected to 10.1.1.1...
     The server is not authenticated. Continue to access it? [Y/N]:y
     Save the server's public key? [Y/N]:y
     The server's public key will be saved with the name 10.1.1.1. Please wait...
     
     Please select public key type for user authentication [R for RSA/D for DSA/E for ECC] Please select [R/D/E]:e 
     Enter password:
     vrpcfg.cfg                      100%          261Bytes            1Kb/s
     ```
* Copy the configuration file from the SCP client when the device functions as an SCP server.
  
  
  
  Run the following command to copy the configuration file from the PC that functions as an SCP client to the specified path on the device:
  
  ```
  [scp](cmdqueryname=scp) source-filename destination-filename
  ```
  
  For example, to copy the **vrpcfg.cfg** file from the SCP client to the device at 10.2.2.2 using SCP, run the following command. (The following information is for reference only.)
  
  
  
  ```
  C:\Documents and Settings\Administrator> scp vrpcfg.cfg scpuser@10.2.2.2:flash:/vrpcfg-backup.cfg 
  The authenticity of host '10.2.2.2 (10.2.2.2)' can't be established.
  DSA key fingerprint is 46:b2:8a:52:88:42:41:d4:af:8f:4a:41:d9:b8:4f:ee.
  Are you sure you want to continue connecting (yes/no)? yes
  Warning: Permanently added '10.2.2.2' (DSA) to the list of known hosts.
  scpuser@10.2.2.2's password:
  vrpcfg.cfg                                    100% 1257     1.2KB/s   00:00
  Read from remote host 10.2.2.2: Connection reset by peer
  
  C:\Documents and Settings\Administrator>
  ```

#### Verifying the Configuration

Run the [**dir**](cmdqueryname=dir) command on the device to check whether the configuration file has been successfully copied from the PC to the device.