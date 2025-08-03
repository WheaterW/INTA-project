Using Tracert to Detect a Path on a VXLAN Network
=================================================

Using Tracert to Detect a Path on a VXLAN Network

#### Prerequisites

Before using the VXLAN tracert function to detect a path between two devices on a VXLAN network, ensure that the VXLAN network has been configured correctly.

![](../public_sys-resources/note_3.0-en-us.png) 

This function is supported only on the CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885, CE6885-SAN, CE6885-LL (standard forwarding mode), CE6885-T, CE6863E-48S8CQ, CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, CE8850-HAM, and CE6820H, CE6820H-K, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820S.



#### Context

The following uses a static IPv4 VXLAN tunnel as an example to describe the VXLAN tracert process.

**Figure 1** VXLAN network diagram  
![](figure/en-us_image_0000001176744463.png)
A VNI-based VXLAN tracert test can be initiated on DeviceA (source) to detect the path between DeviceA and DeviceC (destination). The tracert process is as follows:

1. DeviceA sends test packets to DeviceC. The tracert test can be initiated by specifying parameters of the following combinations:
   * VNI, source VTEP IP address, and destination VTEP IP address
   * VNI, source VTEP IP address, destination VTEP IP address, and VXLAN source port number
   * VNI, source VTEP IP address, destination VTEP IP address, and 7-tuple information
2. When DeviceB receives a packet with the TTL being 1, it decrements the TTL value to 0 and responds with an ICMP Time Exceeded message.
3. After receiving the ICMP Time Exceeded message, DeviceA sends a test packet with the TTL incremented by 1.
4. Upon receipt of the test packet, DeviceC verifies the VNI information and responds with an ICMP Port Unreachable message.
5. DeviceA receives the ICMP Port Unreachable message from DeviceC. The VXLAN tracert test is now complete.

![](../public_sys-resources/note_3.0-en-us.png) 

If the tracert packets used to detect IP network connectivity traverse a VXLAN tunnel, the **tracert** command output does not contain transit node information about the VXLAN tunnel.



#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. (Optional) Enable the VXLAN tracert function on the source.
   1. Enable the VXLAN tracert function, and configure the UDP port number used in VXLAN packets.
      
      
      ```
      [nqa vxlanecho enable](cmdqueryname=nqa+vxlanecho+enable) udp-port udpPort [ source-ip-interface { ifName | ifType ifNum } ]
      ```
   2. Commit the configuration.
      
      
      ```
      [commit](cmdqueryname=commit)
      ```
   
   ![](../public_sys-resources/note_3.0-en-us.png) 
   
   This step is mandatory if the **-r** *replymode* parameter is to be set to **3** in the [**tracert vxlan**](cmdqueryname=tracert+vxlan) command on the source.
3. Enable the VXLAN tracert function on the destination.
   1. Enable the VXLAN tracert function, and configure the UDP port number used in VXLAN packets.
      
      
      ```
      [nqa vxlanecho enable](cmdqueryname=nqa+vxlanecho+enable) udp-port udpPort [ source-ip-interface { ifName | ifType ifNum } ]
      ```
   2. Commit the configuration.
      
      
      ```
      [commit](cmdqueryname=commit)
      ```
4. Detect the path between two devices on an IPv4 VXLAN network.
   
   
   ```
   [tracert vxlan](cmdqueryname=tracert+vxlan) [ -t timeout | -r replymode | -a innersrc-address | -h maxttl ] * vni vniid source source-address peer dest-address [ udp-port dest-port ] [ pipe ] [ load-balance { vxlan-source-udpport vxlan-source-udpport | { source-address lb-src-address destination-address lb-dst-address protocol { udp | lb-protocolid } source-port lb-src-port destination-port lb-dst-port source-mac lb-sourcemac destination-mac lb-destinationmac } } ]
   ```

#### Example

Detect the path between the source 10.1.2.1 and the destination 10.2.2.1 on an IPv4 VXLAN network.

```
<HUAWEI> tracert vxlan vni 111 source 10.1.2.1 peer 10.2.2.1 udp-port 5000 
TRACERT VXLAN: vni 111 source 10.1.2.1 peer 10.2.2.1, press CTRL_C to break
TTL   Replier            Time    Ingress Port           Egress Port                 
1     10.1.1.1           94 ms   100GE1/0/1            100GE1/0/2  
2     10.2.2.1           94 ms   100GE1/0/1             --
```