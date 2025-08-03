Configuring NAT64 ALG
=====================

This section describes how to configure the NAT64 application level gateway (ALG) function.

#### Usage Scenario

ALG is short for application level gateway. Most application layer protocol packets carry user IP addresses and port numbers. NAT64 translates only network layer addresses and transport layer ports. Therefore, you need an ALG to translate the IP addresses and port numbers carried in the Data field of application layer packets. NAT64 ALG provides transparent translation for special application layer protocols.

NAT64 translates only the IP addresses contained in user data packets and the port information in the Transmission Control Protocol (TCP)/User Datagram Protocol (UDP) headers of data packets. For special protocols (for example, FTP) the Data field in a packet contains IP address or port information. NAT64, however, does not take effect on an IP address or port information in the Data field of a packet. As a result, a protocol-specific connection fails to be established. A good way to solve the NAT64 translation issue for these special protocols is to use the ALG function. As a special translation agent for application layer protocols, the ALG interacts with NAT64. The ALG uses NAT64 state information to change the specific data in the Data field of IP packets so that application layer protocols can run across internal and external networks.


#### Pre-configuration Tasks

Before configuring NAT64 ALG, complete the following tasks:

* Configure basic NAT64 functions.
* Configure centralized NAT64 translation.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   The system view is displayed.
2. Run [**nat64 alg server-address**](cmdqueryname=nat64+alg+server-address) *server-ip* [ *end-ip* ] **protocol** { **all** | **ftp** | **dns** | **http** }
   
   An IPv4 server address list of NAT64 ALG is configured for application layer protocols.
3. Run [**commit**](cmdqueryname=commit)
   
   The configuration is committed.
4. Run [**nat64 instance**](cmdqueryname=nat64+instance) *instance-name* [ [**id**](cmdqueryname=id) *id* ]
   
   The NAT64 instance view is displayed.
5. Run [**nat64 alg**](cmdqueryname=nat64+alg) { **all** | **dns** | { **ftp** [ **rate-threshold** *value* ] } | **http** }
   
   NAT64 ALG is enabled for an application layer protocol.
   
   After an IPv4 server address or an IPv4 server address list of NAT64 ALG for a specific or all application layer protocols is configured, the configuration can take effect only if the ALG function for the application layer protocols is enabled in the NAT64 instance view.
6. Run [**commit**](cmdqueryname=commit)
   
   The configuration is committed.

#### Checking the Configurations

After configuring the NAT ALG function, you can check the NAT64 instance configuration, including NAT ALG information.

* Run the [**display nat64 instance**](cmdqueryname=display+nat64+instance) [ *instance-name* ] command to check the configuration of a NAT64 instance.