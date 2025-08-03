Using Ping to Check the Connectivity of Layer 3 Eth-Trunk Member Interfaces
===========================================================================

Using Ping to Check the Connectivity of Layer 3 Eth-Trunk Member Interfaces

#### Prerequisites

Before using the ping command to check the connectivity of a Layer 3 Eth-Trunk member interface, ensure that an IP address has been configured for the Layer 3 Eth-Trunk interface to which the member interface is added.


#### Context

Multiple physical interfaces can be bundled into an Eth-Trunk interface, and each member interface uses a different transmission path and different path-specific service parameters (such as delay time, jitter time, and packet loss ratio). As a result, if service performance of an Eth-Trunk interface deteriorates, it is difficult to determine which member interface has failed. To resolve this problem, ping each Eth-Trunk member interface to help identify the faulty member interface.

![](public_sys-resources/note_3.0-en-us.png) 

This method is applicable to scenarios where devices are directly connected through an Eth-Trunk.



#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enable detection on Layer 3 Eth-Trunk member interfaces on the responder of the ping operation.
   
   
   ```
   [trunk member-port-inspect](cmdqueryname=trunk+member-port-inspect)
   ```
   
   By default, detection on Eth-Trunk member interfaces is disabled.
   
   
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   This command configuration takes effect on all Layer 3 Eth-Trunk interfaces on a device. If you only need to test the connectivity of an Eth-Trunk, disable this function after Eth-Trunk member interfaces are detected. If this function is not disabled, the device will continue to detect Eth-Trunk member interfaces, wasting system resources.
3. Detect Layer 3 Eth-Trunk member interfaces on the initiator of the ping operation.
   
   
   ```
   [ping](cmdqueryname=ping) -a source-ip-address -i interface-type interface-number [ ip ] [ -8021p 8021p-value | -c count | -d | { -f | ignore-mtu } | -h ttl-value | -m time | -p pattern | -q | -r | -ri | -s packetsize | -system-time | -t timeout | { -tos tos-value | -dscp dscp-value } | -v | -vpn-instance vpn-instance-name ] * host [ ip-forwarding ]
   ```
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   When detecting Layer 3 Eth-Trunk member interfaces, specify the **-a** and **-i** parameters to specify the source IP address and interface for sending ICMP Echo Request packets.
   
   The command output contains the following information:
   
   * Response to each ping message: If an echo reply message is not received by the initiator after the timeout period expires, the system displays the message "Request time out", indicating that an Eth-Trunk member interface fails. If an echo reply message is received, the data bytes, message sequence number, and response time are displayed, indicating that no Eth-Trunk member interface has failed.
   * Statistics of ping packets, including the number of sent packets, number of received packets, percentage of the packets that are not replied, and the minimum, maximum and average response time.
   ```
   <HUAWEI> ping -a 192.168.1.1 -i 100ge 1/0/1 10.1.1.2
   PING 10.1.1.2: 56  data bytes, press CTRL_C to break                                                                             
       Reply from 10.1.1.2: bytes=56 Sequence=1 ttl=254 time=2 ms                                                                     
       Reply from 10.1.1.2: bytes=56 Sequence=2 ttl=254 time=1 ms                                                                     
       Reply from 10.1.1.2: bytes=56 Sequence=3 ttl=254 time=2 ms                                                                     
       Reply from 10.1.1.2: bytes=56 Sequence=4 ttl=254 time=1 ms                                                                     
       Reply from 10.1.1.2: bytes=56 Sequence=5 ttl=254 time=2 ms                                                                     
                                                                                                                                       
     --- 10.1.1.2 ping statistics ---                                                                                                 
       5 packet(s) transmitted                                                                                                         
       5 packet(s) received                                                                                                            
       0.00% packet loss                                                                                                               
       round-trip min/avg/max = 1/1/2 ms
   ```