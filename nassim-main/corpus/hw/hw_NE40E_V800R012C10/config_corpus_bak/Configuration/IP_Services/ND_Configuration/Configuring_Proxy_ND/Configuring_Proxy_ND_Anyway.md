Configuring Proxy ND Anyway
===========================

Proxy ND anyway can be deployed if VMs are on the same network segment but different physical networks and the gateways connected to the VMs have the same address.

#### Context

In scenarios where servers are partitioned into VMs, to allow flexible deployment and migration of VMs on multiple servers or gateways, the common solution is to configure Layer 2 interworking between multiple gateways. However, this approach may lead to larger Layer 2 domains on the network and risks of broadcast storms. To resolve this problem, a common way is to enable any proxy ND on a VM gateway so that the gateway sends its own MAC address to the source VM and the traffic sent from the source VM to other VMs is transmitted over routes.

As shown in [Figure 1](#EN-US_TASK_0161511715__en-us_concept_0161511699_fig_dc_vrp_nd_feature_002905), the IPv6 address of VM1 is 2001:db8:300:400::1/64, the IPv6 address of VM2 is 2001:db8:300:400::2/64, and VM1 and VM2 are on the same network segment. DeviceA and DeviceB are connected to two networks using two interface 1s with the same IPv6 address and MAC address. Because the destination IPv6 address and local IPv6 address are on the same network segment, if VM1 wants to communicate with VM2, VM1 will send an NS packet to request for VM2's MAC address. However, because VM1 and VM2 are on different physical networks, VM2 cannot receive the NS packet and therefore fails to send a reply.**Figure 1** Typical networking of any proxy ND  
![](images/fig_dc_vrp_nd_feature_003706.png)  

To address the problem, enable any proxy ND on DeviceA's interface 1 and DeviceB's interface 1.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
3. Run [**ipv6 enable**](cmdqueryname=ipv6+enable)
   
   
   
   IPv6 is enabled on the interface.
4. Run [**ipv6 address**](cmdqueryname=ipv6+address) { *ipv6-address* *prefix-length* | *ipv6-address*/*prefix-length* } [ **tag** *tag-value* ]
   
   
   
   A global unicast address is configured for the interface.
5. Run [**ipv6 nd proxy anyway enable**](cmdqueryname=ipv6+nd+proxy+anyway+enable)
   
   
   
   Proxy ND anyway is enabled.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.