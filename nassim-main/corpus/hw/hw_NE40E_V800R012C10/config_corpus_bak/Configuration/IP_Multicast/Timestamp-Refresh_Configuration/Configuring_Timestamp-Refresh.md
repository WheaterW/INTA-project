Configuring Timestamp-Refresh
=============================

Timestamp-refresh allows a device to refresh the timestamps in RTP packets of input multicast streams that match the traffic policy on the multicast inbound interface to be synchronous with the local time of the device.

#### Usage Scenario

On the network shown in [Figure 1](#EN-US_TASK_0000001461116933__fig1815510644719), after timestamp-refresh is configured on the router where the switching is performed, a traffic policy on the inbound interface filters input multicast streams, and the traffic behavior is associated with a timestamp-refresh instance. Then the mapping between the input multicast streams and the multicast instance is established based on the traffic policy. After establishing the mapping, the router determines the timestamp in the packets of multicast streams and the local time, calculates the offset value for timestamp-refresh, and uses the offset value to refresh the timestamp of multicast streams in a unified manner.

**Figure 1** Networking diagram of timestamp-refresh  
![](figure/en-us_image_0000001445870710.png)![](../../../../public_sys-resources/note_3.0-en-us.png) 

Currently, the timestamp-refresh function supports IPv4 but not IPv6. After IPv6 traffic is configured, this function does not take effect.

Timestamp-refresh alone cannot ensure traffic forwarding. It must be configured with a traffic forwarding function, such as [multicast NAT](dc_ne_multicast_cfg_0005.html), or [PIM](../vrp/dc_vrp_multicast_cfg_0003.html) to allow traffic to be forwarded and the function to take effect.



[Creating a Timestamp-Refresh Instance](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_timestamp_refresh_cfg_0003.html)

When you create a timestamp-refresh instance, the timestamp-refresh instance view is directly displayed. In this view, you can configure the update threshold, type, mode, and offset value for the instance. The purpose of creating a timestamp-refresh instance is to associate this instance with input multicast streams. This simplifies the timestamp-refresh configuration.

[Configuring a Timestamp-Refresh Traffic Policy](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_timestamp_refresh_cfg_0004.html)

After a timestamp-refresh instance is created, you can configure a traffic behavior and bind it to the timestamp-refresh instance in the traffic behavior view. After the traffic policy is applied to the inbound interface of multicast streams, input multicast streams are associated with the timestamp-refresh instance.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_timestamp_refresh_cfg_0005.html)

After timestamp-refresh is configured successfully, you can view the local and global timestamp-refresh offset values and the configurations of timestamp-refresh instances.