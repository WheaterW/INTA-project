Enabling OSPFv3
===============

Creating an OSPFv3 process is a prerequisite for configuring OSPFv3 features. When creating an OSPFv3 process, you need to manually specify a router ID for it.

#### Context

OSPFv3 supports multi-process. Multiple OSPFv3 processes running on one device are differentiated by process IDs. An OSPFv3 process ID is set when an OSPFv3 process is created. The process ID is only locally valid and does not affect packet exchange with other devices.

A router ID is a 32-bit unsigned integer in the format of an IPv4 address. It uniquely identifies a device in an AS. The OSPFv3 router ID must be manually set, and OSPFv3 cannot run properly without a router ID.

When configuring the router ID, ensure that the router ID is unique in an AS. If multiple OSPFv3 processes run on the same device, you are advised to specify different router IDs for the processes.

To ensure OSPFv3 stability, plan router IDs properly during network design and manually set the router IDs during network deployment.

Perform the following steps on each device that needs to run OSPFv3:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ospfv3**](cmdqueryname=ospfv3) [ *process-id* ] [ **vpn-instance** *vpnname* ]
   
   
   
   OSPFv3 is enabled, and the OSPFv3 view is displayed.
   
   You can run the [**description**](cmdqueryname=description) command to configure a description for an OSPFv3 process for easier identification.
3. Run [**router-id**](cmdqueryname=router-id) *router-id*
   
   
   
   A router ID is set.
   
   When configuring the router ID, ensure that the router ID is unique in an AS. You can select the IP address of an interface as the router ID.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Each router ID in an OSPFv3 process must be unique on the entire network. Otherwise, routers cannot establish OSPFv3 neighbor relationships, and the routing information is incorrect.
   
   If a router ID conflict occurs, perform either of the following operations:
   
   * Configure a new router ID.
   * Run the [**undo ospfv3 router-id auto-recover disable**](cmdqueryname=undo+ospfv3+router-id+auto-recover+disable) command to enable the router ID automatic recovery function. After the function is enabled, the system automatically allocates a new router ID.![](../../../../public_sys-resources/note_3.0-en-us.png) 
     + If the automatic recovery function is enabled and a router ID conflict occurs between indirectly connected routers in one OSPFv3 area, the system replaces the conflicted router ID with a newly calculated one. The automatic recovery function takes effect on both configured and automatically generated router IDs.
     + The system can replace a router ID in a maximum of three attempts in case the router ID conflict persists.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.