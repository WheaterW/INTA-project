Verifying the Configuration
===========================

After an HVPLS network evolves to PBB-EVPN, check the operating status of and information about PBB-EVPN functions.

#### Prerequisites

PBB-EVPN has been configured.


#### Procedure

* Run the [**display default-parameter evpn**](cmdqueryname=display+default-parameter+evpn) command to check default PBB-EVPN configurations during PBB-EVPN initialization.
* Run the [**display evpn vpn-instance**](cmdqueryname=display+evpn+vpn-instance) [ **name** *vpn-instance-name* ] command to check PBB-EVPN instance information.
* Run the [**display evpn**](cmdqueryname=display+evpn) [**vpn-instance**](cmdqueryname=vpn-instance) **name** *vpn-instance-name* **df result** [ **esi** *esi* ] command to check the DF election result of the I-EVPN instance.
* Run the [**display evpn**](cmdqueryname=display+evpn) [**vpn-instance**](cmdqueryname=vpn-instance) [**name**](cmdqueryname=name) *vpn-instance-name* **df-timer** **state** command to check the DF timer status of the I-EVPN instance.
* Run the [**display bgp evpn**](cmdqueryname=display+bgp+evpn) { **all** | [**vpn-instance**](cmdqueryname=vpn-instance) *vpn-instance-name* } **esi** [ *esi* ] command to check the PBB-EVPN instance's ESI information.
* Run the [**display bgp evpn**](cmdqueryname=display+bgp+evpn) { **all** | **route-distinguisher** *route-distinguisher* | **vpn-instance** *vpn-instance-name* } **routing-table** [ { **ad-route** | **es-route** | **inclusive-route** | **mac-route** } *prefix* ] command to check PBB-EVPN routing information.
* Run the [**display bgp evpn all routing-table statistics**](cmdqueryname=display+bgp+evpn+all+routing-table+statistics) command to check PBB-EVPN route statistics.
* Run the [**display evpn mac routing-table**](cmdqueryname=display+evpn+mac+routing-table) command to check MAC route information of PBB-EVPN instances.
* Run the [**display evpn mac routing-table limit**](cmdqueryname=display+evpn+mac+routing-table+limit) command to check MAC address limits of PBB-EVPN instances.