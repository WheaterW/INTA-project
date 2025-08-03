Using Ping to Test Connectivity on a VXLAN or IPv6 VXLAN Network
================================================================

Using Ping to Test Connectivity on a VXLAN or IPv6 VXLAN Network

#### Prerequisites

Before using the VXLAN ping function to test connectivity of a VXLAN tunnel, ensure that the VXLAN or IPv6 VXLAN network has been configured correctly.

![](../public_sys-resources/note_3.0-en-us.png) 

This function is supported only on the CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885, CE6885-SAN, CE6885-LL (standard forwarding mode), CE6885-T, CE6863E-48S8CQ, CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, CE8850-HAM, and CE6820H, CE6820H-K, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820S.



#### Context

A VXLAN tunnel is specified by a pair of VTEP IP addresses. A static VXLAN tunnel is created by manually configuring the VXLAN Network Identifier (VNI), IP addresses, and ingress replication lists for the local and remote VTEPs. The tunnel can go up as long as the two VTEPs can communicate with each other at Layer 3.

The following uses an IPv4 scenario as an example. In [Figure 1](#EN-US_TASK_0000001176744459__fig_dc_vrp_feature_ping_102801), DeviceA is connected to Server1, and DeviceC is connected to Server2. To enable communication between VMs on Server1 and Server2, VNIs and VTEP IP addresses are configured for DeviceA and DeviceC to create a static VXLAN tunnel between them. DeviceB is a forwarding device on the IP network.

**Figure 1** VXLAN network diagram  
![](figure/en-us_image_0000001130625012.png)
A VNI-based VXLAN ping test can be initiated on DeviceA (source) to check its connectivity with DeviceC (destination). The ping process is as follows:

1. DeviceA sends a VXLAN Echo Request message to DeviceC. The ping test can be initiated by specifying parameters of the following combinations:
   * VNI, source VTEP IP address, and destination VTEP IP address
   * VNI, source VTEP IP address, destination VTEP IP address, and VXLAN source port number
   * VNI, source VTEP IP address, destination VTEP IP address, and 7-tuple information
2. When receiving the VXLAN Echo Request message, DeviceC verifies the VNI information and returns a VXLAN Echo Reply message.
3. DeviceA receives the VXLAN Echo Reply packet from DeviceC. The VXLAN ping test is now complete.

![](../public_sys-resources/note_3.0-en-us.png) 

After the VXLAN ping/tracert function is enabled using the [**nqa vxlanecho enable**](cmdqueryname=nqa+vxlanecho+enable) command, packets with the destination MAC address 00:00:5E:90:00:01 are identified as VXLAN ping/tracert packets and cannot be forwarded normally.

By default, the source IP address used to perform a ping or tracert operation on a VXLAN network is on the underlay network. If you are not sure whether there is a route from the remote end to the local end, specify the **-a** parameter to configure the IP address of the tunnel as the source IP address.



#### Procedure

* Test connectivity of an IPv4 VXLAN tunnel.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. (Optional) Enable the VXLAN ping function on the source.
     
     
     1. Enable the VXLAN ping function, and configure the UDP port number used in VXLAN packets.
        ```
        [nqa vxlanecho enable](cmdqueryname=nqa+vxlanecho+enable) udp-port udpPort [ source-ip-interface { ifName | ifType ifNum } ]
        ```
     2. Commit the configuration.
        ```
        [commit](cmdqueryname=commit)
        ```![](../public_sys-resources/note_3.0-en-us.png) 
     
     This step is mandatory if the **-r** *replymode* parameter is set to **3** in the [**ping vxlan**](cmdqueryname=ping+vxlan) command on the source.
  3. Enable the VXLAN ping function on the destination.
     
     
     1. Enable the VXLAN ping function, and configure the UDP port number used in VXLAN packets.
        ```
        [nqa vxlanecho enable](cmdqueryname=nqa+vxlanecho+enable) udp-port udpPort [ source-ip-interface { ifName | ifType ifNum } ]
        ```
     2. Commit the configuration.
        ```
        [commit](cmdqueryname=commit)
        ```
  4. Initiate a connectivity test for an IPv4 VXLAN tunnel.
     
     
     ```
     [ping vxlan](cmdqueryname=ping+vxlan) [ -c count | -m interval | -t timeout | -r replymode | -a innersrc-address | -tos tos ] * vni vniid source source-address peer dest-address [ udp-port dest-port ] [ load-balance { vxlan-source-udpport vxlan-source-udpport [ vxlan-source-end-udpport ] | { source-address lb-src-address destination-address lb-dst-address protocol { udp | lb-protocolid } source-port lb-src-port destination-port lb-dst-port source-mac source-mac destination-mac destination-mac } } ]
     ```
  
  
  
  The command output contains the following information:
  
  + Response to each test packet: If no response packet is received before the timer on the source expires, the message "Request time out" is displayed. If a response packet is received, information such as the number of bytes in the payload, packet sequence number, and response time is displayed.
  + Ping statistics: include the numbers of sent and received packets, the packet loss rate, and the minimum, maximum, and average response time durations.
* Test connectivity of an IPv6 VXLAN tunnel.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. (Optional) Enable the VXLAN ping function on the source.
     
     
     ```
     [nqa vxlanecho enable](cmdqueryname=nqa+vxlanecho+enable) ipv6 udp-port udpPort6 [ source-ip-interface { ifName6 | ifType6 ifNum6 } ]
     ```
     
     
     ![](../public_sys-resources/note_3.0-en-us.png) 
     
     This step is mandatory if the **-r** *replymode* parameter is set to **3** in the [**ping vxlan**](cmdqueryname=ping+vxlan) command on the source.
  3. Enable the VXLAN ping function on the destination, and set the listening port number for the VXLAN server.
     
     
     ```
     [nqa vxlanecho enable](cmdqueryname=nqa+vxlanecho+enable) ipv6 udp-port udpPort6 [ source-ip-interface { ifName6 | ifType6 ifNum6 } ]
     ```
  4. Initiate a connectivity test for an IPv6 VXLAN tunnel.
     
     
     ```
     [ping vxlan](cmdqueryname=ping+vxlan) [ -c count | -m interval | -t timeout | -r replymode | -a innersrc-address6 | -tos tos ] * ipv6 vni vniid source source-address6 peer dest-address6 [ udp-port dest-port ] [ load-balance { vxlan-source-udpport vxlan-source-udpport [ vxlan-source-end-udpport ] | { source-address lb-src-address destination-address lb-dst-address protocol { udp | lb-protocolid } source-port lb-src-port destination-port lb-dst-port source-mac source-mac destination-mac destination-mac } } ]
     ```
  
  
  
  The command output contains the following information:
  
  + Response to each test packet: If no response packet is received before the timer on the source expires, the message "Request time out" is displayed. If a response packet is received, information such as the number of bytes in the payload, packet sequence number, and response time is displayed.
  + Ping statistics: include the numbers of sent and received packets, the packet loss rate, and the minimum, maximum, and average response time durations.

#### Example

* Test connectivity of the IPv4 VXLAN tunnel between the source 10.1.1.1 and the destination 10.2.2.1.
  ```
  <HUAWEI> ping vxlan vni 111 source 10.1.1.1 peer 10.2.2.1 udp-port 5001 
  PING VXLAN: vni 111 source 10.1.1.1 peer 10.2.2.1, press CTRL_C to break
      Reply from 10.2.2.1 bytes=52 Sequence=1 time=3 ms
      Reply from 10.2.2.1 bytes=52 Sequence=2 time=3 ms
      Reply from 10.2.2.1 bytes=52 Sequence=3 time=2 ms
      Reply from 10.2.2.1 bytes=52 Sequence=4 time=3 ms
      Reply from 10.2.2.1 bytes=52 Sequence=5 time=3 ms
  
    --- ping vxlan statistics ---
      5 packet(s) transmitted
      5 packet(s) received
      0.00% packet loss
      round-trip min/avg/max = 2/2/3 ms
  ```
* Test connectivity of the IPv6 VXLAN tunnel between the source 2001:DB8:1::1 and the destination 2001:DB8:2::1.
  ```
  <HUAWEI> ping vxlan ipv6 vni 60 source 2001:DB8:1::1 peer 2001:DB8:2::1
  PING VXLAN IPV6: vni 60 source 2001:DB8:1::1 peer 2001:DB8:2::1, press CTRL_C to break
      Reply from 2001:DB8:2::1 
      bytes=52 Sequence=1 time=167 ms
      Reply from 2001:DB8:2::1 
      bytes=52 Sequence=2 time=2 ms
      Reply from 2001:DB8:2::1 
      bytes=52 Sequence=3 time=1 ms
      Reply from 2001:DB8:2::1 
      bytes=52 Sequence=4 time=2 ms
      Reply from 2001:DB8:2::1 
      bytes=52 Sequence=5 time=2 ms
  
    --ping vxlan statistics--
      5 packet(s) transmitted
      5 packet(s) received
      0.00% packet loss
      round-trip min/avg/max = 1/34/167 ms 
  ```