Configuring Interface-based BPDU Tunneling Function
===================================================

When each interface of devices on a carrier network is connected to only one user network, you can configure interface-based bridge protocol data unit (BPDU) tunneling to transparently transmit BPDUs from different user networks over the carrier network.

#### Usage Scenario

If each interface of a provider edge (PE) is connected to one customer edge (CE) and BPDUs sent from user networks are untagged, you can configure interface-based BPDU tunneling to transparently transmit these BPDUs over the carrier network. With interface-based BPDU tunneling configured, BPDUs from user networks are transparently transmitted through different BPDU tunnels over the Layer 2 network of the carrier network to perform the spanning tree calculation.


#### Pre-configuration Tasks

Before configuring interface-based BPDU tunneling, complete the following tasks:

* Check that the interfaces through which BPDUs are transmitted are connected correctly.
* Check that the interfaces through which BPDUs are transmitted are Layer 2 interfaces.


[Enabling the Spanning Tree Calculation](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bpdu-tunnel_cfg_0005.html)

Bridge protocol data units (BPDUs) from user networks are transparently transmitted through different BPDU tunnels over the Layer 2 network of a carrier network to perform the spanning tree calculation.

[Adding an Interface to a Specified VLAN](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bpdu-tunnel_cfg_0006.html)

Each interface on a provider edge (PE) is connected to one user network, and user networks belong to different local area networks (LANs). BPDUs sent from user networks to PEs are untagged. The PEs, however, need to identify the LANs to which the BPDUs belong. In this situation, you need to add the PE interfaces to specified virtual local area networks (VLANs).

[Configuring Interface-based BPDU Tunneling](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bpdu-tunnel_cfg_0007.html)

You can configure interface-based bridge protocol data unit (BPDU) tunneling based on the different roles of provider edges (PEs) and customer edges (CEs) or on the same role of PEs and CEs. After the configuration is complete, when an interface of a PE receives a BPDU from a user network, the PE adds a VLAN tag to the BPDU based on the PVID of the interface, selects a BPDU tunnel based on the VLAN ID in the tag, and transmits the BPDU through the BPDU tunnel. In this manner, BPDUs from different user networks are isolated.

[Configuring an Interface to Allow Packets with Specified VLAN IDs to Pass](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bpdu-tunnel_cfg_0008.html)

To enable users to communicate through a carrier network, configure interfaces on provider edges (PEs) that are connected to the carrier network to allow the passing of packets with specified virtual local area network (VLAN) IDs.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bpdu-tunnel_cfg_0009.html)

After configuring interface-based bridge protocol data unit (BPDU) tunneling, verify the configuration.