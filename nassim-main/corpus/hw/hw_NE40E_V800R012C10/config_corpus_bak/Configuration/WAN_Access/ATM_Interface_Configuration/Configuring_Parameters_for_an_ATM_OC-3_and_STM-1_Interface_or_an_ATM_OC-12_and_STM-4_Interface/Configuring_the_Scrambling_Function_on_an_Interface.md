Configuring the Scrambling Function on an Interface
===================================================

Configuring the scrambling function effectively prevents consecutive 0s or 1s in ATM cells.

#### Context

The scrambling function can effectively prevent continuous 0s or 1s in ATM cells.

Configurations of the scrambling function on the local and remote interfaces must be consistent.

Perform the following steps on the Router:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface atm**](cmdqueryname=interface+atm) *interface-number*
   
   
   
   The ATM interface view is displayed.
3. Run [**scramble**](cmdqueryname=scramble)
   
   
   
   The scrambling function is configured.
   
   This function is valid only for payloads and does not affect cell headers.