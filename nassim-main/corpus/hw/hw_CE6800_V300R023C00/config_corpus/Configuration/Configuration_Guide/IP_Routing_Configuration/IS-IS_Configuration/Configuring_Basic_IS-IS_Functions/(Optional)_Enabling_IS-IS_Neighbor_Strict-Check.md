(Optional) Enabling IS-IS Neighbor Strict-Check
===============================================

(Optional) Enabling IS-IS Neighbor Strict-Check

#### Context

If both IPv4 and IPv6 are configured at two ends, both IPv4 and IPv6 IS-IS neighbor relationships are established between the two ends. By default, IPv4 and IPv6 share the standard topology. As such, when a link recovers from a failure, IPv4 goes up faster than IPv6. When an IS-IS device receives a message indicating that IPv4 goes up, it considers that both IPv4 and IPv6 neighbor relationships are established. If the device sends IPv6 packets to the other end, they are discarded. To prevent this problem, run the **adjacency-strict-check enable** command. This command enables IS-IS neighbor strict-check, ensuring that IS-IS neighbor relationships are established only when IPv4 and IPv6 are both up at the two ends.

![](public_sys-resources/note_3.0-en-us.png) 

The CE6885-LL in low latency mode does not support IPv6.



#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Create an IS-IS process, and enter the IS-IS view.
   
   
   ```
   [isis](cmdqueryname=isis) [ process-id ] [ vpn-instance vpn-instance-name ]
   ```
3. Enable IS-IS neighbor strict-check.
   
   
   ```
   [adjacency-strict-check enable](cmdqueryname=adjacency-strict-check+enable)
   ```
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```