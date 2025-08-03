Configuring a VPWS PW
=====================

This section describes how to establish a P2P VPWS PW between two PEs for communication.

#### Context

LDP VPWS is classified into two modes: PWE3-compatible and PWE3.

* PWE3-compatible mode: does not use Notification messages.
* PWE3 mode: uses Notification messages to advertise the PW status. By default, PWE3 VPWS is used.

Perform the following configurations on the endpoint PEs of a PW.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**mpls l2vpn**](cmdqueryname=mpls+l2vpn)
   
   
   
   MPLS L2VPN is configured, and its view is displayed.
3. (Optional) Run [**mpls l2vpn no-request-message**](cmdqueryname=mpls+l2vpn+no-request-message) **peer** *ip-address*
   
   
   
   The function to send L2VPN Label Request messages to the remote peer is disabled.
4. (Optional) Run [**mpls l2vpn ignore-te-oam-state**](cmdqueryname=mpls+l2vpn+ignore-te-oam-state)
   
   
   
   The PW is configured to ignore the recursive tunnel status monitored by MPLS OAM/MPLS-TP OAM.
5. (Optional) Run [**mpls l2vpn auto-create-session**](cmdqueryname=mpls+l2vpn+auto-create-session)
   
   
   
   The function to automatically establish a remote LDP session is enabled.
6. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
7. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number* [ .*subinterface-number* ]
   
   
   
   The AC interface view is displayed.
8. (Optional) Run [**mpls l2vpn description**](cmdqueryname=mpls+l2vpn+description) *description-text*
   
   
   
   An L2VPN description is configured for the AC interface.
9. (Optional) Run [**mpls l2vpn pw performance disable**](cmdqueryname=mpls+l2vpn+pw+performance+disable)
   
   
   
   PW performance statistics collection is disabled.
10. Run one of the following commands to create a VPWS connection according to the interface type:
    
    
    * Ethernet interface:
      
      [**mpls l2vc**](cmdqueryname=mpls+l2vc) [ **instance-name** *instance-name* ] { *ip-address* | **pw-template** *template-name* } \* *vc-id* [ **tunnel-policy** *policy-name* [ { **endpoint** *endpoint-address* | [ **endpoint** *endpoint4-address* ] } **color** *color-value* ] | [ **control-word** | **no-control-word** ] | [ **raw** | **tagged** | **ip-layer2** | **ip-interworking**] | **access-port** | **ignore-standby-state** ] \*
    * PPP/HDLC interface:
      
      [**mpls l2vc**](cmdqueryname=mpls+l2vc)  [ **instance-name** *instance-name* ] { *ip-address* | **pw-template** *template-name* } \* *vc-id* [ **tunnel-policy** *policy-name* [ { **endpoint** *endpoint-address* | [ **endpoint** *endpoint4-address* ] } **color** *color-value* ] | [ **control-word** | **no-control-word** ] | [ **raw** | **tagged** | **ip-layer2** | **ip-interworking**] | **access-port** | **ignore-standby-state** ] \*
    * ATM interface:
      
      [**mpls l2vc**](cmdqueryname=mpls+l2vc)  [ **instance-name** *instance-name* ] { *ip-address* | **pw-template** *template-name* } \* *vc-id* [ **tunnel-policy** *policy-name* [ **endpoint** *endpoint-address* **color** *color-value* ] | [ **control-word** | **no-control-word** ] | [ **max-atm-cells** *cells-value* ] | [ **atm-pack-overtime** *time* ] | **ignore-standby-state** ] \*
    * TDM interface:
      
      [**mpls l2vc**](cmdqueryname=mpls+l2vc)  [ **instance-name** *instance-name* ] { *ip-address* | **pw-template** *template-name* } \* *vc-id* [ **tunnel-policy** *tnl-policy-name* [ **endpoint** *endpoint-address* **color** *color-value* ] | [ **control-word** | **no-control-word** ] | [ **jitter-buffer** *depth* ] | [ **tdm-encapsulation** *number* ] | [ **tdm-sequence-number** ] | [ **idle-code** *idle-code-value* ] | **rtp-header** | **ignore-standby-state** ] \*![](../../../../public_sys-resources/note_3.0-en-us.png) 
    * The VC IDs with the same encapsulation type must be unique on a PE.
    * The **raw**, **tagged**, and **access-port** parameters are available in this command only for Ethernet links. In addition, the **access-port** parameter can be configured only on Ethernet main interfaces.
    * If an Ethernet sub-interface is used, run the [**vlan-type dot1q**](cmdqueryname=vlan-type+dot1q) *vlan-id* command in the interface view to configure the encapsulation type and VLAN ID of the Ethernet sub-interface.
    * The default tunnel policy uses LDP tunnels for VPWS connections. To use a different type of tunnel, set the **tunnel-policy** *policy-name* parameter for the PW to reference the corresponding tunnel policy.
11. (Optional) Run [**undo interface-parameter-type vccv**](cmdqueryname=undo+interface-parameter-type+vccv)
    
    
    
    The VCCV byte (following the interface parameter) is deleted from the Label Mapping message.
    
    
    
    Run this command if LDP VPWS is configured for a device running VRP V800R005 or later and this device communicates with another device running VRP V300R001 or any branch version of VRP V300R001.
12. (Optional) Run [**mpls l2vpn service-name**](cmdqueryname=mpls+l2vpn+service-name) *service-name*
    
    
    
    An L2VPN service name is specified. The L2VPN service can then be maintained through an NMS based on the specified name.
13. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.