Resetting Traffic Suppression of MAC Flapping-based Loop Detection
==================================================================

After loops are removed from a network and network traffic recovers, reset traffic suppression of MAC flapping-based loop detection.

#### Context

After loops are removed from a network and network traffic recovers, reset traffic suppression of MAC flapping-based loop detection. The system then re-collects MAC flapping statistics.


#### Procedure

1. Run the [**reset loop-detect traffic-suppression**](cmdqueryname=reset+loop-detect+traffic-suppression) [ **vsi** *vsi-name* | **vlan** *vlan-id* ] command to reset traffic suppression of MAC flapping-based loop detection.
   
   
   
   After traffic suppression of MAC flapping-based loop detection is reset, the system re-collects MAC flapping statistics.