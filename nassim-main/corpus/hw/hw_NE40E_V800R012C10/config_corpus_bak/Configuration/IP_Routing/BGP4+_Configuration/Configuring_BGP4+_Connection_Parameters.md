Configuring BGP4+ Connection Parameters
=======================================

By configuring BGP4+ connection parameters, you can optimize BGP4+ network performance.

#### Usage Scenario

BGP4+ can use various timers to minimize the impact of interface flapping or route flapping.

* Timers for BGP4+ Peers
  
  After establishing a BGP4+ connection, two peers periodically send Keepalive messages to each other to detect the status of the BGP4+ peer relationship. If the Router does not receive any Keepalive message or any other type of packets from its peer within a time of period called holdtime period, it considers the BGP4+ connection closed.
  
  When establishing a BGP4+ connection with a peer, the Router compares the hold time values of the two peers. The smaller hold time is used as the negotiated hold time. If the negotiation result is 0, no Keepalive message is sent and whether the Hold timer expires is not detected.
  
  ![](../../../../public_sys-resources/notice_3.0-en-us.png) 
  
  If the value of the timer changes, the BGP4+ connection is interrupted for a short time because the peers need to renegotiate with each other.
* BGP4+ ConnectRetry Timer
  
  After BGP4+ initiates a TCP connection, the ConnectRetry timer will be stopped if the TCP connection is established successfully. If the first attempt to establish a TCP connection fails, BGP4+ re-establishes the TCP connection after the ConnectRetry timer expires. Setting a short ConnectRetry interval reduces the period BGP4+ waits between attempts to establish a TCP connection, which speeds up the establishment of the TCP connection. Setting a long connectRetry interval suppresses routing flapping caused by peer relationship flapping.

#### Pre-configuration Tasks

Before configuring BGP4+ connection parameters, [configure basic BGP4+ functions](dc_vrp_bgp6_cfg_0003.html).


[Configuring Timers for BGP4+ Peers](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bgp6_cfg_0037.html)

Configuring timers properly improves network performance. Changing BGP4+ timer values, however, will interrupt peer relationships.

[Enabling Fast EBGP Connection Reset](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bgp6_cfg_0038.html)

After fast EBGP connection reset is enabled, BGP4+ can rapidly detect EBGP link faults and reset BGP4+ connections on interfaces.

[Configuring a BGP4+ ConnectRetry Timer](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bgp6_cfg_0045.html)

You can control the speed at which BGP4+ peer relationships are established by changing the BGP4+ ConnectRetry timer value.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bgp6_cfg_0039.html)

After configuring BGP4+ connection parameters, check information about BGP4+ peers or peer groups.