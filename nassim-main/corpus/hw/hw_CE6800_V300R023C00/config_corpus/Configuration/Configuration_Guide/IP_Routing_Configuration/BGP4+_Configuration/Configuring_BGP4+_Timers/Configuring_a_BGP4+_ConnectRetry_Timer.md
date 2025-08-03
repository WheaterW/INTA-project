Configuring a BGP4+ ConnectRetry Timer
======================================

Configuring a BGP4+ ConnectRetry Timer

#### Prerequisites

Before configuring a BGP4+ ConnectRetry timer, you have completed the following task:

* [Configure basic BGP4+ functions](vrp_bgp6_cfg_0006.html).

#### Context

The ConnectRetry timer starts after BGP4+ initiates a TCP connection and ends after the TCP connection is established successfully. If the first attempt to establish a TCP connection fails, BGP4+ attempts to reestablish the TCP connection once the ConnectRetry timer expires.

* Setting a short ConnectRetry interval reduces the period BGP4+ waits between attempts to establish a TCP connection, which speeds up the establishment of the TCP connection.
* Setting a long ConnectRetry interval helps suppress routing flapping caused by peer relationship flapping.

A ConnectRetry timer can be configured either for a specified or all peers or peer groups. A ConnectRetry timer configured for a specific peer takes precedence over that configured for the peer group of this peer. In addition, a ConnectRetry timer configured for a specific peer or peer group takes precedence over that configured for all peers or peer groups.


#### Procedure

* Configure the ConnectRetry timer globally.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the BGP view.
     
     
     ```
     [bgp](cmdqueryname=bgp) as-number
     ```
  3. Set a BGP4+ ConnectRetry timer globally.
     
     
     ```
     [timer connect-retry](cmdqueryname=timer+connect-retry) connect-retry-time
     ```
     
     By default, the ConnectRetry timer value is 32s.
  4. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Set a ConnectRetry timer for a specified peer or peer group.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the BGP view.
     
     
     ```
     [bgp](cmdqueryname=bgp) as-number
     ```
  3. Set a ConnectRetry timer for a specified peer or peer group.
     
     
     ```
     [peer](cmdqueryname=peer+timer+connect-retry) { group-name | ipv6-address } timer connect-retry connect-retry-time
     ```
     
     By default, the ConnectRetry timer value is 32s.
     
     
     
     The ConnectRetry timer configured for a peer or peer group takes precedence over that configured for all peers or peer groups.
  4. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```