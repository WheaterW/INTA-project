Disabling DN Bit Setting in OSPFv3 LSAs
=======================================

In a VPN Option A scenario, disabling DN bit setting in OSPFv3 LSAs allows PEs in different ASs to communicate with each other.

#### Usage Scenario

[Figure 1](#EN-US_TASK_0199805295__fig1558113223218) shows a VPN Option A scenario where an OSPFv3 neighbor relationship is established between ASBR1 and ASBR2. Each of the ASBRs imports BGP routes from the connected PE to the OSPFv3 process, generates LSAs, and advertises the LSAs to the peer ASBR. The ASBRs, however, cannot use the received LSAs to generate OSPFv3 routes. This is because LSAs with the DN bit set cannot be used for route calculation, as defined in a standard protocol. Consequently, no OSPFv3 routes will be imported into BGP processes on the ASBRs, and no BGP routes will be advertised to the connected PEs, causing traffic loss. To prevent this issue, you can disable DN bit setting in OSPFv3 LSAs.

**Figure 1** OSPFv3 application in the VPN Option A scenario  
![](figure/en-us_image_0199805634.png)

#### Pre-configuration Tasks

Configure a VPN instance before disabling DN bit setting in OSPFv3 LSAs.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ospfv3**](cmdqueryname=ospfv3) [ *process-id* ] [ **vpn-instance** *vpnname*]
   
   
   
   An OSPFv3 process bound to the existing VPN instance is started, and the view of the OSPFv3 process is displayed.
   
   
   
   An OSPFv3 process can be bound to only one VPN instance. If an OSPFv3 process is not bound to any VPN instance before being started, this process is a public network process. The public network OSPFv3 process cannot be bound to a VPN instance.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Deleting a VPN instance or disabling the IPv6 address family in the VPN instance will delete all the associated OSPFv3 processes.
3. Run [**router-id**](cmdqueryname=router-id) *router-id*
   
   
   
   A router ID is configured.
   
   
   
   A router ID uniquely identifies an OSPFv3 process in an AS. If no router ID is configured, the OSPFv3 process cannot run.
4. Run [**import-route**](cmdqueryname=import-route) **bgp** [ **cost** *cost* | { **route-policy** *route-policy-name* | **route-filter** *route-filter-name* } | **tag** *tag* | **type** *type* ]\*
   
   
   
   The device is configured to import BGP routes into OSPFv3.
5. Run [**dn-bit-set disable**](cmdqueryname=dn-bit-set+disable) { **summary** | **ase** | **nssa** }
   
   
   
   DN bit setting in OSPFv3 LSAs is disabled.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.