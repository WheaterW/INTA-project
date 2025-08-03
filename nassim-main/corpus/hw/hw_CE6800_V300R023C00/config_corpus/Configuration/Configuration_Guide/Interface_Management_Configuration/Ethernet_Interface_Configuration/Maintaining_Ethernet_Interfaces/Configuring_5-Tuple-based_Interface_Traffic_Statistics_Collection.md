Configuring 5-Tuple-based Interface Traffic Statistics Collection
=================================================================

Configuring 5-Tuple-based Interface Traffic Statistics Collection

#### Context

A 5-tuple refers to the five fields contained in packets: source and destination IP addresses, source and destination port numbers, and protocol type. The 5-tuple generally varies with traffic flows on different interfaces.

To check statistics of packets with a specified 5-tuple and learn the traffic forwarding path for fault locating, configure 5-tuple-based interface traffic statistics collection.

![](public_sys-resources/note_3.0-en-us.png) 

This configuration is not supported on the CE6885-LL (low latency mode).



#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Configure 5-tuple-based interface traffic statistics collection.
   
   
   ```
   [port forwarding-path](cmdqueryname=port+forwarding-path) path-id pathnum { src-ip src-ip-data [ srcip-mask-len ] | dst-ip dst-ip-data [ dstip-mask-len ] | protocol { protocolnum | tcp [ l4-src-port src-port-data | l4-dst-port dst-port-data ] * | udp [ l4-src-port src-port-data | l4-dst-port dst-port-data ] * } } * statistics precedence precedencenum
   ```
   
   By default, 5-tuple-based interface traffic statistics collection is not configured.
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display port forwarding-path**](cmdqueryname=display+port+forwarding-path) **path-id** *pathnum* **statistics** command in any view to check statistics about the traffic that contains a specified 5-tuple.