(Optional) Configuring a Switching Delay for PW Switching
=========================================================

When a switching delay is configured for a PW, the master PW fails, the traffic switches to the slave PW after the delay period expires.

#### Usage Scenario

In a VPWS with the master/slave PW redundancy mode, if the master PW fails, traffic immediately switches to the slave PW. If the master PW flaps or an error occurs in the detection mechanism, traffic frequently switches between the master and slave PWs. To prevent this problem in a VPWS with the master/slave PW redundancy mode, configure a switching delay for the PW switching. When the master PW fails, the traffic switches to the slave PW after the delay period expires.

#### Prerequisites

The PW redundancy is in master/slave mode.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view of an AC interface is displayed.
3. Run [**mpls l2vpn holdoff**](cmdqueryname=mpls+l2vpn+holdoff) *holdoffTime*
   
   
   
   A switching delay is configured for the PW switching
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.