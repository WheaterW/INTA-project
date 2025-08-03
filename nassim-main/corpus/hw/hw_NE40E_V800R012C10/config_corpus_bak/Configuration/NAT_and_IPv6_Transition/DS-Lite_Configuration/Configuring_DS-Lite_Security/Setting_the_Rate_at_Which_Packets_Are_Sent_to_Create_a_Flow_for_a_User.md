Setting the Rate at Which Packets Are Sent to Create a Flow for a User
======================================================================

A device can be configured to dynamically detect the traffic forwarding rate and limit the rate at which user sessions are created so that a certain proportion is maintained between the forwarding rate and the session creation rate.

#### Context

A DS-Lite device with a multi-core structure allows flow construction and forwarding processes to share CPU resources. To minimize or prevent DS-Lite packet loss and a CPU usage increase, the device has to maintain a proper ratio of the forwarding rate to the flow creation rate.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ds-lite instance**](cmdqueryname=ds-lite+instance) *instance-name* [ **id** *id* ]
   
   
   
   The DS-Lite instance view is displayed.
3. (Optional) Run [**ds-lite user-session create-rate limit enable**](cmdqueryname=ds-lite+user-session+create-rate+limit+enable)
   
   
   
   The limit on the rate at which packets are sent to create a session is enabled.
   
   
   
   To disable this function, run the [**undo ds-lite user-session create-rate limit enable**](cmdqueryname=undo+ds-lite+user-session+create-rate+limit+enable) command.
4. Run [**ds-lite user-session create-rate**](cmdqueryname=ds-lite+user-session+create-rate) *rate*
   
   
   
   The rate at which packets are sent to create a session is set.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.