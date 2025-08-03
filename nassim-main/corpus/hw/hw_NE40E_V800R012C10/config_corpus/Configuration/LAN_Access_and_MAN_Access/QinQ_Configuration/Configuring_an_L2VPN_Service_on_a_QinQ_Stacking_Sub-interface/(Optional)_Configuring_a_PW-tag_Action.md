(Optional) Configuring a PW-tag Action
======================================

This section describes how to configure a PW-tag action so that a PE changes the P-Tag of packets to be forwarded over a PW in tagged mode to ensure normal communication with non-Huawei devices on an L2VPN network.

#### Context

On the network shown in [Figure 1](#EN-US_TASK_0172363283__en-us_task_0172363265_fig_dc_vrp_qinq_cfg_000302), CE1 and CE2 are connected to the L2VPN network through PE sub-interfaces, PE1 and CE1 are Huawei devices, and PE2 and CE2 are non-Huawei devices.

When a PE transmits multiple services over one PW, the PE adds different P-Tags to packets of different services to isolate the packets on the L2VPN network. When the packets reach the sub-interfaces of another PE on the other end of the PW, each sub-interface accepts only those packets carrying the same P-Tag as that specified on the sub-interface.

However, because the P-Tags on PE1 and PE2 may be different, PE1 cannot communicate with PE2, and users from user networks connected to CE1 and CE2 cannot communicate with each other.

**Figure 1** Networking for accessing an L2VPN through sub-interfaces  
![](images/fig_dc_vrp_qinq_cfg_000302.png)

To address the problem, configure a PW-tag action on the user-side sub-interface of PE1. The PE1 sub-interface changes the P-Tag of packets to that on PE2 before forwarding the packets over the PW. This allows PE1 to communicate with PE2.

[Table 1](#EN-US_TASK_0172363283__en-us_task_0172363265_tab_1) provides the default P-Tag values and the P-Tag values after the PW-tag action.

**Table 1** P-Tag values
| Sub-interface Type | | Default P-Tag Value | P-Tag Value After the PW-Tag Action |
| --- | --- | --- | --- |
| Dot1q sub-interface | | VLAN ID in a packet | New VLAN ID |
| Dot1q VLAN tag termination sub-interface | |
| QinQ VLAN tag termination sub-interface | | Outer VLAN ID in a packet |
| QinQ stacking sub-interface | | Minimum VLAN ID in the VLAN ID range specified on the sub-interface |
| QinQ mapping sub-interface | | Fixed VLAN ID in the system |



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number.subinterface-number*
   
   
   
   The view of a user-side sub-interface on a PE is displayed.
3. Run [**pw-tag**](cmdqueryname=pw-tag) { *vlan-id* | **inner-vlan** | **outer-vlan** } [ **8021p** { *8021p-value* | **inner-vlan** | **outer-vlan** } ]
   
   
   
   A PW-tag action is configured so that the sub-interface changes the P-Tag of packets before forwarding the packets over the PW in tagged mode.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.