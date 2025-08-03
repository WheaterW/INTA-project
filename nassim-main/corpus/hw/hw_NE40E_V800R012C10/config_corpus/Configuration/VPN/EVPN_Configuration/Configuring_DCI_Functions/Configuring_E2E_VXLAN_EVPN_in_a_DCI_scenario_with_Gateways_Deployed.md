Configuring E2E VXLAN EVPN in a DCI scenario with Gateways Deployed
===================================================================

An end-to-end VXLAN EVPN uses the same service platform, which helps implement unified VXLAN VNI resource management.

#### Context

Gateways and DCI-PEs are deployed individually. As edge devices of the underlay network, DCI-PEs only advertise VTEP routes across DCs, but do not store the tenant or host information of DCs.

On the network shown in [Figure 1](#EN-US_TASK_0172363944__fig_dc_vrp_dci_cfg_000301), an end-to-end VXLAN tunnel can be established between Device1 and Device2 to implement communication between DC A and DC B. For example, VMa1 and VMb2 need to communicate with each other. To meet this requirement, establish a BGP EVPN peer relationship between Device1 and Device2 so that they can learn MAC and IP routes from each other. In addition, GW1 and GW2 in the data centers are connected to DCI-PE1 and DCI-PE2, respectively, on the backbone network. An L3VPN based on an MPLS TE tunnel is established between DCI-PE1 and DCI-PE2 to transmit VXLAN packets.

**Figure 1** Configuring E2E VXLAN EVPN in a DCI scenario with gateways deployed  
![](figure/en-us_image_0269830782.png)

#### Procedure

1. Configure basic L3VPN functions on the DCI backbone network. For configuration details, see [Configuring a Basic BGP/MPLS IP VPN](dc_vrp_mpls-l3vpn-v4_cfg_0154.html).
2. Configure an E2E VXLAN tunnel based on BGP EVPN on Device1 and Device2. For details, see [Configuring VXLAN](dc_vrp_vxlan_cfg_1216.html).
   
   
   
   If only Layer 2 communication between VMs needs to be implemented, Layer 3 gateways do not need to be configured. If VMs need to communicate with each other at Layer 3 or with external networks, a Layer 3 gateway needs to be configured.