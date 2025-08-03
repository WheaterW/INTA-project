Using Ping to Check the TCP Reachability on an IPv4 Network
===========================================================

The ping operation can be performed to check whether the client and the TCP server can communicate with each other and check the time taken to set up a TCP connection through three-way handshake.

#### Prerequisites

Before using the [**ping tcp**](cmdqueryname=ping+tcp) command to check the time taken to set up a TCP connection on an IPv4 network, ensure that the TCP server is enabled on the peer end or the peer end is specified as the TCP server using the [**nqa-server tcpconnect**](cmdqueryname=nqa-server+tcpconnect) command.


#### Procedure

1. Run [**ping tcp**](cmdqueryname=ping+tcp) [ **-c** *count* | **-t** *timeout* | **-m** *interval* | **-h** *ttl* | **-vpn-instance** *vrfName* | **-passroute** | **-a** *srcAddress* ] \* *destAddress* [ *destPort* ]
   
   
   
   The time taken to set up a TCP connection on the IPv4 network is displayed.
   
   
   
   For example:
   
   ```
   <HUAWEI> ping tcp 10.1.1.1 3000
     PING TCP 10.1.1.1: 3000, press CTRL_C to break
       Reply from 10.1.1.1: Sequence=1 time=3 ms
       Reply from 10.1.1.1: Sequence=2 time=3 ms
       Reply from 10.1.1.1: Sequence=3 time=3 ms
       Reply from 10.1.1.1: Sequence=4 time=3 ms
       Reply from 10.1.1.1: Sequence=5 time=4 ms
     --- TCP ping statistics ---
       5 packet(s) transmitted
       5 packet(s) received
       0.00% packet loss
       round-trip min/avg/max = 3/3/4 ms
   ```