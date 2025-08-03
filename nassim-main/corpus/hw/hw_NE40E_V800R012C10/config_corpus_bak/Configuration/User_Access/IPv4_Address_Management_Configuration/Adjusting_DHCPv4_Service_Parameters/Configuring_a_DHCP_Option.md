Configuring a DHCP Option
=========================

DHCP provides a framework for parameter transmission over the TCP/IP network. The DHCP client and server can transmit the negotiated parameters and control information to each other through options.

#### Context

When a terminal device, such as the set top box of the digital TV, accesses the network, the NE40E cannot identify its domain according to its user name. Therefore, the NE40E cannot allocate any IP address to the device. In this case, the terminal device uses Option 60 to carry the domain information when initiating the DHCP request. After receiving the DHCP request, the NE40E allocates an IP address to the device according to the domain information contained in Option 60.

Option 121 allows a DHCP server to allocate static routes to DHCP clients.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**dhcp option-60**](cmdqueryname=dhcp+option-60) [ **cn** | [ **offset** *offset-value* ] { **length** *length* | **sub-option** *suboption-id* [ **sub-offset** *sub-offset-id* ] [ **sub-length** *sub-length* ] } ] { **domain-included** | **included-in-domain** } { **partial-match** | **exact-match** } [ **encrypt** ]
   
   
   
   The Option 60 attribute is set for DHCP packets. This attribute allows the device to allocate IP addresses from a corresponding address pool based on the domain name. Option 60 can be configured to contain the domain name. Partial match or exact match of the domain name can be configured. You can configure **encrypt** to encrypt the Option 60 attribute.
   
   If user domain information is obtained from the vendor-class information, the character string following the domain name delimiter (defaulting to @) in the vendor-class field is used as the domain name. If no user domain information is obtained from the vendor-class information, the NE40E performs the following procedure to continue searching for the information. If there is no domain name delimiter in the field, the NE40E performs a fuzzy or exact match of the domain name information based on the configured mode. The procedure will stop after user domain information is obtained.
   1. Check if the [**dhcp option-60**](cmdqueryname=dhcp+option-60) command is configured in the system view. If the command is configured, obtain user domain information from the Option 60 attribute carried in user packets.
   2. Use the authorization domain configured on the BAS interface as the user domain.
3. Run [**aaa**](cmdqueryname=aaa)
   
   
   
   The AAA view is displayed.
4. Run [**domain**](cmdqueryname=domain) *domain-name*
   
   
   
   A domain is created, and the domain view is displayed.
5. Run [**dhcp option121 route**](cmdqueryname=dhcp+option121+route) *ip-addr* *mask* *gateway-address*
   
   
   
   Static routes are allocated to domain users.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.