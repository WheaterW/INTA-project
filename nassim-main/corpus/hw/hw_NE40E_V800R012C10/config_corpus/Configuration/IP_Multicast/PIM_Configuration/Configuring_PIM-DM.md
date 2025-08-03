Configuring PIM-DM
==================

This section describes how to configure Protocol Independent Multicast-Dense Mode (PIM-DM). On a small network with densely distributed members, there can be members on each network segment. PIM-DM can be used to construct and maintain a multicast distribution tree to forward multicast data.

#### Usage Scenario

PIM-DM assumes that all members are densely distributed on the network and each network segment may have members. According to the assumption, the multicast source floods multicast data to each network segment and then prunes the network segment that does not have any member. Through periodic flooding and pruning, PIM-DM creates and maintains a unidirectional loop-free shortest path tree (SPT) that connects the multicast source and group members. [Figure 1](#EN-US_TASK_0172366819__fig_dc_vrp_multicast_cfg_227302) shows the function and position of PIM-DM on a multicast network.

**Figure 1** Application of PIM-DM on a multicast network  
![](images/fig_dc_vrp_multicast_cfg_227302.png)
![](../../../../public_sys-resources/note_3.0-en-us.png) 

Protocol Independent Multicast-Sparse Mode (PIM-SM) applies to large-scale networks with sparse members. For configuration details, see [Configuring PIM-SM](dc_vrp_multicast_cfg_0006.html).



#### Pre-configuration Tasks

Before configuring PIM-DM, configure a unicast routing protocol to ensure normal unicast routing on the network.


[Enabling PIM-DM](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_2267.html)

This section describes how to enable PIM-DM. On a PIM-DM network, PIM-DM must be enabled on interfaces for the Router to set up PIM neighbor relationships with neighboring devices to process data from them.

[(Optional) Disabling State-Refresh](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_2268.html)

This section describes how to disable State-Refresh. State-Refresh can be disabled if all clients receive multicast data. When State-Refresh is disabled on an interface, the interface does not forward State-Refresh messages.

[(Optional) Modifying State-Refresh control parameters](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_2269.html)

This section describes how to modify State-Refresh control parameters. You can configure the interval at which State-Refresh messages are sent, the timeout period for receiving the next State-Refresh message, and the TTL of State-Refresh messages.

[(Optional) Modifying Graft Control Parameters](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_2270.html)

This section describes how to modify graft control parameters. You can configure the interval at which Graft messages are sent according to the actual situation.

[(Optional) Configuring a Limit on the Number of PIM Entries](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_2281.html)

PIM-DM allows you to limit the number of (S, G) and (\*, G) entries separately. After a specified limit is reached, new entries of the corresponding type cannot be created.

[Verifying the PIM-DM Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_2271.html)

After configuring PIM-DM, verify PIM interfaces, PIM neighbors, and the PIM routing table.