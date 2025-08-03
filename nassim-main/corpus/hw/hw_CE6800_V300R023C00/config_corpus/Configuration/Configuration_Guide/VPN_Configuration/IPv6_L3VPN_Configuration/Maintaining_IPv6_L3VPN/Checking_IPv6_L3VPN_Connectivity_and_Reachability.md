Checking IPv6 L3VPN Connectivity and Reachability
=================================================

Checking IPv6 L3VPN Connectivity and Reachability

#### Procedure

* Configure ping to test IPv6 network connectivity.
  
  
  ```
  [ping ipv6](cmdqueryname=ping+ipv6) { [ -a source-ipv6-address | -c echo-number | { -s byte-number | -range [ [ min min-value | max max-value | step step-value ] * ] } | -t timeout | { -tc traffic-class-value | -dscp dscp } | vpn-instance vpn-instance-name | -m wait-time | -name | -nexthop nextHopAddr | -h hoplimit | { -brief | [ -system-time | -ri | -detail ] * } | -p pattern | ignore-mtu ] * destination-ipv6-address [ -i { interface-name | interface-type interface-number } ] [ ipv6-forwarding ] }
  ```
* Configure tracert to test an IPv6 network.
  
  
  
  Test the fault position.
  
  ```
  [tracert ipv6](cmdqueryname=tracert+ipv6) [ -f first-hop-limit | -m max-hop-limit | -p port-number | -q probes | -w timeout | vpn-instance vpn-instance-name | -s size | -name | { -nexthop nextHopAddr | -passroute | -pipe }* | -a source-ipv6-address | { -tc tc | -dscp dscp } ] * host-name  [ -i { ifName | ifType ifNum } ]
  ```