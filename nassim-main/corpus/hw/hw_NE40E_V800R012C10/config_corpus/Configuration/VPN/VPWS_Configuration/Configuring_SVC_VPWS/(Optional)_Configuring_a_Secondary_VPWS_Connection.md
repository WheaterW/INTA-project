(Optional) Configuring a Secondary VPWS Connection
==================================================

This section describes how to configure a secondary VPWS connection for VLL FRR, so that L2VPN traffic can be quickly switched to the backup path if the primary path fails. After the primary path recovers, the L2VPN traffic can be switched back to it according to the revertive switching policy.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**mpls l2vpn**](cmdqueryname=mpls+l2vpn)
   
   
   
   MPLS L2VPN is enabled.
3. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
4. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number* [ .*subinterface-number* ]
   
   
   
   The AC interface view is displayed.
5. Run one of the following commands to create a secondary VPWS connection according to the interface type:
   
   
   * Ethernet interface:
     
     [**mpls static-l2vc**](cmdqueryname=mpls+static-l2vc) { { **destination** *ip-address* | **pw-template** *pw-template-name* *vc-id* } \* | **destination** *ip-address* [ *vc-id* ] } **transmit-vpn-label** *transmit-label-value* **receive-vpn-label** *receive-label-value* [ **tunnel-policy** *tnl-policy-name* [ { **endpoint** *endpoint-address* | [ **endpoint** *endpoint4-address* ] } **color** *color-value* ] | **access-port** | [ **control-word** | **no-control-word** ] | [ **raw** | **tagged** ] | **secondary** ] \*
   * PPP/HDLC interface:
     
     [**mpls static-l2vc**](cmdqueryname=mpls+static-l2vc) { { **destination** *ip-address* | **pw-template** *pw-template-name* *vc-id* } \* | **destination** *ip-address* [ *vc-id* ] } **transmit-vpn-label** *transmit-label-value* **receive-vpn-label** *receive-label-value* [ **tunnel-policy** *tnl-policy-name* [ { **endpoint** *endpoint-address* | [ **endpoint** *endpoint4-address* ] } **color** *color-value* ] | **access-port** | [ **control-word** | **no-control-word** ] | [ **raw** | **tagged** ] | **secondary** ] \*
   * ATM interface:
     
     [**mpls static-l2vc**](cmdqueryname=mpls+static-l2vc) { { **destination** *ip-address* | **pw-template** *pw-template-name* *vc-id* } \* | **destination** *ip-address* [ *vc-id* ] } **transmit-vpn-label** *transmit-label-value* **receive-vpn-label** *receive-label-value* [ **tunnel-policy** *tnl-policy-name* | **access-port** | [ **control-word** | **no-control-word** ] | [ **max-atm-cells** *cells-value* ] | [ **atm-pack-overtime** *time* ] | **secondary** ] \*
   * TDM interface:
     
     [**mpls static-l2vc**](cmdqueryname=mpls+static-l2vc) { { **destination** *ip-address* | **pw-template** *pw-template-name* *vc-id* } \* | **destination** *ip-address* [ *vc-id* ] } **transmit-vpn-label** *transmit-label-value* **receive-vpn-label** *receive-label-value* [ **tunnel-policy** *tnl-policy-name* | **access-port** | [ **control-word** | **no-control-word** ] | [ **jitter-buffer** *depth* ] | [ **tdm-encapsulation** *number* ] | [ **tdm-sequence-number** ] | [ **idle-code** *idle-code-value* ] | [ **rtp-header** ] | **secondary** ] \*
   
   
   
   When configuring a secondary VPWS PW, ensure that the parameter settings for the primary, secondary, and bypass PWs are consistent. Parameter setting inconsistencies may result in the secondary or bypass PW failing to take over traffic if the primary PW fails.
6. (Optional) Run [**mpls l2vpn service-name**](cmdqueryname=mpls+l2vpn+service-name) *service-name*
   
   
   
   An L2VPN service name is specified. The L2VPN service can then be maintained through an NMS based on the specified name.
7. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.