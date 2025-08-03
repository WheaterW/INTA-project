Clearing the SIDs That Are in Delayed Deletion State in EVPN
============================================================

SIDs in the delayed deletion state consume SID resources. If SID resources are insufficient, other services may fail to apply for SIDs. In this case, you can clear the SIDs in the delayed deletion state from EVPN.

#### Procedure

* Run the [**reset bgp slow-delete sid evpn**](cmdqueryname=reset+bgp+slow-delete+sid+evpn) command in the user view to immediately delete SIDs that are in the delayed deletion state from the BGP EVPN public network.
  
  ![](../../../../public_sys-resources/caution_3.0-en-us.png) 
  
  Clearing the SIDs in the delayed deletion state may cause traffic forwarding failures. Therefore, exercise caution when performing this operation.
* Run the [**reset bgp slow-delete sid evpn**](cmdqueryname=reset+bgp+slow-delete+sid+evpn) { **ipv4** | **ipv6** } **vpn** command in the user view to immediately delete SIDs in the delayed deletion state from EVPN L3VPNv4 or EVPN L3VPNv6 routes.
* Run the [**reset evpn slow-delete sid all**](cmdqueryname=reset+evpn+slow-delete+sid+all) command in the user view to immediately delete VPN SIDs that are in the delayed deletion state from BD EVPN and EVPL instances.