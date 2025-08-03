Configuring IPv6 VXLAN in Centralized Gateway Mode Using BGP EVPN
=================================================================

IPv6 VXLAN can be deployed in centralized gateway mode so that all inter-subnet traffic is forwarded through Layer 3 gateways, thereby implementing centralized traffic management.

#### Usage Scenario

To allow intra- and inter-subnet communication between a tenant's VMs located in different geological locations on an IPv6 network, properly deploy Layer 2 and Layer 3 gateways on the network and establish IPv6 VXLAN tunnels.

On the network shown in [Figure 1](#EN-US_TASK_0229407586__fig_dc_vrp_vxlan_cfg_103901), Server2 and Server3 belong to the same network segment and access the IPv6 VXLAN through Device1 and Device2, respectively. Server1 and Server2 belong to different network segments and both access the IPv6 VXLAN through Device1.

* To allow VM1 on Server2 and VM1 on Server3 to communicate, deploy Layer 2 gateways on Device1 and Device2 and establish an IPv6 VXLAN tunnel between Device1 and Device2. This ensures that the VMs on the same network segment can communicate.
* To allow VM1 on Server1 and VM1 on Server3 to communicate, deploy a Layer 3 gateway on Device3 and establish one IPv6 VXLAN tunnel between Device1 and Device3 and another one between Device2 and Device3. This ensures that the VMs on different network segments can communicate.

The VMs and Layer 3 VXLAN gateway can be allocated either IPv4 or IPv6 addresses. This means that either an IPv4 or IPv6 overlay network can be used with IPv6 VXLAN. [Figure 1](#EN-US_TASK_0229407586__fig_dc_vrp_vxlan_cfg_103901) shows an IPv4 overlay network.

**Figure 1** Network diagram of configuring IPv6 VXLAN in centralized gateway mode  
![](figure/en-us_image_0000002126361165.png)
![](../../../../public_sys-resources/note_3.0-en-us.png) 

Layer 3 gateways must be deployed on the IPv6 VXLAN if VMs must communicate with VMs on other network segments or with external networks. Layer 3 gateways do not need to be deployed for VMs communicating on the same network segment.


The following table lists the difference in centralized gateway configuration between IPv4 and IPv6 overlay networks.

| Configuration Task | IPv4 Overlay Network | IPv6 Overlay Network |
| --- | --- | --- |
| Configure a Layer 3 gateway on an IPv6 VXLAN. | Configure an IPv4 address for the VBDIF interface of the Layer 3 gateway. | Configure an IPv6 address for the VBDIF interface of the Layer 3 gateway. |




#### Pre-configuration Tasks

Before configuring IPv6 VXLAN in centralized gateway mode using BGP EVPN, complete the following task:

* Configure an IPv6 routing protocol to achieve Layer 3 connectivity on the IPv6 network.


[Configuring a VXLAN Service Access Point](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vxlan6_cfg_0002.html)

Layer 2 sub-interfaces are used for service access on VXLANs. These Layer 2 sub-interfaces can have different encapsulation types configured to transmit various types of data packets. After a Layer 2 sub-interface is associated with a BD, which is used as a broadcast domain, the sub-interface can transmit data packets through this BD.

[Configuring an IPv6 VXLAN Tunnel](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vxlan6_cfg_0003.html)

Using BGP EVPN to establish an IPv6 VXLAN tunnel between VTEPs involves a series of operations. These include establishing a BGP EVPN peer relationship, configuring an EVPN instance, and configuring ingress replication.

[Configuring a Layer 3 IPv6 VXLAN Gateway](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vxlan6_cfg_0004.html)

To allow users on different network segments to communicate, deploy a Layer 3 gateway and specify the IP address of its VBDIF interface as the default gateway address of the users.

[(Optional) Configuring a Limit on the Number of MAC Addresses Learned by an Interface](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vxlan6_cfg_0014.html)

MAC address learning limiting helps improve VXLAN network security.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vxlan6_cfg_0005.html)

After configuring IPv6 VXLAN in centralized gateway mode using BGP EVPN, verify information about the IPv6 VXLAN tunnels, VNI status, and VBDIF interfaces.