Inbound Interface in an IPv6 Multicast Forwarding Entry Is Incorrect
====================================================================

Inbound Interface in an IPv6 Multicast Forwarding Entry Is Incorrect

#### Fault Symptom

After multicast routing protocol configuration is complete, an IPv6 PIM routing entry can be created, but the inbound interface in the multicast forwarding entry is incorrect. As a result, multicast data cannot be sent to user subnets.

#### Possible Causes

The source IPv6 address of the multicast data packet is the same as the address of the VLANIF interface on the device.


#### Procedure

* Check whether the inbound interface in the multicast forwarding entry is a loopback interface.
  
  
  ```
  [display multicast ipv6 fib](cmdqueryname=display+multicast+ipv6+fib)
  ```
  
  If the interface is a loopback interface, you can change the IPv6 address of the multicast source or the address of the VLANIF interface to ensure that they are different but on the same subnet.