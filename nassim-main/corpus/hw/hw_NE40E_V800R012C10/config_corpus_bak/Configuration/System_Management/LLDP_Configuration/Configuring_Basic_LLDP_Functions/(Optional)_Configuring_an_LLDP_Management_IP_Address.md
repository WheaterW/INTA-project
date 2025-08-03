(Optional) Configuring an LLDP Management IP Address
====================================================

This section describes how to configure an LLDP management IP address, so that an NMS can identify a device based on this management address to detect network topologies.

Carried in the Management Address TLV field in LLDP packets, the LLDP management IP address is used by the NMS to identify a device and helps the NMS to detect network topologies, which facilitates network management.

In non-interface mode, the LLDP management IP address is selected based on the following rules:

1. If an LLDP management IP address is configured using the [**lldp management-address**](cmdqueryname=lldp+management-address) command, the LLDP management IP address has the highest priority and is preferentially used.
2. If neither an LLDP management IP address is configured using the [**lldp management-address**](cmdqueryname=lldp+management-address) command nor the final LLDP management IP address is bound to an interface, the device searches the IP address list for an IP address as the LLDP management IP address. If no default IP address is available, the device uses its bridge MAC address as the LLDP management address.![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The device searches IP addresses of the following interfaces in sequence for the LLDP management IP address: loopback interface, management network interface, and VLANIF interface. For the same type of interfaces, the device selects the smallest IP address as the LLDP management IP address.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**lldp management-address**](cmdqueryname=lldp+management-address) *ip-address*
   
   
   
   The LLDP management IP address is configured.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.