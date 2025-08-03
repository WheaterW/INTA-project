Configuring LPT
===============

LPT detects and reports link faults on the Ethernet user side or faults on an intermediate point-to-point network.

#### Context

LPT enables a device to send fault information of the local link to the peer network edge device through an LPT packet. The peer network edge device closes the user-side interface so that the peer user device detects the fault and starts the backup link. The two user devices communicate using the backup link.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**lpt ptp interface**](cmdqueryname=lpt+ptp+interface) { *interface-name* | *interface-type* *interface-number* }
   
   
   
   A point-to-point LPT root interface is created, and the LPT root interface view is displayed.
3. Run [**lpt enable**](cmdqueryname=lpt+enable)
   
   
   
   LPT is enabled.
4. Run [**lpt holdoff-time**](cmdqueryname=lpt+holdoff-time) *time*
   
   
   
   An interface hold-off time is configured for the LPT instance.
5. Run [**lpt oam-period**](cmdqueryname=lpt+oam-period) *time*
   
   
   
   An OAM detection period is configured for the LPT instance.
6. Run [**lpt recovery-time**](cmdqueryname=lpt+recovery-time) *time*
   
   
   
   A fault recovery period is configured for the LPT instance.
7. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.