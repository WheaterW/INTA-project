Configuring a Remote CEP Service
================================

TDMoPSN supports the establishment of SVC and PWE3 PWs to transmit CEP services.

#### Context

At the edge of a PSN, PE1 on the user side is connected downstream to CE1, and PE2 on the network side is connected to upstream CE2. Both PEs require the following configurations, whereas devices inside the PSN do not.

The following PW types are supported:

* SVC
* PWE3

Referring to the configuration of a PW, take the dynamic PWE3 as an example.

The procedures for configuring the preceding parameters in the two views are as follows:


#### Procedure

* Create a PW in the PW template view.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**mpls l2vpn**](cmdqueryname=mpls+l2vpn)
     
     
     
     MPLS L2VPN is enabled.
  3. Run [**pw-template**](cmdqueryname=pw-template) *pwname*
     
     
     
     A PW template is created and the PW template view is displayed.
  4. Run [**peer-address**](cmdqueryname=peer-address) *ip-address*
     
     
     
     An IP address is assigned to the peer PE of the PW.
  5. Run [**tnl-policy**](cmdqueryname=tnl-policy) *tnlPolicyName*
     
     
     
     A policy is configured for the PW template to select tunnels.
  6. (Optional) Run [**jitter-buffer depth**](cmdqueryname=jitter-buffer+depth) *depth*
     
     
     
     The depth of the jitter buffer is set.
  7. (Optional) Run [**rtp-header**](cmdqueryname=rtp-header)
     
     
     
     The RTP header carried in the TDM transparent transmission encapsulation is configured.
  8. Run [**quit**](cmdqueryname=quit)
     
     
     
     Exit from the PW template view.
  9. Run [**controller cpos**](cmdqueryname=controller+cpos) *cpos-number*
     
     
     
     The CPOS interface view is displayed.
  10. Run [**using vc4**](cmdqueryname=using+vc4)
      
      
      
      The CPOS interface is configured to work in clear channel mode, and a synchronous serial interface is created on the CPOS interface.
  11. Run [**interface**](cmdqueryname=interface) **serial**
      
      
      
      The Serial interface view created in is displayed.
  12. Run [**mpls l2vc**](cmdqueryname=mpls+l2vc) { *ip-address* | **pw-template** *template-name* } \* *vc-id* [ [ **control-word** | **no-control-word** ] | **tunnel-policy** *policy-name* [ { **endpoint** *endpoint-address* | [ **endpoint** *endpoint4-address* ] } **color** *color-value* ] | [ **ip-interworking** | **ip-layer2** ] | [ **secondary** | **bypass** ] | **ignore-standby-state** | **tdm-encapsulation-number** *number* | **tdm-sequence-number** | **jitter-buffer** *depth* | **rtp-header** | **idle-code** *idle-code-value* ] \*
      
      
      
      A dynamic PW is created.
  13. (Optional) Run [**trap-threshold**](cmdqueryname=trap-threshold) { **ces-jtrovr-exc** | **ces-jtrudr-exc** | **ces-lospkt-exc** | **ces-malpkt-exc** | **ces-misorderpkt-exc** | **ces-straypkt-exc** } **trigger-threshold** *trigger-threshold-value* **resume-threshold** *resume-threshold-value*
      
      
      
      The alarm and clear alarm thresholds of CES service performance are set.
  14. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
* Creating a PW in the interface view
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**mpls l2vpn**](cmdqueryname=mpls+l2vpn)
     
     
     
     MPLS L2VPN is enabled.
  3. Run [**controller cpos**](cmdqueryname=controller+cpos) *cpos-number*
     
     
     
     The CPOS interface view is displayed.
  4. Run [**using vc4**](cmdqueryname=using+vc4)
     
     
     
     The CPOS interface is configured to work in clear channel mode, and a synchronous serial interface is created on the CPOS interface.
  5. Run [**interface**](cmdqueryname=interface) **serial**
     
     
     
     The Serial interface view created in is displayed.
  6. Run [**mpls l2vc**](cmdqueryname=mpls+l2vc) { *ip-address* | **pw-template** *pw-template-name* } \* *vc-id* [ **tunnel-policy** *policy-name* [ { **endpoint** *endpoint-address* | [ **endpoint** *endpoint4-address* ] } **color** *color-value* ] | [ **control-word** | **no-control-word** ] | [ **jitter-buffer** *depth* ] | [ **tdm-encapsulation** *number* ] | [ **tdm-sequence-number** ] | [ **idle-code** *idle-code-value* ] | **rtp-header** | **ignore-standby-state** ] \*
     
     
     
     A dynamic PW is created.
  7. (Optional) Run [**trap-threshold**](cmdqueryname=trap-threshold) { **ces-jtrovr-exc** | **ces-jtrudr-exc** | **ces-lospkt-exc** | **ces-malpkt-exc** | **ces-misorderpkt-exc** | **ces-straypkt-exc** } **trigger-threshold** *trigger-threshold-value* **resume-threshold** *resume-threshold-value*
     
     
     
     The alarm and clear alarm thresholds of CES service performance are set.
  8. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.