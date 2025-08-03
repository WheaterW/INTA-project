Using Ping to Test TCP Connectivity on an IPv4 Network
======================================================

Using Ping to Test TCP Connectivity on an IPv4 Network

#### Prerequisites

Before running the [**ping tcp**](cmdqueryname=ping+tcp) command on a device to test TCP connectivity on an IPv4 network, ensure that the TCP server function has been enabled on the peer end.


#### Context

As shown in [Figure 1](#EN-US_TASK_0000001130625000__fig19666175217492), a ping operation can be performed to check whether the source (DeviceA) and destination (TCP server) are able to reach each other and to measure the time they require to set up a TCP connection through a three-way handshake.

The packet exchange during the ping process is as follows:

1. DeviceA sends a TCP SYN packet for establishing a TCP connection with the TCP server according to the specified destination IP address and port number.
2. When receiving the TCP SYN packet, the TCP server accepts the request and responds with a TCP SYN ACK packet.
3. Upon receipt of the TCP SYN ACK packet, DeviceA sends an ACK packet to the TCP server.

After the TCP connection is established, DeviceA calculates the time difference between sending a TCP SYN packet and sending an ACK packet to obtain the time required to set up a TCP connection through a three-way handshake. This helps you learn about the performance of the TCP protocol on the network.

**Figure 1** Network diagram of testing TCP connectivity using the ping function  
![](figure/en-us_image_0000001176664553.png)

#### Procedure

1. (Optional) If the TCP port on the destination end is not enabled, manually enable it.
   1. Enter the system view.
      
      
      ```
      [system-view](cmdqueryname=system-view)
      ```
   2. Specify the listening IP address and listening port number for TCP services on the destination end.
      
      
      ```
      [nqa server tcpconnect](cmdqueryname=nqa+server+tcpconnect) [ vpn-instance vpn-instance-name ] ip-address port-number
      ```
   3. Commit the configuration.
      
      
      ```
      [commit](cmdqueryname=commit)
      ```
2. Initiate a ping test on a source to test the TCP connectivity with a destination.
   
   
   ```
   [ping tcp](cmdqueryname=ping+tcp) [ -c count | -t timeout | -m interval | -h ttl | -vpn-instance vpn-instance-name | -passroute | -a source-ip-address ] * destAddress [ destPort ]
   ```

#### Example

Perform a ping operation to test TCP connectivity with the destination 10.1.1.1.

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

The command output contains the following information:

* Response to each test packet: If no response packet is received before the timer on the source expires, the message "Request time out" is displayed. If a response packet is received, information such as the number of bytes in the payload, packet sequence number, and response time is displayed.
* Ping statistics: include the numbers of sent and received packets, the packet loss rate, and the minimum, maximum, and average response time durations.