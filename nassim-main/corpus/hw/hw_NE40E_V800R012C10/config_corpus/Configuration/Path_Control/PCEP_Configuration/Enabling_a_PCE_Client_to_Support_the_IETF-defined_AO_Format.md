Enabling a PCE Client to Support the IETF-defined AO Format
===========================================================

A PCE client can be enabled to support the IETF-defined association object (AO) format.

#### Usage Scenario

A PCE server and a PCE client run PCEP to communicate. PCEP defines multiple objects to be encoded and decoded at both ends of a PCEP session. Although AOs are a type of PCEP object, PCEP does not support AO encoding or decoding. To address this issue, run the [**association-type enable**](cmdqueryname=association-type+enable) command to enable a PCE client to support the IETF-defined AO format.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**pce-client**](cmdqueryname=pce-client)
   
   
   
   The PCE client view is displayed.
3. Run [**association-type enable**](cmdqueryname=association-type+enable)
   
   
   
   The PCE client is enabled to support the IETF-defined AO format.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.