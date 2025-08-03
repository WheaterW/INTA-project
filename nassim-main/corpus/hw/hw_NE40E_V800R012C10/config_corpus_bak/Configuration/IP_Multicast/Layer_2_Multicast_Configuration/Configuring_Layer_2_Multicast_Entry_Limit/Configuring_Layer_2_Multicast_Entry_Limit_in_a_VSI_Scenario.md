Configuring Layer 2 Multicast Entry Limit in a VSI Scenario
===========================================================

Layer 2 multicast entry limit configurations can be performed in a VSI scenario to limit the multicast group number.

#### Context

On the network shown in [Figure 1](#EN-US_TASK_0172367896__fig_dc_vrp_l2mc_cfg_005401), PE1 is downlinked to a residential network and uplinked to PE2 through a VPLS network to access the IPTV server. To ensure high PE1 performance, stable multicast data transmission on PE1, and subscribers' good image experience, configure Layer 2 multicast entry limit for the VSI on PE1. Layer 2 multicast entry limit can be configured for a VSI, a sub-interface in a VSI, and a PW in a VSI.

**Figure 1** Configuring Layer 2 multicast entry limit in a VSI scenario  
![](images/fig_dc_vrp_l2mc_cfg_005401.png)  

![](../../../../public_sys-resources/note_3.0-en-us.png) 

The prerequisites for configuring Layer 2 multicast entry limit are as follows:

PE1 in the figure needs to be deployed with Layer 2 multicast entry limit.

A PW and a VSI must have been configured.

If multicast entry limit is deployed for a PW, the PW signaling protocol must be set to Label Distribution Protocol (LDP).

If multicast entry limit is deployed for a sub-interface, the sub-interface must have been bound to a VSI. The sub-interface can be an Ethernet sub-interface, a GE sub-interface, or an Eth-Trunk sub-interface.


Layer 2 multicast entry limit configurations can be performed for a VSI, an interface, a sub-interface, or a PW. You can choose the configurations as required.


#### Procedure

* Configuring Layer 2 multicast entry limit for a VSI, interface, sub-interface, or PW
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. The following configurations are parallel. You can configure one or more items as required. For details, see [Table 1](#EN-US_TASK_0172367896__tb_01).
     
     
     
     **Table 1** Configuring Layer 2 multicast entry limit based on different criteria
     | Criteria | Multicast Group Number Limit |
     | --- | --- |
     | VSI | 1. Run the [**vsi**](cmdqueryname=vsi) *vsi-name* command to enter the VSI view. 2. Run the [**l2-multicast limit max-entry**](cmdqueryname=l2-multicast+limit+max-entry) *count* [ **except** { *acl-number* | **acl-name** *acl-name* } ] command to configure a multicast group number limit for the VSI.  **except** { *acl-number* | **acl-name** *acl-name* } is used to prevent groups from being counted against the limit. The ACL specified in this command must have been configured. 3. Run the [**commit**](cmdqueryname=commit) command to commit the configuration. |
     | Interface | 1. Run the [**interface**](cmdqueryname=interface) *interface-type* *interface-number* command to enter the view of an Ethernet, a GE, or an Eth-Trunk interface. 2. Run the [**l2 binding**](cmdqueryname=l2+binding) **vsi** *vsi-name* command to bind the interface to a VSI. 3. Run the [**l2-multicast limit max-entry**](cmdqueryname=l2-multicast+limit+max-entry) *count* [ **except** { *acl-number* | **acl-name** *acl-name* } ] command to configure a multicast group number limit for the interface.  **except** { *acl-number* | **acl-name** *acl-name* } is used to prevent groups from being counted against the limit. The ACL specified in this command must have been configured. |
     | Sub-interface | 1. Run the [**interface**](cmdqueryname=interface) *interface-type* *interface-number.subnumber* command to enter the Ethernet sub-interface view. 2. Run the [**l2 binding**](cmdqueryname=l2+binding) **vsi** *vsi-name* command to bind the sub-interface to a VSI. 3. Run the [**l2-multicast limit max-entry**](cmdqueryname=l2-multicast+limit+max-entry) *count* [ **except** { *acl-number* | **acl-name** *acl-name* } ] command to configure a multicast group number limit for the sub-interface.  **except** { *acl-number* | **acl-name** *acl-name* } is used to prevent groups from being counted against the limit. The ACL specified in this command must have been configured. 4. Run the [**commit**](cmdqueryname=commit) command to commit the configuration. |
     | PW | 1. Run the [**vsi**](cmdqueryname=vsi) *vsi-name* command to enter the VSI view. 2. Run the [**pwsignal**](cmdqueryname=pwsignal) **ldp** command to configure LDP as the PW signaling protocol and enter the VSI-LDP view. 3. Run the [**l2-multicast limit max-entry**](cmdqueryname=l2-multicast+limit+max-entry) *count* [ **except** { *acl-number* | **acl-name** *acl-name* } ] **remote-peer** *ip-address* [ **negotiation-vc-id** *vc-id* ] command to configure a multicast group number limit for a PW.  **except** { *acl-number* | **acl-name** *acl-name* } is used to prevent groups from being counted against the limit. The ACL specified in this command must have been configured. 4. Run the [**commit**](cmdqueryname=commit) command to commit the configuration. |