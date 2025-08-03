Configuring a PW Protection Group
=================================

In a PW APS scenario, a PW protection group consists of primary and secondary PWs. The PWs can be either SS-PWs or MS-PWs.

#### Context

In the PW APS scenarios shown in [Figure 1](dc_vrp_vpws_cfg_6028.html#EN-US_TASK_0172369864__fig_dc_vrp_vpws_cfg_602801) and [Figure 2](dc_vrp_vpws_cfg_6028.html#EN-US_TASK_0172369864__fig_dc_vrp_vpws_cfg_602802), a PW protection group is created between PE1 and PE2. The PWs can be either SS-PWs or MS-PWs. When configuring PW redundancy, note the following guidelines:

Determine whether to use SS-PWs or MS-PWs as follows:

* If the bearer network where PE1 and PE2 reside is small or the two PEs belong to a carrier other than the transport network carrier, use SS-PWs.
* If PE1 and PE2 belong to different ASs on a large transport network and no tunnel or signaling connection can be directly established between them, use MS-PWs.

Determine whether to use dynamic or static PWs as follows:

* Dynamic PWs use LDP signaling to transmit VC labels. The configuration is easy, and the network scalability is high.
* Static PWs use manually configured VC labels. The network controllability is high, but the configuration is complex and the network scalability is low.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

* A static or hybrid MS-PW cannot obtain the TTL value through dynamic negotiation. To ensure the correct forwarding of PW APS negotiation packets between the endpoint PEs of an MS-PW, run the [**mpls l2vpn pw-ttl**](cmdqueryname=mpls+l2vpn+pw-ttl) *ttl-value* [ **secondary** | **bypass** ] command to configure a TTL value, so that the PW APS mechanism knows the specific number of PW segments.
* In the case of SS-PWs, configure the primary and secondary PWs on the endpoint PEs.
* In the case of MS-PWs, configure the primary and secondary PWs on the endpoint PEs and configure VPWS switching on the SPEs.
* The types of PWs within the same protection group must be the same, and the PW types on the two endpoints of a PW segment must also be the same.
* When configuring a PW protection group, ensure that parameter settings for the primary and secondary PWs are consistent. Parameter setting inconsistencies may result in the secondary PW failing to take over traffic if the primary PW fails.

Configure a PW protection group that consists of the primary and secondary PWs on PE1 and PE2. In the case of MS-PWs, you also need to configure VPWS switching on SPE1 and SPE2.


#### Procedure

* Configure a PW protection group that consists of static primary and secondary PWs.
  
  
  
  Perform the following steps on PE1 and PE2 to configure static PWs.
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number*
     
     
     
     The AC interface view is displayed.
  3. Configure the static primary PW.
     
     Run one of the following commands according to the interface type:
     + Ethernet interface: [**mpls static-l2vc**](cmdqueryname=mpls+static-l2vc) { { **destination** *ip-address* | **pw-template** *pw-template-name* *vc-id* } \* | **destination** *ip-address* [ *vc-id* ] } **transmit-vpn-label** *transmit-label-value* **receive-vpn-label** *receive-label-value* [ **tunnel-policy** *tnl-policy-name* [ { **endpoint** *endpoint-address* | [ **endpoint** *endpoint4-address* ] } **color** *color-value* ] | **access-port** | [ **control-word** | **no-control-word** ] | [ **raw** | **tagged** | **ip-interworking** ] ] \*
     + ATM interface: [**mpls static-l2vc**](cmdqueryname=mpls+static-l2vc) { { **destination** *ip-address* | **pw-template** *pw-template-name* *vc-id* } \* | **destination** *ip-address* [ *vc-id* ] } **transmit-vpn-label** *transmit-label-value* **receive-vpn-label** *receive-label-value* [ **tunnel-policy** *tnl-policy-name* [ **endpoint** *endpoint-address* **color** *color-value* ] | **access-port** | [ **control-word** | **no-control-word** ] | [ **max-atm-cells** *cells-value* ] | [ **atm-pack-overtime** *time* ] ] \*
     + TDM interface: [**mpls static-l2vc**](cmdqueryname=mpls+static-l2vc) { { **destination** *ip-address* | **pw-template** *pw-template-name* *vc-id* } \* | **destination** *ip-address* [ *vc-id* ] } **transmit-vpn-label** *transmit-label-value* **receive-vpn-label** *receive-label-value* [ **tunnel-policy** *tnl-policy-name* [ **endpoint** *endpoint-address* **color** *color-value* ] | **access-port** | [ **control-word** | **no-control-word** ] | [ **jitter-buffer** *depth* ] | [ **tdm-encapsulation** *number* ] | [ **tdm-sequence-number** ] | [ **idle-code** *idle-code-value* ] | [ **rtp-header** ] ] \*
  4. Configure the static secondary PW.
     
     Run one of the following commands according to the interface type:
     + Ethernet interface: [**mpls static-l2vc**](cmdqueryname=mpls+static-l2vc) { { **destination** *ip-address* | **pw-template** *pw-template-name* *vc-id* } \* | **destination** *ip-address* [ *vc-id* ] } **transmit-vpn-label** *transmit-label-value* **receive-vpn-label** *receive-label-value* [ **tunnel-policy** *tnl-policy-name* [ { **endpoint** *endpoint-address* | [ **endpoint** *endpoint4-address* ] } **color** *color-value* ] | **access-port** | [ **control-word** | **no-control-word** ] | [ **raw** | **tagged** | **ip-interworking** ] | **secondary** ] \*
     + ATM interface: [**mpls static-l2vc**](cmdqueryname=mpls+static-l2vc) { { **destination** *ip-address* | **pw-template** *pw-template-name* *vc-id* } \* | **destination** *ip-address* [ *vc-id* ] } **transmit-vpn-label** *transmit-label-value* **receive-vpn-label** *receive-label-value* [ **tunnel-policy** *tnl-policy-name* [ **endpoint** *endpoint-address* **color** *color-value* ] | **access-port** | [ **control-word** | **no-control-word** ] | [ **max-atm-cells** *cells-value* ] | [ **atm-pack-overtime** *time* ] | **secondary** ] \*
     + TDM interface: [**mpls static-l2vc**](cmdqueryname=mpls+static-l2vc) { { **destination** *ip-address* | **pw-template** *pw-template-name* *vc-id* } \* | **destination** *ip-address* [ *vc-id* ] } **transmit-vpn-label** *transmit-label-value* **receive-vpn-label** *receive-label-value* [ **tunnel-policy** *tnl-policy-name* [ **endpoint** *endpoint-address* **color** *color-value* ] | **access-port** | [ **control-word** | **no-control-word** ] | [ **jitter-buffer** *depth* ] | [ **tdm-encapsulation** *number* ] | [ **tdm-sequence-number** ] | [ **idle-code** *idle-code-value* ] | [ **rtp-header** ] | **secondary** ] \*
  5. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  6. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure a PW protection group that consists of dynamic primary and secondary PWs.
  
  
  
  Perform the following steps on PE1 and PE2 to configure dynamic PWs.
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number*
     
     
     
     The AC interface view is displayed.
  3. Configure the dynamic primary PW.
     
     Run one of the following commands according to the interface type:
     + Ethernet interface: [**mpls l2vc**](cmdqueryname=mpls+l2vc)  [ **instance-name** *instance-name* ] { *ip-address* | **pw-template** *template-name* } \* *vc-id* [ **tunnel-policy** *policy-name* [ { **endpoint** *endpoint-address* | [ **endpoint** *endpoint4-address* ] } **color** *color-value* ] | [ **control-word** | **no-control-word** ] | [ **raw** | **tagged** | **ip-layer2** | **ip-interworking**] | **access-port** | **ignore-standby-state** ] \*
     + ATM interface: [**mpls l2vc**](cmdqueryname=mpls+l2vc)  [ **instance-name** *instance-name* ] { *ip-address* | **pw-template** *template-name* } \* *vc-id* [ **tunnel-policy** *policy-name* [ **endpoint** *endpoint-address* **color** *color-value* ] | [ **control-word** | **no-control-word** ] | [ **max-atm-cells** *cells-value* ] | [ **atm-pack-overtime** *time* ] | **ignore-standby-state** ] \*
     + TDM interface: [**mpls l2vc**](cmdqueryname=mpls+l2vc)  [ **instance-name** *instance-name* ] { *ip-address* | **pw-template** *template-name* } \* *vc-id* [ **tunnel-policy** *tnl-policy-name* [ **endpoint** *endpoint-address* **color** *color-value* ] | [ **control-word** | **no-control-word** ] | [ **jitter-buffer** *depth* ] | [ **tdm-encapsulation** *number* ] | [ **tdm-sequence-number** ] | [ **idle-code** *idle-code-value* ] | **rtp-header** | **ignore-standby-state** ] \*
  4. Configure the dynamic secondary PW.
     
     Run one of the following commands according to the interface type:
     + Ethernet interface: [**mpls l2vc**](cmdqueryname=mpls+l2vc)  [ **instance-name** *instance-name* ] { *ip-address* | **pw-template** *template-name* } \* *vc-id* [ **access-port** | [ **control-word** | **no-control-word** ] | **ignore-standby-state** | [ **raw** | **tagged** | **ip-layer2** | **ip-interworking** ] | **tunnel-policy** *policy-name* [ { **endpoint** *endpoint-address* | [ **endpoint** *endpoint4-address* ] } **color** *color-value* ] | **secondary** ] \*
     + ATM interface: [**mpls l2vc**](cmdqueryname=mpls+l2vc)  [ **instance-name** *instance-name* ] { *ip-address* | **pw-template** *template-name* } \* *vc-id* [ **tunnel-policy** *policy-name* [ **endpoint** *endpoint-address* **color** *color-value* ] | [ **control-word** | [ **seq-number** ] | **no-control-word** ] | **max-atm-cells** *cells-value* | **atm-pack-overtime** *atm-pack-overtime* | **transmit-atm-cells** *transmit-atm-cell-value* | **ignore-standby-state** | **secondary** ] \*
     + TDM interface: [**mpls l2vc**](cmdqueryname=mpls+l2vc)  [ **instance-name** *instance-name* ] { *ip-address* | **pw-template** *template-name* } \* *vc-id* [ **tunnel-policy** *tnl-policy-name* [ **endpoint** *endpoint-address* **color** *color-value* ] | [ **control-word** | **no-control-word** ] | [ **jitter-buffer** *depth* ] | [ **tdm-encapsulation-number** *number* ] | [ **tdm-sequence-number** ] | [ **rtp-header** ] | **ignore-standby-state** | **secondary** ] \*
  5. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  6. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* (Optional) Configure VPWS switching.
  
  
  
  During MS-PW deployment, perform the following steps on each SPE.
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run any of the following commands based on PW types on endpoint PEs:
     
     
     + If dynamic PWs are configured on the endpoint PEs, run the [**mpls switch-l2vc**](cmdqueryname=mpls+switch-l2vc) *ip-address* *vc-id* [ **tunnel-policy** *policy-name* [ **endpoint** *endpoint-address* **color** *color-value* ] ] **between** *ip-address vc-id* [ **tunnel-policy** *policy-name* [ { **endpoint** *endpoint-address* | [ **endpoint** *endpoint4-address* ] } **color** *color-value* ] ] [ **backup** *ip-address* *vc-id* [ **tunnel-policy** *policy-name* [ { **endpoint** *sw-endpoint-address* | [ **endpoint** *sw-endpoint4-address* ] } **color** *color-value* ] ] ] **encapsulation** *encapsulation-type* [ **control-word-transparent** ] command to configure dynamic VPWS switching.
     + If static PWs are configured on the endpoint PEs, run the [**mpls switch-l2vc**](cmdqueryname=mpls+switch-l2vc) *ip-address vc-id* **trans** *trans-label* **recv** *received-label* [ **tunnel-policy** *policy-name* [ { **endpoint** *endpoint-address* | [ **endpoint** *endpoint4-address* ] } **color** *color-value* ] ] **between** *ip-address vc-id* **trans** *trans-label* **recv** *received-label* [ **tunnel-policy** *policy-name* [ { **endpoint** *sw-endpoint-address* | [ **endpoint** *sw-endpoint4-address* ] } **color** *color-value* ] ] **encapsulation** *encapsulation-type* [ **control-word** | **no-control-word** ] command to configure static VPWS switching.
     + If a static PW is configured on one endpoint PE and a dynamic PW is configured on the other endpoint PE, run the [**mpls switch-l2vc**](cmdqueryname=mpls+switch-l2vc) *ip-address vc-id* [ **tunnel-policy** *policy-name* [ { **endpoint** *endpoint-address* | [ **endpoint** *endpoint4-address* ] } **color** *color-value* ] ] **between** *ip-address vc-id* **trans** *trans-label* **recv** *received-label* [ **tunnel-policy** *policy-name* [ { **endpoint** *sw-endpoint-address* | [ **endpoint** *sw-endpoint4-address* ] } **color** *color-value* ] ] **encapsulation** *encapsulation-type* [ **mtu** *mtu-value* ] [ **control-word** | **no-control-word** ] [ **rtp-header** ] [ **timeslotnum** *timeslotnum* ] [ **tdm-encapsulation** *number* ] command to configure hybrid VPWS switching.
  3. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.