Configuring Rate Limiting for ICMP Messages
===========================================

Configuring Rate Limiting for ICMP Messages

#### Prerequisites

Before configuring rate limiting for ICMP messages, configure link layer protocol parameters for interfaces to ensure that the link layer protocol status of the interfaces is up.


#### Context

Attackers may send a large number of ICMP messages to attack a device. This consumes a significant amount of CPU resources if the device sends all these messages to the CPU for processing and negatively affects other services. To address this issue, configure rate limiting for ICMP messages on the device.

After the configuration is complete, the device discards excess ICMP messages if the number of ICMP messages sent per second by an interface exceeds the configured threshold.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enable rate limiting for ICMP messages.
   
   
   ```
   [undo icmp rate-limit disable](cmdqueryname=undo+icmp+rate-limit+disable)
   ```
3. Configure a rate threshold for ICMP messages.
   
   
   ```
   [icmp rate-limit](cmdqueryname=icmp+rate-limit+interface) [ interface interface-type interface-number1 [ [to](cmdqueryname=to+threshold) interface-number2 ] ] threshold threshold-value
   ```
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```