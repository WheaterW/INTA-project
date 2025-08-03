Configuring IPv6 VXLAN in Centralized Gateway Mode for Static Tunnel Establishment
==================================================================================

IPv6 VXLAN can be deployed in centralized gateway mode so that all inter-subnet traffic is forwarded through Layer 3 gateways, thereby implementing centralized traffic management.

#### Usage Scenario

To allow intra- and inter-subnet communication between a tenant's VMs located in different geological locations on an IPv6 network, properly deploy Layer 2 and Layer 3 gateways on the network and establish IPv6 VXLAN tunnels.

On the network shown in [Figure 1](#EN-US_TASK_0274174836__fig_dc_vrp_vxlan_cfg_103901), Server2 and Server3 belong to the same network segment and access the IPv6 VXLAN through Device1 and Device2, respectively. Server1 and Server2 belong to different network segments and both access the IPv6 VXLAN through Device1.

* To allow VM1 on Server2 and VM1 on Server3 to communicate, deploy Layer 2 gateways on Device1 and Device2 and establish an IPv6 VXLAN tunnel between Device1 and Device2. This ensures that the VMs on the same network segment can communicate.
* To allow VM1 on Server1 and VM1 on Server3 to communicate, deploy a Layer 3 gateway on Device3 and establish one IPv6 VXLAN tunnel between Device1 and Device3 and another one between Device2 and Device3. This ensures that the VMs on different network segments can communicate.

The VMs and Layer 3 VXLAN gateway can be allocated either IPv4 or IPv6 addresses. This means that either an IPv4 or IPv6 overlay network can be used with IPv6 VXLAN. [Figure 1](#EN-US_TASK_0274174836__fig_dc_vrp_vxlan_cfg_103901) shows an IPv4 overlay network.

**Figure 1** Network diagram of configuring IPv6 VXLAN in centralized gateway mode  
![](figure/en-us_image_0000002126480893.png)
![](../../../../public_sys-resources/note_3.0-en-us.png) 

Layer 3 gateways must be deployed on the IPv6 VXLAN if VMs must communicate with VMs on other network segments or with external networks. Layer 3 gateways do not need to be deployed for VMs communicating on the same network segment.


The following table lists the difference in centralized gateway configuration between IPv4 and IPv6 overlay networks.

| Configuration Task | IPv4 Overlay Network | IPv6 Overlay Network |
| --- | --- | --- |
| Configure a Layer 3 gateway on an IPv6 VXLAN. | Configure an IPv4 address for the VBDIF interface of the Layer 3 gateway. | Configure an IPv6 address for the VBDIF interface of the Layer 3 gateway. |




#### Pre-configuration Tasks

Before configuring IPv6 VXLAN in centralized gateway mode for static tunnel establishment, complete the following tasks:

* Configure an IPv6 routing protocol to achieve Layer 3 connectivity on the IPv6 network.


[Configuring a VXLAN Service Access Point](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vxlan6_cfg_0018.html)

Layer 2 sub-interfaces are used for service access on VXLANs. These Layer 2 sub-interfaces can have different encapsulation types configured to transmit various types of data packets. A Layer 2 sub-interface can transmit data packets through a BD after being associated with it.

[Configuring an IPv6 VXLAN Tunnel](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vxlan6_cfg_0019.html)

VXLAN is a tunneling technology that uses MAC-in-UDP encapsulation to extend large Layer 2 networks. If an underlay network is an IPv6 network, you can configure an IPv6 VXLAN tunnel for a virtual network to access a large number of tenants.

[Configuring a Layer 3 IPv6 VXLAN Gateway](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vxlan6_cfg_0020.html)

To allow users on different network segments to communicate, deploy a Layer 3 gateway and specify the IP address of its VBDIF interface as the default gateway address of the users.

[(Optional) Configuring a Static MAC Address Entry](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vxlan6_cfg_0023.html)

Using static MAC address entries to forward user packets helps reduce BUM traffic on the network and prevent bogus attacks.

[(Optional) Configuring a Limit on the Number of MAC Addresses Learned by an Interface](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vxlan6_cfg_0021.html)

MAC address learning limiting helps improve VXLAN network security.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vxlan6_cfg_0022.html)

After configuring IPv6 VXLAN in centralized gateway mode for static tunnel establishment, check IPv6 VXLAN tunnel, VNI, and VBDIF interface information.