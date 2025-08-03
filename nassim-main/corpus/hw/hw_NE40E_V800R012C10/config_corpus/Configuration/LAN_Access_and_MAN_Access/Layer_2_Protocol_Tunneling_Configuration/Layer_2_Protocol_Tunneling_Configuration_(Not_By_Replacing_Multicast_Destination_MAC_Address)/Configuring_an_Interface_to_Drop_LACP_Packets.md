Configuring an Interface to Drop LACP Packets
=============================================

On a VLL network, a main interface bound to a VLL can be configured to drop LACP packets.

#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. Run the [**interface**](cmdqueryname=interface) *interface-type interface-number* command to enter the AC interface view.
3. Run the [**link-protocol discard lacp**](cmdqueryname=link-protocol+discard+lacp) command to configure the interface bound to a VLL to drop LACP packets.
4. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.