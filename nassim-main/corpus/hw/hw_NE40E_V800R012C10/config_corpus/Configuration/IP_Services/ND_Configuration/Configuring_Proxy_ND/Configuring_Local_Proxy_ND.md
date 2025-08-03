Configuring Local Proxy ND
==========================

Local proxy ND can be deployed if hosts on the same network segment and in the same BD want to communicate with each other but the BD is configured with split horizon.

#### Context

Local proxy ND can be deployed if two hosts on the same network segment and in the same BD want to communicate with each other but the BD is configured with split horizon.

On the network shown in [Figure 1](#EN-US_TASK_0172365174__en-us_concept_0161511699_fig_dc_vrp_nd_feature_002904), HostA and HostB are connected to Device. The interfaces connecting HostA and HostB belong to the same BD as Device. Because split horizon is configured on Device for the BD, HostA and HostB cannot communicate with each other at Layer 2.**Figure 1** Typical networking of local proxy ND  
![](images/fig_dc_vrp_nd_feature_003709.png)  

To address this problem, enable local proxy ND on Device's interface 1.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface vbdif**](cmdqueryname=interface+vbdif) *bd-id*
   
   
   
   The VBDIF interface view is displayed.
3. Run [**ipv6 enable**](cmdqueryname=ipv6+enable)
   
   
   
   IPv6 is enabled on the interface.
4. Run [**ipv6 address**](cmdqueryname=ipv6+address) { *ipv6-address* *prefix-length* | *ipv6-address*/*prefix-length* } [ **tag** *tag-value* ]
   
   
   
   A global unicast address is configured for the interface.
5. Run [**ipv6 nd proxy local enable**](cmdqueryname=ipv6+nd+proxy+local+enable)
   
   
   
   Local proxy ND is enabled.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.