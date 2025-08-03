Configuring a BGP ConnectRetry Timer
====================================

You can control the speed at which BGP peer relationships are established by changing the BGP ConnectRetry timer value.

#### Context

After BGP initiates a TCP connection, the ConnectRetry timer will be stopped if the TCP connection is established successfully. If the first attempt to establish a TCP connection fails, BGP re-establishes the TCP connection after the ConnectRetry timer expires.

* Setting a short ConnectRetry interval reduces the period BGP waits between attempts to establish a TCP connection, which speeds up the establishment of the TCP connection.
* Setting a long ConnectRetry interval suppresses routing flapping caused by frequent peer relationship flapping.

A ConnectRetry timer can be configured either for all peers or peer groups, or for a specific peer or peer group. A ConnectRetry timer configured for a specific peer takes precedence over that configured for the peer group of this peer. In addition, a ConnectRetry timer configured for a specific peer or peer group takes precedence over that configured for all peers or peer groups.


#### Procedure

* Configure a BGP ConnectRetry timer for all peers or peer groups.
  
  
  
  Perform the following steps on a BGP Router:
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run [**timer connect-retry**](cmdqueryname=timer+connect-retry) *connect-retry-time*
     
     
     
     The ConnectRetry timer is configured for all BGP peers or peer groups.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure a ConnectRetry timer for a specified peer or peer group.
  
  
  
  Perform the following steps on a BGP Router:
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run [**peer**](cmdqueryname=peer+timer+connect-retry) { *group-name* | *ipv4-address* } **timer** **connect-retry** *connect-retry-time*
     
     
     
     The ConnectRetry timer is configured for a peer or peer group.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.