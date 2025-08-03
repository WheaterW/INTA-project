Configuring the Session-Reflector
=================================

This section describes how to configure the Session-Reflector. The Session-Reflector replies to the probes sent by the Session-Sender after being notified by the Server.

#### Context

After the Session-Reflector is configured, the Session-Reflector can reply to the Session-Sender with timestamps and serial numbers to help collect statistics about the delay, jitter, packet loss rate, and other indicators.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**nqa twamp**](cmdqueryname=nqa+twamp)
   
   
   
   The TWAMP view is displayed.
3. Run [**reflector**](cmdqueryname=reflector)
   
   
   
   The Session-Reflector function is enabled, and the Session-Reflector view is displayed.
4. (Optional) Run [**test-session inactive**](cmdqueryname=test-session+inactive) *timeout*
   
   
   
   An inactive interval is configured for a test session.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.