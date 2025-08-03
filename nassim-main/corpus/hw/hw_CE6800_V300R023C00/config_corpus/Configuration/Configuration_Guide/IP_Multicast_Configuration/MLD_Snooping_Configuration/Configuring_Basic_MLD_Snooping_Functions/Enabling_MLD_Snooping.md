Enabling MLD Snooping
=====================

Enabling MLD Snooping

#### Context

Configuring basic MLD snooping functions is the prerequisite for implementing Layer 2 multicast, and involves enabling MLD snooping, setting the version for MLD messages that can be processed by MLD snooping, and setting the MLD snooping forwarding mode.

After MLD snooping is enabled on a Layer 2 device, it listens to and records the MLD Report messages sent by hosts to a Layer 3 device, and sets up mappings between interfaces and multicast group addresses. The Layer 2 device can then forward multicast data only to the interfaces connected to group members based on the mapping information.

![](../public_sys-resources/note_3.0-en-us.png) 

If MLD snooping is configured in an M-LAG scenario and there are many multicast routing entries and multicast outbound interfaces, high CPU usage will occur due to the large number of entries that need to be delivered, adversely affecting the forwarding of protocol messages. To prevent such an issue, you are advised to reduce the CAR value of multicast services to 100 on the active and standby M-LAG devices.



#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enable MLD snooping globally.
   
   
   ```
   [mld snooping enable](cmdqueryname=mld+snooping+enable)
   ```
   
   By default, MLD snooping is disabled.
3. Enter the VLAN view.
   
   
   ```
   [vlan](cmdqueryname=vlan) vlan-id
   ```
4. Enable MLD snooping in the VLAN.
   
   
   ```
   [mld snooping enable](cmdqueryname=mld+snooping+enable)
   ```
   
   You can run the [**mld snooping enable**](cmdqueryname=mld+snooping+enable) [ **vlan** { *vlan-id1* [ **to** *vlan-id2* ] } &<1-10> ] command in the system view to enable MLD snooping for multiple VLANs in a batch.
   
   ![](../public_sys-resources/note_3.0-en-us.png) 
   * MLD snooping cannot be used together with VLAN mapping in a VLAN.
   * If MLD snooping is configured in a VLAN, PIM-DM cannot be configured on the corresponding VLANIF interface. Similarly, if PIM-DM is configured on a VLANIF interface, MLD snooping cannot be configured in the corresponding VLAN.
   * In a scenario where both Layer 2 and Layer 3 multicast services are configured (Layer 2 multicast is configured in a VLAN and Layer 3 multicast is configured on the corresponding VLANIF interface), MLD snooping must be configured in the VLAN and basic PIM-DM functions must be configured on the VLANIF interface to ensure on-demand multicast traffic forwarding.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```