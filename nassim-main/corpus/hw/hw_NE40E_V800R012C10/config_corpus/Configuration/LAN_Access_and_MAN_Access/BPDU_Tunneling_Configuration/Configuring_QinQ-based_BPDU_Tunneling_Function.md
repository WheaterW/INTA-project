Configuring QinQ-based BPDU Tunneling Function
==============================================

If each user-side interface on a provider edge (PE) is connected to multiple customer edges (CEs), bridge protocol data units (BPDUs) sent from user networks must carry virtual local area network (VLAN) tags to identify these user networks. To transparently transmit BPDUs from user networks over the carrier network and save VLAN ID resources for the carrier network, deploy QinQ-based BPDU tunneling (QinQ is short for 802.1Q in 802.1Q).

#### Usage Scenario

If each user-side interface on a PE is connected to multiple CEs, BPDUs sent from user networks must contain VLAN tags so that the PE device can identify BPDUs from different user networks. To transparently transmit BPDUs from user networks over the carrier network and save VLAN ID resources for the carrier network, you can configure QinQ-based BPDU tunneling. With QinQ-based BPDU tunneling configured, the PEs choose different BPDU tunnels to transmit BPDUs based on their outer VLAN IDs over the carrier network.


#### Pre-configuration Tasks

Before configuring QinQ-based BPDU tunneling, complete the following tasks:

* Check that the interfaces through which BPDUs are transmitted are connected correctly.
* Check that the interfaces through which BPDUs are transmitted are Layer 2 interfaces.


[Enabling the Spanning Tree Calculation](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bpdu-tunnel_cfg_0017.html)

Bridge protocol data units (BPDUs) from user networks are transparently transmitted through different BPDU tunnels over the Layer 2 network of a carrier network to perform the spanning tree calculation.

[Configuring an Interface to Add a Specified VLAN Tag to BPDUs](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bpdu-tunnel_cfg_0018.html)

If multiple user networks are connected to the same interface of a PE, configure the interfaces of CEs to add specified VLAN IDs to bridge protocol data units (BPDUs) before sending them to the PE. The VLAN IDs identify the user networks to which the BPDUs belong.

[Configuring QinQ-based BPDU Tunneling](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bpdu-tunnel_cfg_0019.html)

You can configure QinQ-based bridge protocol data unit (BPDU) tunneling based on the different roles of provider edges (PEs) and customer edges (CEs) or on the same role of PEs and CEs (QinQ is short for 802.1Q in 802.1Q). After QinQ-based BPDU tunneling is configured, the PEs do not send BPDUs to their CPUs for processing. Instead, they transparently transmit the BPDUs through BPDU tunnels over the Layer 2 network of the carrier network to user networks. This configuration also saves virtual local area network (VLAN) ID resources for the carrier network.

[Configuring an Interface to Allow Packets with Specified VLAN IDs to Pass](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bpdu-tunnel_cfg_0020.html)

To enable users to communicate through a carrier network, configure interfaces on provider edges (PEs) that are connected to the carrier network to allow the passing of packets with specified virtual local area network (VLAN) IDs.

[Verifying the Configuration of the QinQ-based BPDU Tunneling Function](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bpdu-tunnel_cfg_0021.html)

After configuring QinQ-based bridge protocol data unit (BPDU) tunneling, verify the configuration (QinQ is short for 802.1Q in 802.1Q).