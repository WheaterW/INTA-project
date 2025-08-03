Configuring an IOAM Packet Analyzer
===================================

Configuring an IOAM Packet Analyzer

#### Prerequisites

There are reachable routes between the device and analyzer.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Create an analyzer and enter its view.
   
   
   ```
   [collector](cmdqueryname=collector) collect collect-id
   ```
3. Configure the analyzer address.
   
   
   ```
   [source](cmdqueryname=source) { [ip](cmdqueryname=ip) ip-address | [ipv6](cmdqueryname=ipv6) ipv6-address } [export host](cmdqueryname=export+host) { [ip](cmdqueryname=ip) ip-address | [ipv6](cmdqueryname=ipv6) ipv6-address } [udp-port](cmdqueryname=udp-port) port-number [ [vpn-instance](cmdqueryname=vpn-instance) vpn-instance-name ]
   ```
4. Exit the analyzer view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
5. Enter the IOAM view.
   
   
   ```
   [ioam](cmdqueryname=ioam)
   ```
6. Specify the IOAM packet analyzer.
   
   
   ```
   [collector](cmdqueryname=collector) [collect](cmdqueryname=collect) collect-id
   ```
7. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```