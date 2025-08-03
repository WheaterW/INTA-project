Verifying the RSVP GR Helper Configuration
==========================================

After configuring RSVP GR, you can verify that the TE tunnel properly forwards data during the GR process.

#### Prerequisites

RSVP GR has been configured.
#### Procedure

* Run the [**display mpls rsvp-te graceful-restart**](cmdqueryname=display+mpls+rsvp-te+graceful-restart) command to check the RSVP-TE GR status.
* Run the [**display mpls rsvp-te graceful-restart peer**](cmdqueryname=display+mpls+rsvp-te+graceful-restart+peer) [ { **interface** *interface-type* *interface-number* | **node-id** } [ *ip-address* ] ] command to check information about the RSVP GR status on a neighbor.