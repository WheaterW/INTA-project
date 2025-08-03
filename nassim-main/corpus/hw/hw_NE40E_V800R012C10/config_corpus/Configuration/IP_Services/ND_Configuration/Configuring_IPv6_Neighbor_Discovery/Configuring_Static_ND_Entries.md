Configuring Static ND Entries
=============================

You can obtain the mappings between IPv6 and MAC addresses of neighbors after configuring static ND entries. ND entries indicate the mappings between IPv6 and MAC addresses. If a device is not enabled to send ND messages, it cannot obtain ND entries. To enable such a device to obtain ND entries, configure static ND on the device.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The view of the interface on which static ND entries need to be configured.
3. Run [**ipv6 enable**](cmdqueryname=ipv6+enable)
   
   
   
   IPv6 is enabled.
4. Run any of the following commands:
   
   
   * To configure static ND entries on a common Layer 3 interface, run the [**ipv6 neighbor**](cmdqueryname=ipv6+neighbor) *ipv6-address* *mac-address* command.
   * To configure static ND entries on a VLANIF interface, run the [**ipv6 neighbor**](cmdqueryname=ipv6+neighbor) *ipv6-address* *mac-address* **vid** *vlan-id* *interface-type* *interface-number* command.
   * To configure static ND entries on a QinQ or dot1q VLAN tag termination sub-interface, run the [**ipv6 neighbor**](cmdqueryname=ipv6+neighbor) *ipv6-address* *mac-address* **vid** *vid* [ **cevid** *cevid* ] command.![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   After the function of sending ND protocol packets is enabled on a device, a common interface like a GE interface either automatically sends multicast NS messages to learn ND entries actively or respond to NS messages to learn ND entries passively. However, a VLAN tag termination sub-interface cannot send multicast NS messages but discards the multicast NS messages instead. Therefore, to enable a VLAN tag termination sub-interface to send multicast NS messages, run the [**ipv6 nd ns multicast-enable**](cmdqueryname=ipv6+nd+ns+multicast-enable) command on the sub-interface. This configuration enables the sub-interface to learn ND entries.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.