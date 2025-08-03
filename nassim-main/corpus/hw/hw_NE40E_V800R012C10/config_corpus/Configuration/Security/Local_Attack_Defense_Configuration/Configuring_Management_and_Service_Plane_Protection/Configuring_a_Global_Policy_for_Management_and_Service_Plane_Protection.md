Configuring a Global Policy for Management and Service Plane Protection
=======================================================================

A global policy for management and service plane protection
can be applied to the entire device to filter packets of certain types.

#### Context

Perform the following steps on the device.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ma-defend global-policy**](cmdqueryname=ma-defend+global-policy)
   
   
   
   A global policy for management and service plane
   protection is created.
3. Run [**protocol**](cmdqueryname=protocol+bgp+ftp+isis+ldp+ospf+pimsm+rip+rsvp+snmp+ssh+telnet) { { **bgp** | **ftp** | **isis** | **ldp** | **ospf** | **pimsm** | **rip** | **rsvp** | **snmp** | **ssh** | **telnet** | **tftp** } | **ipv6** { **bgp4plus** | **ftp** | **ospfv3** | **ssh** | **telnet** | **pimsm** } } { **permit** | **deny** }
   
   
   
   A rule about whether to send the
   packets of specified protocols to the CPU is configured in the global
   policy.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If FTP, SSH, SNMP, TFTP, or TELNET is disabled globally by running
   the [**protocol**](cmdqueryname=protocol) command and is not enabled on any active interface, connectivity
   to the device will be interrupted. (An active interface is an interface
   that can properly receive and send packets.)
   
   To ensure connectivity to the device, configure additional active
   interfaces and enable these protocols on them.
4. Run [**enable**](cmdqueryname=enable)
   
   
   
   The global policy is
   enabled.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is
   committed.