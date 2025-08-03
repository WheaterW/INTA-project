Setting the AS\_Path Attribute
==============================

The AS\_Path attribute is used to prevent routing loops and control route selection.

#### Procedure

* Enable an MBGP device to ignore the AS\_Path attribute during route selection.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run the [**ipv4-family multicast**](cmdqueryname=ipv4-family+multicast) command to enter the BGP-IPv4 multicast address family view, or run the **[**ipv4-multicast vpn-instance**](cmdqueryname=ipv4-multicast+vpn-instance)** **vpn-instance-name** command to enter the BGP-multicast VPN instance IPv4 address family view.
  4. Run [**bestroute as-path-ignore**](cmdqueryname=bestroute+as-path-ignore)
     
     
     
     MBGP is configured to ignore the AS\_Path attribute during route selection.
* Enable the device to remove all the private AS numbers from the AS\_Path attribute carried in BGP Update messages.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run the [**ipv4-family multicast**](cmdqueryname=ipv4-family+multicast) command to enter the BGP-IPv4 multicast address family view, or run the **[**ipv4-multicast vpn-instance**](cmdqueryname=ipv4-multicast+vpn-instance)** **vpn-instance-name** command to enter the BGP-multicast VPN instance IPv4 address family view.
  4. Run [**peer**](cmdqueryname=peer) { *ipv4-address* | *group-name* } [**public-as-only**](cmdqueryname=public-as-only) [ **force** [ **replace** ] [ **include-peer-as** ] | **limited** [ **replace** ] [ **include-peer-as** ] ]
     
     
     
     The AS\_Path attribute is configured to carry only public AS numbers in the BGP Update messages to be sent.
     
     Or run [**peer**](cmdqueryname=peer) { *ipv4-address* | *group-name* } **public-as-only** **import** [ **force** ]
     
     The AS\_Path attribute is configured not to carry private AS numbers in accepted BGP Update messages.
     
     
     
     In general, an AS number is an integer ranging from 1 to 4294967295. A public AS number ranges from 1 to 64511, and from 65536 (which represents 1.0 in the *x*.*y* format) to 4294967294 (65535.65534 in the *x*.*y* format). A private AS number ranges from 64512 to 65534. The AS numbers 65535 and 4294967295 are reserved for special use.
     
     Public AS numbers can be directly used on the Internet, and are assigned and managed by the Internet Assigned Number Authority (IANA). Private AS numbers cannot be directly advertised to the Internet, and are used only within routing domains.
     
     Generally, MBGP routes to be advertised to peers carry either public or private AS numbers. In certain cases, private AS numbers do not need to be advertised. In this case, you can run this command to configure the AS\_Path attribute to carry only public AS numbers.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.