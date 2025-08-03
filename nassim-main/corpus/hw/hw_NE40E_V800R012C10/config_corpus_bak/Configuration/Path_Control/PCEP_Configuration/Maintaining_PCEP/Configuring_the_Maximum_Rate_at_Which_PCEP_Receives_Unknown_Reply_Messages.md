Configuring the Maximum Rate at Which PCEP Receives Unknown Reply Messages
==========================================================================

To improve PCEP session reliability, configure the maximum rate at which PCEP receives unknown reply messages.

#### Context

PCEP involves two PCE roles â PCE server and PCE client. The PCE server computes paths, and the PCE client initiates path computation requests. Each PCReq message (path computation request) sent by the PCE client carries an ID, and the PCRep message (path computation result) replied by the PCE server also carries an ID. If the two IDs are different, the PCRep message is considered an unknown reply message. If the actual rate at which the PCE client receives unknown reply messages is greater than a specified value, the PCE client considers the PCE server faulty and terminates the PCEP session.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**pce-client**](cmdqueryname=pce-client)
   
   
   
   The PCE client view is displayed.
3. Run [**pcep max-unknown-replies**](cmdqueryname=pcep+max-unknown-replies)*max-unknown-replies-value*
   
   
   
   The maximum rate at which the PCE client receives unknown reply messages is configured.
   
   
   
   By default, a PCE client does not terminate the PCEP session after receiving an unknown reply message.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.