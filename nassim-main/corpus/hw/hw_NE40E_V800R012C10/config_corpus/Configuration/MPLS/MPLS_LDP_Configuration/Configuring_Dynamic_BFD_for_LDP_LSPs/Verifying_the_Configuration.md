Verifying the Configuration
===========================

After configuring dynamic BFD for LDP LSP, you can view BFD configurations and session information on the ingress and egress of a specified LDP LSP.

#### Prerequisites

Dynamic BFD for LDP LSP has been configured.
#### Procedure

* Run the [**display mpls bfd session**](cmdqueryname=display+mpls+bfd+session+fec+nexthop+outgoing-interface+protocol) [ **fec** *ip-address* | **nexthop** *ip-address* | **outgoing-interface** *interface-type* *interface-number* | **protocol** { **rsvp-te** | **ldp** } ] [ **verbose** ] command to check BFD session information.
* Run the [**display bfd session**](cmdqueryname=display+bfd+session+all+verbose) **all** **verbose** command on the ingress to check BFD session information.
* Run the [**display bfd session**](cmdqueryname=display+bfd+session+passive-dynamic+verbose) **passive-dynamic** **verbose** command on the egress to check BFD session information.