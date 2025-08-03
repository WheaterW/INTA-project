Configuring a VPWS PW
=====================

Before configuring a static PW, you must specify the VC label. Configuring a dynamic PW does not require this operation.

#### Context

Perform the following configurations on the endpoint PEs of a PW.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**mpls l2vpn**](cmdqueryname=mpls+l2vpn)
   
   
   
   MPLS L2VPN is configured.
3. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
4. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number* [ .*subinterface-number* ]
   
   
   
   The AC interface view is displayed.
5. (Optional) Run [**mpls l2vpn description**](cmdqueryname=mpls+l2vpn+description) *description-text*
   
   
   
   An L2VPN description is configured for the AC interface.
6. (Optional) Run [**mpls l2vpn pw performance disable**](cmdqueryname=mpls+l2vpn+pw+performance+disable)
   
   
   
   PW performance statistics collection is disabled.
7. Run one of the following commands to create a VPWS connection according to the interface type:
   
   
   * Ethernet interface:
     
     [**mpls static-l2vc**](cmdqueryname=mpls+static-l2vc) { { **destination** *ip-address* | **pw-template** *pw-template-name* *vc-id* } \* | **destination** *ip-address* [ *vc-id* ] } **transmit-vpn-label** *transmit-label-value* **receive-vpn-label** *receive-label-value* [ **tunnel-policy** *tnl-policy-name* [ { **endpoint** *endpoint-address* | [ **endpoint** *endpoint4-address* ] } **color** *color-value* ] | **access-port** | [ **control-word** | **no-control-word** ] | [ **raw** | **tagged** | **ip-interworking** ] ] \*
   * PPP/HDLC interface:
     
     [**mpls static-l2vc**](cmdqueryname=mpls+static-l2vc) { { **destination** *ip-address* | **pw-template** *pw-template-name* *vc-id* } \* | **destination** *ip-address* [ *vc-id* ] } **transmit-vpn-label** *transmit-label-value* **receive-vpn-label** *receive-label-value* [ **tunnel-policy** *tnl-policy-name* [ { **endpoint** *endpoint-address* | [ **endpoint** *endpoint4-address* ] } **color** *color-value* ] | **access-port** | [ **control-word** | **no-control-word** ] | [ **raw** | **tagged** | **ip-interworking** ] ] \*
   * ATM interface:
     
     [**mpls static-l2vc**](cmdqueryname=mpls+static-l2vc) { { **destination** *ip-address* | **pw-template** *pw-template-name* *vc-id* } \* | **destination** *ip-address* [ *vc-id* ] } **transmit-vpn-label** *transmit-label-value* **receive-vpn-label** *receive-label-value* [ **tunnel-policy** *tnl-policy-name* [ **endpoint** *endpoint-address* **color** *color-value* ] | **access-port** | [ **control-word** | **no-control-word** ] | [ **max-atm-cells** *cells-value* ] | [ **atm-pack-overtime** *time* ] ] \*
   * TDM interface:
     
     [**mpls static-l2vc**](cmdqueryname=mpls+static-l2vc) { { **destination** *ip-address* | **pw-template** *pw-template-name* *vc-id* } \* | **destination** *ip-address* [ *vc-id* ] } **transmit-vpn-label** *transmit-label-value* **receive-vpn-label** *receive-label-value* [ **tunnel-policy** *tnl-policy-name* [ **endpoint** *endpoint-address* **color** *color-value* ] | **access-port** | [ **control-word** | **no-control-word** ] | [ **jitter-buffer** *depth* ] | [ **tdm-encapsulation** *number* ] | [ **tdm-sequence-number** ] | [ **idle-code** *idle-code-value* ] | [ **rtp-header** ] ] \*
8. (Optional) Run [**mpls l2vpn service-name**](cmdqueryname=mpls+l2vpn+service-name) *service-name*
   
   
   
   An L2VPN service name is specified. The L2VPN service can then be maintained through an NMS based on the specified name.
9. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.