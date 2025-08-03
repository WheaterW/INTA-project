Configuring the Strict MACsec Mode
==================================

Configuring_the_Strict_MACsec_Mode

#### Context

By default, if MACsec negotiation fails, traffic is still forwarded, and data packets are not encrypted. This poses security risks in scenarios that require high data confidentiality. To address this issue, configure the strict MACsec mode on a device, allowing it to discard all packets except MKA, LLDP, and Pause packets if MACsec negotiation fails.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**macsec strict-mode**](cmdqueryname=macsec+strict-mode)
   
   
   
   The strict MACsec mode is configured.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.