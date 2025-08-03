Configuring a Rate Limit for Receiving ND Messages
==================================================

Configuring a Rate Limit for Receiving ND Messages

#### Context

If a device is attacked, it receives a large number of ND messages within a short period. As a result, the device consumes many CPU resources to learn and respond to ND entries, affecting the processing of other services. To resolve this issue, configure a rate limit for receiving ND messages. After the configuration is complete, the device counts the number of ND messages received per period. If the number of ND messages exceeds the configured limit, the device does not process excess ND messages.


#### Procedure

* Configure a rate limit for receiving ND messages globally.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Configure a rate limit for receiving ND messages.
     
     
     
     **Table 1** Configuring a rate limit for receiving ND messages
     | Operation | Command | Description |
     | --- | --- | --- |
     | Configure a rate limit for receiving ND messages. | [**ipv6 nd**](cmdqueryname=ipv6+nd) { [**na**](cmdqueryname=na) | [**ns**](cmdqueryname=ns) | [**ra**](cmdqueryname=ra) | [**rs**](cmdqueryname=rs) } [**anti-attack rate-limit**](cmdqueryname=anti-attack+rate-limit) *limit* | A rate limit refers to the number of ND messages that can be received per second. |
     | Configure a rate limit for receiving ND messages based on a specified source MAC address. | [**ipv6 nd**](cmdqueryname=ipv6+nd) { [**na**](cmdqueryname=na) | [**ns**](cmdqueryname=ns) | [**ra**](cmdqueryname=ra) | [**rs**](cmdqueryname=rs) } [**anti-attack rate-limit source-mac**](cmdqueryname=anti-attack+rate-limit+source-mac) *mac-address* [**maximum**](cmdqueryname=maximum) *max-value* | After a rate limit for receiving ND messages based on a specified source MAC address is configured, the device counts the number of ND messages received per period based on the specified source MAC address. If the number of ND messages exceeds the configured limit, the device does not process excess ND messages. |
     | Configure a rate limit for receiving ND messages based on any source MAC address. | [**ipv6 nd**](cmdqueryname=ipv6+nd) { [**na**](cmdqueryname=na) | [**ns**](cmdqueryname=ns) | [**ra**](cmdqueryname=ra) | [**rs**](cmdqueryname=rs) } [**anti-attack rate-limit source-mac all**](cmdqueryname=anti-attack+rate-limit+source-mac+all) [**maximum**](cmdqueryname=maximum) *max-value* | After a rate limit for receiving ND messages based on any source MAC address is configured, the device counts the number of ND messages received per period based on any source MAC address. If the number of ND messages exceeds the configured limit, the device does not process excess ND messages. |
     | Configure a rate limit for receiving ND messages based on a specified source IPv6 address. | [**ipv6 nd**](cmdqueryname=ipv6+nd) { [**na**](cmdqueryname=na) | [**ns**](cmdqueryname=ns) | [**ra**](cmdqueryname=ra) | [**rs**](cmdqueryname=rs) } [**anti-attack rate-limit source-ip**](cmdqueryname=anti-attack+rate-limit+source-ip) *ipv6-address* [**maximum**](cmdqueryname=maximum) *max-value* | After a rate limit for receiving ND messages based on a specified source IPv6 address is configured, the device counts the number of ND messages received per period based on the specified source IPv6 address. If the number of ND messages exceeds the configured limit, the device does not process excess ND messages. |
     | Configure a rate limit for receiving ND messages based on any source IPv6 address. | [**ipv6 nd**](cmdqueryname=ipv6+nd) { [**na**](cmdqueryname=na) | [**ns**](cmdqueryname=ns) | [**ra**](cmdqueryname=ra) | [**rs**](cmdqueryname=rs) } [**anti-attack rate-limit source-ip all**](cmdqueryname=anti-attack+rate-limit+source-ip+all) [**maximum**](cmdqueryname=maximum) *max-value* | After a rate limit for receiving ND messages based on any source IPv6 address is configured, the device counts the number of ND messages received per period based on any source IPv6 address. If the number of ND messages exceeds the configured limit, the device does not process excess ND messages. |
     | Configure a rate limit for receiving ND messages based on a specified destination IPv6 address. | [**ipv6 nd**](cmdqueryname=ipv6+nd) { **ns** | **na** | **rs** | **ra** } **anti-attack** **rate-limit** **destination-ip** *ipv6-address* **maximum** *max-value* | To resolve this issue, configure a rate limit for receiving ND messages based on a specified destination IPv6 address. After the configuration is complete, the device counts the number of ND messages received per period based on the specified destination IPv6 address. If the number of ND messages exceeds the configured limit, the device does not process excess ND messages. |
     | Configure a rate limit for receiving ND messages based on any destination IPv6 address. | [**ipv6 nd**](cmdqueryname=ipv6+nd) { **ns** | **na** | **rs** | **ra** } **anti-attack** **rate-limit** **destination-ip** **all** **maximum** *max-value* | To resolve this issue, configure a rate limit for receiving ND messages based on any destination IPv6 address. After the configuration is complete, the device counts the number of ND messages received per period based on any destination IPv6 address. If the number of ND messages exceeds the configured limit, the device does not process excess ND messages. |
     | Configure a rate limit for receiving ND messages based on a specified target IPv6 address. | [**ipv6 nd**](cmdqueryname=ipv6+nd) { **ns** | **na** } **anti-attack** **rate-limit** **target-ip** *ipv6-address* **maximum** *max-value* | To resolve this issue, configure a rate limit for receiving ND messages based on a specified target IPv6 address. After the configuration is complete, the device counts the number of ND messages received per period based on the specified target IPv6 address. If the number of ND messages exceeds the configured limit, the device does not process excess ND messages. |
     | Configure a rate limit for receiving ND messages based on any target IPv6 address. | [**ipv6 nd**](cmdqueryname=ipv6+nd) { **ns** | **na** } **anti-attack** **rate-limit** **target-ip** **all** **maximum** *max-value* | To resolve this issue, configure a rate limit for receiving ND messages based on any target IPv6 address. After the configuration is complete, the device counts the number of ND messages received per period based on any target IPv6 address. If the number of ND messages exceeds the configured limit, the device does not process excess ND messages. |
  3. (Optional) Configure an interval for recording ND logs for potential attacks and sending the corresponding ND traps.
     
     
     ```
      [ipv6 nd anti-attack log-trap-timer](cmdqueryname=ipv6+nd+anti-attack+log-trap-timer) time-value
     ```
     
     
     
     After a rate limit is configured for ND messages, the device counts the number of received ND messages. If the number of ND messages received in a specified period exceeds the configured limit, the device discards excess ND messages. The device considers this is a potential attack, and records ND logs for the potential attack and sends the corresponding ND traps to the NMS. If potential attacks frequently occur, the device generates a large number of logs and traps. To resolve this issue, configure a large interval for recording ND logs and sending ND traps.
  4. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Configure a rate limit for receiving ND messages on an interface.
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
  5. Configure a rate limit for receiving ND messages.
     
     
     
     **Table 2** Configuring a rate limit for receiving ND messages
     | Operation | Command | Description |
     | --- | --- | --- |
     | Configure a rate limit for receiving ND messages. | [**ipv6 nd**](cmdqueryname=ipv6+nd) { [**na**](cmdqueryname=na) | [**ns**](cmdqueryname=ns) | [**ra**](cmdqueryname=ra) | [**rs**](cmdqueryname=rs) } [**anti-attack rate-limit**](cmdqueryname=anti-attack+rate-limit) *limit* | A rate limit refers to the number of ND messages that can be received per second. |
     | Configure a rate limit for receiving ND messages based on a specified source IPv6 address. | [**ipv6 nd**](cmdqueryname=ipv6+nd) { [**na**](cmdqueryname=na) | [**ns**](cmdqueryname=ns) | [**ra**](cmdqueryname=ra) | [**rs**](cmdqueryname=rs) } [**anti-attack rate-limit source-ip**](cmdqueryname=anti-attack+rate-limit+source-ip) *ipv6-address* [**maximum**](cmdqueryname=maximum) *max-value* | After a rate limit for receiving ND messages based on a specified source IPv6 address is configured, the device counts the number of ND messages received per period based on the specified source IPv6 address. If the number of ND messages exceeds the configured limit, the device does not process excess ND messages. |
  6. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```

#### Verifying the Configuration

Run the [**display ipv6 nd anti-attack rate-limit configuration**](cmdqueryname=display+ipv6+nd+anti-attack+rate-limit+configuration) command to check the configuration of the rate limit for receiving ND messages.