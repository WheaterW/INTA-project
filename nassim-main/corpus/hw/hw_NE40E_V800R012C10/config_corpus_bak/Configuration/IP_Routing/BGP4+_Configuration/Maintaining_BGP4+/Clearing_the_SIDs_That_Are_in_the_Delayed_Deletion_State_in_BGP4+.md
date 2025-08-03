Clearing the SIDs That Are in the Delayed Deletion State in BGP4+
=================================================================

SIDs in the delayed deletion state consume SID resources. If SID resources are insufficient, other services may fail to apply for SIDs. In this case, you can clear the SIDs in the delayed deletion state from BGP4+.

#### Procedure

* To immediately clear all SIDs in the delayed deletion state from BGP4+, run the [**reset bgp slow-delete sid**](cmdqueryname=reset+bgp+slow-delete+sid+ipv6) **ipv6** command in the user view.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  Clearing the SIDs in the delayed deletion state may cause traffic forwarding failures. Therefore, exercise caution when performing this operation.
* To immediately clear the SIDs in the delayed deletion state from the BGP-VPN instance IPv6 address family, run the [**reset bgp slow-delete sid**](cmdqueryname=reset+bgp+slow-delete+sid+ipv6+vpn) **ipv6** **vpn** command in the user view.