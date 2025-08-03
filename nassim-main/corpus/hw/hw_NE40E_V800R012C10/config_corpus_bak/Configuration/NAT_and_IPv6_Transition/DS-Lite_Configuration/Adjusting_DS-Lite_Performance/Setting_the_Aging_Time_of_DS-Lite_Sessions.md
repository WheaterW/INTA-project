Setting the Aging Time of DS-Lite Sessions
==========================================

The aging time of DS-Lite sessions of each protocol can be set. After the configured aging time elapses, DS-Lite sessions age, and system resources can be released.

#### Context

Perform the following steps on the Router:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**nat session aging-time**](cmdqueryname=nat+session+aging-time) { **tcp** | **udp** | **icmp** | **fin-rst** | **syn** | **fragment** | **dns** | **ftp** | **http** | **rtsp** | **sip** | **pptp** | **tcp** **long-link** | **ip** } *aging-time*
   
   
   
   An aging time is set for a specified type of session.
   
   
   
   The changed aging time takes effect on new DS-Lite session entries, not on existing DS-Lite session entries.
3. (Optional) Set the fast aging time for DNS sessions.
   
   
   
   You are advised to configure this function when DNS traffic is heavy. After the fast aging function for DNS sessions is enabled, if the device receives DNS request and response packets at the same time, the DNS sessions age according to the configured fast aging time to save system resources.
   
   
   
   1. Run **nat session dns fast-aging enable**
      
      The fast aging function is enabled for DNS sessions.
   2. Run **nat session dns fast-aging-time** *aging-time*
      
      A fast aging time is set for DNS sessions.
4. Run [**ds-lite instance**](cmdqueryname=ds-lite+instance) *instance-name* [ **id** *id* ]
   
   
   
   The DS-Lite instance view is displayed.
5. Run [**ds-lite session aging-time**](cmdqueryname=ds-lite+session+aging-time) { **tcp** | **udp** | **syn** | **fin-rst** | **icmp** | **ftp** | **rtsp** | **sip** | **pptp** | **fragment** } *aging-time*
   
   
   
   An aging time is set for DS-Lite sessions of a specified protocol.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.