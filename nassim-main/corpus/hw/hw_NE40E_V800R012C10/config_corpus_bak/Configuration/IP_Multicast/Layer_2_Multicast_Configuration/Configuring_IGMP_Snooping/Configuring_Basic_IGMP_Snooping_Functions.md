Configuring Basic IGMP Snooping Functions
=========================================

Configuring basic IGMP snooping functions is the prerequisite for implementing Layer 2 multicast. Configuring basic IGMP snooping functions involves enabling IGMP snooping, setting the version for IGMP messages that can be processed by IGMP snooping, and setting the IGMP snooping forwarding mode.

#### Context

After IGMP snooping is enabled on a Layer 2 device, the Layer 2 device listens to IGMP Report messages exchanged between the connected Layer 3 device and user hosts and uses these IGMP Report messages to set up mappings between interfaces and multicast group addresses. Based on the mappings, the Layer 2 device forwards received multicast data to connected member ports.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**igmp-snooping enable**](cmdqueryname=igmp-snooping+enable)
   
   
   
   IGMP snooping is enabled globally.
3. Enable IGMP snooping for the VLAN or VSI.
   
   
   
   **Table 1** Enabling IGMP snooping for the VLAN or VSI
   | Usage Scenario | Configuration Procedure |
   | --- | --- |
   | Enabling IGMP snooping on a specified VLAN | 1. Run the [**vlan**](cmdqueryname=vlan) *vlan-id* command to enter the VLAN view. 2. Run the [**igmp-snooping enable**](cmdqueryname=igmp-snooping+enable) command to enable IGMP snooping for the VLAN.  By default, IGMP snooping is disabled.  NOTE:  IGMP snooping must be enabled in the system view before being enabled on a VLAN. |
   | Enabling IGMP snooping for multiple VLANs in a VLAN scenario | Run the [**igmp-snooping enable vlan**](cmdqueryname=igmp-snooping+enable+vlan) { *vlan-id1* [ **to** *vlan-id2* ] } & <1-10> command to enable IGMP snooping for multiple VLANs. |
   | Enabling IGMP snooping for a specified VSI in a VPLS scenario | 1. Run the [**vsi**](cmdqueryname=vsi) *vsi-name* [ **static** ] command to enter the VSI view. 2. Run the [**igmp-snooping enable**](cmdqueryname=igmp-snooping+enable) command to enable IGMP snooping for the VSI.  NOTE:  Before enabling IGMP snooping for a VSI, you must enable IGMP snooping globally in the system view. Otherwise, IGMP snooping cannot be enabled for the VSI. |
4. (Optional) Run [**igmp-snooping version**](cmdqueryname=igmp-snooping+version) *number*
   
   
   
   A version is set for IGMP snooping to process IGMP messages.
   
   IGMP snooping can process IGMPv1, IGMPv2, and IGMPv3 messages.
   
   * If the version number is set to 1, only IGMPv1 messages can be processed.
   * If the version number is set to 2, both IGMPv1 and IGMPv2 messages can be processed.
   * If the version number is set to 3, IGMPv1, IGMPv2, and IGMPv3 messages can be processed.
5. (Optional) Run **igmp-snooping ip-policy** *acl-number*
   
   
   
   A policy is configured to filter Report messages in a VLAN or VSI. The configuration enables you to limit users that can enjoy multicast services.
   
   
   
   To filter IGMP Report messages sent by specific hosts, run this command. This improves multicast service deployment security.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.