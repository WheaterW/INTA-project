Configuring BFD for BGP
=======================

BFD for BGP provides BGP with a fast fault detection mechanism, which speeds up network convergence.

#### Usage Scenario

Currently, voice and video services are widely applied. These services are quite sensitive to the packet loss and delay. BGP periodically sends Keepalive messages to a peer to monitor the peer's status, but this mechanism takes an excessively long time, more than 1 second, to detect a fault. When the data transmission rate reaches the level of Gbit/s, such slow detection will cause a large amount of data to be lost. As a result, the requirement for high reliability of carrier-class networks cannot be met.

To address this issue, BFD for BGP can be configured. BFD for BGP can detect faults on links between BGP peers within milliseconds. This speeds up link detection, ensures fast link switching, and reduces traffic loss.


#### Pre-configuration Tasks

Before configuring BFD for BGP, complete the following tasks:

* Configure link layer protocol parameters and IP addresses for interfaces and ensure that the link layer protocol on the interfaces is up.
* [Configure basic BGP functions.](dc_vrp_bgp_cfg_3004.html)

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bfd**](cmdqueryname=bfd)
   
   
   
   BFD is enabled globally on the local device.
3. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
4. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
5. Run [**peer**](cmdqueryname=peer+bfd+enable+single-hop-prefer) { *group-name* | *ipv4-address* } **bfd** **enable** [ **single-hop-prefer** ] [ **compatible** ]
   
   
   
   BFD is configured for a peer or peer group, and default BFD parameters are used to establish a BFD session.
   
   
   
   A BFD session can be established only when the peer relationship is in the Established state.
   
   After BFD is enabled for a peer group, BFD sessions will be created on the peers that belong to this peer group and are not configured with the [**peer bfd block**](cmdqueryname=peer+bfd+block) command.
   
   The **compatible** parameter configures the compatibility mode, which ensures that the local and peer devices use the same detection mode when a Huawei device is connected to a non-Huawei device. The **compatible** parameter must be used together with the **single-hop-prefer** parameter.
   * In the scenario where Huawei devices are interconnected, the same parameters must be configured on the local and peer devices. If the devices are configured with different BFD parameters, services may be affected.
   * In the scenario where a Huawei device is connected to a non-Huawei device, to implement BFD interworking, select a proper configuration mode from the following table to ensure consistent configurations on the local and peer devices.
     
     **Table 1** Configuration modes for the **compatible** and **single-hop-prefer** parameters
     | Whether **single-hop-prefer** Is Configured | Whether **compatible** Is Configured | Direct IBGP Scenario | Multi-hop IBGP Scenario | Direct EBGP Scenario | Multi-hop EBGP Scenario |
     | --- | --- | --- | --- | --- | --- |
     | N | N | In the packets sent by BFD, the UDP port number is 4784, and the TTL is 253. | In the packets sent by BFD, the UDP port number is 4784, and the TTL is 253. | In the packets sent by BFD, the UDP port number is 3784, and the TTL is 255. | In the packets sent by BFD, the UDP port number is 4784, and the TTL is 253. |
     | Y | N | In the packets sent by BFD, the UDP port number is 3784, and the TTL is 255. | In the packets sent by BFD, the UDP port number is 4784, and the TTL is 253. | In the packets sent by BFD, the UDP port number is 3784, and the TTL is 255. | In the packets sent by BFD, the UDP port number is 4784, and the TTL is 253. |
     | N | Y | In the packets sent by BFD, the UDP port number is 4784, and the TTL is 255. | In the packets sent by BFD, the UDP port number is 4784, and the TTL is 255. | In the packets sent by BFD, the UDP port number is 3784, and the TTL is 255. | In the packets sent by BFD, the UDP port number is 4784, and the TTL is 255. |
     | Y | Y | In the packets sent by BFD, the UDP port number is 3784, and the TTL is 255. | In the packets sent by BFD, the UDP port number is 4784, and the TTL is 255.  If the peer UDP port number is 3784, the local BFD session can learn the port number and change the local UDP port number to 3784. | In the packets sent by BFD, the UDP port number is 3784, and the TTL is 255. | In the packets sent by BFD, the UDP port number is 4784, and the TTL is 255.  If the peer UDP port number is 3784, the local BFD session can learn the port number and change the local UDP port number to 3784. |
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     In the preceding table, the UDP port numbers in the packets sent by BFD are those obtained during initial negotiation. BFD has the automatic adaptation function. If the UDP port number of a received response packet is different from that of the sent packet, BFD automatically changes the UDP port number of the sent packet to be the same as that in the peer end.
6. (Optional) Run [**peer**](cmdqueryname=peer+bfd+min-tx-interval+min-rx-interval+detect-multiplier) { *group-name* | *ipv4-address* } **bfd** { **min-tx-interval** *min-tx-interval* | **min-rx-interval** *min-rx-interval* | **detect-multiplier** *multiplier* } \*
   
   
   
   BFD session parameters are modified.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The BFD parameters of a single peer take precedence over those of a peer group. If BFD parameters are configured on peers, they will be used in BFD session establishment.
   
   When changing the default values, pay attention to the network status and the network reliability requirement. A short interval for transmitting BFD packets can be configured for a link that has a higher reliability requirement. A long interval for transmitting BFD packets can be configured for a link that has a lower reliability requirement.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   There are three formulas: Actual interval for the local device to send BFD packets = max {Locally configured interval for transmitting BFD packets, Remotely configured interval for receiving BFD packets}, Actual interval for the local device to receive BFD packets = max {Remotely configured interval for transmitting BFD packets, Locally configured interval for receiving BFD packets}, and Local detection period = Actual interval for receiving BFD packets x Remotely configured BFD detection multiplier.
   
   For example:
   
   * On the local device, the configured interval for transmitting BFD packets is 200 ms, the interval for receiving BFD packets is 300 ms, and the detection multiplier is 4.
   * On the peer device, the configured interval for transmitting BFD packets is 100 ms, the interval for receiving BFD packets is 600 ms, and the detection multiplier is 5.
   
   Then:
   
   * On the local device, the actual interval for transmitting BFD packets is 600 ms calculated by using the formula max {200 ms, 600 ms}; the interval for receiving BFD packets is 300 ms calculated by using the formula max {100 ms, 300 ms}; the detection period is 1500 ms calculated by multiplying 300 ms by 5.
   * On the peer device, the actual interval for transmitting BFD packets is 300 ms calculated by using the formula max {100 ms, 300 ms}; the interval for receiving BFD packets is 600 ms calculated by using the formula max {200 ms, 600 ms}; the detection period is 2400 ms calculated by multiplying 600 ms by 4.
7. (Optional) Run [**peer**](cmdqueryname=peer+bfd+valid-ttl-hops) { *group-name* | *ipv4-address* } **bfd** **valid-ttl-hops** *valid-ttl-hops-value*
   
   
   
   A TTL value is set for checking the BFD session with a specified peer or peer group.
   
   
   
   In scenarios where EBGP peers are indirectly connected, you can configure a TTL value for a BFD session so that the traffic forwarding path is quickly adjusted if BFD detects a fault on the link between the local device and the specified BGP peer. Specifically, the local interface used to establish the BFD session forwards only the packets with a TTL value greater than or equal to the configured TTL value. If the TTL value in a BFD packet is smaller than the configured TTL value, the interface discards this packet, the BFD session goes down, and BFD notifies BGP of this event. In this manner, BGP routes are re-converged so that the traffic forwarding path is adjusted.
   
   The [**peer bfd valid-ttl-hops**](cmdqueryname=peer+bfd+valid-ttl-hops) and [**peer bfd enable single-hop-prefer**](cmdqueryname=peer+bfd+enable+single-hop-prefer) commands are mutually exclusive.
   
   
   
   The [**peer bfd valid-ttl-hops**](cmdqueryname=peer+bfd+valid-ttl-hops) and [**peer bfd enable per-link one-arm-echo**](cmdqueryname=peer+bfd+enable+per-link+one-arm-echo) commands are mutually exclusive.
8. (Optional) Run [**peer**](cmdqueryname=peer+bfd+block) *ipv4-address* **bfd** **block**
   
   
   
   A peer is prevented from inheriting the BFD function of the peer group to which it belongs.
   
   
   
   After a peer is added to a peer group enabled with BFD, the peer inherits the BFD configuration of the group and creates a BFD session. To prevent the peer from inheriting the BFD function of the peer group, perform this step.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The [**peer bfd block**](cmdqueryname=peer+bfd+block) command and the [**peer bfd enable**](cmdqueryname=peer+bfd+enable) command are mutually exclusive. After the [**peer bfd block**](cmdqueryname=peer+bfd+block) command is run, the BFD session is automatically deleted.
9. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

After BFD for BGP is configured, you can run the [**display bgp bfd session**](cmdqueryname=display+bgp+bfd+session+vpnv4+vpn-instance+peer+all) { [ **vpnv4** **vpn-instance** *vpn-instance-name* ] **peer** *ipv4-address* | **all** } command to view information about the BFD session established by BGP.