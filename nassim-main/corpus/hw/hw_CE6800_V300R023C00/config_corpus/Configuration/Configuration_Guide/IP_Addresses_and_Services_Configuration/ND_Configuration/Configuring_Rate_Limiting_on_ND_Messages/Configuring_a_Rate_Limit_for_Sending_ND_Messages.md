Configuring a Rate Limit for Sending ND Messages
================================================

Configuring a Rate Limit for Sending ND Messages

#### Context

If a device is attacked, it receives a large number of ND or ND Miss messages within a short period. As a result, the device consumes many CPU resources to learn and respond to ND entries, affecting the processing of other services. To resolve this issue, configure a rate limit for sending ND messages. After the configuration is complete, the device counts the number of ND messages sent per period. If the number exceeds the configured limit, the device delays scheduling or ignores excess ND messages.

![](public_sys-resources/note_3.0-en-us.png) 

The priorities of rate limits for sending ND messages are as follows: rate limit for sending ND multicast messages configured in the interface view > rate limit for sending ND messages configured in the interface view > rate limit for sending ND multicast messages configured in the system view > rate limit for sending ND messages configured in the system view



#### Procedure

* Configure a rate limit for sending ND messages in the system view.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Configure a rate limit for sending ND messages on the device.
     
     
     
     **Table 1** Configuring a rate limit for sending ND messages on the device
     | Operation | Command | Description |
     | --- | --- | --- |
     | Configure a rate limit for sending ND messages on the device. | [**ipv6 nd**](cmdqueryname=ipv6+nd) { [**rs**](cmdqueryname=rs) | [**ra**](cmdqueryname=ra) | [**ns**](cmdqueryname=ns) | [**na**](cmdqueryname=na) } [**send rate-limit**](cmdqueryname=send+rate-limit) *rate-limit* | The rate limit specifies the maximum number of ND messages that can be sent per second on the device. |
     | Configure a rate limit for sending ND multicast messages on the device. | [**ipv6 nd**](cmdqueryname=ipv6+nd) { [**rs**](cmdqueryname=rs) | [**ra**](cmdqueryname=ra) | [**ns**](cmdqueryname=ns) | [**na**](cmdqueryname=na) } [**send multicast rate-limit**](cmdqueryname=send+multicast+rate-limit) *rate-limit* | The rate limit specifies the maximum number of ND multicast messages that can be sent per second on the device. |
  3. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Configure a rate limit for sending ND messages in the interface view.
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
  5. Configure a rate limit for sending ND messages on the interface.
     
     
     
     **Table 2** Configuring a rate limit for sending ND messages on the interface
     | Operation | Command | Description |
     | --- | --- | --- |
     | Configure a rate limit for sending ND messages on a specified interface. | [**ipv6 nd**](cmdqueryname=ipv6+nd) { [**rs**](cmdqueryname=rs) | [**ra**](cmdqueryname=ra) | [**ns**](cmdqueryname=ns) | [**na**](cmdqueryname=na) } [**send rate-limit**](cmdqueryname=send+rate-limit) *rate-limit* | The rate limit specifies the maximum number of ND messages that can be sent per second on the interface. |
     | Configure a rate limit for sending ND multicast messages on a specified interface. | [**ipv6 nd**](cmdqueryname=ipv6+nd) { [**rs**](cmdqueryname=rs) | [**ra**](cmdqueryname=ra) | [**ns**](cmdqueryname=ns) | [**na**](cmdqueryname=na) } [**send multicast rate-limit**](cmdqueryname=send+multicast+rate-limit) *rate-limit* | The rate limit specifies the maximum number of ND multicast messages that can be sent per second on the interface. |
  6. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```