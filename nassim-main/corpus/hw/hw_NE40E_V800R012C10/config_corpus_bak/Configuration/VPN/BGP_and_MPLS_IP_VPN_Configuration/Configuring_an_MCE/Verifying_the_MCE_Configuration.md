Verifying the MCE Configuration
===============================

After configuring the MCE, check the routes to the LAN
and remote sites for each type of service in the VRF table of the
MCE.

#### Prerequisites

The MCE has been configured.
#### Procedure

* Run the [**display
  ip routing-table vpn-instance**](cmdqueryname=display+ip+routing-table+vpn-instance) *vpn-instance-name* [ **verbose** ] command to check the VRF
  table on the MCE.