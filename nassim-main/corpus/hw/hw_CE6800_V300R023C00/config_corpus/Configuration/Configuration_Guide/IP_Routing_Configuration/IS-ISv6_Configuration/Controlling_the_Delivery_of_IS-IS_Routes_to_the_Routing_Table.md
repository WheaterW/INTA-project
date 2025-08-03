Controlling the Delivery of IS-IS Routes to the Routing Table
=============================================================

Controlling the Delivery of IS-IS Routes to the Routing Table

#### Context

IP packets are forwarded through routes in the IP routing table. Routes in the IS-IS IPv6 routing table take effect only after they are successfully added to the IP routing table.

You can configure a filter, such as a basic ACL6, an IP prefix list, or a route-policy, to filter IPv6 IS-IS routes so that only the matched routes are delivered to the IPv6 routing table. Unmatched IPv6 IS-IS routes are neither added to the IP routing table nor selected.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the IS-IS view.
   
   
   ```
   [isis](cmdqueryname=isis) [ process-id ]
   ```
3. Configure the device to deliver only matched IPv6 IS-IS routes to the IPv6 routing table.
   
   
   ```
   [ipv6 filter-policy](cmdqueryname=ipv6+filter-policy) { acl6-number | acl6-name acl6-name-string | ipv6-prefix ipv6-prefix-name | route-policy route-policy-name } import
   ```
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display isis route**](cmdqueryname=display+isis+route) [ *process-id* | **vpn-instance** *vpn-instance-name* ] [ **ipv6** ] [ **verbose** | [ **level-1** | **level-2** ] | *ip-address* [ *mask* | *mask-length* ] ] \* command to check IPv6 IS-IS routing information.