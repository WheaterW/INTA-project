Overview of BPDU Tunneling
==========================

A bridge protocol data unit (BPDU) tunnel is a path along which BPDUs are transparently transmitted over a carrier network.

#### Definition

BPDUs are Layer 2 protocol packets. As shown in [Figure 1](#EN-US_CONCEPT_0172363697__fig_dc_vrp_bpdu-tunnel_cfg_000201), BPDUs are encapsulated using IEEE 802.3 and are transmitted in multicast mode.

BPDUs are used to transmit Spanning Tree Protocol (STP) and Multiple Spanning Tree Protocol (MSTP) information. The path along which BPDUs are transparently transmitted over a carrier network is known as a Layer 2 protocol tunnel or a BPDU tunnel.

**Figure 1** Basic format of BPDUs  
![](images/fig_dc_vrp_bpdu-tunnel_cfg_000201.png)  

[Table 1](#EN-US_CONCEPT_0172363697__tab_dc_vrp_bpdu-tunnel_cfg_000201) lists fields in a BPDU.

**Table 1** Fields in a BPDU
| Field | Length | Description |
| --- | --- | --- |
| Destination address | 48 bits | Well-known destination MAC address. For general users, the well-known destination MAC address of BPDUs is 0180-C200-0000. |
| Source address | 48 bits | Source MAC address. |
| Length | 16 bits | Length of BPDU data. |



#### Background

As shown in [Figure 2](#EN-US_CONCEPT_0172363697__fig_dc_vrp_bpdu-tunnel_cfg_000202), MSTP runs on user networks 1 and 2. BPDUs from user networks 1 and 2 need to be transparently transmitted over the carrier network and need to reach each other to perform the spanning tree calculation. When BPDUs from user network 1 reach PE1 on the carrier network, PE1 cannot determine whether these BPDUs are transmitted from a user network or a carrier network, because all BPDUs contain the same destination MAC address 0180-C200-0000. PE1 then sends all the BPDUs to its central processing unit (CPU) for processing and performs the spanning tree calculation.

In this situation, devices on user network 1 perform the spanning tree calculation with PE1, instead of devices on user network 2. As a result, BPDUs from user network 1 cannot reach user network 2.

**Figure 2** Transparent transmission of BPDUs over the carrier network  
![](images/fig_dc_vrp_bpdu-tunnel_cfg_000202.png)  

To address this problem, BPDUs must be transparently transmitted over the carrier network. To implement the transparent transmission, the following conditions must be met:

* Branches of a user network can exchange BPDUs.
* BPDUs sent from a user network cannot be processed by the CPUs on carrier network devices.
* BPDUs from different user networks must be isolated and free from interference.

Configuring BPDU tunneling on carrier network devices meets the preceding conditions. After BPDU tunneling is configured, the carrier network can transparently transmit BPDUs between user networks through BPDU tunnels.