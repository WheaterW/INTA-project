Clearing Layer 2 Traffic Suppression Statistics
===============================================

Before collecting Layer 2 traffic suppression statistics, you need to delete the existing statistics.

#### Procedure

1. Run the [**reset traffic-statistics suppression interface**](cmdqueryname=reset+traffic-statistics+suppression+interface) { *interface-name* | *interface-type* *interface-num* } **vsi** *vsi-name* or [**reset counters interface**](cmdqueryname=reset+counters+interface) { *interface-name* | *interface-type* *interface-num* } **suppression** **vsi** *vsi-name* command to clear Layer 2 traffic suppression statistics about specified VPLS services on the specified interface.
2. Run the [**reset traffic-statistics suppression vsi**](cmdqueryname=reset+traffic-statistics+suppression+vsi) **name** *vsi-name* **peer** *peer-address* [ **negotiation-vc-id** *negotiation-vc-id* ] command to clear traffic suppression statistics about the specified PW.
3. Run the [**reset traffic-statistics suppression interface**](cmdqueryname=reset+traffic-statistics+suppression+interface) { *interface-name* | *interface-type* *interface-num* } [ **vlan** *vlanid* | **bd** *bd-id* ] or [**reset counters interface**](cmdqueryname=reset+counters+interface) { *interface-name* | *interface-type* *interface-num* } **suppression** [ **vlan** *vlan-id* | **bd** *bd-id* ] command to clear Layer 2 traffic suppression statistics about specified Layer 2 services on the specified interface.
4. Run the [**reset traffic-statistics suppression vsi**](cmdqueryname=reset+traffic-statistics+suppression+vsi) **name** *vsi-name* [ **peer** *peer-address* [ **negotiation-vc-id** *negotiation-vc-id* ] | **uni** ] command to clear traffic suppression statistics about the specified VSI.
5. Run the [**reset traffic-statistics suppression bd**](cmdqueryname=reset+traffic-statistics+suppression+bd) *bd-id* command to clear Layer 2 traffic suppression statistics about the specified BD.