Configuring User-Level Rate Limiting
====================================

Configuring User-Level Rate Limiting

#### Context

User-level rate limiting can be configured to accurately limit the rate based on user MAC addresses, reducing the impact on common users.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enable user-level rate limiting globally.
   
   
   ```
   [cpu-defend host-car enable](cmdqueryname=cpu-defend+host-car+enable)
   ```
3. Set the user-level rate limit.
   
   
   ```
   [cpu-defend host-car](cmdqueryname=cpu-defend+host-car) [ mac-address mac-address | car-id car-id ] pps pps-value
   ```
4. Specify the packet types to which user-level rate limiting is applied.
   
   
   ```
   [cpu-defend host-car](cmdqueryname=cpu-defend+host-car) { { arp | dhcp-request | dhcpv6-request | nd } * | all }
   ```
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   The CE6885-LL in low latency mode does not support dhcpv6-request or nd.
5. Enter the interface view.
   
   
   ```
   interface interface-type interface-number
   ```
6. Enable user-level rate limiting on an interface.
   
   
   ```
   [undo host-car disable](cmdqueryname=undo+host-car+disable)
   ```
   
   
   
   By default, user-level rate limiting is disabled on interfaces.
   
   When user-level rate limiting is enabled globally, user-level rate limiting is also enabled on interfaces. In this case, you can run the **host-car disable** command in the interface view to disable user-level rate limiting on interfaces as needed.
7. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Example

Enable user-level rate limiting, set the user-level rate limit to 15 pps, and limit the rate of only ARP packets.

```
<HUAWEI> system-view
[~HUAWEI] [cpu-defend host-car enable](cmdqueryname=cpu-defend+host-car+enable)
[*HUAWEI] [cpu-defend host-car](cmdqueryname=cpu-defend+host-car) pps 15
[*HUAWEI] [cpu-defend host-car](cmdqueryname=cpu-defend+host-car) arp
[*HUAWEI] commit
```