Configuring an interface board-based Policy for Management and Service Plane Protection
=======================================================================================

An interface board-based policy for management and service
plane protection can be applied to an interface board to filter packets
of certain types.

#### Context

An interface board-based policy takes effect only on the
specified interface board.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ma-defend slot-policy**](cmdqueryname=ma-defend+slot-policy) *slot-policy-id*
   
   
   
   An interface
   board-based policy for management and service plane protection is
   created.
3. Run [**protocol**](cmdqueryname=protocol+bgp+ftp+isis+ldp+ospf+pimsm+rip+rsvp+snmp+ssh+telnet) { { **bgp** | **ftp** | **isis** | **ldp** | **ospf** | **pimsm** | **rip** | **rsvp** | **snmp** | **ssh** | **telnet** | **tftp** } | **ipv6** { **bgp4plus** | **ftp** | **ospfv3** | **ssh** | **telnet** | **pimsm** } } { **permit** | **deny** }
   
   
   
   The rule about whether to send the
   packets of specified protocols to the CPU is configured in the interface
   board-based policy.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If FTP, SSH, SNMP, TFTP, or TELNET is disabled globally by running
   the [**protocol**](cmdqueryname=protocol) command and is not enabled on any active interface, connectivity
   to the device will be interrupted. (An active interface is an interface
   that can properly receive and send packets.)
   
   To ensure connectivity to the device, configure additional active
   interfaces and enable these protocols on them.
4. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
5. Run [**slot**](cmdqueryname=slot) *slot-id*
   
   
   
   The slot view is displayed.
6. Run [**ma-defend-slot**](cmdqueryname=ma-defend-slot) *slot-policy-id*
   
   
   
   The configured interface
   board-based policy is applied to the interface board in the slot.
7. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is
   committed.