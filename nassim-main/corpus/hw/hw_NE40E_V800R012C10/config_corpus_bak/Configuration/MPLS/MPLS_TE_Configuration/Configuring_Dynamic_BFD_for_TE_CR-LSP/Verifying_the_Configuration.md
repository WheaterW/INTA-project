Verifying the Configuration
===========================

After configuring dynamic BFD for TE CR-LSP, you can verify that a CR-LSP is Up and a BFD session is successfully established.

#### Procedure

* Run the [**display bfd session**](cmdqueryname=display+bfd+session) **dynamic** [ **verbose** ] command to check information about the BFD session on the ingress.
* Run the [**display bfd session**](cmdqueryname=display+bfd+session) **passive-dynamic** [ **peer-ip** *peer-ip* **remote-discriminator** *discriminator* ] [ **verbose** ] command to check information about the BFD session passively created on the egress.
* Run the following commands to check BFD statistics.
  
  
  + Run the [**display bfd statistics**](cmdqueryname=display+bfd+statistics) command to check statistics about all BFD sessions.
  + Run the [**display bfd statistics session**](cmdqueryname=display+bfd+statistics+session) **dynamic** command to check statistics about dynamic BFD sessions.
* Run the [**display mpls bfd session**](cmdqueryname=display+mpls+bfd+session) [ **protocol** **rsvp-te** | **outgoing-interface** *interface-type* *interface-number* ] [ **verbose** ] command to check information about the MPLS BFD session.