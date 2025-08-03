Configuring QinQ Mapping
========================

QinQ mapping allows a device to map a user virtual local area network (VLAN) ID to a carrier VLAN ID, shielding different user VLAN IDs in packets.

#### Usage Scenario

QinQ mapping is deployed on Layer 2 edge devices to map user VLAN IDs in packets from users. The devices map the VLAN IDs in user packets to specified VLAN IDs before forwarding the packets to the public network. QinQ mapping is applicable (but not limited) to the following scenarios:

* VLAN IDs deployed in new sites and old sites conflict, but the new sites need to communicate with the old sites.
* VLAN ID planning at each site on the public network is different. As a result, the VLAN IDs conflict. These sites, however, do not need to communicate with each other.
* VLAN IDs on both ends of the public network are different.

The NE40E supports the following QinQ mapping mode:

* 1 to 1 QinQ mapping
  
  When a QinQ mapping sub-interface receives a single-tagged packet, the sub-interface replaces the VLAN ID in the packet with a specified VLAN ID.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

When receiving a Layer 2 multicast packet from the network side, a QinQ mapping sub-interface connected to a VPLS network removes the outer tag, adds the learned inner and outer tags to the packet, and then forwards the packet to a downstream device.

#### Pre-configuration Tasks

Before configuring QinQ mapping, plan user VLANs so that user packets carry one or two VLAN tags.



[Configuring 1 to 1 QinQ Mapping](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_qinq_cfg_0049.html)

When a 1 to 1 QinQ mapping-enabled sub-interface receives a single-tagged packet, the sub-interface replaces the virtual local area network (VLAN) ID in the packet with a specified VLAN ID.

[Verifying the QinQ Mapping Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_qinq_cfg_0050.html)

After configuring QinQ mapping functions, verify the configuration.