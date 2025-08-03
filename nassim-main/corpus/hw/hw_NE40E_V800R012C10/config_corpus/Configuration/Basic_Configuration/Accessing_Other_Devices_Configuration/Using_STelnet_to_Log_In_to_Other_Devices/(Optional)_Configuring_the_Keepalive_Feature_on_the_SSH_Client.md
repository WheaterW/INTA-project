(Optional) Configuring the Keepalive Feature on the SSH Client
==============================================================

After the keepalive feature is configured on the SSH client, the client sends keepalive packets at the configured interval to the SSH server to check whether the connection between them is normal. The keepalive feature implements fast fault detection.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ssh client keepalive-interval**](cmdqueryname=ssh+client+keepalive-interval) *seconds*
   
   
   
   The interval at which the client sends keepalive packets to the server is configured.
   
   
   
   If the client does not receive a response from the server during an interval, the client sends another keepalive packet to the server. If the server still does not respond, the client is disconnected from the server.
3. Run [**ssh client keepalive-maxcount**](cmdqueryname=ssh+client+keepalive-maxcount) *count*
   
   
   
   The maximum number of keepalive packets that the client sends to the server is configured.
   
   
   
   The interval at which the client sends keepalive packets to the server must be greater than the maximum number of keepalive packets that the client sends to the server. For example, if the interval is 0 (no keepalive packet is sent), the setting of the maximum number of keepalive packets does not take effect.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.