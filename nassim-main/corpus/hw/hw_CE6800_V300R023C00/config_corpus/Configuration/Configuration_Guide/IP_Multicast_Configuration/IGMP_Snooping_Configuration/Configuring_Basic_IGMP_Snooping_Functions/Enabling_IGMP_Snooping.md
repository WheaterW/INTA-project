Enabling IGMP Snooping
======================

Enabling IGMP Snooping

#### Context

Configuring basic IGMP snooping functions is the prerequisite for implementing Layer 2 multicast, and involves enabling IGMP snooping, setting the version for IGMP messages that can be processed by IGMP snooping, and setting the IGMP snooping forwarding mode.

After IGMP snooping is enabled on a Layer 2 device, it listens to and records the IGMP Report messages sent from hosts to a Layer 3 device, and sets up mappings between interfaces and multicast group addresses. The Layer 2 device can then forward multicast data only to the interfaces connected to group members based on the mapping information.

![](../public_sys-resources/note_3.0-en-us.png) 

* If IGMP snooping is configured in a VLAN, PIM-DM cannot be configured on the corresponding VLANIF interface. Similarly, if PIM-DM is configured on a VLANIF interface, IGMP snooping cannot be configured in the corresponding VLAN.
* When configuring IGMP snooping in an M-LAG scenario, ensure that either the configuration of IGMP snooping querier or IGMP snooping proxy is consistent on the primary and backup M-LAG devices.
* If IGMP snooping is configured in an M-LAG scenario and there are many multicast routing entries and multicast outbound interfaces, high CPU usage will occur due to the high number of entries that need to be delivered, adversely affecting the forwarding of protocol packets. To prevent such an issue, you are advised to reduce the CAR value of IGMP multicast services to 100 on the master and backup M-LAG devices, reducing the CPU usage.
* IGMP snooping cannot be used together with VLAN mapping.
* The following pairs of functions cannot be both configured in the same VLAN:
  
  IGMP snooping querier and IGMP snooping proxy
  
  Report and Leave message suppression and IGMP snooping proxy
* In a scenario where both Layer 2 multicast and Layer 3 multicast are enabled (that is, Layer 2 multicast is configured in a VLAN, and Layer 3 multicast is configured on the corresponding VLANIF interface), you must perform the following operations to ensure that multicast traffic can be forwarded normally:
  
  Enable IGMP snooping in the VLAN.
  
  Enable PIM and IGMP on the corresponding VLANIF interface.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enable IGMP snooping globally.
   
   
   ```
   [igmp snooping enable](cmdqueryname=igmp+snooping+enable)
   ```
   
   By default, IGMP snooping is disabled.
3. Enter the VLAN view.
   
   
   ```
   [vlan](cmdqueryname=vlan) vlan-id
   ```
4. Enable IGMP snooping in the VLAN.
   
   
   ```
   [igmp snooping enable](cmdqueryname=igmp+snooping+enable)
   ```
   
   To enable IGMP snooping for multiple VLANs in a batch, run the [**igmp snooping enable**](cmdqueryname=igmp+snooping+enable) [ **vlan** { *vlan-id1* [ **to** *vlan-id2* ] } &<1-10> ] command in the system view.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```