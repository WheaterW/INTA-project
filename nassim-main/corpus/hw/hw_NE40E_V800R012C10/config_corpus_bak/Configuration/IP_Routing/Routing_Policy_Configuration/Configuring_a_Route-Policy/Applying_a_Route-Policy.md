Applying a Route-Policy
=======================

A route-policy takes effect only when it is applied to a routing protocol.

#### Context

Route-policies apply to direct routes, static routes, RIP/RIPng, IS-IS, OSPF/OSPFv3, BGP/MPLS IP VPN, and BGP/BGP4+. In addition, a route-policy can be applied to an FRR scenario. Choose one of the following configurations as needed:

* [Apply a route-policy to direct routes.](#EN-US_TASK_0172366570__step_dc_vrp_route-policy_cfg_004201)
* [Apply a route-policy to static routes.](#EN-US_TASK_0172366570__step_dc_vrp_route-policy_cfg_004202)
* [Apply a route-policy to IPv6 static routes.](#EN-US_TASK_0172366570__step155151234185119)
* [Apply a route-policy to RIP routes.](#EN-US_TASK_0172366570__step_dc_vrp_route-policy_cfg_004203)
* [Apply a route-policy to RIPng routes.](#EN-US_TASK_0172366570__step_dc_vrp_route-policy_cfg_004204)
* [Apply a route-policy to IPv4 IS-IS routes.](#EN-US_TASK_0172366570__step_dc_vrp_route-policy_cfg_004205)
* [Apply a route-policy to IPv6 IS-IS routes.](#EN-US_TASK_0172366570__step_dc_vrp_route-policy_cfg_004206)
* [Apply a route-policy to OSPF routes.](#EN-US_TASK_0172366570__step_dc_vrp_route-policy_cfg_004207)
* [Apply a route-policy to OSPFv3 routes.](#EN-US_TASK_0172366570__step_dc_vrp_route-policy_cfg_004208)
* [Apply a route-policy to BGP routes.](#EN-US_TASK_0172366570__step_dc_vrp_route-policy_cfg_004209)
* [Apply a route-policy to BGP4+ routes.](#EN-US_TASK_0172366570__step_dc_vrp_route-policy_cfg_004210)
* [Apply a route-policy to BGP/MPLS IP VPN routes.](#EN-US_TASK_0172366570__step_dc_vrp_route-policy_cfg_004212)
* [Apply a route-policy to EVPN.](dc_vrp_evpn_cfg_0150.html)


#### Procedure

* Apply a route-policy to direct routes.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Perform the following operations as required to apply a route-policy to direct routes. For details, see [Table 1](#EN-US_TASK_0172366570__tab_dc_vrp_route-policy_cfg_004201).
     
     
     
     **Table 1** Applying a route-policy to direct routes
     | Objectives | Command | Reference |
     | --- | --- | --- |
     | To configure the device to advertise the public network ARP Vlink direct routes that match a route-policy (specified by the **route-policy** *route-policy-name* parameter) | [**arp vlink-direct-route advertise**](cmdqueryname=arp+vlink-direct-route+advertise) [ **route-policy** *route-policy-name* ] | [Configuring the Advertisement of Public Network IPv4 ARP Vlink Direct Routes](dc_vrp_ip-route_cfg_0055.html) |
     | To configure a device to advertise IPv6 Neighbor Discovery Protocol (NDP) Vlink direct routes that match a route-policy (specified by the **route-policy** *route-policy-name* parameter) on the public network | [**ipv6 nd vlink-direct-route advertise**](cmdqueryname=ipv6+nd+vlink-direct-route+advertise) [ **route-policy** *route-policy-name* ] | [Configuring the Advertisement of IPv6 NDP Vlink Direct Routes on the Public Network](dc_vrp_ip-route_cfg_0056.html) |
     | To apply a route-policy to direct routes on the public network  NOTE:  Currently, QoS information, such as the traffic behavior or local ID, can be configured for direct routes only based on a route-policy. A router applies different QoS policies to packets based on the QoS information while forwarding these packets. In this manner, traffic statistics can be collected, and authentication and accounting can be performed based on the direct routes. | [**ip direct-routing-table**](cmdqueryname=ip+direct-routing-table) **route-policy** *route-policy-name* | - |
     | To apply a route-policy to public network IPv6 direct routes.  NOTE:  Currently, QoS information, such as the traffic behavior or local ID, can be configured for direct routes only based on a route-policy. After QoS information is configured for routes, the device can apply different QoS policies to packets based on the QoS information during packet forwarding. In this manner, traffic statistic collection, authentication, and accounting can be performed based on direct routes. | [**ipv6 direct-routing-table**](cmdqueryname=ipv6+direct-routing-table) **route-policy** *route-policy-name* | - |
  3. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Apply a route-policy to static routes.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**ip static-routing-table**](cmdqueryname=ip+static-routing-table) **route-policy** *route-policy-name*
     
     
     
     A route-policy is applied to public network static routes.
  3. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Apply a route-policy to IPv6 static routes.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**ipv6 static-routing-table**](cmdqueryname=ipv6+static-routing-table) **route-policy** *route-policy-name*
     
     
     
     A route-policy is applied to public network static routes.
  3. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Apply a route-policy to RIP routes.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**rip**](cmdqueryname=rip) [ *process-id* ]
     
     
     
     A RIP process is enabled, and the RIP view is displayed.
  3. Perform the following operations as required to apply a route-policy to RIP routes. For details, see [Table 2](#EN-US_TASK_0172366570__tab_dc_vrp_route-policy_cfg_004203).
     
     
     
     **Table 2** Applying a route-policy to RIP routes
     | Objectives | Command | Reference |
     | --- | --- | --- |
     | To configure a device to generate a default route or advertise a default route in the routing table to neighbors only when the matching conditions of a route-policy (specified by the **route-policy** *route-policy-name* parameter) are met | [**default-route originate**](cmdqueryname=default-route+originate) [ **cost** *cost* | **tag** *tag* | **route-policy** *route-policy-name* [ **avoid-learning** ] ] \* | [Configuring RIP to Advertise Default Routes](dc_vrp_rip_cfg_0025.html) |
     | To configure RIP to import the BGP routes that match a route-policy (specified by the **route-policy** *route-policy-name* parameter) | [**import-route**](cmdqueryname=import-route) **bgp** [ **permit-ibgp** ] [ **cost** { *cost* | **transparent** } | **route-policy** *route-policy-name* ] \* | [Configuring RIP to Import External Routes](dc_vrp_rip_cfg_0026.html) |
     | To configure RIP to import the routes from another routing protocol that match a route-policy (specified by the **route-policy** *route-policy-name* parameter) | [**import-route**](cmdqueryname=import-route) { **static** | **direct** | **unr** | { **isis** | **ospf** | **rip** } [ *process-id* ] } [ **cost** *cost* | **route-policy** *route-policy-name* ] \* | [Configuring RIP to Import External Routes](dc_vrp_rip_cfg_0026.html) |
     | To set a preference for RIP routes that match a route-policy (specified by the **route-policy** *route-policy-name* parameter) | [**preference**](cmdqueryname=preference) { *preference* | **route-policy** *route-policy-name* } \* | [(Optional) Configuring a RIP Preference](dc_vrp_rip_cfg_0023.html) |
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Apply a route-policy to RIPng routes.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**ripng**](cmdqueryname=ripng) [ *process-id* ]
     
     
     
     A RIPng process is enabled, and the RIPng view is displayed.
  3. Perform the following operations as required to apply a route-policy to RIPng routes. For details, see [Table 3](#EN-US_TASK_0172366570__tab_dc_vrp_route-policy_cfg_004204).
     
     
     
     **Table 3** Applying a route-policy to RIPng routes
     | Objectives | Command | Reference |
     | --- | --- | --- |
     | To configure RIPng to import the routes from another routing protocol that match a route-policy (specified by the **route-policy** *route-policy-name* parameter) | [**import-route**](cmdqueryname=import-route) { **static** | **direct** | **bgp** [ **permit-ibgp** ] | **unr** | { **isis** | **ospfv3** | **ripng** } [ *process-id* ] } [ **cost** *cost* | **route-policy** *route-policy-name* ] \* | [Configuring RIPng to Import External Routes](dc_vrp_ripng_cfg_0019.html) |
     | To set a preference for RIPng routes that match a route-policy (specified by the **route-policy** *route-policy-name* parameter) | [**preference**](cmdqueryname=preference) { *preference* | **route-policy** *route-policy-name* } \* | [(Optional) Configuring the RIPng Priority](dc_vrp_ripng_cfg_0006.html) |
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Apply a route-policy to IPv4 IS-IS routes.
  
  
  + To apply a route-policy in the IS-IS view, perform the following operations:
    1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
    2. Run the [**isis**](cmdqueryname=isis) [ *process-id* ] command to enter the IS-IS view.
    3. Perform the following operations as required to apply a route-policy to IS-IS routes. For details, see [Table 4](#EN-US_TASK_0172366570__tab_dc_vrp_route-policy_cfg_004205).
       
       **Table 4** Applying a route-policy to IPv4 IS-IS routes in the IS-IS view
       | Objectives | Command | Reference |
       | --- | --- | --- |
       | To configure IS-IS to generate and advertise default routes to the IS-IS domain only when external routes that match a route-policy (specified by the **route-policy** *route-policy-name* parameter) exist in the routing table of a border device (This prevents routing blackhole when link faults make some important external routes unavailable but default routes are still advertised.) | [**default-route-advertise**](cmdqueryname=default-route-advertise) **route-policy** *route-policy-name* [ **cost** *cost* | **tag** *tag* | [ **level-1** | **level-1-2** | **level-2** ] ] \* [ **avoid-learning** ] | [Configuring IS-IS to Generate IPv4 Default Routes](dc_vrp_isis_cfg_1011.html) |
       | To configure IS-IS to advertise the routes that are imported from another routing protocol and match a route-policy | [**filter-policy**](cmdqueryname=filter-policy) **route-policy** *route-policy-name* **export** [ *protocol* [ *process-id* ] ] | - |
       | To configure IS-IS to accept the routes that match a route-policy | [**filter-policy**](cmdqueryname=filter-policy) **route-policy** *route-policy-name* **import** | [Configuring IS-IS to Import External Routes (IPv4)](dc_vrp_isis_cfg_1015.html) |
       | To configure IS-IS to import the routes from another routing protocol that match a route-policy | [**import-route**](cmdqueryname=import-route) { **direct** | **static** | **unr** | { **ospf** | **rip** | **isis** } [ *process-id* ] | **bgp** [ **permit-ibgp** ] } [ **cost-type** { **external** | **internal** } | **cost** *cost* | **tag** *tag* | **route-policy** *route-policy-name* | [ **level-1** | **level-2** | **level-1-2** ] ] \*  [**import-route**](cmdqueryname=import-route) { { **ospf** | **rip** | **isis** } [ *process-id* ] | **bgp** [ **permit-ibgp** ] | **direct** | **unr** } **inherit-cost** [ { **level-1** | **level-2** | **level-1-2** } | **tag** *tag* | **route-policy** *route-policy-name* ] \*  [**import-route**](cmdqueryname=import-route) { **ospf** | **isis** } [ *process-id* ] [ **cost-type** { **external** | **internal** } | **cost** *cost* | **tag** *tag* | **route-policy** *route-policy-name* | [ **level-1** | **level-2** | **level-1-2** ] | **no-sid** ] \*  [**import-route**](cmdqueryname=import-route) { **ospf** | **isis** } [ *process-id* ] **inherit-cost** [ { **level-1** | **level-2** | **level-1-2** } | **tag** *tag* | **route-policy** *route-policy-name* | **no-sid** ] \* | [Configuring IS-IS to Import External Routes (IPv4)](dc_vrp_isis_cfg_1015.html) |
       | To allow Level-1 routes to leak to a Level-2 area | [**import-route isis level-1 into level-2**](cmdqueryname=import-route+isis+level-1+into+level-2) [ **filter-policy** **route-policy** *route-policy-name* | **direct** **allow-filter-policy** | **tag** *tag* | **no-sid** ] \* | [Configuring IS-IS Route Leaking (IPv4)](dc_vrp_isis_cfg_1007.html) |
       | To allow Level-2 routes to leak to a Level-1 area | [**import-route isis level-2 into level-1**](cmdqueryname=import-route+isis+level-2+into+level-1) [ **filter-policy** **route-policy** *route-policy-name* | **direct** **allow-filter-policy** | **tag** *tag* | **no-sid** ] \* | [Configuring IS-IS Route Leaking (IPv4)](dc_vrp_isis_cfg_1007.html) |
       | To configure a preference value for the IS-IS routes that match a route-policy | [**preference**](cmdqueryname=preference) { **route-policy** *route-policy-name* | *preference* } \* | [Configuring a Preference Value for IPv4 IS-IS](dc_vrp_isis_cfg_1014.html) |
    4. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
  + To apply a route-policy in the IS-IS FRR view, perform the following operations:
    1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
    2. Run the [**isis**](cmdqueryname=isis) [ *process-id* ] command to enter the IS-IS view.
    3. Run the [**frr**](cmdqueryname=frr) command to enter the IS-IS FRR view.
    4. Run the [**frr-policy route**](cmdqueryname=frr-policy+route) **route-policy** *route-policy-name* command to configure IS-IS to add the backup routes that match a route-policy to the IP routing table.
       
       For details on how to configure IS-IS Auto FRR (IPv4), see [Configuring IS-IS Auto FRR](dc_vrp_isis_cfg_0091.html).
    5. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
* Apply a route-policy to IPv6 IS-IS routes.
  
  
  + To apply a route-policy in the IS-IS view, perform the following operations:
    1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
    2. Run the [**isis**](cmdqueryname=isis) [ *process-id* ] command to enter the IS-IS view.
    3. Perform the following operations as required to apply a route-policy to IPv6 IS-IS routes. For details, see [Table 5](#EN-US_TASK_0172366570__tab_dc_vrp_route-policy_cfg_004206).
       
       **Table 5** Applying a route-policy to IPv6 IS-IS routes in the IS-IS view
       | Objectives | Command | Reference |
       | --- | --- | --- |
       | To configure IS-IS to generate and advertise default IPv6 routes to the IS-IS domain only when external routes that match a route-policy (specified by the **route-policy** *route-policy-name* parameter) exist in the routing table of a border device | [**ipv6 default-route-advertise**](cmdqueryname=ipv6+default-route-advertise) **route-policy** *route-policy-name* [ **cost** *cost* | **tag** *tag* | [ **level-1** | **level-2** | **level-1-2** ] ] \* [ **avoid-learning**| **learning-avoid-loop** ] | [Configuring IS-IS to Generate IPv6 Default Routes](dc_vrp_isis_cfg_1034.html) |
       | To configure IS-IS to advertise the routes that are imported from another routing protocol and match a route-policy | [**ipv6 filter-policy**](cmdqueryname=ipv6+filter-policy) **route-policy** *route-policy-name* **export** [ *protocol* [ *process-id* ] ] | - |
       | To configure IS-IS to accept the IPv6 routes that match a route-policy | [**ipv6 filter-policy**](cmdqueryname=ipv6+filter-policy) **route-policy** *route-policy-name* **import** | [Configuring IPv6 IS-IS to Import External Routes](dc_vrp_isis_cfg_1038.html) |
       | To configure IS-IS to import the routes from another routing protocol that match a route-policy | [**ipv6 import-route**](cmdqueryname=ipv6+import-route) { **direct** | **static** | **unr** | { **ripng** | **isis** | **ospfv3** } [ *process-id* ] } | **bgp** [ **permit-ibgp** ] } [ **cost** *cost* | **tag** *tag* | **route-policy** *route-policy-name* | [ **level-1** | **level-2** | **level-1-2** ] ] \*  [**ipv6 import-route**](cmdqueryname=ipv6+import-route) { { **ospfv3** | **ripng** | **isis** } [ *process-id* ] | **bgp** [ **permit-ibgp** ] | **direct** | **unr** } **inherit-cost** [ **tag** *tag* | **route-policy** *route-policy-name* | [ **level-1** | **level-2** | **level-1-2** ] ] \* | [Configuring IPv6 IS-IS to Import External Routes](dc_vrp_isis_cfg_1038.html) |
       | To allow Level-1 routes to leak to a Level-2 area | [**ipv6 import-route isis level-1 into level-2**](cmdqueryname=ipv6+import-route+isis+level-1+into+level-2) [ **filter-policy** **route-policy** *route-policy-name* | **direct allow-filter-policy** | **tag** *tag* ] \* | [Configuring IPv6 IS-IS Route Leaking](dc_vrp_isis_cfg_1030.html) |
       | To allow Level-2 routes to leak to a Level-1 area | [**ipv6 import-route isis level-2 into level-1**](cmdqueryname=ipv6+import-route+isis+level-2+into+level-1) [ **filter-policy** **route-policy** *route-policy-name* | **direct allow-filter-policy** | **tag** *tag* ] \* | [Configuring IPv6 IS-IS Route Leaking](dc_vrp_isis_cfg_1030.html) |
       | To configure a preference value for the IS-IS routes that match a route-policy | [**ipv6 preference**](cmdqueryname=ipv6+preference) { **route-policy** *route-policy-name* | *preference* } \* | [Configuring a Preference Value for IPv6 IS-IS](dc_vrp_isis_cfg_1037.html) |
    4. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
  + To apply a route-policy in the IS-IS IPv6 topology view, perform the following operations:
    1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
    2. Run the [**isis**](cmdqueryname=isis) [ *process-id* ] command to enter the IS-IS view.
    3. Run the [**ipv6 topology**](cmdqueryname=ipv6+topology) **topology-name** [ **topology-id** { **multicast** | *topology-id* } ] command to bind the IS-IS process to an IPv6 topology and enter the IS-IS IPv6 topology view.
    4. Run the [**import-route**](cmdqueryname=import-route) { **direct** | **isis** [ *process-id* ] **inherit-cost** [ **tag** *tag* | **route-policy** *route-policy-name* | { **level-1** | **level-2** | **level-1-2** } ] \* command to configure IS-IS to import routes from another protocol into the current topology.
       
       For details on how to configure IPv6 IS-IS multi-topology, see [Enabling MT for an IS-IS Process](dc_vrp_isis_cfg_0105.html).
    5. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
* Apply a route-policy to OSPF routes.
  
  
  + To apply a route-policy in the OSPF view, perform the following operations:
    
    1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
    2. Run the [**ospf**](cmdqueryname=ospf) [ *process-id* ] command to enable an OSPF process and enter the OSPF view.
    3. To apply a route-policy to OSPF routes in the OSPF process view, see [Table 6](#EN-US_TASK_0172366570__tab_dc_vrp_route-policy_cfg_004207).
       
       **Table 6** Applying a route-policy to OSPF routes
       | Objectives | Command | Reference |
       | --- | --- | --- |
       | To configure OSPF to advertise the default routes in the routing table that are not generated by OSPF to a common area based on the parameters of a route-policy (specified by the **route-policy** *route-policy-name* parameter) | [**default-route-advertise**](cmdqueryname=default-route-advertise) [ [ **always** | **permit-calculate-other** ] | **cost** *cost* | **type** *type* | **route-policy** *route-policy-name* | **distribute-delay** *delay-time* ] \*  [**default-route-advertise**](cmdqueryname=default-route-advertise) [ **permit-calculate-other** | **cost** *cost* | **type** *type* | **route-policy** *route-policy-name* | **distribute-delay** *delay-time* | [**permit-ibgp**](cmdqueryname=permit-ibgp) ] \*  [**default-route-advertise**](cmdqueryname=default-route-advertise) **summary** **cost** *cost* | [Configuring OSPF to Import a Default Route](dc_vrp_ospf_cfg_2041.html) |
       | To configure OSPF to accept the routes that match a route-policy | [**filter-policy**](cmdqueryname=filter-policy) **route-policy** *route-policy-name* [ **secondary** ] **import** | [Configuring OSPF to Filter Received Routes](dc_vrp_ospf_cfg_0044.html) |
       | To configure OSPF to advertise the routes that match a route-policy | [**filter-policy**](cmdqueryname=filter-policy) **route-policy** *route-policy-name* **export** [ *protocol* [ *process-id* ] ] | [Configuring OSPF to Filter the Routes to Be Advertised](dc_vrp_route-policy_cfg_0036_copy.html) |
       | To configure OSPF to import routes from another protocol | [**import-route**](cmdqueryname=import-route) { **bgp** [ **permit-ibgp** ] | **direct** | **unr** | **rip** [ *process-id-rip* ] | **static** | **isis** [ *process-id-isis* ] | **ospf** [ *process-id-ospf* ] [ **cost** *cost* | **route-policy** *route-policy-name* | **tag** *tag* | **type** *type* ] \* } | [Configuring OSPF to Import External Routes](dc_vrp_ospf_cfg_2040.html) |
       | To configure a route-policy for OSPF local MT so that only the routes that match the route-policy (specified by the **route-policy** *route-policy-name* parameter) are added to the MIGP routing table | [**local-mt filter-policy**](cmdqueryname=local-mt+filter-policy) **route-policy** *route-policy-name* | - |
       | To configure a preference value for OSPF routes that match a route-policy | [**preference**](cmdqueryname=preference) [ **ase** | **inter** | **intra** ] { *preference* | **route-policy** *route-policy-name* } \* | [(Optional) Setting the OSPF Preference](dc_vrp_ospf_cfg_2023.html) |
    4. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
  + To apply a route-policy in the OSPF area view, perform the following operations:
    
    1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
    2. Run the [**ospf**](cmdqueryname=ospf) [ *process-id* ] command to enable an OSPF process and enter the OSPF view.
    3. Run the [**area**](cmdqueryname=area) *area-id* command to enter the OSPF area view.
    4. Perform either of the following operations to apply a route-policy in the OSPF area view:
       
       - Run the [**filter**](cmdqueryname=filter) **route-policy** *route-policy-name* **export** command to apply a route-policy to outgoing Type 3 LSAs (summary LSAs) in the area.
       - Run the [**filter**](cmdqueryname=filter) **route-policy** *route-policy-name* **import** command to apply a route-policy to incoming Type 3 LSAs in the area.
       
       For details on the configuration of applying a route-policy to Type-3 LSAs, see [Configuring OSPF to Filter LSAs in an Area](dc_vrp_ospf_cfg_2044.html)
    5. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
  + To apply a route-policy in the OSPF FRR view, perform the following operations:
    
    1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
    2. Run the [**ospf**](cmdqueryname=ospf) [ *process-id* ] command to enable an OSPF process and enter the OSPF view.
    3. Run the [**frr**](cmdqueryname=frr) command to enter the OSPF FRR view.
    4. Run the [**loop-free-alternate**](cmdqueryname=loop-free-alternate) command to enable OSPF IP FRR to generate a loop-free backup link.
    5. Run the [**frr-policy route**](cmdqueryname=frr-policy+route) **route-policy** *route-policy-name* command to configure OSPF to add the backup routes that match a route-policy to the IP routing table.
       
       For details on how to configure OSPF IP FRR, see [Configuring OSPF IP FRR](dc_vrp_ospf_cfg_2009.html).
    6. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
* Apply a route-policy to OSPFv3 routes.
  
  
  + To apply a route-policy in the OSPFv3 view, perform the following operations:
    
    1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
    2. Run the [**ospfv3**](cmdqueryname=ospfv3) [ *process-id* ] command to enable an OSPFv3 process and enter the OSPFv3 view.
    3. Perform the following operations as required to apply a route-policy in the OSPFv3 view. For details, see [Table 7](#EN-US_TASK_0172366570__tab_dc_vrp_route-policy_cfg_004208).
       
       **Table 7** Applying a route-policy to OSPFv3 routes
       | Objectives | Command | Reference |
       | --- | --- | --- |
       | To configure OSPFv3 to advertise the default routes in the routing table that are not generated by OSPFv3 to an OSPFv3 routing area based on the parameters of a route-policy (specified by the **route-policy** *route-policy-name* parameter) | [**default-route-advertise**](cmdqueryname=default-route-advertise) [ **always** | **permit-calculate-other** | **cost** *cost* | **type** *type* | **tag** *tag* | **distribute-delay** *delay* | **route-policy** *route-policy-name* ] \* | [Configuring OSPFv3 to Filter the Routes to Be Advertised](dc_vrp_ospfv3_cfg_2029.html) |
       | To configure OSPFv3 to accept the routes that match a route-policy | [**filter-policy**](cmdqueryname=filter-policy) **route-policy** *route-policy-name* [ **secondary** ] **import** | [Configuring OSPFv3 to Filter Received Routes](dc_vrp_ospfv3_cfg_2028.html) |
       | To configure OSPFv3 to import routes from another protocol | [**import-route**](cmdqueryname=import-route) { **bgp** [ **permit-ibgp** ] | **direct** | **unr**  | **static** | **isis** [ *process-id* ] | **ripng** [ *process-id* ] | **ospfv3** [ *process-id* ] } [ **cost** *cost* | **tag** *tag* | **type** *type* | **route-policy** *route-policy-name* ] \* } | [Configuring OSPFv3 to Import External Routes](dc_vrp_ospfv3_cfg_2026.html) |
       | To configure a preference value for OSPF routes that match a route-policy | [**preference**](cmdqueryname=preference) [ **ase** ] { *preference* | **route-policy** *route-policy-name* } \* | - |
    4. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
  + To apply a route-policy in the OSPFv3 area view, perform the following operations:
    
    1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
    2. Run the [**ospfv3**](cmdqueryname=ospfv3) [ *process-id* ] command to enable an OSPFv3 process and enter the OSPFv3 view.
    3. Run the [**area**](cmdqueryname=area) *area-id* command to enter the OSPFv3 area view.
    4. Perform either of the following operations to apply a route-policy in the OSPFv3 area view:
       
       - Run the [**filter**](cmdqueryname=filter) **route-policy** *route-policy-name* **export** command to apply a route-policy to outgoing Type 3 LSAs (Inter-Area-Prefix-LSAs) in the OSPFv3 area.
       - Run the [**filter**](cmdqueryname=filter) **route-policy** *route-policy-name* **import** command to apply a route-policy to incoming Type 3 LSAs in the OSPFv3 area.
       
       For details on how to apply a route-policy to Type 3 LSAs in an OSPFv3 area, see [Configuring OSPFv3 to Filter LSAs in an Area](dc_vrp_ospfv3_cfg_2078.html).
    5. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
  + To apply a route-policy in the OSPFv3 FRR view, perform the following operations:
    
    1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
    2. Run the [**ospfv3**](cmdqueryname=ospfv3) [ *process-id* ] command to enable an OSPFv3 process and enter the OSPFv3 view.
    3. Run the [**frr**](cmdqueryname=frr) command to enter the OSPFv3 FRR view.
    4. Run the [**loop-free-alternate**](cmdqueryname=loop-free-alternate) command to enable OSPFv3 IP FRR.
    5. Run the [**frr-policy route**](cmdqueryname=frr-policy+route) **route-policy** *route-policy-name* command to configure OSPFv3 to add the backup routes that match a route-policy to the IP routing table.
       
       For details on how to configure OSPFv3 IP FRR, see [Configuring OSPFv3 IP FRR](dc_vrp_ospfv3_cfg_2031.html).
    6. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
* Apply a route-policy to BGP routes.
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**bgp**](cmdqueryname=bgp) { *as-number-plain* | *as-number-dot* } command to enter the BGP view.
  3. Run the [**ipv4-family**](cmdqueryname=ipv4-family) **unicast** command to enter the IPv4 unicast address family view.
  4. Perform the following operations as required to apply a route-policy to BGP routes. For details, see [Table 8](#EN-US_TASK_0172366570__tab_dc_vrp_route-policy_cfg_004209).
     
     
     
     **Table 8** Applying a route-policy to BGP routes
     | Objectives | Command | Reference |
     | --- | --- | --- |
     | To configure a summary BGP route | [**aggregate**](cmdqueryname=aggregate) *ipv4-address* { *mask* | *mask-length* } [ **as-set** | **attribute-policy** *route-policy-name1* | **detail-suppressed** | **origin-policy** *route-policy-name2* | **suppress-policy** *route-policy-name3* ] \* | [Configuring BGP Route Summarization](dc_vrp_bgp_cfg_4028.html) |
     | To configure BGP route dampening | [**dampening**](cmdqueryname=dampening) [ *half-life-reach* *reuse* *suppress* *ceiling* | **route-policy** *route-policy-name* ] \*[ **update-standard** ] | [Configuring BGP Route Dampening](dc_vrp_bgp_cfg_4051.html) |
     | To configure BGP to import routes from another routing protocol | [**import-route**](cmdqueryname=import-route) *protocol* [ *process-id* ] [ **med** *med* | **route-policy** *route-policy-name* ] \*[ **non-relay-tunnel** ] | [Configuring BGP to Import Routes](dc_vrp_bgp_cfg_3007.html) |
     | To configure BGP to import local routes | [**network**](cmdqueryname=network) *ipv4-address* [ *mask* | *mask-length* ] [ **route-policy** *route-policy-name* ] [ **non-relay-tunnel** ] | [Configuring BGP to Import Routes](dc_vrp_bgp_cfg_3007.html) |
     | To enable BGP route recursion based on a route-policy | [**nexthop recursive-lookup**](cmdqueryname=nexthop+recursive-lookup) **route-policy** *route-policy-name* | [Configuring the Next\_Hop Attribute](dc_vrp_bgp_cfg_4015.html) |
     | To configure a BGP device to send a default route to a peer or a peer group and use a route-policy (specified by the **route-policy** *route-policy-name* parameter) to modify the attributes of the default route | [**peer**](cmdqueryname=peer) { *group-name* | *ipv4-address* } **default-route-advertise** [ **route-policy** *route-policy-name* ] [ **conditional-route-match-all** { *ipv4-address1* { *mask1* | *mask-length1* } } &<1-4> | **conditional-route-match-any** { *ipv4-address2* { *mask2* | *mask-length2* } } &<1-4> ] | [Configuring a Device to Send Default Routes to Its Peer](dc_vrp_bgp_cfg_3052.html) |
     | To configure BGP to ignore bit error detection results when an export route-policy is used.  NOTE:  When bit-error-triggered protection switching is configured, bit errors occur, and Local\_Pref or MED is modified using an export route-policy, run the command to apply the Local\_Pref or MED in the export route-policy. | [**peer**](cmdqueryname=peer) { *group-name* | *ipv4-address* } **route-policy** *route-policy-name* **export** **ignore-bit-error** | - |
     | To configure a device to accept the routes that match a route-policy from a peer or peer group or advertise the routes that match a route-policy to a peer or peer group | [**peer**](cmdqueryname=peer) { *group-name* | *ipv4-address* } **route-policy** *route-policy-name* { **import** | **export** } | [Applying a Policy to BGP Route Advertisement](dc_vrp_bgp_cfg_3114.html)  [Applying a Policy to BGP Route Acceptance](dc_vrp_bgp_cfg_3115.html) |
     | To use a route-policy to set a BGP preference value | [**preference**](cmdqueryname=preference) **route-policy** *route-policy-name* | [Setting a BGP Preference Value](dc_vrp_bgp_cfg_4011.html) |
     | To prevent the BGP routes that match a route-policy from being added to the IP routing table | [**routing-table rib-only**](cmdqueryname=routing-table+rib-only) [ **route-policy** *route-policy-name* ] | [(Optional) Preventing a Device from Adding BGP Routes to the IP Routing Table](dc_vrp_bgp_cfg_3038.html) |
  5. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
* Apply a route-policy to BGP4+ routes.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) { *as-number-plain* | *as-number-dot* }
     
     
     
     The BGP view is displayed.
  3. Run [**ipv6-family**](cmdqueryname=ipv6-family) [ **unicast** ]
     
     
     
     The IPv6 unicast address family view is displayed.
  4. Perform the following operations as required to apply a route-policy to BGP4+ routes. For details, see [Table 9](#EN-US_TASK_0172366570__tab_dc_vrp_route-policy_cfg_004210).
     
     
     
     **Table 9** Applying a route-policy to BGP4+ routes
     | Objectives | Command | Reference |
     | --- | --- | --- |
     | To configure a summary BGP4+ route | [**aggregate**](cmdqueryname=aggregate) *ipv6-address* *prefix-length* [ **as-set** | **attribute-policy** *route-policy-name1* | **detail-suppressed** | **origin-policy** *route-policy-name2* | **suppress-policy** *route-policy-name3* ] \* | [Configuring BGP4+ Route Summarization](dc_vrp_bgp6_cfg_0014.html) |
     | To configure BGP4+ route dampening and apply dampening parameters to the routes that match a route-policy (specified by the **route-policy** *route-policy-name* parameter) so that specified-requirement dampening can be performed by BGP based on the applied route-policy | [**dampening**](cmdqueryname=dampening) [ *half-life-reach* *reuse* *suppress* *ceiling* | **route-policy** *route-policy-name* ] \* | [Configuring BGP4+ Route Dampening](dc_vrp_bgp6_cfg_0035.html) |
     | To configure BGP4+ to import the routes from another routing protocol that match a route-policy | [**import-route**](cmdqueryname=import-route) *protocol* [ *process-id* ] [ **med** *med* | **route-policy** *route-policy-name* ] \* | [Configuring BGP4+ to Import Routes](dc_vrp_bgp6_cfg_0010.html) |
     | To configure BGP4+ to advertise local routes | [**network**](cmdqueryname=network) *ipv6-address* *prefix-length* [ **route-policy** *route-policy-name* ] | [Configuring BGP4+ to Import Routes](dc_vrp_bgp6_cfg_0010.html) |
     | To enable BGP4+ route recursion based on a route-policy | [**nexthop recursive-lookup**](cmdqueryname=nexthop+recursive-lookup) **route-policy** *route-policy-name* | [Setting the Next\_Hop Attribute](dc_vrp_bgp6_cfg_0024.html) |
     | To configure a BGP4+ device to send a default route to a peer or a peer group and use a route-policy (specified by the **route-policy** *route-policy-name* parameter) to modify the attributes of the default route | [**peer**](cmdqueryname=peer) { *group-name* | *ipv6-address* } **default-route-advertise** [ **route-policy** *route-policy-name* ] { **conditional-route-match-all** | **conditional-route-match-any** } { *ipv6-address* *mask-length* } } &<1-4> | [Configuring BGP4+ to Advertise Default Routes to Peers or Peer Groups](dc_vrp_bgp6_cfg_0015.html) |
     | To configure a device to accept the routes that match a route-policy from a peer or peer group or advertise the routes that match a route-policy to a peer or peer group | [**peer**](cmdqueryname=peer) { *group-name* | *ipv6-address* } **route-policy** *route-policy-name* { **import** | **export** } | [Applying a Policy to BGP4+ Route Advertisement](dc_vrp_bgp6_cfg_0030.html)  [Configuring a Policy for Receiving BGP4+ Routes](dc_vrp_bgp6_cfg_0031.html) |
     | To use a route-policy to set a BGP4+ preference value | [**preference**](cmdqueryname=preference) **route-policy** *route-policy-name* | [Setting a BGP4+ Preference](dc_vrp_bgp6_cfg_0020.html) |
     | To prevent the BGP4+ routes that match a route-policy from being added to the IPv6 routing table | [**routing-table rib-only**](cmdqueryname=routing-table+rib-only) [ **route-policy** *route-policy-name* ] | [(Optional) Preventing BGP4+ from Adding Routes to the IP Routing Table](dc_vrp_bgp6_cfg_0083.html) |
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Apply a route-policy to BGP/MPLS IP VPN routes.
  
  
  + To apply a route-policy in the BGP-VPNv4 address family view, perform the following operations:
    
    1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
    2. Run the [**bgp**](cmdqueryname=bgp) { *as-number-plain* | *as-number-dot* } command to enter the BGP view.
    3. Run the [**ipv4-family**](cmdqueryname=ipv4-family) **vpnv4** command to enter the BGP-VPNv4 address family view.
    4. Run the [**nexthop recursive-lookup bit-error-detection**](cmdqueryname=nexthop+recursive-lookup+bit-error-detection) { **med** **+** *med-adjust-value* | **local-preference** **-** *localpref-adjust-value* } \* [ **route-policy** *route-policy-name* ] command to associate bit error events with the adjustment of the MED or Local\_Pref value for routes that match a route-policy. If **route-policy** *route-policy-name* is not specified in the command, the MED or Local\_Pref values of all routes are adjusted.
       
       For details on how to apply a route-policy to bit-error-triggered L3VPN route switching, see [Configuring Bit-Error-Triggered L3VPN Route Switching](dc_vrp_cfg_error-code_000013.html).
    5. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
  + To apply a route-policy in the VPN instance view, perform the following operations:
    
    1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
    2. Run the [**ip vpn-instance**](cmdqueryname=ip+vpn-instance) *vpn-instance-name* command to enter the VPN instance view.
    3. To apply a route-policy to BGP/MPLS IP VPN routes in the VPN instance view, perform one of the following operations as required:
       - To associate the current address family of the VPN instance with an export route-policy, run the [**export**](cmdqueryname=export) **route-policy** *route-policy-name* [ **add-ert-first** ] command. Only one route-policy can be associated with the current address family. If the command is run more than once and the specified route-policies are different, the route-policy specified in the latest configuration overrides the previous one.
         
         The [**export route-policy**](cmdqueryname=export+route-policy) command can control route advertisement between different VPN instances on the same PE, whereas the [**peer route-policy**](cmdqueryname=peer+route-policy) **export** command can control only the VPNv4 or VPNv6 routes that a PE sends to other PE peers.
       - To associate the current address family of the VPN instance with an import route-policy, run the [**import**](cmdqueryname=import) **route-policy** *route-policy-name* command. Only one route-policy can be associated with the current address family. If the command is run more than once and the specified route-policies are different, the route-policy specified in the latest configuration overrides the previous one.
         
         The [**import route-policy**](cmdqueryname=import+route-policy) command can control route acceptance between different VPN instances on the same PE, whereas the [**peer route-policy**](cmdqueryname=peer+route-policy) **import** command can control only the VPNv4 or VPNv6 routes that a PE accepts from other PE peers.
       - To configure the device to advertise VPN ARP Vlink direct routes, run the [**arp vlink-direct-route advertise**](cmdqueryname=arp+vlink-direct-route+advertise) [ **route-policy** *route-policy-name* ] command. The **route-policy** *route-policy-name* parameter specifies the route-policy used to filter the ARP Vlink direct routes to be advertised. For details, see [Configuring Route Exchange Between PEs and CEs](dc_vrp_mpls-l3vpn-v4_cfg_0158.html#EN-US_TASK_0172369257__step_dc_vrp_mpls-l3vpn-v4_cfg_015807).
    4. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
  + To apply a route-policy in the VPN instance IPv4 address family view, perform the following operations:
    
    1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
    2. Run the [**ip vpn-instance**](cmdqueryname=ip+vpn-instance) *vpn-instance-name* command to enter the VPN instance view.
    3. Run the [**ipv4-family**](cmdqueryname=ipv4-family) command to enable the IPv4 address family for the VPN instance and enter the VPN instance IPv4 address family view.
    4. Run the [**ip**](cmdqueryname=ip) { **direct-routing-table** | **static-routing-table** } **route-policy** *route-policy-name* command to apply a route-policy to the direct or static routes in the VPN instance IPv4 address family.
       
       If the [**ip route-policy**](cmdqueryname=ip+route-policy) command is run, the device modifies a specified attribute of the direct or static routes that match the specified route-policy.
    5. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
  + To apply a route-policy in the VPN instance IPv6 address family view, perform the following operations:
    
    1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
    2. Run the [**ip vpn-instance**](cmdqueryname=ip+vpn-instance) *vpn-instance-name* command to enter the VPN instance view.
    3. Run the [**ipv6-family**](cmdqueryname=ipv6-family) command to enable the IPv6 address family for the VPN instance and enter the VPN instance IPv6 address family view.
    4. Run the [**ipv6**](cmdqueryname=ipv6) { **direct-routing-table** | **static-routing-table** } **route-policy** *route-policy-name* command to apply a route-policy to the direct or static routes in the VPN instance IPv6 address family.
    5. Run the [**nd vlink-direct-route advertise**](cmdqueryname=nd+vlink-direct-route+advertise) [ **route-policy** *route-policy-name* ] command to configure the device to advertise VPN NDP Vlink direct routes. The **route-policy** *route-policy-name* parameter specifies the route-policy used to filter the NDP Vlink direct routes to be advertised. For details, see [Configuring Route Exchange Between PEs and CEs](dc_vrp_mpls-l3vpn-v6_cfg_2061.html#EN-US_TASK_0172369590__step_dc_vrp_mpls-l3vpn-v6_cfg_206106).
    6. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.