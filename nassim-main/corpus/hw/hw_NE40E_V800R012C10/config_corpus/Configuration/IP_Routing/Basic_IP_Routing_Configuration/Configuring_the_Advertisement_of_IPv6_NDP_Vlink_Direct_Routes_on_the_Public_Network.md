Configuring the Advertisement of IPv6 NDP Vlink Direct Routes on the Public Network
===================================================================================

On an IPv6 public network, advertising IPv6 neighbor discover protocol (NDP) Vlink direct routes allows precise control of data traffic.

#### Applicable Environment

IP packets are forwarded through a specified physical interface, but cannot be forwarded through a logical interface. If packets reach a logical interface, the device obtains information about the layer-3 interfaces using IPv6 NDP and generates relevant routing entries. The routes recorded by the routing entries are called IPv6 NDP Vlink direct routes.

As shown in [Figure 1](#EN-US_TASK_0172365361__fig_dc_vrp_ip-route_cfg_005601), Device D uses logical interfaces to connect to Devices A, B, and C at three sites. Device E only needs to communicate with Device B, but not with Device A and Device C. You can configure Device D to advertise IPv6 NDP Vlink direct routes and configure a route-policy on Device D to filter out routes to the network segment of the VLAN for which the logical interfaces are configured and filter out routes to Device A and Device C.

**Figure 1** Networking diagram of advertising IPv6 NDP Vlink direct routes on the public network  
![](images/fig_dc_vrp_ip-route_cfg_005601.png)  

Before IPv6 NDP Vlink direct routes are advertised, a route-policy can be used to filter the advertised routes and only routes that pass the filtering can be advertised. In this manner, data traffic can be precisely controlled.

Perform the following steps on the Router on which IPv6 NDP Vlink direct routes need to be advertised.


#### Pre-configuration Tasks

Before advertising IPv6 NDP Vlink direct routes on the public network, complete the following task:

* Configuring parameters of a link layer protocol and assigning an IP address to each interface to ensure that the link layer protocol on the interfaces is Up

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ipv6 nd vlink-direct-route advertise**](cmdqueryname=ipv6+nd+vlink-direct-route+advertise) [ **route-policy** *route-policy-name* | **route-filter** *route-filter-name* ]
   
   
   
   Advertising IPv6 NDP Vlink direct routes is enabled.
   
   
   
   You can specify **route-policy** *route-policy-name* or **route-filter** *route-filter-name* to filter routes.![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   At present, **apply** clauses cannot be used to set routing attributes for the NDP Vlink direct routes that match the filtering rules.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
   
   
   
   After advertising IPv6 NDP Vlink direct routes is enabled, IPv6 NDP Vlink direct routes can be advertised only if they are imported to dynamic routing protocols. Perform the following steps on the Router based on the type of the dynamic routing protocol:
   * If RIPng is used, run the [**import-route**](cmdqueryname=import-route) **direct** [ **cost** *cost* | **route-policy** *route-policy-name* ] \* command to import IPv6 NDP Vlink direct routes to RIPng.
   * If OSPFv3 is used, run the [**import-route**](cmdqueryname=import-route) **direct** [ **cost** *cost* | **inherit-cost** | **route-policy** *route-policy-name* | **tag** *tag* | **type** *type* ] \* command to import IPv6 NDP Vlink direct routes to OSPFv3.
   * If IS-IS is used, run the [**import-route**](cmdqueryname=import-route) **direct** [ **cost-type** { **external** | **internal** } | **cost** *cost* | **tag** *tag* | **route-policy** *route-policy-name* | [ **level-1** | **level-2** | **level-1-2** ] ] \* command to import IPv6 NDP Vlink direct routes to IS-IS.
   * If BGP4+ is used, run the [**import-route**](cmdqueryname=import-route) **direct** [ **med** *med* | **route-policy** *route-policy-name* ] \* command to import IPv6 NDP Vlink direct routes to BGP4+.

#### Verifying the Configuration

Run the [**display ipv6 routing-table**](cmdqueryname=display+ipv6+routing-table) [ **verbose** ] command to check information about advertised IPv6 NDP Vlink direct routes on the public network.