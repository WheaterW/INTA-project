Verifying the Configuration
===========================

After configuring the static BFD for TE CR-LSP, you can view configurations, such as the status of the BFD sessions of Up.

#### Prerequisites

The static BFD for TE CR-LSP has been configured.


#### Procedure

* Run the [**display bfd session**](cmdqueryname=display+bfd+session) **mpls-te** **interface** *tunnel-name* **te-lsp** [ **verbose** ] command to check information about BFD sessions on the ingress.
* Run the following commands to check information about BFD sessions on the egress.
  
  
  + Run the [**display bfd session**](cmdqueryname=display+bfd+session) **all** [ **for-ip** | **for-lsp** | **for-te** ] [ **verbose** ] command to check information about all BFD sessions.
  + Run the [**display bfd session**](cmdqueryname=display+bfd+session) **static** [ **for-ip** | **for-lsp** | **for-te** ] [ **verbose** ] command to check information about static BFD sessions.
  + Run the [**display bfd session**](cmdqueryname=display+bfd+session) **peer-ip** *peer-ip* [ **vpn-instance** *vpn-name* ] [ **verbose** ] command to check information about BFD sessions with reverse IP links.
  + Run the [**display bfd session**](cmdqueryname=display+bfd+session) **ldp-lsp** **peer-ip** *ip-address* [ **nexthop** *nexthop-ip* [ **interface** *interface-type* *interface-number* ] ] [ **verbose** ] command to check information about the BFD sessions with reverse LDP LSPs.
  + Run the [**display bfd session**](cmdqueryname=display+bfd+session) **mpls-te** **interface** *tunnel-name* **te-lsp** [ **verbose** ] command to check information about the BFD sessions with reverse CR-LSPs.
  + Run the [**display bfd session**](cmdqueryname=display+bfd+session) **mpls-te** **interface** *tunnel-name* [ **verbose** ] command to check information about the BFD sessions with reverse TE tunnels.
* Run the following commands to check BFD statistics.
  
  
  + Run the [**display bfd statistics session**](cmdqueryname=display+bfd+statistics+session) **all** [ **for-ip** | **for-lsp** | **for-te** ] command to check statistics about all BFD sessions.
  + Run the [**display bfd statistics session**](cmdqueryname=display+bfd+statistics+session) **static** [ **for-ip** | **for-lsp** | **for-te** ] command to check statistics about static BFD sessions.
  + Run the [**display bfd statistics session**](cmdqueryname=display+bfd+statistics+session) **peer-ip** *peer-ip* [ **vpn-instance** *vpn-name* ] command to check statistics about the BFD sessions with reverse IP links.
  + Run the [**display bfd statistics session**](cmdqueryname=display+bfd+statistics+session) **ldp-lsp** **peer-ip** *peer-ip* [ **nexthop** *nexthop-ip* [ **interface** *interface-type* *interface-number* ] ] command to check statistics about the BFD sessions with reverse LDP LSPs.
  + Run the [**display bfd statistics session**](cmdqueryname=display+bfd+statistics+session) **mpls-te** **interface** *interface-type* *interface-number* **te-lsp** command to check statistics about BFD sessions with reverse CR-LSPs.