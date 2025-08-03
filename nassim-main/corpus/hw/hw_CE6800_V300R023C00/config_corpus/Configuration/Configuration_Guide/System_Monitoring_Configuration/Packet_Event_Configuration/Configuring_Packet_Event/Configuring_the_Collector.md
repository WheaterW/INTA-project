Configuring the Collector
=========================

Configuring the Collector

#### Context

If packets are discarded or the packet latency exceeds the threshold on a device, flow entries will be generated and reported to the collector in UDP packets of the NetStream V9 format.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. (Optional) Configure the collector.
   
   
   
   Skip this step if the collector has been configured in other service modules.
   
   
   
   1. Create a collector and enter the collector view.
      
      
      ```
      [collector](cmdqueryname=collector) collect collect-id
      ```
   2. Configure the collector address. (CE6885-LL (low latency mode) does not support the source or destination IPv6 addresses of collectors.)
      
      
      ```
      [source](cmdqueryname=source) { [ip](cmdqueryname=ip) ip-address | [ipv6](cmdqueryname=ipv6) ipv6-address } [export host](cmdqueryname=export+host) { [ip](cmdqueryname=ip) ip-address | [ipv6](cmdqueryname=ipv6) ipv6-address } [udp-port](cmdqueryname=udp-port) port-number [ [vpn-instance](cmdqueryname=vpn-instance) vpn-instance-name ]
      ```
   3. Exit the collector view.
      
      
      ```
      [quit](cmdqueryname=quit)
      ```
3. Configure the ID of the collector to which flow entries are reported.
   1. Enter the packet monitoring view.
      
      
      ```
      [packet event monitor](cmdqueryname=packet+event+monitor)
      ```
   2. Configure the collector ID.
      
      
      ```
      [collector](cmdqueryname=collector) collect collect-id
      ```
   3. Exit the packet monitoring view.
      
      
      ```
      [quit](cmdqueryname=quit)
      ```
4. Exit the collector view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```