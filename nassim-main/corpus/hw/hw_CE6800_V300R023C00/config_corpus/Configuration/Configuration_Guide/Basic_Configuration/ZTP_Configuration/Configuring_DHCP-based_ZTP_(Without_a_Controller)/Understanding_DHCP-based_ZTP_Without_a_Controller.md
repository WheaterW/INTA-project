Understanding DHCP-based ZTP Without a Controller
=================================================

Understanding DHCP-based ZTP Without a Controller

#### Basic Networking

In [Figure 1](#EN-US_CONCEPT_0000001512834846__fig16534750131417), the device functions as a DHCP client to periodically send DHCP request packets to the DHCP server in order to obtain configuration information. The DHCP server responds with DHCP reply packets that contain information about the IP address allocated to the device, IP address of the intermediate file server, and intermediate file server login method. After receiving the DHCP reply packets, the device connects to the intermediate file server to obtain the configuration information about the deployment files, based on which the device then automatically obtains deployment files from the specified deployment file server and sets them as the files to be loaded for the next startup. These deployment files are then automatically loaded by the device upon restart.

**Figure 1** DHCP-based ZTP  
![](figure/en-us_image_0000001512834906.png)

* **DHCP server**: allocates a temporary management IP address, default gateway address, DNS server address, and intermediate file server address to the device to be deployed.
* **Syslog server**: uploads user logs recorded during the ZTP process to the NMS.
* **DHCP relay agent**: forwards packets exchanged between the device to be deployed and the DHCP server when they are located on different network segments.
* **Intermediate file server**: stores the intermediate file required for ZTP, which can be an INI file or a Python script. By parsing the intermediate file, the device to be deployed obtains information about the deployment file server address and deployment files. An intermediate file server must be an SFTP, HTTP, TFTP, or FTP file server.
* **Deployment file server**: stores the deployment files to be loaded to the device to be deployed, including the system software, configuration file, and patch file. The deployment file server and intermediate file server can be combined, which must be an SFTP, HTTP, TFTP, or FTP file server.
* **DNS server**: provides mappings between domain names and IP addresses, and resolves the file server domain name to an IP address for the device to be deployed. Based on the resolved IP address, the device can obtain requested files from the file server.


#### Deployment Process

* [Figure 2](#EN-US_CONCEPT_0000001512834846__fig833142114548) shows the DHCP-based ZTP process.

**Figure 2** DHCP-based ZTP process  
![](figure/en-us_image_0000001513154446.png)

The ZTP process involves the following phases:

1. Powering on and starting the device
   
   If a non-factory configuration file is available, the device starts with that configuration file. Otherwise, the device automatically starts the ZTP process.
2. Obtaining DHCP information
   
   The device broadcasts DHCP Request packets through its management network interface and Ethernet interfaces. After receiving the DHCP request packet, the DHCP server sends a DHCP reply packet to the device. Options in the packet contain the device-requested information, including the IP address allocated to the device, default gateway address, IP address of the intermediate file server, IP address of the Syslog server, and intermediate file name. The device obtains the IPv4 address of the Syslog server from the DHCP reply packet to enable the Syslog server function. Information about important phases during ZTP is recorded in user logs, which the Syslog server will upload to the NMS.
3. Enabling the Syslog server
   
   The device obtains the IPv4 address of the Syslog server from the DHCP reply packet to enable the Syslog server function. Information about important phases during ZTP is recorded in user logs, which the Syslog server will upload to the NMS.
4. Obtaining the intermediate file and deployment files
   
   The device downloads the intermediate file from the intermediate file server according to the information carried in the DHCP reply packet, and then downloads deployment files from the deployment file server according to the intermediate file.
   
   If the intermediate file is an INI file, the device downloads deployment files based on the deployment file server address and deployment file names contained in the intermediate file. If the intermediate file is a Python script, the device automatically runs the script to download deployment files from the deployment file server.
5. Restarting the device
   
   The device automatically sets the downloaded deployment files as those to be loaded for its next startup. The device then restarts to complete automatic deployment.

1. Powering on and starting the device
   
   If a non-factory configuration file is available, the device starts with that configuration file. Otherwise, the device automatically starts the ZTP process.
2. Obtaining DHCP information
   
   The device sends a DHCP request packet through VLANIF 1. The DHCP server sends a DHCP reply packet to the device. Options in the packet contain the device-requested information, including the IP address allocated to the device, default gateway address, IP address of the file server, IP address of the Syslog server, and deployment file information. The device obtains the IPv4 address of the Syslog server from the DHCP reply packet to enable the Syslog server function. Information about important phases during ZTP is recorded in user logs, which the Syslog server will upload to the NMS.
3. Enabling the Syslog server
   
   The device obtains the IPv4 address of the Syslog server from the DHCP reply packet to enable the Syslog server function. Information about important phases during ZTP is recorded in user logs, which the Syslog server will upload to the NMS.
4. Obtaining deployment files
   
   The device downloads deployment files from the deployment file server based on the information obtained from the DHCP reply packet.
5. Restarting the device
   
   The device automatically sets the downloaded deployment files as those to be loaded for its next startup. The device then restarts to complete automatic deployment.