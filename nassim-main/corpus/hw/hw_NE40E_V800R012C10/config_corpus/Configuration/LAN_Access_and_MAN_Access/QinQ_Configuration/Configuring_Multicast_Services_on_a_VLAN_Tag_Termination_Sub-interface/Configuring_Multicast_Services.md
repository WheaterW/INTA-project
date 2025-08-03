Configuring Multicast Services
==============================

After a dot1q or QinQ VLAN tag termination sub-interface is configured, configure multicast services for the sub-interface so user hosts of this sub-interface can communicate with multicast sources.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number.subinterface-number*
   
   
   
   The dot1q or QinQ VLAN tag termination sub-interface view is displayed.
3. Perform the actions described in [Table 1](#EN-US_TASK_0172363276__tab_1) to configure the multicast service for the dot1q or QinQ VLAN tag termination sub-interface.
   
   
   
   **Table 1** Configuring the multicast service for a dot1q or QinQ VLAN tag termination sub-interface
   | Service Type | Action | Remarks |
   | --- | --- | --- |
   | Layer 2 multicast | Run [**igmp-snooping static-router-port**](cmdqueryname=igmp-snooping+static-router-port) **vsi** *vsi-name*  The dot1q or QinQ VLAN tag termination sub-interface is configured as a static router interface for a virtual switching instance (VSI). | The VSI specified in the command must have been bound to the dot1q or QinQ VLAN tag termination. |
   | Configure the dot1q or QinQ VLAN tag termination sub-interface as a static multicast member interface for a VSI: * In the dot1q VLAN tag termination sub-interface view, run the [**l2-multicast static-group**](cmdqueryname=l2-multicast+static-group) [ **source-address** *source-address-ip-address* ] **group-address** *group-address* [**dot1q**](cmdqueryname=dot1q) [**vid**](cmdqueryname=vid) *vid* **vsi** *vsi-name* command. * In the QinQ VLAN tag termination sub-interface view, run the [**l2-multicast static-group**](cmdqueryname=l2-multicast+static-group) [ **source-address** *source-address-ip-address* ] **group-address** *group-address* **qinq** **pe-vid** *pe-vid* **ce-vid** *ce-id* **vsi** *vsi-name* command. | The VSI specified in the command must have been bound to the dot1q or QinQ VLAN tag termination. |
   | Run the [**igmp-snooping group-policy**](cmdqueryname=igmp-snooping+group-policy) { *acl-number* | **acl-name** *acl-name* } [ **version** *number* ] **qinq** **pe-vid** *vlan-id* **ce-vid** { *vid1* [ **to** *vid2* ]} &<1-10> command to set a limit on the range of multicast groups that hosts can join. | - |
   | Layer 3 multicast | Run the [**igmp static-group**](cmdqueryname=igmp+static-group) *StaticGrp* [ **inc-step-mask** { *IncStepGrpMask* | *IncStepGrpMaskLen* } **number** *TotalNum* ] [ **source** *SourceAddr* ] { **qinq** **pe-vid** *peVidValue* **ce-vid** *lowCeValue* [ **to** *highCeValue* ] | **dot1q****vid** *lowVidValue* [ **to** *highVidValue* ]} command to statically add a QinQ or dot1q VLAN tag termination sub-interface to multicast groups in batches or a single multicast group. | The static group with tag parameters can be configured only on the QinQ VLAN tag termination sub-interface or the dot1q VLAN tag termination sub-interface. |
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.