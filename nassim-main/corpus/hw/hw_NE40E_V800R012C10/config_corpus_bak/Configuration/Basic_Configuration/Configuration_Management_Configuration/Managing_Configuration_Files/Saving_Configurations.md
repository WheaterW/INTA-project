Saving Configurations
=====================

Configurations can be saved in a configuration file either automatically or manually.

#### Context

To avoid configuration loss on a device due to power-off or an unexpected reset, the system supports automatic and manual configuration saving.

The configuration file can be automatically saved on the local device or the backup server. If the local database is insufficient in space or damaged or disaster tolerance backup is required, save the configuration file on the backup server to harden the database security.

Perform the following steps on a device.


#### Procedure

* Enable the system to automatically save configurations.
  
  
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**set save-configuration**](cmdqueryname=set+save-configuration) [ **interval** *interval* | **cpu-limit** *cpu-usage* | **delay** *delay-interval* ] \* command to enable the system to automatically save configurations.
     
     + To specify an interval at which configurations are automatically saved, set the **interval** *interval* parameter.
     + To prevent the auto-save function from deteriorating system performance, set the **cpu-limit** *cpu-usage* parameter to specify an upper threshold for CPU usage. In this way, when the auto-save timer is triggered and the CPU usage of the device is detected to be higher than the upper threshold, the device will stop the current auto-save operation.
     + To specify a delay for the device to automatically back up configurations, set the **delay** *delay-interval* parameter. If configurations are changed, the device will automatically save configurations after the delay expires.
     + If the **interval** *interval* and **delay** *delay-interval* parameters are both set, the parameter that specifies an earlier time triggers the auto-save operation. When the time specified by the other parameter arrives, the device checks the configurations again. It performs a new auto-save operation only when detecting a configuration change.
     
     With the auto-save function enabled, a device automatically saves configurations to the next-startup configuration file on condition that the current configurations are different from those in the next-startup configuration file and the time specified using the **interval** *interval* parameter arrives, regardless of whether the [**save**](cmdqueryname=save) command is run.
  3. (Optional) Run the [**set save-configuration backup-to-server**](cmdqueryname=set+save-configuration+backup-to-server) **server** [ [**ipv6**](cmdqueryname=ipv6) ] *server-ip* [ **vpn-instance** *vpn-instance-name* ] **transport-type** { **tftp** | { **ftp** | **sftp** } [ **port** *port-value* ] **user** *user-name* **password** *password* } [ **path** *folder* ] command to configure the configuration file to be saved on the specific server.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     + When TFTP is used to transmit files, run the [**tftp client-source**](cmdqueryname=tftp+client-source) command to configure the loopback interface of the Router as the source address of the client.
     + The system supports a maximum of five file servers. The servers are independent of each other. If a file fails to be uploaded to one of the servers, the system reports an alarm to the NMS and records a log locally.
     + In disaster recovery scenarios, you can run the [**set save-configuration backup-to-server server**](cmdqueryname=set+save-configuration+backup-to-server+server) command repeatedly to configure multiple file servers. Before running this command, you need to enable the auto-save function using the [**set save-configuration**](cmdqueryname=set+save-configuration) command and enable the FTP, SFTP, or TFTP service on the server.
     + A device supports a server with the same IP address but different VPN instances. To be specific, if different VPN instances have been configured for a server with a specific IP address, the device can send configuration files to any of the VPN instances.
* Save configurations manually.
  
  
  
  Run the [**save**](cmdqueryname=save) [ *configuration-file* ] command to save the current configuration.
  
  The configuration file name extension must be .dat, .cfg, or .zip.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  When you save the configuration file for the first time without specifying *configuration-file*, you are asked whether to name the configuration file **vrpcfg.zip**. The configuration file containing only the default configurations is initially named **vrpcfg.zip**.