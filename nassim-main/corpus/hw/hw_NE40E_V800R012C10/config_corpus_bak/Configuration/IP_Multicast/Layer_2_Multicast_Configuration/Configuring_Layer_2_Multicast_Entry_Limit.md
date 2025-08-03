Configuring Layer 2 Multicast Entry Limit
=========================================

Layer 2 multicast entry limit is a feature used on a Layer 2 network (VLAN or VPLS networking) to prevent bandwidth resources from exceeding the total bandwidth of the aggregation network and ensure service quality for most subscribers.

#### Usage Scenario

As IPTV service applications become increasingly popular among consumers, multicast services are widely deployed. The following problems may arise when IPTV services are deployed on a Layer 2 network:

* Sparsely distributed multicast groups (programs) may increase network deployment burdens.
* If network bandwidth is insufficient, the aggregation network cannot bear all multicast traffic, which degrades subscribers' image experience.

To solve the preceding problems, Layer 2 multicast entry limit can be used to control IPTV services on the aggregation network based on different criteria, including global multicast group number limits. Layer 2 multicast entry limit enables service providers to offer more flexible and refined contents and subscriber-specific policies to ensure service quality for most subscribers.

On the network shown in [Figure 1](#EN-US_TASK_0172367890__fig_dc_vrp_l2mc_cfg_005301), a UPE is downlinked to CEs through a VLAN or VPLS network. Layer 2 multicast entry limit can be deployed on the UPE to limit the multicast group number for IPTV channels delivered by the UPE to CEs.

**Figure 1** Layer 2 multicast entry limit networking  
![](images/fig_dc_vrp_l2mc_cfg_005301.png)  

For details, see [Table 1](#EN-US_TASK_0172367890__tb_01).

**Table 1** Layer 2 multicast entry limit criteria
| Scenario | Criteria | Description |
| --- | --- | --- |
| VLAN scenario | VLAN | Limits the multicast group number for a VLAN. |
| Interface | Limits the multicast group number for an interface. |
| Interface + VLAN | Limits the multicast group number for a VLAN on a specified interface. |
| VPLS scenario | VSI | Limits the multicast group number for a VSI. |
| Interface | Limits the multicast group number for an interface. |
| Sub-interface | Limits the multicast group number for a sub-interface. |
| PW | Limits the multicast group number for a PW. |



#### Pre-configuration Tasks

Before configuring Layer 2 multicast entry limit, complete the following tasks:

* Connect and configure interfaces correctly to ensure that the link layer protocol status of the interfaces is Up.
* Complete basic VLAN or VSI configurations.
* Enable IGMP snooping on the device where multicast entry limit is to be enabled and for the VLAN or VSI where the device resides.


[Configuring Layer 2 Multicast Entry Limit in a VLAN Scenario](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_l2mc_cfg_0057.html)

To limit the number of multicast groups in a VLAN scenario, configure Layer 2 multicast entry limit.

[Configuring Layer 2 Multicast Entry Limit in a VSI Scenario](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_l2mc_cfg_0054.html)

Layer 2 multicast entry limit configurations can be performed in a VSI scenario to limit the multicast group number.

[Verifying the Layer 2 Multicast Entry Limit Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_l2mc_cfg_0055.html)

After configuring Layer 2 multicast entry limit, verify information such as the limit on the number of multicast groups.