Using Ping to Check VPLS MAC Connectivity
=========================================

You can perform a ping operation to check the connectivity of Layer 2 forwarding links on a VPLS network by specifying the MAC address and VSI name.

#### Procedure

* Run the [**ping vpls mac**](cmdqueryname=ping+vpls+mac) *mac-address* **vsi** *vsi-name* [ **vlan** *vlan-id* | **-c** *count* | **-m** *time-value* | **-s** *packetsize* | **-t** *timeout* | **-exp** *exp* | **-r** *replymode* | **-h** *ttl* | **-a** *source-ip-address* | **-g** ] \* command to perform a VPLS MAC ping test in common packet sending mode.
  
  
  ```
  <HUAWEI> ping vpls mac 00e0-fc12-3456 vsi a1
   Ping mac 00e0-fc12-3456 vsi a1: 142 data bytes, press CTRL_C to break
      Reply from 10.1.1.2: bytes=142 Sequence=1 time=16 ms
      Reply from 10.1.1.2: bytes=142 Sequence=2 time=4 ms
      Reply from 10.1.1.2: bytes=142 Sequence=3 time=7 ms
      Reply from 10.1.1.2: bytes=142 Sequence=4 time=8 ms
      Reply from 10.1.1.2: bytes=142 Sequence=5 time=8 ms
   The IP address of the PE is 192.168.2.9.
  
    --- vsi: a1, mac: 00e0-fc12-3456 ping statistics---
      5 packet(s) transmitted
      5 packet(s) received
      0.00% packet loss
      round-trip min/avg/max=4/8/16 ms
  ```
* Run the [**ping vpls mac**](cmdqueryname=ping+vpls+mac) *mac-address* **vsi** *vsi-name* **rapid** [ **vlan** *vlan-id* | **-c** *rapidCount* | **-s** *packetsize* | **-t** *timeout* | **-exp** *exp* | **-r** *replymode* | **-h** *ttl* | **-a** *source-ip-address* | **-g** ] \* command to perform a VPLS MAC ping test in rapid packet sending mode.
  
  
  ```
  <HUAWEI> ping vpls mac 00e0-fc12-3456 vsi a1 rapid
   Ping mac 00e0-fc12-3456 vsi a1: 142 data bytes, press CTRL_C to break
  
  !!!!!
  
    --- vsi: a1, mac: 00e0-fc12-3456 ping statistics---
      5 packet(s) transmitted
      5 packet(s) received
      0.00% packet loss
      round-trip min/avg/max=16/16/17 ms
  ```
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  **!** indicates that the path is reachable, and **.** indicates that the path is unreachable.
* (Optional) Run the [**display vpls-ping statistics**](cmdqueryname=display+vpls-ping+statistics) command to check VPLS MAC ping packet statistics.
  
  
  
  If the test using the [**ping vpls mac**](cmdqueryname=ping+vpls+mac) command fails, you can run this command to check whether a VPLS fault or a device fault occurs.
* (Optional) Run the [**reset vpls-ping statistics**](cmdqueryname=reset+vpls-ping+statistics) command to clear VPLS MAC ping packet statistics.