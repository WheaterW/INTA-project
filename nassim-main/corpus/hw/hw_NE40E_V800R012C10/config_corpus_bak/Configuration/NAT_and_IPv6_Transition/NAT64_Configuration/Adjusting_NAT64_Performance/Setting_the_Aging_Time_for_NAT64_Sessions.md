Setting the Aging Time for NAT64 Sessions
=========================================

Setting_the_Aging_Time_for_NAT64_Sessions

#### Context

The aging time of NAT64 sessions for various protocols can be adjusted, so that expired NAT64 sessions are deleted as soon as possible and system resources can be released.

Perform the following steps on the Router on which the aging time of NAT64 sessions is to be set:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. (Optional) Set the fast aging time for DNS sessions.
   
   
   
   You are advised to configure this function when DNS traffic is heavy. After the fast aging function for DNS sessions is enabled, if the device receives DNS request and response packets at the same time, the DNS sessions age according to the configured fast aging time to save system resources.
   
   
   
   1. Run **nat session dns fast-aging enable**
      
      The fast aging function is enabled for DNS sessions.
   2. Run **nat session dns fast-aging-time** *aging-time*
      
      A fast aging time is set for DNS sessions.
3. (Optional) Run [**nat64 instance**](cmdqueryname=nat64+instance) *instance-name* [ **id** *id* ]
   
   
   
   The NAT64 instance view is displayed.
4. (Optional) Run [**nat64 session aging-time**](cmdqueryname=nat64+session+aging-time) { **fin-rst** | **fragment** | **ftp** | **icmp** | **pptp** | **rtsp** | **sip** | **syn** | **tcp** | **udp** } *aging-time*
   
   
   
   An aging time is set for a specified type of session.
   
   
   
   If an aging time is set for a NAT64 instance, this aging time is used when a session is established in the instance. If no aging time is set for a NAT64 instance, the aging time set in the system view is used when a session is established in the instance.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.