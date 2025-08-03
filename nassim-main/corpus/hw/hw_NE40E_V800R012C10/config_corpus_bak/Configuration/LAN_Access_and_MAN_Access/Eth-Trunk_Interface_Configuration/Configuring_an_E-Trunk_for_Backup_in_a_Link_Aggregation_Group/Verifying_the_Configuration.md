Verifying the Configuration
===========================

After configuring an E-Trunk, check the configurations, including the E-Trunk priority, system ID, source IP address, peer IP address, revertive switching delay, master/backup status, dynamic BFD session parameters, and E-Trunk description.

#### Prerequisites

An E-Trunk has been configured.


#### Procedure

* Run the [**display e-trunk**](cmdqueryname=display+e-trunk) *etrunk-id* command to check E-Trunk details.
* Run the [**display e-trunk bfd session all**](cmdqueryname=display+e-trunk+bfd+session+all) command to check the bindings between dynamic BFD sessions and E-Trunks.
* Add Eth-Trunk interfaces working in static LACP mode to the E-Trunk and then run the [**display lacp brief**](cmdqueryname=display+lacp+brief) command to check brief LACP information.
* Run the [**display current-configuration**](cmdqueryname=display+current-configuration) command to check the configuration of whitelist session-CAR for E-Trunk.