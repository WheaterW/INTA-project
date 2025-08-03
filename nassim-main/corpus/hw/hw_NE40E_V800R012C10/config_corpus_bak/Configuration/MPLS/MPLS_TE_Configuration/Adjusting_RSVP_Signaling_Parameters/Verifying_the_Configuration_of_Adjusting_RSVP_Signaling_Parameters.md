Verifying the Configuration of Adjusting RSVP Signaling Parameters
==================================================================

After adjusting RSVP signaling parameters, you can view the refresh parameters, RSVP reservation confirmation status, RSVP Hello extension status, and RSVP timer parameters.

#### Prerequisites

RSVP signaling parameters have been adjusted.


#### Procedure

* Run the [**display mpls rsvp-te**](cmdqueryname=display+mpls+rsvp-te) command to check RSVP-TE configurations.
* Run the [**display mpls
  rsvp-te psb-content**](cmdqueryname=display+mpls+rsvp-te+psb-content) [ *ingress-lsr-id* *tunnel-id* *lsp-id* ] command to check RSVP-TE PSB information.
* Run the [**display mpls
  rsvp-te rsb-content**](cmdqueryname=display+mpls+rsvp-te+rsb-content) [ *ingress-lsr-id* *tunnel-id* *lsp-id* ] command to check RSVP-TE RSB information.
* Run the [**display mpls rsvp-te
  statistics**](cmdqueryname=display+mpls+rsvp-te+statistics) { **global** | **interface** [ *interface-type* *interface-number* ] } command to check RSVP-TE statistics.