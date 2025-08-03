Checking Statistics About Downstream Layer 3 IPv4 Multicast Packets
===================================================================

You can check statistics about downstream Layer 3 IPv4 multicast packets to diagnose multicast traffic faults on a device.

#### Context

If multicast traffic is discarded, you can check statistics about downstream Layer 3 IPv4 multicast packets and determine the device that discarded the traffic. Before checking statistics about downstream Layer 3 IPv4 multicast packets, enable a device to collect statistics about downstream Layer 3 IPv4 multicast packets. To enable a device to collect statistics about downstream Layer 3 IPv4 multicast packets based on a multicast source and group, run the **multicast egress statistics** command. To enable a device to collect statistics about downstream Layer 3 IPv4 multicast packets based on a slot, run the **multicast egress statistics enable** command. You can diagnose faults by clearing and checking statistics about downstream Layer 3 IPv4 multicast packets.


#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. Run either of the following commands:
   
   
   * To enable the device to collect statistics about downstream Layer 3 IPv4 multicast packets based on a multicast source and group, run the [**multicast egress statistics**](cmdqueryname=multicast+egress+statistics) [ **vpn-instance** *vpn-instance-name* ] *source-address* *group-address* **slot** *slot-id* command.
   * To enable the device to collect statistics about downstream Layer 3 IPv4 multicast packets based on a slot, run the [**multicast egress statistics enable**](cmdqueryname=multicast+egress+statistics+enable) **slot** *slot-id* command. This command is supported only by the admin VS.
3. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
4. Run the [**display multicast egress statistics**](cmdqueryname=display+multicast+egress+statistics) [ **vpn-instance** *vpn-instance-name* ] *source-address* *group-address* **slot** *slot-id* or [**display multicast egress statistics**](cmdqueryname=display+multicast+egress+statistics) **slot** *slot-id* command to check statistics about downstream Layer 3 IPv4 multicast packets.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * During fault diagnosis, you may need to clear the existing statistics about downstream Layer 3 IPv4 multicast packets and then check the new statistics about downstream Layer 3 IPv4 multicast packets. To clear statistics about downstream Layer 3 IPv4 multicast packets, run the [**reset multicast egress statistics**](cmdqueryname=reset+multicast+egress+statistics) [ **vpn-instance** *vpn-instance-name* ] *source-source* *group-address* **slot** *slot-id* or [**reset multicast egress statistics**](cmdqueryname=reset+multicast+egress+statistics) **slot** *slot-id* **all** command. You can run the preceding commands repeatedly as required.
   * The [**display multicast egress statistics**](cmdqueryname=display+multicast+egress+statistics) **slot** *slot-id* and [**reset multicast egress statistics**](cmdqueryname=reset+multicast+egress+statistics) **slot** *slot-id* **all** commands are supported only by the admin VS.