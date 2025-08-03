Disabling Fast DCN Session Restart Triggered by DCN PPPoE Terminate Packets
===========================================================================

Disabling fast DCN session restart triggered by DCN PPPoE Terminate packets prevents such packets from being used to launch an attack, which improves device reliability.

#### Background

DCN PPPoE Terminate packets are used to instruct a peer end to fast restart a DCN session. Due to the lack of an authentication mechanism in DCN, if DCN PPPoE Terminate packets are used to launch an attack, devices fail to be managed by the NMS. To address this problem, disable fast DCN session restart triggered by DCN PPPoE Terminate packets.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**dcn**](cmdqueryname=dcn)
   
   
   
   The DCN view is displayed.
3. Run [**fast-terminate disable**](cmdqueryname=fast-terminate+disable)
   
   
   
   Fast DCN session restart triggered by DCN PPPoE Terminate packets is disabled.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.