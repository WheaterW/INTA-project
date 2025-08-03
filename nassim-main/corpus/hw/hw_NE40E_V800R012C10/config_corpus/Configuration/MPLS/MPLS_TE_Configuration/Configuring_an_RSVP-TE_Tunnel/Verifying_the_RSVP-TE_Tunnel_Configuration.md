Verifying the RSVP-TE Tunnel Configuration
==========================================

After configuring the RSVP-TE tunnel, you can view statistics about the RSVP-TE tunnel and its status.

#### Prerequisites

An RSVP-TE tunnel has been configured.


#### Procedure

* Run the [**display mpls te link-administration bandwidth-allocation**](cmdqueryname=display+mpls+te+link-administration+bandwidth-allocation) [ **interface** *interface-type* *interface-number* ] command to check the allocated link bandwidth information.
* Run the [**display ospf**](cmdqueryname=display+ospf) [ *process-id* ] **mpls-te** [ **area** *area-id* ] [ **self-originated** ] command to check OSPF TE information.
* Run either of the following commands to check the IS-IS TE status:
  + [**display isis traffic-eng advertisements**](cmdqueryname=display+isis+traffic-eng+advertisements) [ *lsp-id* | **local** ] [ **level-1** | **level-2** | **level-1-2** ] [ *process-id* | **vpn-instance** *vpn-instance-name* ]
  + [**display isis traffic-eng statistics**](cmdqueryname=display+isis+traffic-eng+statistics) [ *process-id* | **vpn-instance** *vpn-instance-name* ]
* Run the [**display explicit-path**](cmdqueryname=display+explicit-path) [ [ **name** ] *path-name* ] [ **verbose** ] command to check the configured explicit paths.
* Run the [**display mpls te cspf destination**](cmdqueryname=display+mpls+te+cspf+destination) *ip-address* [ **affinity** { *properties* [ **mask** *mask-value* ] | { { **include-all** | **include-any** } { *pri-in-name-string* } &<1-32> | **exclude** { *pri-ex-name-string* } &<1-32> } \* } | **bandwidth** **ct0** *ct0-bandwidth* | **explicit-path** *path-name* | **hop-limit** *hop-limit-number* | **metric-type** { **igp** | **te** } | **priority** *setup-priority* | **srlg-strict** *exclude-path-name* | **tie-breaking** { **random** | **most-fill** | **least-fill** } ] \* [ **hot-standby** [ **explicit-path** *hsb-path-name* | **overlap-path** | **affinity** { *hsb-properties* [ **mask** *hsb-mask-value* ] | { { **include-all** | **include-any** } { *hsb-in-name-string* } &<1-32> | **exclude** { *hsb-ex-name-string* } &<1-32> } \* } | **hop-limit** *hsb-hop-limit-number* | **srlg** { **preferred** | **strict** } ] \* ] command to check the path that is calculated using CSPF based on specified conditions.
* Run the [**display mpls te cspf tedb**](cmdqueryname=display+mpls+te+cspf+tedb) { **all** | **area** *area-id* | **interface** *ip-address* | **network-lsa** | **node** [ *router-id* ] | **srlg** [ *srlg-number* ] [ **igp-type** { **isis** | **ospf** } ] | **overload-node** } command to check information about TEDBs that meet specified conditions and can be used by CSPF to calculate a path.
* Run the [**display mpls rsvp-te**](cmdqueryname=display+mpls+rsvp-te) command to check RSVP information.
* Run the [**display mpls rsvp-te psb-content**](cmdqueryname=display+mpls+rsvp-te+psb-content) [ *ingress-lsr-id* *tunnel-id* [ *lsp-id* ] ] command to check information about the RSVP-TE PSB.
* Run the [**display mpls rsvp-te rsb-content**](cmdqueryname=display+mpls+rsvp-te+rsb-content) [ *ingress-lsr-id* *tunnel-id* *lsp-id* ] command to check information about the RSVP-TE RSB.
* Run the [**display mpls rsvp-te established**](cmdqueryname=display+mpls+rsvp-te+established) [ **interface** *interface-type* *interface-number* *peer-ip-address* ] command to check information about the established RSVP LSPs.
* Run the [**display mpls rsvp-te peer**](cmdqueryname=display+mpls+rsvp-te+peer) [ **interface** *interface-type* *interface-number* | *peer-address* ] command to check the RSVP neighbor parameters.
* Run the [**display mpls rsvp-te reservation**](cmdqueryname=display+mpls+rsvp-te+reservation) [ **interface** *interface-type* *interface-number* *peer-ip-address* ] command to check information about RSVP resource reservation.
* Run the [**display mpls rsvp-te request**](cmdqueryname=display+mpls+rsvp-te+request) [ **interface** *interface-type* *interface-number* *peer-ip-address* ] command to check information about RSVP LSP resource reservation requests.
* Run the [**display mpls rsvp-te sender**](cmdqueryname=display+mpls+rsvp-te+sender) [ **interface** *interface-type* *interface-number* *peer-ip-address* ] command to check information about an RSVP transmit end.
* Run the [**display mpls rsvp-te statistics**](cmdqueryname=display+mpls+rsvp-te+statistics) { **global** | **interface** [ *interface-type* *interface-number* ] } command to check RSVP-TE statistics.
* Run the [**display mpls te link-administration admission-control**](cmdqueryname=display+mpls+te+link-administration+admission-control) [ **interface** *interface-type* *interface-number* ] command to check tunnels established on the local node.
* Run the [**display affinity-mapping**](cmdqueryname=display+affinity-mapping) [ **attribute** *affinity-name* ] [ **verbose** ] command to check information about an affinity name template.
* Run the [**display mpls te tunnel**](cmdqueryname=display+mpls+te+tunnel) [ **destination** *ip-address* ] [ **lsp-id** *lsr-id* *session-id* *local-lsp-id* | **lsr-role** { **all** | **egress** | **ingress** | **remote** | **transit** } ] [ **name** *tunnel-name* ] [ { **incoming-interface** | **interface** | **outgoing-interface** } *interface-type* *interface-number* ] [ **verbose** ] command to check tunnel information.
* Run the [**display mpls te tunnel statistics**](cmdqueryname=display+mpls+te+tunnel+statistics) or [**display mpls lsp statistics**](cmdqueryname=display+mpls+lsp+statistics) command to check tunnel statistics.
* Run the [**display mpls te tunnel-interface**](cmdqueryname=display+mpls+te+tunnel-interface) command to check information about a tunnel interface on the ingress of a tunnel.