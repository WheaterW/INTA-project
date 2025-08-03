ZTP Fundamentals
================

ZTP Fundamentals

#### Typical Networking

In [Figure 1](#EN-US_CONCEPT_0000001512834834__fig16534750131417), the device functions as a DHCP client to periodically send DHCP request packets to the DHCP server in order to obtain configuration information. The DHCP server responds with DHCP reply packets that contain information about the IP address allocated to the device, IP address of the intermediate file server, and intermediate file server login method. After receiving the DHCP reply packets, the device connects to the intermediate file server to obtain the configuration information about the deployment files, based on which the device then automatically obtains deployment files from the specified deployment file server and sets them as the files to be loaded for the next startup. These deployment files are then automatically loaded by the device upon restart.

**Figure 1** Typical network diagram of ZTP  
![](../images/en-us_image_0000001513154418.png "Click to enlarge")

* **DHCP server**: allocates a temporary management IP address, default gateway address, DNS server address, and intermediate file server address to the device to be deployed.
* **Syslog server**: uploads user logs recorded during the ZTP process to the network management system (NMS).
* **DHCP relay agent**: forwards packets exchanged between the device to be deployed and the DHCP server when they are located on different network segments.
* **Intermediate file server**: stores the intermediate file required for ZTP, which can be an INI file or a Python script. By parsing the intermediate file, the device to be deployed obtains information about the deployment file server address and deployment files. An intermediate file server must be an SFTP, HTTP, TFTP, or FTP file server.
* **Deployment file server**: stores the deployment files to be loaded to the device to be deployed, including the system software, configuration file, and patch file. The deployment file server and intermediate file server can be combined, which must be an SFTP, HTTP, TFTP, or FTP file server.
* **DNS server**: provides mappings between domain names and IP addresses, and resolves the file server domain name to an IP address for the device to be deployed. Based on the resolved IP address, the device can obtain requested files from the file server.
  
  ![](../public_sys-resources/note_3.0-en-us.png) 
  
  TFTP, FTP, or HTTP poses security risks, and SFTP is recommended for file transfer.


#### Deployment Modes

Devices support multiple ZTP deployment modes, which are applicable to different scenarios, as described in [Table 1](#EN-US_CONCEPT_0000001512834834__table15648518151313). You can select a proper deployment mode as required.

**Table 1** ZTP modes
| Deployment Mode | Description | Application Scenario | Task |
| --- | --- | --- | --- |
| DHCP-based ZTP (with a controller) | : Option 148 is configured on the DHCP server on the network. This option parameter specifies the controller address information. Devices obtain the information through DHCP. The device establishes a NETCONF connection with the controller based on the obtained controller information. Then you can perform deployment configuration on the device through the controller. | This mode applies to batch device deployment when a controller is deployed. | [Configuring DHCP-based ZTP (with a Controller)](../galaxy_ztp_cfg_0040.html) |
| DHCP-based ZTP (without a controller) | During deployment, the device functions as a DHCP client to periodically send DHCP request packets to the DHCP server in order to obtain configuration information. The DHCP server responds with DHCP reply packets that contain information about the IP address allocated to the device, IP address of the intermediate file server, and intermediate file server login method. After receiving the DHCP reply packets, the device connects to the intermediate file server to obtain the configuration information about the deployment files, based on which the device then automatically obtains deployment files from the specified deployment file server and sets them as the files to be loaded for the next startup. These deployment files are then automatically loaded by the device upon restart. | This mode applies to batch device deployment when no controller is deployed. | [Configuring DHCP-based ZTP (Without a Controller)](../galaxy_ztp_cfg_0029.html) |

DHCP-based ZTP is simple. You can use this deployment mode as long as a DHCP server is deployed. However, this deployment mode may cause data leakage and interception, which poses security risks. In deployment scenarios that require high security, you can deploy a dedicated bootstrap server and use two-way authentication and data encryption to ensure the data reliability for DHCP-based ZTP. For details, see [SZTP Fundamentals](en-us_concept_0000001513154370.html) and [Configuring DHCP-based ZTP (Without a Controller)](../galaxy_ztp_cfg_0029.html).


#### Deployment Process

Device deployment processes include the deployment processes for devices with factory configurations and with non-factory configurations.

* After a device is powered on with factory configurations, if the device receives a packet carrying DHCP option 143, the device starts the SZTP process. Otherwise, the device starts the DHCP-based ZTP process.
* When a device is powered on with non-factory configurations, ZTP is not supported by default, and the device starts using the non-factory configuration file.

**Figure 2** Deployment process after a device is powered on with factory configurations  
![](../images/en-us_image_0000001512834870.png "Click to enlarge")
![](../public_sys-resources/note_3.0-en-us.png) 

* When deploying a device with factory configurations, you are advised not to manually deliver the same configurations as those delivered during ZTP. If the deployment fails, the configurations will be deleted.
* ZTP processes depend on OPS. You can run the ****ops stop process**** **process-id** command to stop a ZTP process. Running this command may retain the configurations that have been delivered during ZTP on the device.