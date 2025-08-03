Verifying the Configuration
===========================

After configuring dynamic BFD to monitor an LDP tunnel, you can view BFD session information on the ingress on which an LDP tunnel is established.

#### Prerequisites

The dynamic BFD for LDP tunnel function has been configured.
#### Procedure

* Run the [**display mpls bfd session**](cmdqueryname=display+mpls+bfd+session+protocol+ldp+fec+bfd-type+ldp-tunnel) **protocol** **ldp** [ **fec** *ip-address* ] [ **bfd-type ldp-tunnel** ] [ **verbose** ] command to check information about all BFD sessions that monitor LDP tunnels on the ingress.