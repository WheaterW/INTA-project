Checking IPv4 L3VPN Connectivity and Reachability
=================================================

Checking IPv4 L3VPN Connectivity and Reachability

#### Procedure

* Run the [**ping**](cmdqueryname=ping) command to check the connectivity of the IPv4 network from the source to the destination. Perform either of the following operations according to the displayed detailed or brief information.
  
  
  + Run the following command to display detailed information:
    ```
    [ping](cmdqueryname=ping) [ ip ] { [ -c count | -i { interface-name | interface-type interface-number } | -nexthop nexthop-address | { -range [ min min-value | max max-value | step step-value ] * | -s packetsize } | -t timeout | -m time | -a source-ip-address [ -ignore-vpn | -response-vpn respVrfName ] | -h ttl-value | -p pattern | { -tos tos-value | -dscp dscp-value } | { -f | ignore-mtu } | -q | -r | -vpn-instance vpn-instance-name | -v | -name | -system-time | -ri | -8021p 8021p-value | -detail ] * host [ ip-forwarding ] }
    ```
  + Run the following command to display brief information:
    ```
    [ping](cmdqueryname=ping) [ ip ] { [ -c count | -i { interface-name | interface-type interface-number } | -nexthop nexthop-address | { -range [ min min-value | max max-value | step step-value ] * | -s packetsize } | -t timeout | -m time | -a source-ip-address | -h ttl-value | -p pattern | { -tos tos-value | -dscp dscp-value } | { -f | ignore-mtu } | -vpn-instance vpn-instance-name | -name | -8021p 8021p-value | -brief ] * host [ ip-forwarding ] }
    ```
* Run the [**tracert**](cmdqueryname=tracert) [ **-a** *source-ip-address* | **-f** *first-TTL* | **-m** *max-TTL* | **-p** *port* | **-q** *nqueries* | **-vpn-instance** *vpn-instance-name* | **-w** *timeout* ] \* *host* command to check the gateways through which IPv4 packets pass from the source to the destination.