Configuring Routed Proxy ND
===========================

Routed proxy ND can be deployed if hosts are on the same network segment but different physical networks and the gateways connected to the hosts have different addresses.

#### Context

If hosts that need to communicate are on the same network segment but different physical networks and the gateway connected to the hosts are configured with different IP addresses, enable routed proxy ND on the interfaces connecting the Router and hosts.

On the network shown in [Figure 1](#EN-US_TASK_0161511714__en-us_concept_0161511699_fig_dc_vrp_nd_feature_002901), DeviceA and DeviceB are connected to different networks, and the IPv6 addresses of Interface1 and Interface2 are on different network segments. HostA and HostB are used as an example. To communicate with HostB, HostA must first send an NS message to request HostB's MAC address because the destination IPv6 address is on the same network segment as the local IPv6 address. However, as HostA and HostB are located on different physical networks, HostB cannot receive the NS message and therefore does not respond.**Figure 1** Typical networking of routed proxy ND  
![](images/fig_dc_vrp_nd_feature_003705.png)  

To address this problem, enable routed ND proxy on DeviceA's interface 1 and DeviceB's interface 2.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
3. Run [**ipv6 enable**](cmdqueryname=ipv6+enable)
   
   
   
   IPv6 is enabled on the interface.
4. Run [**ipv6 address**](cmdqueryname=ipv6+address) { *ipv6-address* *prefix-length* | *ipv6-address*/*prefix-length* } [ **tag** *tag-value* ]
   
   
   
   A global unicast address is configured for the interface.
5. Run [**ipv6 nd proxy route enable**](cmdqueryname=ipv6+nd+proxy+route+enable) [ **prune** ]
   
   
   
   Routed proxy ND is enabled.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.