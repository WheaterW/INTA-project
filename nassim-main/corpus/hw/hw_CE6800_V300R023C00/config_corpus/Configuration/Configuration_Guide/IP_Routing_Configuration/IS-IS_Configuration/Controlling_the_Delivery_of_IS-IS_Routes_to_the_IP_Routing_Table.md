Controlling the Delivery of IS-IS Routes to the IP Routing Table
================================================================

Controlling the Delivery of IS-IS Routes to the IP Routing Table

#### Context

IP packets are forwarded through routes in the IP routing table. As such, IS-IS routes can be used for packet forwarding only after they are delivered to the IP routing table.

To control the delivery of IS-IS routes to the IP routing table, you can configure a basic ACL, IP prefix list, or route-policy, so that only the matching IS-IS routes are delivered to the IP routing table.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the IS-IS view.
   
   
   ```
   [isis](cmdqueryname=isis) [ process-id ]
   ```
3. Configure the device to deliver only matching IS-IS routes to the IP routing table.
   
   
   ```
   [filter-policy](cmdqueryname=filter-policy) { acl-number | acl-name acl-name | ip-prefix ip-prefix-name | route-policy route-policy-name } import
   ```
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display isis route**](cmdqueryname=display+isis+route) [ *process-id* | **vpn-instance** *vpn-instance-name* ] [ **ipv4** ] [ **verbose** | [ **level-1** | **level-2** ] | *ip-address* [ *mask* | *mask-length* ] ] command to check IS-IS routing information.