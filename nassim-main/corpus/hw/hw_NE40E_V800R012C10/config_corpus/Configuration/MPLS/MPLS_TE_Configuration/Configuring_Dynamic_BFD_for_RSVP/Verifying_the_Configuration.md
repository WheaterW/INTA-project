Verifying the Configuration
===========================

After configuring dynamic BFD for TE RSVP, you can view the status of a BFD session for RSVP.

#### Procedure

* Run the [**display mpls rsvp-te bfd session**](cmdqueryname=display+mpls+rsvp-te+bfd+session) { **all** | **interface** *interface-type* *interface-number* | **peer** *ip-address* } [ **verbose** ] command to check information about the BFD for RSVP session.
* Run the [**display mpls rsvp-te**](cmdqueryname=display+mpls+rsvp-te) **interface** [ *interface-type interface-number* ] command to view BFD for RSVP configurations on a specific interface.