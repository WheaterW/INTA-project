Configuring Intra-VLAN Proxy ND
===============================

Intra-VLAN proxy ND can be deployed if hosts are on the same VLAN but the VLAN is configured with Layer 2 port isolation.

#### Context

If hosts belong to the same VLAN but the VLAN is configured with Layer 2 port isolation, intra-VLAN proxy ND needs to be enabled on the associated VLAN interfaces to enable host interworking.

As shown in [Figure 1](#EN-US_TASK_0161511716__en-us_concept_0161511699_fig_dc_vrp_nd_feature_002902), HostA and HostB are connected to Device, and the interfaces connecting Device to HostA and HostB belong to the same VLAN. Because intra-VLAN Layer 2 port isolation is configured on Device, HostA and HostB cannot communicate with each other at Layer 2.**Figure 1** Typically networking of intra-VLAN proxy ND  
![](images/fig_dc_vrp_nd_feature_003707.png)  

To address this problem, enable intra-VLAN proxy ND on Device's interface 1.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface vlanif**](cmdqueryname=interface+vlanif) *vlan-id* or [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The VLANIF interface view or Layer 3 sub-interface view is displayed.
3. Run [**ipv6 enable**](cmdqueryname=ipv6+enable)
   
   
   
   IPv6 is enabled on the interface.
4. Run [**ipv6 address**](cmdqueryname=ipv6+address) { *ipv6-address* *prefix-length* | *ipv6-address*/*prefix-length* } [ **tag** *tag-value* ]
   
   
   
   A global unicast address is configured for the interface.
5. Run [**ipv6 nd proxy inner-access-vlan enable**](cmdqueryname=ipv6+nd+proxy+inner-access-vlan+enable)
   
   
   
   Intra-VLAN proxy ND is enabled.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.