Verifying the Configuration of Optimizing MPLS
==============================================

After you adjust MPLS parameters, verify MPLS-enabled interface information.

#### Prerequisites

MPLS parameters have been adjusted.


#### Procedure

1. Run the [**display mpls rsvp-te interface**](cmdqueryname=display+mpls+rsvp-te+interface) [ *interface-type* *interface-number* ] command to check MPLS TE-enabled interface information, including the interface MTU.
2. Run the [**display mpls ldp interface**](cmdqueryname=display+mpls+ldp+interface+verbose) [ *interface-type* *interface-number* | **verbose** ] command to check the MTU information of MPLS LDP-enabled interfaces.
3. Run the [**display mpls interface**](cmdqueryname=display+mpls+interface+verbose) [ *interface-type* *interface-number* ] [ **verbose** ] command to check MPLS-enabled interface information.