Enabling DHCPv4 Proxy
=====================

To improve DHCPv4 server security, the NE40E is required not to contain real DHCPv4 server addresses in DHCPv4 packets sent to users. To meet this requirement, configure DHCPv4 proxy.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number* [ *.subinterface-number* ]
   
   
   
   The interface view is displayed.
3. Run [**bas**](cmdqueryname=bas)
   
   
   
   A BAS interface is created, and its view is displayed.
4. Run [**access-type**](cmdqueryname=access-type) **layer2-subscriber** [ **default-domain** { **pre-authentication** *predname* | **authentication** [ **force** | **replace** ] *dname* } \* ]
   
   
   
   The access type and related attributes are configured for Layer 2 common users.
   
   
   
   When setting the user access type on a BAS interface, you can set the service attributes of the access users at the same time or later.
5. Run [**dhcp-proxy enable**](cmdqueryname=dhcp-proxy+enable)
   
   
   
   DHCPv4 proxy is enabled.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * Currently, DHCPv4 proxy is used only for the remote address pool of the BAS. The configuration modification does not take effect on online users.
   * DHCPv4 proxy can also be used for Layer 2 users or users using Layer 2 leased line services.
6. (Optional) Run [**dhcp lease-proxy**](cmdqueryname=dhcp+lease-proxy) [ *lease-time* ]
   
   
   
   DHCP lease proxy is enabled on the BAS interface, and the proxy lease is specified.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Using a shorter proxy lease can accelerate the identification of client or link faults. However, users renew their leases more frequently, increasing the processing load of the device. To balance the conflict between fault detection and device load, run the [**dhcp lease-proxy**](cmdqueryname=dhcp+lease-proxy) **first-step** *first-step* **second-step** *second-step* command to enable DHCP lease proxy with step-based proxy leases.
7. (Optional) Run [**dhcp lease-proxy renew-packet through-time**](cmdqueryname=dhcp+lease-proxy+renew-packet+through-time) *time-value*
   
   
   
   The maximum number of times that a lease proxy user's client sends lease renewal packets to the DHCP server before T1 (1/2 of the lease) or T2 (7/8 of the lease) arrives is configured.
8. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.