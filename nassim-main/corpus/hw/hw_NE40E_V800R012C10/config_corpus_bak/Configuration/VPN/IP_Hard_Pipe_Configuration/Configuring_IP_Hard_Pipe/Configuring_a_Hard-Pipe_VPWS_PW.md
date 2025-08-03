Configuring a Hard-Pipe VPWS PW
===============================

Configuring a hard-pipe VPWS PW to carry private line services of high-value customers implements P2P services over the hard pipe.

#### Context

VPWS enables carriers to provide L2VPN services over different media through the same IP hard pipe network. By providing P2P services over the hard pipe, this implementation enhances private line services for high-value customers.


#### Procedure

1. Configure MPLS L2VPN.
   1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
   2. Run the [**mpls l2vpn**](cmdqueryname=mpls+l2vpn) command to configure MPLS L2VPN.
   3. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
   4. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
2. Create a tunnel policy.
   1. Run the [**tunnel-policy**](cmdqueryname=tunnel-policy) *policy-name* command to create a tunnel policy and enter its view.
   2. Run the [**tunnel binding**](cmdqueryname=tunnel+binding) **destination** *dest-ip-address* **te** { *tunnel-name* | *tunnel-type**tunnel-number* } & <1-32> [ **ignore-destination-check** ] [ **down-switch** | **include-ldp** ] command to specify the TE tunnel for binding in the tunnel policy.
   3. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
   4. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
3. Configure a hard-pipe VPWS PW.
   
   Hard pipe only applies to static VPWS PWs, including SS-PWs and MS-PWs. Determine which procedure to take based on the PW type:
   * Static SS-PW
     1. Run the [**interface**](cmdqueryname=interface) *interface-type* *interface-number* command to enter the AC interface view.
     2. Run either of the following commands to create an SVC VPWS connection based on the AC interface type:
        + Ethernet interface: [**mpls static-l2vc**](cmdqueryname=mpls+static-l2vc) { { **destination** *ip-address* | **pw-template** *pw-template-name* *vc-id* } \* | **destination** *ip-address* [ *vc-id* ] } **transmit-vpn-label** *transmit-label-value* **receive-vpn-label** *receive-label-value* [ **tunnel-policy** *tnl-policy-name* | **access-port** | [ **control-word** | **no-control-word** ] | [ **raw** | **tagged** ] ] \*
        + Non-Ethernet interface: [**mpls static-l2vc**](cmdqueryname=mpls+static-l2vc) { { **destination** *ip-address* | **pw-template** *pw-template-name* *vc-id* } \* | **destination** *ip-address* [ *vc-id* ] } **transmit-vpn-label** *transmit-label-value* **receive-vpn-label** *receive-label-value* [ **tunnel-policy** *tnl-policy-name* | **access-port** | [ **control-word** | **no-control-word** ] | [ **jitter-buffer** *depth* ] | [ **tdm-encapsulation** *number* ] | [ **tdm-sequence-number** ] | [ **idle-code** *idle-code-value* ] | [ **rtp-header** ] ] \*
     3. Run either of the following commands to configure the hard pipe function for a static PW based on the AC interface type:
        + Ethernet interface: [**mpls l2vpn hard-pipe**](cmdqueryname=mpls+l2vpn+hard-pipe) **bandwidth** *bandwidth* [ **burst-time** *burst-time* ] [ **expand-ratio** *expand-ratio* ]
        + Non-Ethernet interface: [**mpls l2vpn hard-pipe**](cmdqueryname=mpls+l2vpn+hard-pipe) [ **expand-ratio** *expand-ratio* ]
     4. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
     5. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
   * Static MS-PW:
     1. Run the [**mpls switch-l2vc**](cmdqueryname=mpls+switch-l2vc) [ **instance-name** *instance-name* ] *ip-address vc-id* **trans** *trans-label* **recv** *received-label* [ **tunnel-policy** *policy-name* ] [ **oam-packet** **pop** **flow-label** ] **between** *ip-address vc-id* **trans** *trans-label* **recv** *received-label* [ **tunnel-policy** *policy-name* ] [ **oam-packet** **pop** **flow-label** ] **encapsulation** *encapsulation-type* [ **control-word** | **no-control-word** ] command to configure a static MS-PW.
     2. Run the [**mpls switch-l2vc**](cmdqueryname=mpls+switch-l2vc) *peer-ip* *vc-id* **encapsulation** *encapsulation-type* **hard-pipe** [ **bandwidth** *bandwidth* **expand-ratio** *expand-ratio* ] command to configure the hard pipe function for the static MS-PW.
     3. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.