Setting a BGP ConnectRetry Timer
================================

Setting a BGP ConnectRetry Timer

#### Prerequisites

Before setting a BGP ConnectRetry timer, you have completed the following task:

* [Configure basic BGP functions.](vrp_bgp_cfg_0014.html)

#### Context

The ConnectRetry timer starts after BGP initiates a TCP connection and ends after the TCP connection is established successfully. If the first attempt to establish a TCP connection fails, BGP attempts to reestablish the TCP connection once the ConnectRetry timer expires.

* Setting a short ConnectRetry interval reduces the period BGP waits between attempts to establish a TCP connection, which speeds up the establishment of the TCP connection.
* Setting a long ConnectRetry interval helps suppress routing flapping caused by peer relationship flapping.

A ConnectRetry timer can be configured for one or all peers or peer groups. A ConnectRetry timer configured for a specific peer takes precedence over that configured for the peer group of this peer. In addition, the timer configured for a specific peer or peer group takes precedence over that configured for all peers or peer groups.


#### Procedure

* Set a BGP ConnectRetry timer for all peers or peer groups.
  
  
  
  Perform the following steps on a BGP device:
  
  
  
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the BGP view.
     
     
     ```
     [bgp](cmdqueryname=bgp) as-number
     ```
  3. Set a BGP ConnectRetry timer for all peers or peer groups of the device.
     
     
     ```
     [timer connect-retry](cmdqueryname=timer+connect-retry) connect-retry-time
     ```
     
     By default, the ConnectRetry timer value is 32s.
  4. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Configure a BGP ConnectRetry timer for a specified peer or peer group.
  
  
  
  Perform the following steps on a BGP device:
  
  
  
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
     [peer](cmdqueryname=peer+timer+connect-retry) { group-name | ipv4-address } timer connect-retry connect-retry-time
     ```
     
     By default, the ConnectRetry timer value is 32s.
  4. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```