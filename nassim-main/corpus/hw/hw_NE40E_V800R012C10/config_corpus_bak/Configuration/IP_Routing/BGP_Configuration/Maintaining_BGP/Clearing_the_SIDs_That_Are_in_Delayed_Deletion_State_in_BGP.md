Clearing the SIDs That Are in Delayed Deletion State in BGP
===========================================================

SIDs in the delayed deletion state consume SID resources. If SID resources are insufficient, other services may fail to apply for SIDs. In this case, you can clear the SIDs in the delayed deletion state from BGP.

#### Procedure

* To immediately clear all SIDs in the delayed deletion state from BGP, run the [**reset bgp slow-delete sid**](cmdqueryname=reset+bgp+slow-delete+sid+all) **all** command in the user view.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  Clearing the SIDs in the delayed deletion state may cause traffic forwarding failures. Therefore, exercise caution when performing this operation.
* To immediately clear the SIDs in the delayed deletion state from the BGP IPv4 unicast address family, run the [**reset bgp slow-delete sid**](cmdqueryname=reset+bgp+slow-delete+sid+ipv4) **ipv4** command in the user view.
* To immediately clear the SIDs in the delayed deletion state from the BGP-VPN instance IPv4 address family, run the [**reset bgp slow-delete sid**](cmdqueryname=reset+bgp+slow-delete+sid+ipv4+vpn) **ipv4** **vpn** command in the user view.
* To immediately clear the End.DT46 SIDs in the delayed deletion state from an instance, run the [**reset bgp slow-delete end-dt46 sid**](cmdqueryname=reset+bgp+slow-delete++end-dt46+sid) command in the user view.