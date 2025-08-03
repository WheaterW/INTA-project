Configuring Layer 2 Multicast Entry Limit in a VLAN Scenario
============================================================

To limit the number of multicast groups in a VLAN scenario, configure Layer 2 multicast entry limit.

#### Context

On the network shown in [Figure 1](#EN-US_TASK_0172367893__fig_dc_vrp_l2mc_cfg_005701), PE1 is downlinked to a residential network VLAN 20 and uplinked to PE2 through an MPLS or a VPLS network to access the IPTV server. To save link bandwidth between PE1 and the residential network and ensure good subscribers' image experience, configure Layer 2 multicast entry limit for the VLAN on PE1. If some service providers group all the programs into one or more VLAN channels, Layer 2 multicast entry limit can also be configured to limit the multicast group number for each channel. In a VLAN scenario, Layer 2 multicast entry limit can be configured for a VLAN, GE 0/1/1, or a VLAN channel.**Figure 1** Configuring Layer 2 multicast entry limit in a VLAN scenario  
![](images/fig_dc_vrp_l2mc_cfg_005701.png)  

![](../../../../public_sys-resources/note_3.0-en-us.png) 

On this network, PE1 is a Layer 2 device in a VLAN scenario. Configure Layer 2 multicast entry limit on PE1.

Layer 2 multicast entry limit cannot be performed for a protection VLAN.


Layer 2 multicast entry limit can be configured for a VLAN, an interface, or a VLAN on a specified interface. Perform the following configurations as needed.


#### Procedure

* On PE1, configure Layer 2 multicast entry limit for a VLAN, an interface, or a VLAN on a specified interface.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. According to different restriction granularities, single-granularity or integrated deployment of the restriction on the number of channels may be implemented. The following configurations are parallel. You can configure one or more items as required. For details, see [Table 1](#EN-US_TASK_0172367893__tb_01).
     
     
     
     **Table 1** Configuring Layer 2 multicast entry limit based on different criteria
     | Criteria | Multicast Group Number Limit |
     | --- | --- |
     | VLAN | 1. Run the [**l2-multicast limit max-entry**](cmdqueryname=l2-multicast+limit+max-entry) *count* **vlan** { *vlan-id1* [ **to** *vlan-id2* ] } &<1-10> [ **except** { *acl-number* | **acl-name** *acl-name* } ] command to configure a multicast group number limit for a VLAN.  **except** { *acl-number* | **acl-name** *acl-name* } is used to prevent groups from being counted against the limit. The ACL specified in this command must have been configured. |
     | Interface | 1. Run the [**interface**](cmdqueryname=interface) *interface-type* *interface-number* command to enter the view of an Ethernet, a GE, or an Eth-Trunk interface. 2. Run the [**portswitch**](cmdqueryname=portswitch) command to switch the interface to a Layer 2 interface. 3. Run the [**l2-multicast limit max-entry**](cmdqueryname=l2-multicast+limit+max-entry) *count* [ **except** { *acl-number* | **acl-name** *acl-name* } ] command to configure a multicast group number limit for the interface.  **except** { *acl-number* | **acl-name** *acl-name* } is used to prevent groups from being counted against the limit. The ACL specified in this command must have been configured. |
     | Interface + VLAN | 1. Run the [**interface**](cmdqueryname=interface) *interface-type* *interface-number* command to enter the view of an Ethernet, a GE, or an Eth-Trunk interface. 2. Run the [**portswitch**](cmdqueryname=portswitch) command to switch the interface to a Layer 2 interface. 3. Run the [**l2-multicast limit max-entry**](cmdqueryname=l2-multicast+limit+max-entry) *count* [ **vlan** { { *vlan-id1* [ **to** *vlan-id2* ] } &<1-10> } ] [ **except** { *acl-number* | **acl-name** *acl-name* } ] command to configure a multicast group number limit for a specified VLAN on the interface.  **except** { *acl-number* | **acl-name** *acl-name* } is used to prevent groups from being counted against the limit. The ACL specified in this command must have been configured. |