Verifying the PBB VPLS Configuration
====================================

After configuring PBB VPLS, check the configurations, including
the B-SMAC address, B-DMAC address, and VSI information.

#### Procedure

* Run the [**display pbb backbone-source-mac**](cmdqueryname=display+pbb+backbone-source-mac) [ *source-mac-address* ] command to check
  B-SMAC addresses.
* Run the [**display pbb
  backbone-destination-mac**](cmdqueryname=display+pbb+backbone-destination-mac) [ *destination-mac-address* ] command to check B-DMAC addresses.
* Run the [**display b-vsi binding**](cmdqueryname=display+b-vsi+binding) [ *vsi-name* ] command to check I-VSIs bound to a specified B-VSI.