Setting the Rate at Which Packets Are Sent to Create a Flow for a User
======================================================================

A device can be configured to dynamically detect the traffic forwarding rate and limit the rate at which packets are sent to create a flow for each user.

#### Context

A NAT device with a multi-core structure allows flow construction and forwarding processes to share CPU resources. To minimize or prevent NAT packet loss and a CPU usage increase, the device has to maintain a proper ratio of the forwarding rate to the flow creation rate.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**nat instance**](cmdqueryname=nat+instance) *instance-name* [ **id** *id* ]
   
   
   
   The NAT instance view is displayed.
3. (Optional) Run [**nat user-session create-rate limit enable**](cmdqueryname=nat+user-session+create-rate+limit+enable)
   
   
   
   The limit on the rate at which packets are sent to create a user flow is set.
4. Perform either of the following operations:
   
   
   * If the rate accuracy is low, run the [**nat user-session create-rate**](cmdqueryname=nat+user-session+create-rate) *rate* command.
   * If the rate accuracy is high, run the [**nat user-session create-rate extended-range**](cmdqueryname=nat+user-session+create-rate+extended-range) *rate* command.![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If both the [**nat user-session create-rate extended-range**](cmdqueryname=nat+user-session+create-rate+extended-range) and [**nat user-session create-rate**](cmdqueryname=nat+user-session+create-rate) commands are run, the latest configuration takes effect.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.