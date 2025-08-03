Adjusting DS-Lite Performance
=============================

DS-Lite performance on a DS-Lite device can be improved.

#### Usage Scenario

You can configure the following parameters to adjust DS-Lite performance:

* Aging time of session entries: The time of aging session entries for each protocol can be set. After a specified aging time elapses, DS-Lite session entries for a specific protocol automatically age so that a DS-Lite device can release resources.
* TCP maximum segment size (MSS) adjustment: When the MTU of a link is small, DS-Lite packets may be fragmented. You can change the MSS value of TCP packets so that DS-Lite packets do not need to be fragmented, improving the DS-Lite conversion efficiency.

#### Pre-configuration Tasks

Before adjusting DS-Lite performance, complete the following tasks:

* Configure basic DS-Lite functions.
* Configure DS-Lite translation for user traffic.


[Setting the Aging Time of DS-Lite Sessions](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ds-lite_cfg_0055.html)

The aging time of DS-Lite sessions of each protocol can be set. After the configured aging time elapses, DS-Lite sessions age, and system resources can be released.

[Setting the MTU Value for DS-Lite Services](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ds-lite_cfg_0071.html)

You can change the MTU value so that the packets for DS-Lite are not fragmented, improving DS-Lite translation efficiency.

[Setting the TCP MSS Value in DS-Lite Service Packets](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ds-lite_cfg_0056.html)

The maximum segment size (MSS) value defined in TCP specifies the length of a TCP packet to be sent without fragmentation. Two devices exchange SYN packets to negotiate the MSS value for a TCP connection to be established.

[Verifying the Configuration of Adjusting DS-Lite Performance](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ds-lite_cfg_0057.html)

After configuring the DS-Lite performance parameters, you can run display commands to verify the configuration.