Monitoring the BFD Operating Status
===================================

This section describes how to monitor the BFD operating status.

#### Procedure

* Run the [**display bfd session**](cmdqueryname=display+bfd+session) { **all** | **static** | **dynamic** | **discriminator** *discr-value* | **peer-ip** *peer-ip* [ **vpn-instance** *vpn-name* ] } [ **verbose** ] command in any view to check information about BFD sessions.
* Run the [**display bfd statistics**](cmdqueryname=display+bfd+statistics) command in any view to check global BFD statistics.
* Run the [**display bfd statistics session**](cmdqueryname=display+bfd+statistics+session) { **all** | **static** | **dynamic** | **discriminator** *discr-value* | **peer-ip** *peer-ip* [ **vpn-instance** *vpn-name* ] } command in any view to check statistics about BFD sessions.
* Run the [**display bfd configuration**](cmdqueryname=display+bfd+configuration) { **all** | **static** } [ **for-ip** | **for-ipv6** | **for-lsp** | **for-te** | **for-pw** | **for-vsi-pw** | **for-evpn-vpws** ] **verbose**  command in any view to check the BFD session configuration.
* Run the [**display bfd interface**](cmdqueryname=display+bfd+interface) [ *interface-type* *interface-number* ] command to check information about BFD interfaces.