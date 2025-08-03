Configuring the Analyzer
========================

Configuring the Analyzer

#### Context

After the source address, destination address, and destination UDP port number are configured on the device, the device can send flow entries to a specified analyzer, enabling the network administrator to monitor the network status on the analyzer. Ensure that there are reachable routes between the device and analyzer.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Create an analyzer and enter the analyzer view.
   
   
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
5. Enter the AnyFlow view.
   
   
   ```
   [any-flow](cmdqueryname=any-flow)
   ```
6. Specify the analyzer.
   
   
   ```
   [collector](cmdqueryname=collector) collect collect-id
   ```
7. Return to the system view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
8. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```