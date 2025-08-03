Resetting BGP EVPN Connections
==============================

Resetting BGP EVPN Connections

#### Context

![](../public_sys-resources/notice_3.0-en-us.png) 

Because BGP EVPN peer relationships are interrupted when BGP EVPN connections are reset (using [**reset bgp**](cmdqueryname=reset+bgp)), exercise caution when running this command.

To reset BGP EVPN connections, run the following reset commands in the user view as required.


#### Procedure

* Reset all BGP EVPN connections.
  
  
  ```
  [reset bgp](cmdqueryname=reset+bgp) [ instance instance-name ] evpn all
  ```
* Reset BGP EVPN connections with a specified AS.
  
  
  ```
  [reset bgp](cmdqueryname=reset+bgp) [ instance instance-name ] evpn as-number
  ```
* Reset BGP EVPN connections with a specified peer.
  
  
  ```
  [reset bgp](cmdqueryname=reset+bgp) [ instance instance-name ] evpn ipv4-address
  ```
* Reset BGP EVPN connections with a specified peer group.
  
  
  ```
  [reset bgp](cmdqueryname=reset+bgp) [ instance instance-name ] evpn group group-name
  ```