Monitoring EVPN Running Status
==============================

To monitor the running status of EVPN VPLS and EVPN VPWS, check the label and SID information of EVPN peers.

#### Context

In routine maintenance, you can run the following display commands in any view to check the running status of EVPN peers.


#### Procedure

* Run the [**display evpn vpn-instance name**](cmdqueryname=display+evpn+vpn-instance+name) *evpnName* **remote-label** command in any view to check the label information of EVPN peers.
* Run the [**display evpn vpn-instance name**](cmdqueryname=display+evpn+vpn-instance+name) *evpnName* **remote-sid** command in any view to check the SID information of EVPN peers.