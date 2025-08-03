Setting the Rate at Which Packets Are Sent to Create a Flow for a User
======================================================================

A device can be configured to dynamically detect the traffic forwarding rate and limit the rate at which packets are sent to create a flow for each user.

#### Context

A NAT64 device with a multi-core structure allows flow construction and forwarding processes to share CPU resources. To minimize or prevent NAT64 packet loss and a CPU usage increase, the device has to maintain a proper ratio of the forwarding rate to the flow creation rate.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**nat64 instance**](cmdqueryname=nat64+instance) *instance-name* [ **id** *id* ]
   
   
   
   The NAT64 instance view is displayed.
3. (Optional) Run [**nat64 user-session create-rate limit enable**](cmdqueryname=nat64+user-session+create-rate+limit+enable)
   
   
   
   The limit on the rate at which packets are sent to create a user flow is set.
   
   
   
   To disable this function, run the [**undo ds-lite user-session create-rate limit enable**](cmdqueryname=undo+ds-lite+user-session+create-rate+limit+enable) command.
4. Run [**nat64 user-session create-rate**](cmdqueryname=nat64+user-session+create-rate) *rate*
   
   
   
   The rate at which packets are sent to create a flow on a NAT64 device is set.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.