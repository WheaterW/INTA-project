Verifying the Configuration
===========================

After configuring static EVPN VPWS over SRv6 BE, verify EVPL instance information.

#### Prerequisites

Static EVPN VPWS over SRv6 BE has been configured.


#### Procedure

* Run the [**display bgp evpn evpl**](cmdqueryname=display+bgp+evpn+evpl) command to check all EVPL instance information.
* Run the [**display bgp evpn**](cmdqueryname=display+bgp+evpn) { **all** | **route-distinguisher** *route-distinguisher* } **routing-table** [ { **ad-route** | **es-route** | **inclusive-route** | **mac-route** | **prefix-route** } *prefix* ] command to check BGP EVPN route information.
* Run the [**display segment-routing ipv6 local-sid**](cmdqueryname=display+segment-routing+ipv6+local-sid) **end-dx2** **evpl-instance** *evpl-id* **forwarding** command to check information about the SRv6 BE local SID table.