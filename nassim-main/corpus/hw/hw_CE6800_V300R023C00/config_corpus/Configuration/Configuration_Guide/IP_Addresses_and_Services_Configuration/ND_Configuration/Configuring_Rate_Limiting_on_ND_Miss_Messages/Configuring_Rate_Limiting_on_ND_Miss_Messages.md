Configuring Rate Limiting on ND Miss Messages
=============================================

Configuring Rate Limiting on ND Miss Messages

#### Context

When a device sends IPv6 packets, if the MAC address corresponding to the destination IPv6 address of the packets does not exist, the device generates ND Miss messages. This consumes CPU resources and prevents the device from processing normal services. Rate limiting on ND Miss messages can be deployed to help reduce CPU resource consumption by ND Miss messages, protecting other services.


#### Procedure

* Configure rate limiting on ND Miss messages globally.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Configure rate limiting on ND Miss messages.
     
     
     
     **Table 1** Configuring rate limiting on ND Miss messages
     | Operation | Command | Description |
     | --- | --- | --- |
     | Configure rate limiting on ND Miss messages. | [**ipv6 nd miss anti-attack rate-limit**](cmdqueryname=ipv6+nd+miss+anti-attack+rate-limit) *limit-number* | When a device sends IPv6 packets, if the MAC address corresponding to the destination IPv6 address of the packets does not exist, the device generates ND Miss messages. This consumes CPU resources and prevents the device from processing normal services. Running this command resolves the problem, as it enables the device to process only the allowed number of ND Miss messages within a specified period, protecting other services. |
     | Configure a rate limit for receiving ND Miss messages based on a specified source IPv6 address. | [**ipv6 nd miss anti-attack rate-limit source-ip**](cmdqueryname=ipv6+nd+miss+anti-attack+rate-limit+source-ip) *ipv6-address* **maximum** *max-value* | If a device is attacked, it receives a large number of ND Miss messages within a short period. As a result, the device consumes many CPU resources to learn and respond to ND entries, affecting the processing of other services. To resolve this issue, configure a rate limit for receiving ND Miss messages based on a specified source IPv6 address. After the configuration is complete, the device counts the number of ND Miss messages received per period based on the specified source IPv6 address. If the number exceeds the configured limit, the device does not process excess ND Miss messages. |
     | Configure a rate limit for receiving ND Miss messages based on any source IPv6 address. | [**ipv6 nd miss anti-attack rate-limit source-ip all maximum**](cmdqueryname=ipv6+nd+miss+anti-attack+rate-limit+source-ip+all+maximum) *max-value* | If a device is attacked, it receives a large number of ND Miss messages within a short period. As a result, the device consumes many CPU resources to learn and respond to ND entries, affecting the processing of other services. To resolve this issue, configure a rate limit for receiving ND Miss messages based on any source IPv6 address. After the configuration is complete, the device counts the number of ND Miss messages received per period based on any source IPv6 address. If the number exceeds the configured limit, the device does not process excess ND Miss messages. |
  3. (Optional) Configure an interval for recording ND logs for potential attacks and sending the corresponding ND traps.
     
     
     ```
      [ipv6 nd anti-attack log-trap-timer](cmdqueryname=ipv6+nd+anti-attack+log-trap-timer) time-value
     ```
     
     
     
     After a rate limit is configured for ND Miss messages, the device counts the number of received ND Miss messages. If the number of ND Miss messages received in a specified period exceeds the configured limit, the device discards excess ND Miss messages. The device considers this is a potential attack, and records ND logs for the potential attack and sends the corresponding ND traps to the NMS. If potential attacks frequently occur, the device generates a large number of logs and traps. To resolve this issue, configure a large interval for recording ND logs and sending ND traps.
  4. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Configure rate limiting on ND Miss messages on an interface.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the interface view.
     
     
     ```
     [interface](cmdqueryname=interface) interface-type interface-number
     ```
  3. Switch the interface working mode to Layer 3.
     
     
     ```
     [undo portswitch](cmdqueryname=undo+portswitch)
     ```
  4. Enable IPv6.
     
     
     ```
     [ipv6 enable](cmdqueryname=ipv6+enable)
     ```
  5. Configure rate limiting on ND Miss messages.
     
     
     
     **Table 2** Configuring rate limiting on ND Miss messages
     | Operation | Command | Description |
     | --- | --- | --- |
     | Configure rate limiting on ND Miss messages. | [**ipv6 nd miss anti-attack rate-limit**](cmdqueryname=ipv6+nd+miss+anti-attack+rate-limit) *limit* | When a device sends IPv6 packets, if the MAC address corresponding to the destination IPv6 address of the packets does not exist, the device generates ND Miss messages. This consumes CPU resources and prevents the device from processing normal services. Running this command resolves the problem, as it enables the device to process only the allowed number of ND Miss messages within a specified period, protecting other services. |
     | Configure a rate limit for receiving ND Miss messages based on a specified source IPv6 address. | [**ipv6 nd miss anti-attack rate-limit source-ip**](cmdqueryname=ipv6+nd+miss+anti-attack+rate-limit+source-ip) *ipv6-address* **maximum** *max-value* | If a device is attacked, it receives a large number of ND Miss messages within a short period. As a result, the device consumes many CPU resources to learn and respond to ND entries, affecting the processing of other services. To resolve this issue, configure a rate limit for receiving ND Miss messages based on a specified source IPv6 address. After the configuration is complete, the device counts the number of ND Miss messages received per period based on the specified source IPv6 address. If the number exceeds the configured limit, the device does not process excess ND Miss messages. |
  6. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```