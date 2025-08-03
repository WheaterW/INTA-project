Understanding DHCP-based ZTP with a Controller
==============================================

Understanding DHCP-based ZTP with a Controller

#### Fundamentals

In [Figure 1](#EN-US_CONCEPT_0000001563994661__fig11150103123217), the controller functions as a DHCP server, and the device to be deployed functions as a DHCP client. The device periodically sends DHCP request packets to the controller to obtain controller information. Upon receiving each request packet, the controller sends a DHCP reply packet to the device. The reply packet contains the IP address allocated to the device and the IP address and port number of the controller. The device then establishes a NETCONF connection with the controller based on the controller information to obtain the deployment configurations from the controller.

**Figure 1** Network diagram of DHCP-based ZTP when a controller is deployed  
![](figure/en-us_image_0000001563994729.png)

* **iMaster NCE-Fabric**: functions as a DHCP server to allocate the temporary management IP address, default gateway address, controller's IP address and port number, DNS server's IP address, bootstrap server's IP address and port number, and Syslog server's IP address to the device that performs ZTP.
* **DHCP server**: allocates the temporary management IP address, default gateway address, controller's IP address and port number, DNS server's IP address, bootstrap server's IP address and port number, and Syslog server's IP address to the device that performs ZTP.
* **DNS server**: provides mappings between domain names and IP addresses, and resolves the domain name of the bootstrap server to an IP address.
* **Bootstrap server**: stores CA certificates applied by users. For security purposes, no initial certificate is available on iMaster NCE-Fabric. For this reason, the device needs to download a CA certificate from the bootstrap server so that two-way authentication for establishing a NETCONF connection between the device and iMaster NCE-Fabric can be successfully performed. Currently, iMaster NCE-Fabric integrates the bootstrap server function.
* **Syslog server**: uploads user logs recorded during the ZTP process to the NMS.
* **DHCP relay agent**: forwards packets exchanged between the device to be deployed and the DHCP server when they are located on different network segments.

The DHCP server can be deployed independently, in which case it will send the allocated temporary management IP address, allocated default gateway address, and a Python script containing controller information to the device. The device then runs the Python script. For details about ZTP in this scenario, see "Using ZTP to Automatically Deployed an Underlay Network - Simplified Deployment (Third-Party Server)" in the [Huawei CloudFabric Data Center Network Solution Product Documentation](https://support.huawei.com/enterprise/en/network-solution/cloudfabric-pid-22604572).


#### ZTP Process

[Figure 2](#EN-US_CONCEPT_0000001563994661__fig990719312244) shows the flowchart of DHCP-based ZTP when a controller is deployed.

**Figure 2** Flowchart of DHCP-based ZTP when a controller is deployed  
![](figure/en-us_image_0000001563994717.png)

The ZTP process involves the following phases:

1. Powering on and starting the device
   
   If a non-factory configuration file is available, the device starts with that configuration file. Otherwise, the device automatically starts the ZTP process.
2. Obtaining information through DHCP
   
   The device broadcasts DHCP Request packets through its management network interface and Ethernet interfaces. The DHCP server sends a DHCP reply packet to the device. If the reply packet contains the DHCP Option 148 and controller information, the device starts the DHCP Option-based ZTP process. After entering the DHCP option-based ZTP process with a controller, the device obtains information such as the device IP address, default gateway address, controller's IP address and port number, bootstrap server's IP address and port number, and Syslog server's IP address from the DHCP server. The device obtains the IP address of the Syslog server from the DHCP reply packet to enable the Syslog server function. Information about important phases during ZTP is recorded in user logs, which the Syslog server will upload to the NMS.
3. (Optional) Downloading a CA certificate from the bootstrap server
   
   This phase is mandatory when no initial certificate is available on the controller and you want to use controller-based ZTP.
   
   After receiving a DHCP reply packet carrying the DHCP option 43 field (suboption 5), the device downloads a CA certificate from the bootstrap server as follows:
   
   1. The device establishes an HTTPS connection with the bootstrap server based on the obtained IP address and port number of the bootstrap server.
   2. The device sends a request packet to the bootstrap server to download a CA certificate. The request packet carries the device ESN or the IP address of the bootstrap server. If the option parameter specifies the certificate verification mode as **ESN**, the request packet carries the device ESN. If the option parameter specifies the certificate verification mode as **DOMAIN\_IP**, the request packet carries the IP address of the bootstrap server.
   3. The bootstrap server searches for the CA certificate based on the ESN or IP address in the request packet and sends a response packet carrying the CA certificate to the device. The response packet also carries the device ESN or the IP address of the bootstrap server.
   4. After receiving the response packet from the bootstrap server, the device terminates the HTTPS connection with the bootstrap server, parses the response packet, and verifies the validity of the certificate. If the CA certificate sent by the bootstrap server has been signed, the device verifies the signature of the certificate. After the signature verification is successful, the device verifies the certificate. If the CA certificate sent by the bootstrap server has not been signed, the device determines whether to trust the certificate based on the option parameter setting. If the option parameter specifies that the certificate can be trusted, the device verifies the certificate. Otherwise, the device verifies the signature first. In this case, signature verification will fail.
      
      The device verifies the certificate based on the certificate verification mode specified by an option parameter. If the certificate verification mode is **ESN**, the device verifies the certificate based on the device ESN. If the certificate authentication mode is **DOMAIN\_IP**, the device verifies the certificate based on the IP address of the bootstrap server. If the verification fails, the device fails to obtain a CA certificate.
   5. The device imports the obtained CA certificate to the default domain.
4. Establishing a NETCONF connection with the controller
   
   After receiving a DHCP reply packet that contains the DHCP option 148 field carrying the controller information, the device enables NETCONF and proactive NETCONF registration, creates an SSH user named **huawei**. The device establishes a NETCONF connection with the controller based on the obtained IP address and port number of the controller.
5. Restarting the device
   
   The device obtains the deployment configurations from the controller and restarts to complete automatic deployment.