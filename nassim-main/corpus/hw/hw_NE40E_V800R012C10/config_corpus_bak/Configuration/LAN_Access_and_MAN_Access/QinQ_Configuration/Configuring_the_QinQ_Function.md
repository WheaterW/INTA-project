Configuring the QinQ Function
=============================

A QinQ-enabled device is capable of virtual local area network (VLAN) stacking, which expands VLAN space and reduces the consumption of VLAN ID resources.

#### Usage Scenario

The 12-bit VLAN tag defined in IEEE 802.1Q identifies only a maximum of 4096 VLANs, unable to isolate and identify mass users in the growing metro Ethernet (ME) network. QinQ is therefore developed to expand the VLAN space by adding another 802.1Q tag to an 802.1Q tagged packet. In this way, the number of VLANs increases to 4096 x 4096.

The major differences between QinQ tunneling and selective QinQ are as follows:

**Table 1** QinQ tunneling application scenario
| QinQ Function | Description | Application Scenario |
| --- | --- | --- |
| QinQ tunneling | All data frames that arrive on a QinQ interface are encapsulated with the same outer tag. This encapsulation mode does not distinguish users or services and therefore does not support multi-user and multi-service scenarios. | QinQ tunneling applies where there is no need to distinguish users and services. |
| Selective QinQ | All data frames that arrive on a QinQ interface can be encapsulated with different VLAN tags that distinguish users or services. This encapsulation mode supports multi-user and multi-service scenarios. | Selective QinQ applies when users and services must be distinguished. |

#### Pre-configuration Tasks

Before configuring the QinQ function, plan user VLANs so that packets from the CE to PE carry one VLAN tag.



[Configuring a QinQ Tunnel](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_qinq_cfg_0055_1.html)

After the QinQ tunnel is configured, the interface adds an outer VLAN tag to packets that carry an inner VLAN tag. These packets can then be forwarded on the public network. 

[Configuring Selective QinQ](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_qinq_cfg_0046_1.html)

You can configure selective QinQ on a Layer 2 interface. This configuration allows the interface to add a public virtual local area network (VLAN) tag to a user packet that carries a private VLAN tag so that the user packet can be forwarded over the public network.

[(Optional) Configuring Ethernet Interfaces to Retain the Original Outer TPID EtherType Value in Received QinQ Packets](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_qinq_cfg_0002.html)

All QinQ-enabled devices use 0x8100 as the inner TPID EtherType value. However, different devices use different outer TPID EtherType values. Upon receiving QinQ packets whose outer TPID EtherType value is not 0x8100 from a non-Huawei device, a Huawei device changes the value to 0x8100 by default. This may result in traffic interruptions. To prevent this issue, configure Ethernet interfaces on the Huawei device to retain the original outer TPID EtherType value in received QinQ packets.

[Verifying the QinQ Function Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_qinq_cfg_0007_1.html)

After configuring QinQ, check the detailed information about the outer virtual local area network (VLAN) and the protocol type of the outer VLAN tag.