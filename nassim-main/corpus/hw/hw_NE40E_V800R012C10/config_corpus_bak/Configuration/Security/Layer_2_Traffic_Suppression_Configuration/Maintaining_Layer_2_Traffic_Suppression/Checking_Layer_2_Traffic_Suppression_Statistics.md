Checking Layer 2 Traffic Suppression Statistics
===============================================

You can run the corresponding **display** commands to check interface-specific Layer 2 traffic suppression statistics.

#### Procedure

1. Run the [**display interface**](cmdqueryname=display+interface) { *interface-name* | *interface-type interface-num* } **suppression vsi** *vsi-name* or [**display traffic-statistics suppression interface**](cmdqueryname=display+traffic-statistics+suppression+interface) { *interface-name* | *interface-type interface-num* } **vsi** *vsi-name* command to check Layer 2 traffic suppression statistics about specified VPLS services on the specified interface.
2. Run the [**display traffic-statistics suppression interface**](cmdqueryname=display+traffic-statistics+suppression+interface) { *interface-name* | *interface-type* *interface-num* } { **vlan** *vlan-id* | **bd** *bd-id* } or [**display interface**](cmdqueryname=display+interface) { *interface-name* | *interface-type* *interface-num* } **suppression** [ **vlan** *vlan-id* | **bd** *bd-id* ] command to check Layer 2 traffic suppression statistics about specified Layer 2 services on the specified interface.
3. Run the [**display traffic-statistics vsi**](cmdqueryname=display+traffic-statistics+vsi) *vsi-name* **suppression** **peer** *peer-address* [ **negotiation-vc-id** *vcIdValue* ] command to check PW traffic suppression statistics.
4. Run the [**display traffic-statistics suppression bd**](cmdqueryname=display+traffic-statistics+suppression+bd) *bd-id* command to check Layer 2 traffic suppression statistics about the specified BD.