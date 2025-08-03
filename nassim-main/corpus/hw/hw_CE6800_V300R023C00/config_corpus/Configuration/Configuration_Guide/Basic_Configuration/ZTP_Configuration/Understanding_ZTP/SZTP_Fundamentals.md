SZTP Fundamentals
=================

SZTP Fundamentals

#### Context

SZTP applies to scenarios that require high security. DHCP-based ZTP is easy to implement because you only need to deploy a DHCP server. However, it may lead to data leakage or interception, posing security risks. To mitigate the security risks, you can deploy a DHCP server and a dedicated bootstrap server and use two-way authentication and data encryption.


#### Basic Networking

In [Figure 1](#EN-US_CONCEPT_0000001513154370__fig16534750131417), the device functions as a DHCP client to periodically send DHCP request packets to the DHCP server in order to obtain configuration information. The DHCP server responds with DHCP reply packets that contain information about the IP address allocated to the device, as well as the IP address or domain name of the bootstrap server. After obtaining such information, the device establishes an HTTPS connection with the bootstrap server through two-way authentication based on an initial certificate. The device then obtains information about deployment files from the bootstrap server, connects to the deployment file server, obtains the deployment files, and sets them as the files to be loaded for the next startup. These deployment files are then automatically loaded by the device upon restart.

**Figure 1** SZTP networking  
![](../images/en-us_image_0000001563754745.png "Click to enlarge")

* **DHCP server**: allocates a temporary management IP address, default gateway address, DNS server address, and bootstrap server address or domain name to the device to be deployed through SZTP.
* **DHCP relay agent**: forwards packets exchanged between the device to be deployed and the DHCP server when they are located on different network segments.
* **Bootstrap server**: is used to guide SZTP. After establishing a secure connection with the device to be deployed through SZTP, the bootstrap server sends deployment file information (such as the address of the deployment file server and deployment file version) to the device.
* **Deployment file server**: stores the deployment files to be loaded to the device to be deployed, including the system software, configuration file, and patch file.
* **DNS server**: provides mappings between domain names and IP addresses, and resolves the domain name of the bootstrap server to an IP address.
* **Syslog server**: uploads user logs recorded during the SZTP process to the NMS.![](../public_sys-resources/note_3.0-en-us.png) 
  
  A deployment file server used for SZTP must be an HTTPS server.


#### Trusted Connection

During SZTP, the device establishes a trusted connection with the bootstrap server through two-way authentication and obtains deployment file information from the server. The device then functions as an HTTPS client to establish an HTTPS connection with the deployment file server and download deployment files. Certificates listed in [Table 1](#EN-US_CONCEPT_0000001513154370__table728912121159) are required for establishing a secure connection between the device and bootstrap server.

**Table 1** Certificates on which a trusted connection depends
| Certificate Type | Description |
| --- | --- |
| Device identity certificate | This certificate is an initial certificate. It is an 802.1AR certificate generated using the Huawei CA signature before device delivery. By default, Huawei devices have built-in identity certificates before delivery. The certificate contains information such as the public key and device SN. |
| Huawei root CA certificate | / |
| Huawei level-2 CA certificate | / |
| Ownership voucher | It is a Cryptographic Message Syntax (CMS) file, which is issued by the device vendor to the customer. Huawei plans to use the carrier's level-2 CA to issue an ownership voucher to the customer. The voucher contains the release time, expiration time, hardware serial number for connecting to Huawei devices, and root certificate of the bootstrap server. |
| Owner certificate | This certificate is an X.509 certificate, which is used to identify an owner. The device can use this certificate to verify the signature of conveyed information. |


![](../public_sys-resources/note_3.0-en-us.png) 

The ownership voucher is valid only when the Huawei level-2 CA certificate is pre-configured on the bootstrap server.

The bootstrap server has a built-in Huawei level-2 CA certificate, an ownership voucher, and an owner certificate. Initial device certificates include the device identity certificate, Huawei root CA certificate, and Huawei level-2 CA certificate.

* You can configure deployment file information (such as the deployment file server address and deployment file name) on the bootstrap server. The deployment file information is stored in onboarding information.
* If the device does not have a built-in trust root certificate, it establishes an untrusted connection with the bootstrap server. The bootstrap server encapsulates the onboarding information, ownership voucher, and owner certificate into bootstrapping data and sends the data to the device.
* After verifying the signature of the ownership voucher, the device performs operations shown in [Figure 2](#EN-US_CONCEPT_0000001513154370__fig91121911194116): It uses the built-in Huawei root level-2 CA certificate to authenticate the owner certificate to form a complete trust chain, and then verifies the signature of the onboarding information. The device parses the deployment file information from the onboarding information, establishes an HTTPS connection with the deployment file server, and downloads the deployment files.**Figure 2** Establishing a trust chain  
  ![](../images/en-us_image_0000001563994673.png)
  
  In practice, you can deploy one or more bootstrap servers based on security requirements. If multiple bootstrap servers are deployed, a redirect-to bootstrap server address may be configured on a bootstrap server. Redirection information is stored in Redirect Information. When an untrusted connection is established between the device and bootstrap server, the bootstrap server encapsulates the Redirect Information, ownership voucher, and owner certificate into bootstrapping data and sends the data to the device to establish a trusted connection. The device then obtains the IP address of the redirect-to bootstrap server and the trust anchor certificate from the Redirect Information. After the trust anchor certificate is installed, the device establishes a trusted connection with the redirect-to bootstrap server until the device obtains the onboarding information, which contains deployment file information.

#### Deployment Process

[Figure 3](#EN-US_CONCEPT_0000001513154370__fig833142114548) shows the SZTP process.

**Figure 3** SZTP process  
![](../images/en-us_image_0000001720755253.png)

The SZTP process involves the following phases:

1. Powering on and starting the device
   
   If a non-factory configuration file is available, the device starts with that configuration file. Otherwise, the device automatically starts the ZTP process.
2. Obtaining DHCP information
   
   The device broadcasts DHCP Request packets through its management network interface and Ethernet interfaces. The DHCP server sends a DHCP reply packet to the device. If the reply packet contains the DHCP option 143 field, the device starts the SZTP process. If the reply packet does not contain the DHCP option 143 field, the device starts the DHCP-based ZTP process. After entering the SZTP process, the device obtains information such as the device IP address, default gateway address, Syslog server address, and bootstrap server address from the DHCP server. The device obtains the IPv4 address of the Syslog server from the DHCP reply packet to enable the Syslog server function. Information about important phases during SZTP is recorded in user logs, which the Syslog server will upload to the NMS.
3. Obtaining deployment file information
   
   The device parses the bootstrap server address from the DHCP option 143 field, establishes a secure connection with the bootstrap server, and obtains deployment file information.
4. Restarting the device
   
   The device automatically sets the downloaded deployment files as those to be loaded for its next startup. The device then restarts to complete automatic deployment.

![](../public_sys-resources/note_3.0-en-us.png) 

* When deploying a device with factory configurations, you are advised not to manually deliver the same configurations as those delivered during ZTP. If the deployment fails, the configurations will be deleted.
* SZTP processes depend on OPS. You can run the **ops stop process** *process-id* command to stop a ZTP process. Running this command may retain the configurations that have been delivered during SZTP on the device.