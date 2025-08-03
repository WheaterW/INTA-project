Configuring Basic MLD Snooping Functions
========================================

Configuring basic MLD snooping functions involves enabling MLD snooping and setting the MLD version. Those basic functions need to be configured before you configure other MLD snooping functions.

#### Context

After MLD snooping is enabled on a Layer 2 device, the device listens to and analyzes MLD Report messages sent from user hosts to a Layer 3 device. The Layer 2 device then uses the message information to set up the mapping between interfaces and multicast group addresses. After receiving the data of a multicast group, the Layer 2 device reads the mapping and forwards the data only to the interfaces connected to users interested in the data.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**mld-snooping enable**](cmdqueryname=mld-snooping+enable)
   
   
   
   MLD snooping is enabled globally.
3. Enable MLD snooping in a VLAN or VSI.
   
   
   
   **Table 1** Enabling MLD snooping in a VLAN or VSI
   | Usage Scenario | Configuration Procedure |
   | --- | --- |
   | Enabling MLD snooping in a specified VLAN | 1. Run the [**vlan**](cmdqueryname=vlan) *vlan-id* command to enter the VLAN view. 2. Run the [**mld-snooping enable**](cmdqueryname=mld-snooping+enable) command to enable MLD snooping in the VLAN.  NOTE:  Before enabling MLD snooping in a VLAN, enable MLD snooping in the system view. Otherwise, MLD snooping fails to be enabled in the VLAN. |
   | Enabling MLD snooping in multiple VLANs | Run the [**mld-snooping enable vlan**](cmdqueryname=mld-snooping+enable+vlan) { *vlan-id1* [ **to** *vlan-id2* ] } & <1-10> command to enable MLD snooping in multiple VLANs. |
   | Enabling MLD snooping in a specified VSI in a VPLS scenario | 1. Run the [**vsi**](cmdqueryname=vsi) *vsi-name* [ **static** ] command to enter the VSI view. 2. Run the [**mld-snooping enable**](cmdqueryname=mld-snooping+enable) command to enable MLD snooping in the VSI.  NOTE:  Before enabling MLD snooping in a VSI, enable MLD snooping in the system view. Otherwise, MLD snooping fails to be enabled in the VSI. |
4. (Optional) Run [**mld-snooping version**](cmdqueryname=mld-snooping+version) *number*
   
   
   
   A version is configured for MLD snooping to process MLD messages.
   
   
   
   MLD snooping can process MLDv1 and MLDv2 messages.
   
   * If the version number is set to 1, only MLDv1 messages can be processed.
   * If the version number is set to 2, both MLDv1 and MLDv2 messages can be processed.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.