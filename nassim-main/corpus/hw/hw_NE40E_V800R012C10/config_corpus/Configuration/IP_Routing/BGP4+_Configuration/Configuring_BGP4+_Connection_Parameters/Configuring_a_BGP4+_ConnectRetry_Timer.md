Configuring a BGP4+ ConnectRetry Timer
======================================

You can control the speed at which BGP4+ peer relationships are established by changing the BGP4+ ConnectRetry timer value.

#### Context

After BGP4+ initiates a TCP connection, the ConnectRetry timer will be stopped if the TCP connection is established successfully. If the first attempt to establish a TCP connection fails, BGP4+ attempts to reestablish the TCP connection once the ConnectRetry timer expires.

* Setting a short ConnectRetry interval reduces the period BGP4+ waits between attempts to establish a TCP connection, which speeds up the establishment of the TCP connection.
* Setting a long connectRetry interval suppresses routing flapping caused by peer relationship flapping.

A ConnectRetry timer can be configured either for all peers or peer groups, or for a specific peer or peer group. The timer configured for a specific peer takes precedence over that configured for the peer group of the peer. In addition, the timer configured for a specific peer group takes precedence over that configured globally.


#### Procedure

* Configure the ConnectRetry timer globally.
  
  
  
  Perform the following steps on a BGP4+ Router:
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run [**timer connect-retry**](cmdqueryname=timer+connect-retry) *connect-retry-time*
     
     
     
     A BGP4+ ConnectRetry timer is configured for all peers or peer groups.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure a ConnectRetry timer for a specified peer or peer group.
  
  
  
  Perform the following steps on a BGP4+ Router:
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run [**peer**](cmdqueryname=peer+timer+connect-retry) { *group-name* | *ipv6-address* } **timer** **connect-retry** *connect-retry-time*
     
     
     
     A ConnectRetry timer is configured for a specified peer or peer group.
     
     
     
     The ConnectRetry timer configured for a peer takes precedence over that configured for a peer group. The ConnectRetry timer configured for a peer or peer group takes precedence over that configured for all peers or peer groups.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.