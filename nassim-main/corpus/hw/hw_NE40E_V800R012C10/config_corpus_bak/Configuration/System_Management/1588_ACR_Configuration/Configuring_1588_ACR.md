Configuring 1588 ACR
====================

In a 1588 ACR domain, a clock client establishes a client/server relationship only with a remote clock server. The client initiates unicast negotiation requests to the server and uses 1588v2 packets to implement clock recovery.

#### Applicable Environment

On the IP RAN shown in [Figure 1](#EN-US_TASK_0000001778921454__fig_dc_ne_1588v2_cfg_503101), two PEs are connected by a Layer 3 network deployed with 1588v2-unaware devices. PE1 attached to an NGC is connected to a BITS. 1588 ACR-capable PE2 initiates a request for negotiation and exchanges unicast packets with PE1 to set up a connection. If the connection is successful, PE2 exchanges 1588v2 packets with PE1 over the connection to implement clock synchronization.

**Figure 1** Network diagram of 1588 ACR  
![](figure/en-us_image_0000001825721057.png)

#### Pre-configuration Tasks

Before configuring 1588 ACR in single-server mode, complete the following tasks:

* Configure static routes or an IGP to ensure IP route reachability among nodes.
* Ensure that the clock server has correctly imported clock signals from a BITS.
* Activate the license file for clock synchronization on the main control board using the [**license active**](cmdqueryname=license+active) *file-name* command. When the clock synchronization license is not loaded, the [**ptp-adaptive enable**](cmdqueryname=ptp-adaptive+enable) configuration is not allowed.![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  Only the M2K and M2K-B support this command.


[Configuring the Unicast Negotiation Function for a Client](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_1588v2_cfg_5032.html)

The unicast negotiation function and parameters for a connection between a client and a clock server are configured on the Router functioning as a 1588 ACR client.

[Configuring the Unicast Negotiation Function for a Server](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_1588v2_cfg_5033.html)

The unicast negotiation function and parameters for a connection between a client and a clock server are configured on the Router functioning as a 1588 ACR clock server.

[(Optional) Adjusting Parameters for Establishing a Unicast Negotiation Connection](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_1588v2_cfg_5034.html)

Adjustable parameters include the maximum number of consecutive Announce packets that the client fails to receive (If the number of unreceived Announce packets exceeds the threshold, the client determines that the connection to the server fails), duration of the Sync, Delay\_Resp, and Announce packets (After the duration of a Sync packet, a Delay\_Resp packet, or an Announce packet expires, the client re-establishes the connection with the server), DSCP value (the DSCP value ensures that 1588v2 packets reach the destination even if a congestion occurs on the network), and the interval at which the server sends Sync, Delay\_Resp, and Announce packets.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_1588v2_cfg_5035.html)

After configuring 1588 ACR on the Router, verify the configuration.