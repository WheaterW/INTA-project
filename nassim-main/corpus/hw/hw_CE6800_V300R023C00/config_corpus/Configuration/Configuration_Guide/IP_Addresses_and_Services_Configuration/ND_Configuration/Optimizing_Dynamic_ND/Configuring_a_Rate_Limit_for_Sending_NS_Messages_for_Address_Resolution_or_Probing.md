Configuring a Rate Limit for Sending NS Messages for Address Resolution or Probing
==================================================================================

Configuring a Rate Limit for Sending NS Messages for Address Resolution or Probing

#### Context

If the remote device has a limited capability of receiving NS messages or the local device has a limited capability of processing NA messages, run the [**ipv6 nd ns send rate-limit**](cmdqueryname=ipv6+nd+ns+send+rate-limit) command on the local device to configure a rate limit for sending NS messages for address resolution or probing. This prevents a failure to learn ND entries or incorrect deletion of ND entries caused by NA message discarding.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Configure a rate limit for sending NS messages for address resolution or probing.
   
   
   ```
   [ipv6 nd ns send rate-limit](cmdqueryname=ipv6+nd+ns+send+rate-limit) rate-limit
   ```
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```