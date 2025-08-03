Adjusting the BGP Network Convergence Speed
===========================================

You can adjust the BGP network convergence speed by adjusting BGP peer connection parameters to adapt to changes on large-scale networks.

#### Usage Scenario

BGP is used to transmit routing information on large-scale networks. Frequent network changes affect the establishment and maintenance of BGP peer relationships, which in turn affects the BGP network convergence speed.

The route dampening and triggered update functions of BGP suppress frequent route changes to a certain extent, but cannot minimize the impact of network flapping on BGP connections.

You can configure BGP timers and disable rapid EBGP connection reset to suppress BGP network flapping and speed up BGP network convergence.

* BGP Keepalive and Hold timers
  
  BGP uses Keepalive messages to maintain BGP peer relationships and monitor connection status. After establishing a BGP connection, two peers send Keepalive messages periodically to each other to detect the BGP connection status based on the Keepalive timer. If a router does not receive any Keepalive message or any other types of packets from its peer within the hold time set by the Hold timer, the router considers the BGP connection interrupted and terminates the BGP connection.
* BGP MinRouteAdvertisementIntervalTimer
  
  BGP does not periodically update a routing table. When BGP routes change, BGP updates the changed BGP routes in the BGP routing table by sending Update messages. If a route changes frequently, to prevent the router from sending Update messages upon every change, set the interval at which Update messages are sent.
* Rapid EBGP peer reset
  
  Rapid EBGP connection reset is enabled by default so that EBGP can quickly detect the status of interfaces used to establish EBGP connections. If the interface status changes frequently, you can disable rapid EBGP connection reset so that direct EBGP sessions will not be reestablished and deleted as interface alternates between Up and Down, which speeds up network convergence.
* BGP ConnectRetry Timer
  
  After BGP initiates a TCP connection, the ConnectRetry timer will be stopped if the TCP connection is established successfully. If the first attempt to establish a TCP connection fails, BGP attempts to establish the TCP connection again after the ConnectRetry timer expires.
  
  Setting a short ConnectRetry interval reduces the period BGP waits between attempts to establish a TCP connection, which speeds up the establishment of the TCP connection.
  
  Setting a long ConnectRetry interval suppresses routing flapping caused by frequent peer relationship flapping.

After slow peer detection is configured on a device, the device identifies the slow BGP peer (if any) and removes it from the update peer-group to prevent this slow peer from affecting route advertisement to other peers in this update peer-group. Slow peer detection speeds up BGP network convergence.


#### Pre-configuration Tasks

Before setting parameters for a BGP peer connection, [configure basic BGP functions](dc_vrp_bgp_cfg_3004.html).


[Configuring BGP Keepalive and Hold Timers](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bgp_cfg_3047.html)

The values of BGP Keepalive and Hold timers determine the speed at which BGP detects network faults. You can adjust the values of these timers to improve network performance.

[Configuring a MinRouteAdvertisementIntervalTimer](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bgp_cfg_3048.html)

A proper MinRouteAdvertisementIntervalTimer can be configured to suppress frequent route changes, improving BGP network stability.

[Disabling Rapid EBGP Connection Reset](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bgp_cfg_3049.html)

Disabling rapid EBGP connection reset can prevent frequent reestablishment and deletion of EBGP sessions if route flapping occurs. This speeds up BGP network convergence.

[Configuring a BGP ConnectRetry Timer](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bgp_cfg_3089.html)

You can control the speed at which BGP peer relationships are established by changing the BGP ConnectRetry timer value.

[Enabling Slow Peer Detection](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bgp_cfg_4099.html)

After slow peer detection is configured on a device, the device identifies the slow BGP peer (if any) and removes it from the update peer-group to prevent this slow peer from affecting route advertisement to other peers in this update peer-group. Slow peer detection speeds up BGP network convergence.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bgp_cfg_3050.html)

After the BGP network convergence speed is adjusted, you can view information about BGP peers and peer groups.