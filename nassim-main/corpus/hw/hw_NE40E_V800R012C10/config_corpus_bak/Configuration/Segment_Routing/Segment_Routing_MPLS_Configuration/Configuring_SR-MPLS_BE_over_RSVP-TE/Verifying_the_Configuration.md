Verifying the Configuration
===========================

After configuring SR-MPLS BE over RSVP-TE, check tunnel information on the ingress of the involved SR LSP.

#### Prerequisites

SR-MPLS BE over RSVP-TE has been configured.


#### Procedure

Run the [**display segment-routing prefix mpls forwarding**](cmdqueryname=display+segment-routing+prefix+mpls+forwarding) command to check information about the SR label forwarding table and determine whether the outbound interface of the SR LSP is an RSVP-TE tunnel interface.