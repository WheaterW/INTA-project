Configuring the Interface Bound to GRE
======================================

A GRE tunnel's source interface or the interface where the source address of a GRE tunnel resides must be bound to GRE. The GRE tunnel can use these interfaces to transmit GRE-encapsulated packets only after these interfaces are bound to GRE.

#### Context

Perform the following steps on the endpoint Routers of a tunnel.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number*
   
   
   
   The interface view is displayed.
3. Run [**ipv6 enable**](cmdqueryname=ipv6+enable)
   
   
   
   IPv6 is enabled on the interface.
4. Run [**ipv6 address**](cmdqueryname=ipv6+address) { *ipv6-address* *prefix-length* | *ipv6-address*/*prefix-length* }
   
   
   
   An IPv6 address is configured for the interface.
5. (Optional) Run [**target-board**](cmdqueryname=target-board) *slot-number* [ **backup** *slave-slot-number* ]
   
   
   
   The mapping from the tunnel source interface to the tunnel service board is configured.
   
   
   
   If the tunnel interface used by GRE is named in the format of slot ID/subcard ID/interface ID, this command must be run before GRE is bound to the interface using the [**binding tunnel gre**](cmdqueryname=binding+tunnel+gre) command. After the configuration is complete, the tunnel sends packets received from the source tunnel interface to the corresponding tunnel service board for processing. If the command is not run, the GRE tunnel interface must be named by interface ID.
   
   If a device is equipped with multiple tunnel service boards, the **backup** *slave-slot-number* parameter can be configured to specify a standby GRE tunnel service board for 1:1 protection, thereby enhancing GRE service reliability. After 1:1 protection is configured for GRE tunnel service boards, configure two GRE tunnels with the same source and same destination on the active and standby GRE tunnel service boards. When the tunnel on the active tunnel service board works, the GRE tunnel on the standby tunnel service board does not work. If the GRE tunnel on the active tunnel service board fails, services are switched to the standby tunnel service board.
6. Run [**binding tunnel gre**](cmdqueryname=binding+tunnel+gre)
   
   
   
   The interface is bound to GRE.
7. Run [**quit**](cmdqueryname=quit)
   
   
   
   Exit the interface view.
8. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.