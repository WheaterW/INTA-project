Configuring a PW Protection Group
=================================

In an E-PW APS scenario, a PW protection group consists of either primary and secondary PWs or primary and bypass PWs. The primary and secondary PWs can be either SS-PWs or MS-PWs.

#### Context

In an E-PW APS scenario, PE1 connects to PE2 and PE3 over a pair of primary and secondary PWs and PE2 and PE3 connect to each other over a bypass PW. The PW protection group consists of the primary and secondary PWs on PE1 and consists of the primary and bypass PWs on PE2 and PE3. The primary and secondary PWs can be dynamic SS-PWs, static SS-PWs, dynamic MS-PWs, or static MS-PWs. The bypass PW is usually an SS-PW. Its static/dynamic type is the same as that of the primary PW in the PW protection group. When configuring PW redundancy, note the following guidelines:

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
* When configuring a PW protection group, ensure that parameter settings for the primary, secondary, and bypass PWs are consistent. If inconsistencies exist, the secondary or bypass PW may fail to take over services when the primary PW fails, leading to service interruption.

Configure a PW protection group that consists of primary and secondary PWs on PE1 and a PW protection group consisting of primary and bypass PWs on PE2 and PE3. In the case of MS-PWs, you also need to configure VPWS switching on SPE1 and SPE2.


#### Procedure

* Configure a PW protection group that consists of static primary and secondary PWs.
  
  
  
  Perform the following steps on PE1:
  
  
  
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**interface**](cmdqueryname=interface) *interface-type interface-number* command to enter the AC interface view.
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
  5. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
  6. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
* Configure a PW protection group that consists of static primary and bypass PWs.
  
  
  
  Perform the following steps on PE2 and PE3.
  
  
  
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**interface**](cmdqueryname=interface) *interface-type interface-number* command to enter the AC interface view.
  3. Configure the static primary PW.
     
     Run one of the following commands according to the interface type:
     + Ethernet interface: [**mpls static-l2vc**](cmdqueryname=mpls+static-l2vc) { { **destination** *ip-address* | **pw-template** *pw-template-name* *vc-id* } \* | **destination** *ip-address* [ *vc-id* ] } **transmit-vpn-label** *transmit-label-value* **receive-vpn-label** *receive-label-value* [ **tunnel-policy** *tnl-policy-name* [ { **endpoint** *endpoint-address* | [ **endpoint** *endpoint4-address* ] } **color** *color-value* ] | **access-port** | [ **control-word** | **no-control-word** ] | [ **raw** | **tagged** | **ip-interworking** ] ] \*
     + ATM interface: [**mpls static-l2vc**](cmdqueryname=mpls+static-l2vc) { { **destination** *ip-address* | **pw-template** *pw-template-name* *vc-id* } \* | **destination** *ip-address* [ *vc-id* ] } **transmit-vpn-label** *transmit-label-value* **receive-vpn-label** *receive-label-value* [ **tunnel-policy** *tnl-policy-name* [ **endpoint** *endpoint-address* **color** *color-value* ] | **access-port** | [ **control-word** | **no-control-word** ] | [ **max-atm-cells** *cells-value* ] | [ **atm-pack-overtime** *time* ] ] \*
     + TDM interface: [**mpls static-l2vc**](cmdqueryname=mpls+static-l2vc) { { **destination** *ip-address* | **pw-template** *pw-template-name* *vc-id* } \* | **destination** *ip-address* [ *vc-id* ] } **transmit-vpn-label** *transmit-label-value* **receive-vpn-label** *receive-label-value* [ **tunnel-policy** *tnl-policy-name* [ **endpoint** *endpoint-address* **color** *color-value* ] | **access-port** | [ **control-word** | **no-control-word** ] | [ **jitter-buffer** *depth* ] | [ **tdm-encapsulation** *number* ] | [ **tdm-sequence-number** ] | [ **idle-code** *idle-code-value* ] | [ **rtp-header** ] ] \*
  4. Configure a static bypass PW.
     
     
     
     Run one of the following commands according to the interface type:
     
     + Ethernet interface: [**mpls static-l2vc**](cmdqueryname=mpls+static-l2vc) { { **destination** *ip-address* | **pw-template** *pw-template-name* *vc-id* } \* | **destination** *ip-address* [ *vc-id* ] } **transmit-vpn-label** *transmit-label-value* **receive-vpn-label** *receive-label-value* [ **tunnel-policy** *tnl-policy-name* [ { **endpoint** *endpoint-address* | [ **endpoint** *endpoint4-address* ] } **color** *color-value* ] | **access-port** | [ **control-word** | **no-control-word** ] | [ **raw** | **tagged** ] ] \* **bypass**
     + ATM interface: [**mpls static-l2vc**](cmdqueryname=mpls+static-l2vc) { { **destination** *ip-address* | **pw-template** *pw-template-name* *vc-id* } \* | **destination** *ip-address* [ *vc-id* ] } **transmit-vpn-label** *transmit-label-value* **receive-vpn-label** *receive-label-value* [ **tunnel-policy** *tnl-policy-name* [ **endpoint** *endpoint-address* **color** *color-value* ] | **access-port** | [ **control-word** | **no-control-word** ] | [ **max-atm-cells** *cells-value* ] | [ **atm-pack-overtime** *time* ] ] \* **bypass**
     + TDM interface: [**mpls static-l2vc**](cmdqueryname=mpls+static-l2vc) { { **destination** *ip-address* | **pw-template** *pw-template-name* *vc-id* } \* | **destination** *ip-address* [ *vc-id* ] } **transmit-vpn-label** *transmit-label-value* **receive-vpn-label** *receive-label-value* [ **tunnel-policy** *tnl-policy-name* [ **endpoint** *endpoint-address* **color** *color-value* ] | **access-port** | [ **control-word** | **no-control-word** ] | [ **jitter-buffer** *depth* ] | [ **tdm-encapsulation** *number* ] | [ **tdm-sequence-number** ] | [ **idle-code** *idle-code-value* ] | [ **rtp-header** ] ] \* **bypass**
  5. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
  6. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
* Configure a PW protection group that consists of dynamic primary and secondary PWs.
  
  
  
  Perform the following steps on PE1:
  
  
  
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**interface**](cmdqueryname=interface) *interface-type interface-number* command to enter the AC interface view.
  1. Configure the dynamic primary PW.
     
     Run one of the following commands according to the interface type:
     + Ethernet interface: [**mpls l2vc**](cmdqueryname=mpls+l2vc)  [ **instance-name** *instance-name* ] { *ip-address* | **pw-template** *template-name* } \* *vc-id* [ **tunnel-policy** *policy-name* [ { **endpoint** *endpoint-address* | [ **endpoint** *endpoint4-address* ] } **color** *color-value* ] | [ **control-word** | **no-control-word** ] | [ **raw** | **tagged** | **ip-layer2** | **ip-interworking**] | **access-port** | **ignore-standby-state** ] \*
     + ATM interface: [**mpls l2vc**](cmdqueryname=mpls+l2vc)  [ **instance-name** *instance-name* ] { *ip-address* | **pw-template** *template-name* } \* *vc-id* [ **tunnel-policy** *policy-name* [ **endpoint** *endpoint-address* **color** *color-value* ] | [ **control-word** | **no-control-word** ] | [ **max-atm-cells** *cells-value* ] | [ **atm-pack-overtime** *time* ] | **ignore-standby-state** ] \*
     + TDM interface: [**mpls l2vc**](cmdqueryname=mpls+l2vc)  [ **instance-name** *instance-name* ] { *ip-address* | **pw-template** *template-name* } \* *vc-id* [ **tunnel-policy** *tnl-policy-name* [ **endpoint** *endpoint-address* **color** *color-value* ] | [ **control-word** | **no-control-word** ] | [ **jitter-buffer** *depth* ] | [ **tdm-encapsulation** *number* ] | [ **tdm-sequence-number** ] | [ **idle-code** *idle-code-value* ] | **rtp-header** | **ignore-standby-state** ] \*
  2. Configure the dynamic secondary PW.
     
     Run one of the following commands according to the interface type:
     + Ethernet interface: [**mpls l2vc**](cmdqueryname=mpls+l2vc)  [ **instance-name** *instance-name* ] { *ip-address* | **pw-template** *template-name* } \* *vc-id* [ **access-port** | [ **control-word** | **no-control-word** ] | **ignore-standby-state** | [ **raw** | **tagged** | **ip-layer2** | **ip-interworking** ] | **tunnel-policy** *policy-name* [ { **endpoint** *endpoint-address* | [ **endpoint** *endpoint4-address* ] } **color** *color-value* ] | **secondary** ] \*
     + ATM interface: [**mpls l2vc**](cmdqueryname=mpls+l2vc)  [ **instance-name** *instance-name* ] { *ip-address* | **pw-template** *template-name* } \* *vc-id* [ **tunnel-policy** *policy-name* [ **endpoint** *endpoint-address* **color** *color-value* ] | [ **control-word** | [ **seq-number** ] | **no-control-word** ] | **max-atm-cells** *cells-value* | **atm-pack-overtime** *atm-pack-overtime* | **transmit-atm-cells** *transmit-atm-cell-value* | **ignore-standby-state** | **secondary** ] \*
     + TDM interface: [**mpls l2vc**](cmdqueryname=mpls+l2vc)  [ **instance-name** *instance-name* ] { *ip-address* | **pw-template** *template-name* } \* *vc-id* [ **tunnel-policy** *tnl-policy-name* [ **endpoint** *endpoint-address* **color** *color-value* ] | [ **control-word** | **no-control-word** ] | [ **jitter-buffer** *depth* ] | [ **tdm-encapsulation-number** *number* ] | [ **tdm-sequence-number** ] | [ **rtp-header** ] | **ignore-standby-state** | **secondary** ] \*
* Configure a PW protection group that consists of dynamic primary and bypass PWs.
  
  
  
  Perform the following steps on PE2 and PE3.
  
  
  
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**interface**](cmdqueryname=interface) *interface-type interface-number* command to enter the AC interface view.
  3. Configure the dynamic primary PW.
     
     Run one of the following commands according to the interface type:
     + Ethernet interface: [**mpls l2vc**](cmdqueryname=mpls+l2vc)  [ **instance-name** *instance-name* ] { *ip-address* | **pw-template** *template-name* } \* *vc-id* [ **tunnel-policy** *policy-name* [ { **endpoint** *endpoint-address* | [ **endpoint** *endpoint4-address* ] } **color** *color-value* ] | [ **control-word** | **no-control-word** ] | [ **raw** | **tagged** | **ip-layer2** | **ip-interworking**] | **access-port** | **ignore-standby-state** ] \*
     + ATM interface: [**mpls l2vc**](cmdqueryname=mpls+l2vc)  [ **instance-name** *instance-name* ] { *ip-address* | **pw-template** *template-name* } \* *vc-id* [ **tunnel-policy** *policy-name* [ **endpoint** *endpoint-address* **color** *color-value* ] | [ **control-word** | **no-control-word** ] | [ **max-atm-cells** *cells-value* ] | [ **atm-pack-overtime** *time* ] | **ignore-standby-state** ] \*
     + TDM interface: [**mpls l2vc**](cmdqueryname=mpls+l2vc)  [ **instance-name** *instance-name* ] { *ip-address* | **pw-template** *template-name* } \* *vc-id* [ **tunnel-policy** *tnl-policy-name* [ **endpoint** *endpoint-address* **color** *color-value* ] | [ **control-word** | **no-control-word** ] | [ **jitter-buffer** *depth* ] | [ **tdm-encapsulation** *number* ] | [ **tdm-sequence-number** ] | [ **idle-code** *idle-code-value* ] | **rtp-header** | **ignore-standby-state** ] \*
  4. (Optional) Configure a dynamic bypass PW.
     
     Run one of the following commands according to the interface type:
     + Ethernet interface: [**mpls l2vc**](cmdqueryname=mpls+l2vc) { *ip-address* | **pw-template** *template-name* } \* *vc-id* [ **tunnel-policy** *tnl-policy-name* [ { **endpoint** *endpoint-address* | [ **endpoint** *endpoint4-address* ] } **color** *color-value* ] | [ **control-word** | **no-control-word** ] | [ **raw** | **tagged** ] | **access-port** | **ignore-standby-state** ] \* **bypass**
     + ATM interface: [**mpls l2vc**](cmdqueryname=mpls+l2vc) { *ip-address* | **pw-template** *template-name* } \* *vc-id* [ **tunnel-policy** *nl-policy-name* [ **endpoint** *endpoint-address* **color** *color-value* ] | [ **control-word** | **no-control-word** ] | [ **max-atm-cells** *cells-value* ] | [ **atm-pack-overtime** *time* ] | **ignore-standby-state** ] \* **bypass**
     + TDM interface: [**mpls l2vc**](cmdqueryname=mpls+l2vc) { *ip-address* | **pw-template** *pw-template-name* } \* *vc-id* [ **tunnel-policy** *policy-name* [ **endpoint** *endpoint-address* **color** *color-value* ] | [ **control-word** | **no-control-word** ] | **jitter-buffer** *depth* | [ **tdm-encapsulation** *number* ] | **tdm-sequence-number** | [ **idle-code** *idle-code-value* ] | **rtp-header** | **ignore-standby-state** ] \* **bypass**
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