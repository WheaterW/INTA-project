MSDP Peer Stuck in the DISABLED State
=====================================

MSDP Peer Stuck in the DISABLED State

#### Fault Symptom

An MSDP peer is configured but is always in the DISABLED state.

#### Possible Causes

MSDP sets up a peer relationship between a local interface address and a remote MSDP peer address over a TCP connection. The MSDP peer connection may be in the DISABLED state in the following situations:

* If two MSDP peers have no route to each other, a TCP connection cannot be established.
* If the local interface address differs from the MSDP peer address configured on the remote device, the TCP connection cannot be established.


#### Procedure

* Check whether there are reachable routes between the two devices that will be configured as MSDP peers.
  1. Check whether the two devices that will become MSDP peers have learned ARP entries from each other.
     
     
     ```
     [display arp](cmdqueryname=display+arp)
     ```
  2. Check whether there are reachable unicast routes between the two devices that will be configured as MSDP peers.
     
     
     ```
     [display ip routing-table](cmdqueryname=display+ip+routing-table)
     ```
* Check whether the interface addresses of the MSDP peers are correct.
  1. Check whether the address of the local interface is the same as the address of the remote MSDP peer.
     
     
     ```
     [display current-configuration interface](cmdqueryname=display+current-configuration+interface) [ interface-type [ interface-number ]| interface-number ] [ include-default ]
     ```