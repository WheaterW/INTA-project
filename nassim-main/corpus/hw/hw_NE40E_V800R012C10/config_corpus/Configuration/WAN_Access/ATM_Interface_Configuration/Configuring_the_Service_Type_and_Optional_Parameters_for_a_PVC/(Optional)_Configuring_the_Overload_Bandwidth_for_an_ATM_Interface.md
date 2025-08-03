(Optional) Configuring the Overload Bandwidth for an ATM Interface
==================================================================

The overhead bandwidth of an ATM interface refers to the sum of committed bandwidth of all PVCs and PVPs on the interface.

#### Context

Perform the following steps on the Router:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface atm**](cmdqueryname=interface+atm) *interface-number*
   
   
   
   The ATM interface view is displayed.
3. Run [**service bandwidth-overload**](cmdqueryname=service+bandwidth-overload) *overload-value*
   
   
   
   The overload bandwidth is configured for an ATM interface.
   
   You can run the [**service bandwidth-overload**](cmdqueryname=service+bandwidth-overload) command to set the overload bandwidth of the PVCs and PVPs of all services on the ATM interface.