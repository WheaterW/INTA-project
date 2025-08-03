(Optional) Enabling IPv6 IS-IS Neighbor Strict-Check
====================================================

(Optional) Enabling IPv6 IS-IS Neighbor Strict-Check

#### Context

During the establishment of IPv6 IS-IS neighbor relationships, if both IPv4 and IPv6 are configured at both ends, both IPv4 and IPv6 neighbor relationships are established. By default, IPv4 and IPv6 share the standard topology in IPv6 IS-IS. If the link between the two ends fails and then recovers, IPv4 goes up faster than IPv6. When one end receives a message indicating that IPv4 goes up, it considers that both IPv4 and IPv6 neighbor relationships are restored. If IPv6 traffic is transmitted on the network, a large amount of data is discarded. To prevent this problem, run the **adjacency-strict-check enable** command to enable IPv6 IS-IS neighbor strict-check to ensure that IPv6 IS-IS neighbor relationships are established only when IPv4 and IPv6 are both up at the two ends.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Create an IS-IS process and enter the IS-IS view.
   
   
   ```
   [isis](cmdqueryname=isis) [ process-id ]
   ```
3. Enable IPv6 IS-IS neighbor strict-check.
   
   
   ```
   [adjacency-strict-check enable](cmdqueryname=adjacency-strict-check+enable)
   ```
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```