Configuring the Advertisement of Public Network IPv4 ARP Vlink Direct Routes
============================================================================

On an IPv4 network, advertising public network IPv4 ARP Vlink direct routes helps with precise control of data traffic.

#### Usage Scenario

Layer 3 IP forwarding requires physical interfaces to be specified. In a VLAN environment, however, such forwarding cannot be implemented through logical interfaces. Therefore, Layer 3 interfaces of VLAN users need to be obtained through ARP and routing entries containing Layer 3 interface information needs to be generated. Such routes are called IPv4 ARP Vlink direct routes.

As shown in [Figure 1](#EN-US_TASK_0172365357__fig_dc_vrp_ip-route_cfg_005501), DeviceD uses logical interfaces to connect to Devices A, B, and C at three sites. DeviceE only needs to communicate with DeviceB, but not with DeviceA or DeviceC. You can configure DeviceD to advertise IPv4 ARP Vlink direct routes and configure a route-policy on DeviceD to filter out routes to the network segment of the VLAN for which the logical interfaces are configured and filter out routes to DeviceA and DeviceC.

**Figure 1** Networking diagram of advertising IPv4 ARP Vlink direct routes on the public network  
![](images/fig_dc_vrp_ip-route_cfg_005501.png)  

Before IPv4 ARP Vlink direct routes are advertised, a route-policy can be configured to filter the advertised routes and only routes that match the route-policy can be advertised. In this manner, data traffic can be precisely controlled.

Perform the following steps on the Router on which IPv4 ARP Vlink direct routes need to be advertised.


#### Pre-configuration Tasks

Before advertising IPv4 ARP Vlink direct routes on the public network, configure parameters of a link layer protocol and assign an IP address to each interface to ensure that the link layer protocol on the interfaces is Up.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**arp vlink-direct-route advertise**](cmdqueryname=arp+vlink-direct-route+advertise) [ **route-policy** *route-policy-name* | **route-filter** *route-filter-name* ]
   
   
   
   Advertisement of public network IPv4 ARP Vlink direct routes is configured.
   
   
   
   To filter the routes, you can specify **route-policy** *route-policy-name* or **route-filter** *route-filter-name*.![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Currently, apply clauses cannot be used to set route attributes for matched ARP Vlink direct routes.
   
   
   
   
   After the device is enabled to advertise IPv4 ARP Vlink direct routes, such routes can be advertised only after they are imported to the routing table of a dynamic routing protocol. Perform any of the following operations based on the routing protocol on the Router:
   * To import IPv4 ARP Vlink direct routes to RIP, run the [**import-route**](cmdqueryname=import-route) **direct** [ **cost** *cost* | **route-policy** *route-policy-name* ] \* command, and then configure advertisement.
   * To import IPv4 ARP Vlink direct routes to OSPF, run the [**import-route**](cmdqueryname=import-route) **direct** [ **cost** *cost* | **route-policy** *route-policy-name* | **tag** *tag* | **type** *type* ] \* command, and then configure advertisement.
   * To import IPv4 ARP Vlink direct routes to IS-IS, run the [**import-route**](cmdqueryname=import-route) **direct** [ **cost-type** { **external** | **internal** } | **cost** *cost* | **tag** *tag* | **route-policy** *route-policy-name* | [ **level-1** | **level-2** | **level-1-2** ] ] \* command, and then configure advertisement.
   * To import IPv4 ARP Vlink direct routes to BGP, run the [**import-route**](cmdqueryname=import-route) **direct** [ **med** *med* | **route-policy** *route-policy-name* ] \* command, and then configure advertisement.
3. (Optional) Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
4. (Optional) Run [**arp vlink-direct-route preference**](cmdqueryname=arp+vlink-direct-route+preference) *preference-value*
   
   
   
   A preference is configured for ARP Vlink direct routes.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

After configuring advertisement of public network IPv4 ARP Vlink direct routes, run the [**display ip routing-table**](cmdqueryname=display+ip+routing-table) **verbose** command to check public network IPv4 ARP Vlink direct routes.