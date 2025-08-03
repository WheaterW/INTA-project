Configuring the Scrambling Function for a POS Interface
=======================================================

POS interfaces support the scrambling function for the payload data to avoid excessive consecutive 1s or 0s, which helps the receiver extract line clock signals.

#### Context

The scrambling function must be enabled on both of the directly connected interfaces.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface pos**](cmdqueryname=interface+pos) *interface-number*
   
   
   
   The POS interface view is displayed.
3. Run [**scramble**](cmdqueryname=scramble)
   
   
   
   The scrambling function of the payload is enabled for the POS interface.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.