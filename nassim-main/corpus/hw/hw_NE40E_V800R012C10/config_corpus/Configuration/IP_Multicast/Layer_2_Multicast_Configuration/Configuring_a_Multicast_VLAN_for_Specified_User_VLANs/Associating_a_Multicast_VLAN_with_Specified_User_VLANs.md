Associating a Multicast VLAN with Specified User VLANs
======================================================

If users in different VLANs need to receive the same multicast data flow, you can configure a multicast VLAN to manage the multicast source and multicast group members and save bandwidth.

#### Context

The multicast VLAN function involves two concepts: multicast VLAN and user VLAN.

* A multicast VLAN is the VLAN to which the interface connecting the Router to a multicast source belongs. A multicast VLAN is used to aggregate multicast flows. The system supports a maximum of 128 multicast VLANs.
* A user VLAN is a VLAN to which member hosts of a multicast group belong. A user VLAN is used to receive multicast flows from the multicast VLAN.
* A multicast VLAN can be associated with a maximum of 4093 user VLANs.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**vlan**](cmdqueryname=vlan) *vlan-id*
   
   
   
   The VLAN view is displayed.
3. Run [**igmp-snooping enable**](cmdqueryname=igmp-snooping+enable)
   
   
   
   IGMP snooping is enabled for the multicast VLAN.
4. Run [**multicast-vlan enable**](cmdqueryname=multicast-vlan+enable)
   
   
   
   The multicast VLAN function is enabled.
5. Run [**multicast-vlan user-vlan**](cmdqueryname=multicast-vlan+user-vlan) { { *vlan-id1* [ **to** *vlan-id2* ] } &<1-10> }
   
   
   
   The multicast VLAN is associated with the specified user VLANs.
   
   
   
   A multicast VLAN can be associated with multiple user VLANs, but a user VLAN can be associated with only one multicast VLAN.
6. (Optional) Run [**multicast-vlan igmp-querier-election user-vlan**](cmdqueryname=multicast-vlan+igmp-querier-election+user-vlan) { *vlan-id1* [ **to** *vlan-id2* ] } &<1-10>
   
   
   
   Querier election is enabled in the user VLAN.
   
   
   
   If two Routers are connected to the same user VLAN and the multicast VLAN function is enabled, the user VLAN will receive two copies of identical multicast data. To resolve this issue, enable the querier election function for the user VLAN. After querier election is configured for the user VLAN, the Router that fails in querier election deletes forwarding entries and does not create forwarding entries even if it receives Report messages from the user VLAN. In this case, the Router does not send multicast flows to the user VLAN.![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Before using this function, run the [**igmp-snooping send-query source-address**](cmdqueryname=igmp-snooping+send-query+source-address) command on each Router to configure a source IP address for Query messages sent by the querier.
7. (Optional) Run [**igmp-snooping send-query source-address**](cmdqueryname=igmp-snooping+send-query+source-address) *ip-source-address*
   
   
   
   The source IP address of IGMP Query messages sent by the device is configured.
   
   
   
   If the default source IP address of IGMP Query messages is in use, perform this step to change this source IP address. If the [**igmp-snooping send-query source-address**](cmdqueryname=igmp-snooping+send-query+source-address) command is run in both the system view and VLAN view, the configuration in the VLAN view preferentially takes effect.
8. (Optional) Run [**multicast-vlan send-query prune-source-port**](cmdqueryname=multicast-vlan+send-query+prune-source-port)
   
   
   
   The multicast VLAN is configured not to send received General Query messages back to the source interface through user VLANs.
   
   
   
   When the multicast VLAN and user VLANs are configured on the same interface, General Query messages are forwarded through this interface by default. The forwarding process does not change the source MAC address of the messages. Therefore, the upstream device learns the MAC entry with the MAC address of the interface as the source MAC address. If the upstream device has learned the source MAC address from another interface, MAC address flapping occurs on the device. To prevent this problem, perform this step.
9. Run [**port isolate-state exclude multicast**](cmdqueryname=port+isolate-state+exclude+multicast)
   
   
   
   The VLAN is configured not to isolate multicast traffic or multicast packets.
10. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.