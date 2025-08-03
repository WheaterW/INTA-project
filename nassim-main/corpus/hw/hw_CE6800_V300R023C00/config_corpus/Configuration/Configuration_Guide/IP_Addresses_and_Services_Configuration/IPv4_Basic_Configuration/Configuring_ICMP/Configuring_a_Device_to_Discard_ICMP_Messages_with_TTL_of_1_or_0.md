Configuring a Device to Discard ICMP Messages with TTL of 1 or 0
================================================================

Configuring a Device to Discard ICMP Messages with TTL of 1 or 0

#### Prerequisites

Before configuring a device to discard ICMP messages with TTL of 1 or 0, configure link layer protocol parameters for interfaces to ensure that the link layer protocol status of the interfaces is up.


#### Context

If a device receives an IP datagram whose destination address is not a local address and the TTL value is 1 or 0, the device sends an ICMP TTL Exceeded message. When a device receives a large number of ICMP messages with TTL of 1 or 0, usually sent by an attacker, device performance deteriorates because the device processes these messages.

To address this issue, configure the device to discard ICMP messages with TTL of 1 or 0. This improves network performance and security.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Configure the device to discard ICMP messages with TTL of 1 or 0.
   
   
   ```
   [icmp ttl-exceeded drop](cmdqueryname=icmp+ttl-exceeded+drop+all+slot) { all | slot slot-id }
   ```
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```