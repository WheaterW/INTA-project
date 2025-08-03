Configuring Bit-Error-Triggered PW Switching
============================================

This section describes how to configure bit-error-triggered pseudo wire (PW) switching. This function helps minimize the impact of bit errors on L2VPN services when bit-error-triggered RSVP-TE tunnel switching fails to remove bit errors.

#### Usage Scenario

In a scenario where an RSVP-TE tunnel carries L2VPN services under PW redundancy protection, you can configure bit-error-triggered PW switching in addition to bit-error-triggered RSVP-TE tunnel switching. If the primary and backup constraint-based routed label switched paths (CR-LSPs) of the RSVP-TE tunnel are both in the excessive bit error rate (BER) state or the TE hot standby protection fails and bit-error-triggered RSVP-TE tunnel switching cannot protect services against bit errors, bit-error-triggered PW switching can do so.

The principles for bit-error-triggered PW switching are as follows:

* If the RSVP-TE tunnel carrying the primary PW enters the excessive BER state but the RSVP-TE tunnel carrying the secondary PW is in the normalized BER state, traffic switches to the secondary PW.
* If the RSVP-TE tunnel carrying the primary PW enters the normalized BER state, traffic switches back to the primary PW.
* If the RSVP-TE tunnels carrying the primary and secondary PWs are both in the excessive BER state, traffic travels along the primary PW.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

The bit error status of the RSVP-TE tunnel carrying the PW refers to the bit error status of the CR-LSP that transmits traffic in the tunnel.

A PW can be either a single-segment PW (SS-PW) or a multi-segment PW (MS-PW):

* For an SS-PW, bit-error-triggered protection switching is enabled on endpoint provider edges (PEs).
* For an MS-PW, bit-error-triggered protection switching is enabled on both endpoint PEs and intermediate superstratum provider edges (SPEs).



#### Pre-configuration Tasks

Before configuring bit-error-triggered PW switching, complete the following tasks:

* Configure PW redundancy.
* [Configure bit-error-triggered RSVP-TE tunnel switching.](dc_vrp_cfg_error-code_000007.html)

#### Procedure

* Enable bit-error-triggered protection switching for an SS-PW. The following steps must be performed on both endpoint PEs.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number*
     
     
     
     The attachment circuit (AC) interface view is displayed.
  3. Run [**mpls l2vpn pw bit-error-detection**](cmdqueryname=mpls+l2vpn+pw+bit-error-detection)
     
     
     
     Bit-error-triggered PW switching is enabled.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Enable bit-error-triggered protection switching for an MS-PW.
  1. Configure each PE.
     
     
     1. Run [**system-view**](cmdqueryname=system-view)
        
        The system view is displayed.
     2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number*
        
        The AC interface view is displayed.
     3. Run [**mpls l2vpn pw bit-error-detection**](cmdqueryname=mpls+l2vpn+pw+bit-error-detection)
        
        Bit-error-triggered PW switching is enabled.
     4. Run [**commit**](cmdqueryname=commit)
        
        The configuration is committed.
  2. Configure each SPE.
     
     
     1. Run [**system-view**](cmdqueryname=system-view)
        
        The system view is displayed.
     2. Run [**mpls switch-l2vc**](cmdqueryname=mpls+switch-l2vc) *ip-address* *vc-id* **between** *ip-address* *vc-id* **encapsulation** *encapsulation-type* **bit-error-detection**
        
        Bit-error-triggered PW switching is enabled.
     3. Run [**commit**](cmdqueryname=commit)
        
        The configuration is committed.