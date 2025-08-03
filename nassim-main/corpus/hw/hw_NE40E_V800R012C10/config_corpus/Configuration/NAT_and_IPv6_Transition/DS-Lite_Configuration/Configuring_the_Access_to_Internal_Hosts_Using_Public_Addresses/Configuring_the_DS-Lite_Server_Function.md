Configuring the DS-Lite Server Function
=======================================

This section describes how to configure the DS-Lite server function so that external users can proactively access the private network server.

#### Context

DS-Lite can be configured to allow users on a private network to access public network services, while hiding the structure of the private network and shielding internal hosts. In this case, a user on an external network cannot communicate with a private network user.

To solve this problem, the DS-Lite internal server is introduced. The DS-Lite internal server statically configures the mapping between the private IP address and port number and the public IP address and port number or between the private IP address and the public IP address, reversing translation from public IP addresses to private IP addresses


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ds-lite instance**](cmdqueryname=ds-lite+instance) *instance-name* [ **id** *id* ]
   
   
   
   The DS-Lite instance view is displayed.
3. Run either of the following commands to configure an internal DS-Lite server:
   
   
   * If multiple internal servers are assigned the same public IP address, run the [**ds-lite server**](cmdqueryname=ds-lite+server) **protocol** { **tcp** | **udp** } **global** *global-address* [ *global-protocol* | *global-protocol*-number ] [ **vpn-instance** *vpn-instance-name* ] **inside** *host-address* [ *host-port* | *host-port*-number ] **cpe** *cpe-address* [ **vpn-instance** *vpn-instance-name* ] [ **outbound** ] command to configure a DS-Lite internal server for a specific type of packet.
   * If each internal server is assigned a specific public IP address, run the [**ds-lite server**](cmdqueryname=ds-lite+server) **global** *global-address* [ **vpn-instance** *vpn-instance-name* ] **inside** *host-address* **cpe** *cpe-address* [ **vpn-instance** *vpn-instance-name* ] [ **outbound** ] command to configure a DS-Lite internal server.
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The IP address of the DS-Lite internal server cannot be the same as the IP address of a DHCP server. Otherwise, a message indicating a conflict is displayed.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.