Configuring Primary and Secondary SVC PWs
=========================================

To ensure that a primary PW fault does not interrupt services in a static PW FRR scenario, you need to configure a secondary PW for the primary PW, so that traffic can be switched to the secondary PW for transmission.

#### Procedure

* Configure a pair of primary and secondary PWs on each PE.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**mpls l2vpn**](cmdqueryname=mpls+l2vpn)
     
     
     
     MPLS L2VPN is enabled.
  3. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  4. (Optional) Configure a PW template.
     
     
     1. Run the [**pw-template**](cmdqueryname=pw-template) *pw-template-name* command to create a PW template and enter its view.
     2. Configure the attributes of the PW template. The following steps can be performed in any order. Determine which steps to perform based on your requirements.
        + Run the [**peer-address**](cmdqueryname=peer-address) *ip-address* command to specify the IP address of the peer device for the PW.
        + Run the [**control-word**](cmdqueryname=control-word) command to enable the control word function.
        + Run the [**tnl-policy**](cmdqueryname=tnl-policy) *policy-name* command to specify the tunnel policy to be used by the PW.
        + Run the [**mtu**](cmdqueryname=mtu) *mtu-value* command to configure the MTU in the PW template.
        + Run the [**bfd-detect**](cmdqueryname=bfd-detect) [ **detect-multiplier** *multiplier* | **min-rx-interval** *rx-interval* | **min-tx-interval** *tx-interval* ] \* [ **track** **group** *group-name* ] command to set BFD session detection parameters.
        + Run the [**jitter-buffer depth**](cmdqueryname=jitter-buffer+depth) *depth* command to configure the depth of the jitter buffer for the TDMoPSN application.
        + Run the [**idle-code**](cmdqueryname=idle-code) *idle-code-value* command to configure the idle code that is filled when a jitter buffer underflow occurs.
        + Run the [**tdm-encapsulation-number**](cmdqueryname=tdm-encapsulation-number) *number* command to specify the number of TDM frames encapsulated in a CESoPSN packet for the TDMoPSN application.
     3. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
  5. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number* [ .*subinterface-number* ]
     
     
     
     The AC interface view is displayed.
  6. Configure the primary PW.
     
     Run either of the following commands to create a VPWS PW according to the interface type:
     + Ethernet interface:
       
       [**mpls static-l2vc**](cmdqueryname=mpls+static-l2vc) { { **destination** *ip-address* | **pw-template** *pw-template-name* *vc-id* } \* | **destination** *ip-address* [ *vc-id* ] } **transmit-vpn-label** *transmit-label-value* **receive-vpn-label** *receive-label-value* [ **tunnel-policy** *tnl-policy-name* [ { **endpoint** *endpoint-address* | [ **endpoint** *endpoint4-address* ] } **color** *color-value* ] | **access-port** | [ **control-word** | **no-control-word** ] | [ **raw** | **tagged** ] ] \*
     + TDM interface:
       
       [**mpls static-l2vc**](cmdqueryname=mpls+static-l2vc) { { **destination** *ip-address* | **pw-template** *pw-template-name* *vc-id* } \* | **destination** *ip-address* [ *vc-id* ] } **transmit-vpn-label** *transmit-label-value* **receive-vpn-label** *receive-label-value* [ **tunnel-policy** *tnl-policy-name* [ **endpoint** *endpoint-address* **color** *color-value* ] | [ **control-word** | **no-control-word** ] | **jitter-buffer** *depth* | **tdm-encapsulation** *number* | **tdm-sequence-number** | **idle-code** *idle-code-value* | **rtp-header** ] \*
  7. Configure the secondary PW.
     
     Run either of the following commands to create a secondary VPWS PW according to the interface type:
     + Ethernet interface:
       
       [**mpls static-l2vc**](cmdqueryname=mpls+static-l2vc) { { **destination** *ip-address* | **pw-template** *pw-template-name* *vc-id* } \* | **destination** *ip-address* [ *vc-id* ] } **transmit-vpn-label** *transmit-label-value* **receive-vpn-label** *receive-label-value* [ **tunnel-policy** *tnl-policy-name* [ { **endpoint** *endpoint-address* | [ **endpoint** *endpoint4-address* ] } **color** *color-value* ] | **access-port** | [ **control-word** | **no-control-word** ] | [ **raw** | **tagged** ] ] \* **secondary**
     + TDM interface:
       
       [**mpls static-l2vc**](cmdqueryname=mpls+static-l2vc) { { **destination** *ip-address* | **pw-template** *pw-template-name* *vc-id* } \* | **destination** *ip-address* [ *vc-id* ] } **transmit-vpn-label** *transmit-label-value* **receive-vpn-label** *receive-label-value* [ **tunnel-policy** *tnl-policy-name* [ **endpoint** *endpoint-address* **color** *color-value* ] | [ **control-word** | **no-control-word**] | **jitter-buffer** *depth* | **tdm-encapsulation** *number* | **tdm-sequence-number** | **idle-code** *idle-code-value* | **rtp-header** ] \* **secondary**
  8. Run [**mpls l2vpn stream-dual-receiving**](cmdqueryname=mpls+l2vpn+stream-dual-receiving)
     
     
     
     The primary and secondary PWs are configured to both receive packets.
     
     
     
     In static PW FRR scenarios, if you do not configure the primary and secondary PWs to both receive packets, long-lasting packet loss or even service interruption may occur after a traffic switchover.
  9. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  10. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
* Configure VPWS switching on each SPE.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**mpls l2vpn**](cmdqueryname=mpls+l2vpn)
     
     
     
     MPLS L2VPN is enabled.
  3. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  4. Run [**mpls switch-l2vc**](cmdqueryname=mpls+switch-l2vc) [ **instance-name** *instance-name* ] *ip-address vc-id* **trans** *trans-label* **recv** *received-label* [ **tunnel-policy** *policy-name* [ { **endpoint** *endpoint-address* | [ **endpoint** *endpoint4-address* ] } **color** *color-value* ] ] **between** *ip-address vc-id* **trans** *trans-label* **recv** *received-label* [ **tunnel-policy** *policy-name* [ { **endpoint** *sw-endpoint-address* | [ **endpoint** *sw-endpoint4-address* ] } **color** *color-value* ] ] **encapsulation** *encapsulation-type* [ **control-word** | **no-control-word** ]
     
     
     
     A static MS-PW is configured.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.