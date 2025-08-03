Configuring an I-VSI and a B-VSI
================================

An I-VSI can be bound to a B-VSI only after their B-MAC addresses and the I-VSI's I-tag are configured.

#### Procedure

* Configure an I-VSI.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**vsi**](cmdqueryname=vsi) *vsi-name*
     
     
     
     The I-VSI view is displayed.
  3. Run [**pbb i-tag**](cmdqueryname=pbb+i-tag) *i-tag*
     
     
     
     An I-tag is configured.
     
     
     
     An I-tag is a field in the MAC header of a public network packet and applies only to an I-VSI. The I-VSIs on the endpoint PEs of a VPLS PW must have the same I-tag, and this I-tag must be unique on the entire network.
  4. Run [**pbb backbone-source-mac**](cmdqueryname=pbb+backbone-source-mac) *source-mac-address*
     
     
     
     A B-SMAC address is configured.
     
     
     
     + The B-SMAC address is a virtual MAC address.
     + The B-SMAC and B-DMAC addresses in an I-VSI must be different.
     + A B-SMAC address can be configured in either an I-VSI or a B-VSI. If an I-VSI and the B-VSI to which the I-VSI is bound have different B-SMAC addresses, the B-SMAC address configured in the I-VSI takes effect.
     + In scenarios where multiple paths exist between two PEs and multiple I-VSIs are bound to a B-VSI, to implement load balancing, ensure that at least one I-VSI has a B-SMAC address configured. In addition, the B-SMAC addresses configured in different I-VSIs must be different.![](../../../../public_sys-resources/note_3.0-en-us.png) 
       
       In local PBB VPLS, the B-SMAC and B-DMAC addresses must be configured in the I-VSIs and one I-VSI's B-DMAC address must be the same as the other I-VSI's B-SMAC address.
  5. Run [**pbb backbone-destination-mac**](cmdqueryname=pbb+backbone-destination-mac) *destination-mac-address* **static**
     
     
     
     A B-DMAC address is configured.
     
     
     
     + The B-DMAC address is a virtual MAC address.
     + A B-DMAC address can be configured only in an I-VSI, and must be the same as the B-SMAC address configured on the remote end.
  6. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure a B-VSI.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**vsi**](cmdqueryname=vsi) *vsi-name*
     
     
     
     The B-VSI view is displayed.
  3. Run [**pbb backbone-source-mac**](cmdqueryname=pbb+backbone-source-mac) *source-mac-address*
     
     
     
     A B-SMAC address is configured.
     
     
     
     + The B-SMAC address is a virtual MAC address.
     + A B-SMAC address can be configured in either an I-VSI or a B-VSI. If an I-VSI and the B-VSI to which the I-VSI is bound have different B-SMAC addresses, the B-SMAC address configured in the I-VSI takes effect.
     + In scenarios where multiple paths exist between two PEs and multiple I-VSIs are bound to a B-VSI, to implement load balancing, ensure that at least one I-VSI has a B-SMAC address configured. In addition, the B-SMAC addresses configured in different I-VSIs must be different.
  4. (Optional) Run [**pbb mac-withdraw mac-opt-compatible**](cmdqueryname=pbb+mac-withdraw+mac-opt-compatible)
     
     
     
     The B-VSI is configured to send MAC Withdraw messages that carry the 0x406 TLV.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.