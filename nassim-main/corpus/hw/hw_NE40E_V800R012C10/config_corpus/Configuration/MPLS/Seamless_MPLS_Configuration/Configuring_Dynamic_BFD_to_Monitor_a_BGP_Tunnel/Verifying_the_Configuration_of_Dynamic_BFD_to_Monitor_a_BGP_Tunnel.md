Verifying the Configuration of Dynamic BFD to Monitor a BGP Tunnel
==================================================================

After configuring a dynamic BFD session to monitor a BGP tunnel, you can view BGP BFD session information on the ingress of the BGP tunnel.

#### Prerequisites

The dynamic BFD for BGP tunnel function has been configured.


#### Procedure

* Run the [**display mpls bfd session**](cmdqueryname=display+mpls+bfd+session+protocol+bgp+fec+verbose) **protocol** **bgp** [ **fec** *fec-address* [ **verbose** ] ] command to check information about a BFD session with the protocol type of BGP on the ingress on an E2E BGP tunnel.