Configuring Passive BFD Echo
============================

Configuring Passive BFD Echo

#### Context

BFD Echo is a rapid fault detection mechanism in which the local system sends BFD Echo packets and the remote system loops back the packets. Passive Echo applies only to single-hop IP links.

BFD mainly works in asynchronous mode (for details, see [BFD Detection Mechanism](vrp_bfd_cfg_0003.html#EN-US_CONCEPT_0000001130622344__section_dc_vrp_bfd_feature_000601)). In this mode, BFD supports the Echo function, which is an auxiliary function specific to the mode. If the peer device that supports the Echo function is deployed on a network, you can enable passive BFD Echo on the local device to interwork with the peer device.

In passive Echo, two devices are directly connected, and a BFD session in asynchronous mode is set up on each device. After the Echo and passive Echo functions are enabled on both devices, they work in asynchronous Echo mode and send BFD packets to each other. Before passive Echo is enabled, BFD in asynchronous mode can only adopt the larger detection interval supported by one end; however, after passive Echo is enabled, the smaller interval is adopted for fast link fault detection.

As shown in [Figure 1](#EN-US_TASK_0000001130622336__fig_dc_vrp_bfd_feature_000501), DeviceA is directly connected to DeviceB, and a BFD session in asynchronous mode is set up on each device. After the Echo and passive Echo functions are enabled on DeviceB and DeviceA respectively, the two devices work in asynchronous Echo mode and send BFD packets to each other. If DeviceA has a higher BFD performance than DeviceB, for example, the minimum intervals for receiving BFD packets supported by DeviceA and DeviceB are 3 ms and 100 ms respectively, BFD sessions in asynchronous mode can only adopt the larger interval (100 ms). After passive Echo is enabled, the smaller interval is adopted for fast link detection. If passive Echo is disabled, DeviceA and DeviceB can still send BFD packets to detect link failures, but the larger interval is used instead.

**Figure 1** Network diagram of configuring passive BFD Echo  
![](figure/en-us_image_0000001176661909.png)

[Figure 1](#EN-US_TASK_0000001130622336__fig_dc_vrp_bfd_feature_000501) shows the process of establishing a passive BFD Echo session:

1. DeviceB functions as the BFD session initiator and sends a BFD packet to DeviceA. The Required Min Echo RX Interval field value carried in the packet is greater than 0, which requires DeviceA to support passive BFD Echo.
2. After receiving the packet, DeviceA checks the value of the Required Min Echo RX Interval field, which is greater than 0. If DeviceA has passive BFD Echo enabled, it checks whether any ACL that restricts passive BFD Echo is referenced, and if such one is referenced, only the BFD session that matches specific ACL rules can enter the Echo mode. If no ACL is referenced, the BFD session immediately enters Echo mode.
3. DeviceB periodically sends BFD packets, and DeviceA sends BFD packets (the source and destination IP addresses are the local IP address, and the destination physical address is DeviceB's physical address) at the locally configured minimum interval for receiving BFD packets. Both DeviceA and DeviceB start a receive timer, with the receive interval being the same as the interval at which they each send BFD packets.

#### Procedure

1. Enter the system view.
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. (Optional) Create a basic ACL.
   ```
   [acl](cmdqueryname=acl) { name basic-acl-name { basic | [ basic ] number basic-acl-number } | [ number ] basic-acl-number }
   ```
3. (Optional) Configure an ACL rule.
   ```
   [rule](cmdqueryname=rule) [ rule-id ] [ name rule-name ] { deny | permit } [ fragment-type { fragment | non-fragment | non-subseq | fragment-subseq | fragment-spe-first } | source { source-ip-address { source-wildcard | 0 | src-netmask } | any } | time-range time-name | vpn-instance vpn-instance-name ] *
   ```
4. (Optional) Return to the system view.
   ```
   [quit](cmdqueryname=quit)
   ```
5. Enter the BFD view.
   ```
   [bfd](cmdqueryname=bfd)
   ```
6. Enable passive BFD Echo.
   ```
   [echo-passive](cmdqueryname=echo-passive) { all | acl basic-acl-number }
   ```
   * **all**: enables passive Echo for all BFD sessions.
   * **acl**: enables passive Echo for BFD sessions that match the configured ACL rule. You can enable passive Echo for BFD packets that match the permit action and disable passive Echo for BFD packets that match the deny action or do not match any ACL rules.![](public_sys-resources/note_3.0-en-us.png) 
   
   If an ACL rule is created or modified after a BFD session goes up, this ACL rule can take effect only after the BFD session goes down and then up or the parameters of the BFD session are modified.
7. Commit the configuration.
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display bfd session**](cmdqueryname=display+bfd+session) { **all** { [ **for-ip** ] | **for-ipv6** } | **discriminator** *discr-value* | **dynamic** | **peer-ip** { *peer-ip* [ **vpn-instance** *vpn-instance-name* ] | **default-ip** } | **peer-ipv6** *peer-ipv6* [ **vpn-instance** *vpn-instance-name* ] | **static** { [ **for-ip** ] | **for-ipv6** } | **static-auto** } [ **verbose** ] command to check BFD session information.