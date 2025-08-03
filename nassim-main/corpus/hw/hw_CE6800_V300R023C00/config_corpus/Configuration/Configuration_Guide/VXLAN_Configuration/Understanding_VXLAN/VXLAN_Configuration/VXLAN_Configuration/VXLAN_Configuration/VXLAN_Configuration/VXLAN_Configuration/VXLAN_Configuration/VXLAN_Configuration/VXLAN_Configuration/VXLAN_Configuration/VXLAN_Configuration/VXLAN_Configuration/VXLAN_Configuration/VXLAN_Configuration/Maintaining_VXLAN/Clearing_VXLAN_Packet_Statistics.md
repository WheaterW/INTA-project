Clearing VXLAN Packet Statistics
================================

Clearing VXLAN Packet Statistics

#### Context

Before collecting new VXLAN packet statistics, you can clear the existing statistics on the device to improve information accuracy.

![](../public_sys-resources/note_3.0-en-us.png) 

Because cleared VXLAN packet statistics cannot be restored, exercise caution when performing this operation.



#### Procedure

* In the user view, clear packet statistics about a specified BD.
  
  
  ```
  [reset bridge-domain](cmdqueryname=reset+bridge-domain) bd-id statistics
  ```
* In the user view, clear VXLAN tunnel packet statistics.
  
  
  ```
  [reset vxlan statistics](cmdqueryname=reset+vxlan+statistics) source source-ip-address peer peer-ip-address [ vni vni-id ]
  ```
* In the user view, clear IPv6 VXLAN tunnel packet statistics. 
  
  
  ```
  [reset vxlan statistics](cmdqueryname=reset+vxlan+statistics) source source-ipv6 peer peer-ipv6 [ vni vni-id ]
  ```
* In any view, clear VXLAN statistics about a specified board.
  
  
  ```
  [reset fwm vxlan](cmdqueryname=reset+fwm+vxlan) { l2subif | bridge-domain | tunnel | evpn | oam } [statistics](cmdqueryname=statistics) [ all ] slot slot-id
  ```