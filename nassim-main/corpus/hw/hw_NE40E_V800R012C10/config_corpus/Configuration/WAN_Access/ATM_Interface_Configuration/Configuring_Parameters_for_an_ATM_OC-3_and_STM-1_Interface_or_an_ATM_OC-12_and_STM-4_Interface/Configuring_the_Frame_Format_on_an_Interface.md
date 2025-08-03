Configuring the Frame Format on an Interface
============================================

ATM interfaces complying with different standards need to be configured with different frame formats.

#### Context

Perform the following steps on the Router:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**slot**](cmdqueryname=slot) *slot-id*
   
   
   
   The slot view is displayed.
3. Run [**frame-format**](cmdqueryname=frame-format) { **sdh** |**sonet** **card**  *cardid* }
   
   
   
   The frame format is configured.
   
   For an ATM STM-1 optical interface, the frame format is SDH; for an ATM OC-3 interface, the frame format is SONET.
   
   By default, the SDH frame format is used.