Configuring BFD for BGP
=======================

Configuring BFD for BGP

#### Prerequisites

Before configuring BFD for BGP, you have completed the following tasks:

* Configure parameters of the link layer protocol and IP addresses for interfaces to ensure that the link layer protocol on the interfaces is up.
* [Configure basic BGP functions.](vrp_bgp_cfg_0014.html)

#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enable BFD globally.
   
   
   ```
   [bfd](cmdqueryname=bfd)
   ```
3. Return to the system view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
4. Enter the BGP view.
   
   
   ```
   [bgp](cmdqueryname=bgp) as-number
   ```
5. Configure BFD for a peer or peer group, and establish a BFD session using default parameters.
   
   
   ```
   [peer](cmdqueryname=peer+bfd+enable+single-hop-prefer+compatible) { group-name | ipv4-address } bfd enable [ [ single-hop-prefer ] [ compatible ]|[ per-link ] one-arm-echo ]
   ```
   
   A BFD session can be established only when the peer relationship is in the Established state.
   
   After BFD is enabled for a peer group, BFD sessions will be created on the peers that belong to this peer group and that are not configured with the [**peer bfd block**](cmdqueryname=peer+bfd+block) command.
6. (Optional) Modify BFD session parameters.
   
   
   ```
   [peer](cmdqueryname=peer) { group-name | ipv4-address } bfd { min-tx-interval min-tx-interval | min-rx-interval min-rx-interval | detect-multiplier multiplier } *
   ```
   
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   The BFD parameters of peers take precedence over those of peer groups. As such, if BFD parameters are configured on peers, they will be used in BFD session establishment.
   
   In most cases, default values are used for the minimum interval for transmitting BFD messages and the default detection multiplier. When changing the default values, take note of the network status and network reliability requirements. A short interval for transmitting BFD messages can be configured for a link that has a higher reliability requirement, while a long interval can be configured for a link with a lower reliability requirement.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   There are three formulas: Minimum interval for the local device to send BFD messages = Max {Locally configured interval for transmitting BFD messages, remotely configured interval for receiving BFD messages}; Minimum interval for the local device to receive BFD messages = Max {Remotely configured interval for transmitting BFD messages; Locally configured interval for receiving BFD messages}; Local detection period = Actual interval for receiving BFD messages x Remotely configured BFD detection multiplier.
   
   For example:
   
   * On the local device, the configured interval for transmitting BFD messages is 200 ms, the interval for receiving BFD messages is 300 ms, and the detection multiplier is 4.
   * On the peer device, the configured interval for transmitting BFD messages is 100 ms, the interval for receiving BFD messages is 600 ms, and the detection multiplier is 5.
   
   Then:
   
   * On the local device, the actual interval for transmitting BFD messages is 600 ms calculated using the formula max {200 ms, 600 ms}; the interval for receiving BFD messages is 300 ms calculated using the formula max {100 ms, 300 ms}; the detection period is 1500 ms calculated by multiplying 300 ms by 5.
   * On the peer device, the actual interval for transmitting BFD messages is 300 ms calculated using the formula max {100 ms, 300 ms}; the interval for receiving BFD messages is 600 ms calculated using the formula max {200 ms, 600 ms}; the detection period is 2400 ms calculated by multiplying 600 ms by 4.
7. (Optional) Prevent a peer from inheriting the BFD function from a peer group.
   
   
   ```
   [peer](cmdqueryname=peer+bfd+block) ipv4-address bfd block
   ```
   
   If a peer joins a peer group enabled with BFD, the peer inherits the BFD configuration of the group and creates a BFD session. To prevent the peer from inheriting the BFD function of the peer group, perform this step.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   The [**peer bfd block**](cmdqueryname=peer+bfd+block) and [**peer bfd enable**](cmdqueryname=peer+bfd+enable) commands are mutually exclusive. After the [**peer bfd block**](cmdqueryname=peer+bfd+block) command is run, the BFD session is automatically deleted.
8. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

After configuring BFD for BGP, check the configurations.

* Run the [**display bgp bfd session**](cmdqueryname=display+bgp+bfd+session) { **peer** *ipv4-address* | **all** } command to check information about the BFD sessions established between BGP peers.