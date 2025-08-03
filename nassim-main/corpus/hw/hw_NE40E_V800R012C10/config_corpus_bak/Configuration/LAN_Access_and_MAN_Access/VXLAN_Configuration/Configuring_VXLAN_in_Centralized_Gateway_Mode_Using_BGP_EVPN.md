Configuring VXLAN in Centralized Gateway Mode Using BGP EVPN
============================================================

VXLAN can be deployed in centralized gateway mode so that all inter-subnet traffic is forwarded through Layer 3 gateways, thereby implementing centralized traffic management.

#### Usage Scenario

An enterprise may allocate VMs in different locations to a tenant over an IPv4 network. Some VMs are on the same subnet, while others are not. To allow communication between VMs, properly deploy Layer 2 and Layer 3 VXLAN gateways and establish VXLAN tunnels.

On the network shown in [Figure 1](#EN-US_TASK_0000001884468548__en-us_task_0274174836_fig_dc_vrp_vxlan_cfg_103901), Server2 and Server3 belong to the same subnet and access the VXLAN through Device1 and Device2, respectively. Server1 and Server2 belong to different subnets and both access the VXLAN through Device1.

* To enable communication between VM1 on Server2 and VM1 on Server3, deploy Layer 2 VXLAN gateways on Device1 and Device2 and establish a VXLAN tunnel between Device1 and Device2 so that tenants on the same subnet can communicate.
* To enable communication between VM1 on Server1 and VM1 on Server3, deploy a Layer 3 VXLAN gateway on Device3 and establish VXLAN tunnels between Device1 and Device3 and between Device2 and Device3 so that tenants on different subnets can communicate.

The VMs and Layer 3 VXLAN gateway can be allocated either IPv4 or IPv6 addresses. This means that either an IPv4 or IPv6 overlay network can be used with IPv4 VXLAN. [Figure 1](#EN-US_TASK_0000001884468548__en-us_task_0274174836_fig_dc_vrp_vxlan_cfg_103901) shows an IPv4 overlay network.

**Figure 1** Network diagram of configuring VXLAN in centralized gateway mode  
![](figure/en-us_image_0000002126480901.png)
![](../../../../public_sys-resources/note_3.0-en-us.png) 

If only VMs on the same subnet need to communicate with each other, Layer 3 VXLAN gateways do not need to be deployed. If VMs on different subnets need to communicate with each other or VMs on the same subnet need to communicate with external networks, Layer 3 VXLAN gateways must be deployed.


The following table lists the differences in centralized gateway configuration between IPv4 and IPv6 overlay networks.

| Configuration Task | IPv4 Overlay Network | IPv6 Overlay Network |
| --- | --- | --- |
| Configure a Layer 3 VXLAN gateway. | Configure an IPv4 address for the VBDIF interface of the Layer 3 gateway. | Configure an IPv6 address for the VBDIF interface of the Layer 3 gateway. |




#### Prerequisites

Before configuring VXLAN in centralized gateway mode using BGP EVPN, complete the following task:

* Configure a routing protocol to ensure Layer 3 connectivity.


[Configuring a VXLAN Service Access Point](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vxlan6_cfg_0018b.html)

Layer 2 sub-interfaces are used for service access on VXLANs. These Layer 2 sub-interfaces can have different encapsulation types configured to transmit various types of data packets. A Layer 2 sub-interface can transmit data packets through a BD after being associated with it.

[Configuring a VXLAN Tunnel](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vxlan_cfg_1214.html)

To allow VXLAN tunnel establishment between VTEPs using EVPN, establish a BGP EVPN peer relationship, configure an EVPN instance, and configure ingress replication.

[Configuring a Layer 3 VXLAN Gateway](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vxlan_cfg_1215.html)

To allow users on different network segments to communicate, a Layer 3 VXLAN gateway must be deployed, and the default gateway address of the users must be the IP address of the VBDIF interface of the Layer 3 gateway.

[(Optional) Configuring a Static MAC Address Entry](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vxlan_cfg_0023b.html)

Using static MAC address entries to forward user packets helps reduce BUM traffic on the network and prevent bogus attacks.

[(Optional) Configuring a Limit on the Number of MAC Addresses Learned by an Interface](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vxlan6_cfg_0021b.html)

MAC address learning limiting helps improve VXLAN network security.

[Verifying the Configuration of VXLAN in Centralized Gateway Mode Using BGP EVPN](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vxlan_cfg_1049.html)

After configuring VXLAN in centralized gateway mode for dynamic tunnel establishment, check VXLAN tunnel, VNI, and VBDIF interface information.