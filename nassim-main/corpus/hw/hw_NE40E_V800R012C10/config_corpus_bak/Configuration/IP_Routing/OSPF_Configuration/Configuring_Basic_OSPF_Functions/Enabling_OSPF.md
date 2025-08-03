Enabling OSPF
=============

After an OSPF process is created, a router ID is configured for the Router, an interface on which OSPF runs and the area to which the interface belongs are specified, routes can be discovered and calculated in the AS.

#### Context

OSPF on the Router requires a router ID. The router ID is a 32-bit unsigned integer, which uniquely identifies the Router in the AS. To ensure the stability of OSPF, manually set the router ID of each Router during network planning.

OSPF prevents the link state database (LSDB) size from unexpectedly growing by partitioning an AS into different areas. An area is regarded as a logical group, and each group is identified by an area ID. At the border of an area resides the Router instead of a link. A network segment (or a link) belongs to only one area. The area to which each OSPF interface belongs must be specified.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ospf**](cmdqueryname=ospf) [ *process-id* ] [ **router-id** *router-id* ] \*
   
   
   
   An OSPF process is started, and the OSPF view is displayed.
   
   
   
   The NE40E supports OSPF multi-instance. To run OSPF in a VPN instance, run the [**ospf**](cmdqueryname=ospf) [ *process-id* ] [ **router-id** *router-id* | **vpn-instance** *vpn-instance-name* ] \* command.
   
   * The NE40E supports OSPF multi-process. Processes can be classified by service type. The Routers exchange packets regardless of process IDs.
   * **router-id** *router-id* specifies the router ID of the Router.
     
     By default, the Router automatically selects an IP address of the current interface as the router ID. When configuring a router ID, ensure that it is unique in an AS. You can configure the IP address of an interface as the router ID.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     Each router ID in an OSPF process must be unique. Otherwise, no OSPF neighbor relationships can be established, and routing information is incorrect.
     
     If a router ID conflict occurs, perform either of the following operations:
     
     + Run the [**ospf**](cmdqueryname=ospf) **router-id** *router-id* command to configure a new router ID.
     + Run the [**undo ospf router-id auto-recover disable**](cmdqueryname=undo+ospf+router-id+auto-recover+disable) command to enable the router ID automatic recovery function. After the function is enabled, the system automatically allocates a new router ID if a router ID conflict occurs.![](../../../../public_sys-resources/note_3.0-en-us.png) 
       - If the automatic recovery function is enabled and a router ID conflict occurs between indirectly connected Routers in one OSPF area, the conflicting router ID is replaced with a newly calculated one, regardless of whether the conflicting router ID was manually configured or automatically generated.
       - The system can replace a router ID in a maximum of three attempts in case the router ID conflict persists.
     
     After a router ID is replaced, the [**reset ospf**](cmdqueryname=reset+ospf) [ *process-id* ] **process** command needs to be run to validate the new router ID.
   * If a VPN instance is specified, the OSPF process belongs to this VPN instance. If a VPN instance is not specified, the OSPF process belongs to the public-network instance.
   
   You can run the [**description**](cmdqueryname=description) command to configure a description for the OSPF process for easier identification.
3. Run [**area**](cmdqueryname=area) *area-id*
   
   
   
   The OSPF area view is displayed.
   
   OSPF areas are classified as a backbone area (with area ID 0) or non-backbone areas. The backbone area forwards inter-area routing information. The routing information exchanged between non-backbone areas must be forwarded through the backbone area.
   
   You can run the [**description**](cmdqueryname=description) command to configure a description for the OSPF area for easier identification.
4. To configure OSPF, you can configure the network segments included in an area or enable OSPF on an interface.
   
   
   * To configure the network segments included in an area, run the [**network**](cmdqueryname=network) *address* *wildcard-mask* [ **description** *text* ] command, in which **description** specifies the description of an OSPF network segment.
     
     OSPF runs on an interface only when both of the following conditions are met:
     
     + The mask length of the interface's IP address is greater than or equal to that specified in the [**network**](cmdqueryname=network) command.
       
       ![](../../../../public_sys-resources/note_3.0-en-us.png) 
       
       If *wildcard-mask* in the [**network**](cmdqueryname=network) command are all 0s and the IP address of the interface is the same as the IP address specified in the [**network**](cmdqueryname=network) *address* command, OSPF is also enabled on the interface.
     + The interface's primary IP address belongs to the network segment specified in the [**network**](cmdqueryname=network) command.
     
     By default, OSPF advertises the IP address of a loopback interface in the form of a host route with a 32-bit mask, regardless of the mask length configured for the IP address. To allow a loopback interface to advertise its network-segment routes, its network type must be set to NBMA or broadcast in the interface view. For details on how to set the network type, see [Configuring Network Types for OSPF Interfaces](dc_vrp_ospf_cfg_2029.html).
   * Enable OSPF on an interface.
     1. Run the [**quit**](cmdqueryname=quit) command twice to return to the system view.
     2. Run the [**interface**](cmdqueryname=interface) *interface-type* *interface-number* command to enter the interface view.
     3. Run the [**ospf enable**](cmdqueryname=ospf+enable) [ *process-id* ] **area** *area-id* command to enable OSPF on the interface. The specified area ID can be a decimal integer or in the IPv4 address format. Regardless of the specified format, the area ID is displayed as an IPv4 address.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.