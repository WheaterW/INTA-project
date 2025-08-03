Configuring BGP EVPN Soft Reset
===============================

Configuring BGP EVPN Soft Reset

#### Context

BGP EVPN soft reset performs a soft reset on BGP EVPN connections. The soft reset triggers BGP EVPN peers to send EVPN routes to a local device without tearing down the BGP EVPN connections and allows the local device to refresh the BGP EVPN routing table.


#### Procedure

* In the user view, configure BGP EVPN soft reset.
  
  
  ```
  [refresh bgp evpn](cmdqueryname=refresh+bgp+evpn) { all | peer-address | group group-name } { export | import }
  ```