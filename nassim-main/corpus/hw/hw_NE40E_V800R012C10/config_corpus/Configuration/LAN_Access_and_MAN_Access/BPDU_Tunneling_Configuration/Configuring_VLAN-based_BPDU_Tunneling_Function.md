Configuring VLAN-based BPDU Tunneling Function
==============================================

If each user-side interface on a PE is connected to multiple CEs, BPDUs sent from user networks must carry VLAN tags to identify these user networks. To transparently transmit BPDUs from user networks over the carrier network, deploy VLAN-based BPDU tunneling.

#### Usage Scenario

If each user-side interface on a provider edge (PE) is connected to multiple customer edges (CEs), BPDUs sent from user networks must contain VLAN tags so that the PE device can identify BPDUs from different user networks. To transparently transmit BPDUs from user networks over the carrier network, you can configure VLAN-based BPDU tunneling. With VLAN-based BPDU tunneling configured, BPDUs from user networks are transparently transmitted through different BPDU tunnels over the Layer 2 network of the carrier network to perform the spanning tree calculation.


#### Pre-configuration Tasks

Before configuring VLAN-based BPDU tunneling, complete the following tasks:

* Check that the interfaces through which BPDUs are transmitted are connected correctly.
* Check that the interfaces through which BPDUs are transmitted are Layer 2 interfaces.


[Enabling the Spanning Tree Calculation](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bpdu-tunnel_cfg_0011.html)

Bridge protocol data units (BPDUs) from user networks are transparently transmitted through different BPDU tunnels over the Layer 2 network of a carrier network to perform the spanning tree calculation.

[Configuring an Interface to Add a Specified VLAN ID to BPDUs](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bpdu-tunnel_cfg_0012.html)

If multiple user networks are connected to the same interface of a provider edge (PE), configure the interfaces of customer edges (CEs) to add specified virtual local area network (VLAN) IDs to bridge protocol data units (BPDUs) before sending them to the PE. The VLAN IDs identify the user networks to which the BPDUs belong.

[Configuring VLAN-based BPDU Tunneling](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bpdu-tunnel_cfg_0013.html)

You can configure VLAN-based bridge protocol data unit (BPDU) tunneling based on the different roles of provider edges (PEs) and customer edges (CEs) or on the same role of PEs and CEs (VLAN is short for virtual local area network). After VLAN-based BPDU tunneling is configured, the PEs do not send BPDUs to their CPUs for processing. Instead, they transparently transmit the BPDUs through BPDU tunnels over the Layer 2 network of the carrier network to user networks.

[Configuring an Interface to Allow Packets with Specified VLAN IDs to Pass](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bpdu-tunnel_cfg_0014.html)

To enable users to communicate through a carrier network, configure interfaces on provider edges (PEs) that are connected to the carrier network to allow the passing of packets with specified virtual local area network (VLAN) IDs.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bpdu-tunnel_cfg_0015.html)

After configuring VLAN-based bridge protocol data unit (BPDU) tunneling, verify the configuration (VLAN is short for virtual local area network).