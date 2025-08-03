Verifying the Configuration
===========================

After configuring EVPN functions, check the operating status of and information about these functions.

#### Prerequisites

EVPN functions have been configured.


#### Procedure

* Run the [**display default-parameter evpn**](cmdqueryname=display+default-parameter+evpn) command to check default EVPN configurations during EVPN initialization.
* Run the [**display evpn vpn-instance**](cmdqueryname=display+evpn+vpn-instance) [ [**name**](cmdqueryname=name) *vpn-instance-name* ] command to check EVPN instance information.
* Run the [**display evpn**](cmdqueryname=display+evpn) [**vpn-instance**](cmdqueryname=vpn-instance) [**name**](cmdqueryname=name) *vpn-instance-name* **df result** [ **esi** *esi* ] command to check the DF election result of the EVPN instance.
* Run the [**display evpn**](cmdqueryname=display+evpn) [**vpn-instance**](cmdqueryname=vpn-instance) [**name**](cmdqueryname=name) *vpn-instance-name* **df-timer** **state** command to check the DF timer status of the EVPN instance.
* Run the [**display bgp evpn**](cmdqueryname=display+bgp+evpn) { **all** | [**vpn-instance**](cmdqueryname=vpn-instance) *vpn-instance-name* } **esi** [ *esi* ] command to check the EVPN instance's ESI information.
* Run the [**display bgp evpn**](cmdqueryname=display+bgp+evpn) { **all** | **route-distinguisher** *route-distinguisher* | **vpn-instance** *vpn-instance-name* } **routing-table** [ { **ad-route** | **es-route** | **inclusive-route** | **mac-route** } *prefix* ] command to check BGP EVPN route information.
* Run the [**display bgp evpn all routing-table statistics**](cmdqueryname=display+bgp+evpn+all+routing-table+statistics) command to check EVPN route statistics.
* Run the [**display evpn mac routing-table**](cmdqueryname=display+evpn+mac+routing-table) command to check the EVPN instance's MAC route information.
* Run the [**display evpn mac routing-table limit**](cmdqueryname=display+evpn+mac+routing-table+limit) command to check the EVPN instance's MAC address limits.
* Run the [**display evpn mac routing-table statistics**](cmdqueryname=display+evpn+mac+routing-table+statistics) command to display the EVPN instance's MAC route statistics.
* Run the [**display arp broadcast-suppress user bridge-domain**](cmdqueryname=display+arp+broadcast-suppress+user+bridge-domain) *bd-id* command to check the ARP broadcast suppression table of a specified BD.
* Run the [**display arp packet statistics bridge-domain**](cmdqueryname=display+arp+packet+statistics+bridge-domain) *bd-id* command to check the ARP packet statistics of a specified BD.