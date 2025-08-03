Configuring Self-Loop Detection on the GE Interface
===================================================

After the self-loop detection function is enabled, the self-loop on an interface can be detected and then the interface is blocked.

#### Context

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

A router enabled with the loopback detect
function periodically sends specially constructed loopback detect
packets. If a self-loop exists on an interface, the loopback detect
packets will be looped back to the router, and the router can then
determine that a self-loop has occurred. A malicious attacker can
trick a loopback-detect-enabled router into believing that a self-loop
has occurred, by sending loopback detect packets obtained using Sniffer
back to the router.

The GE interface self-loop detection function
is used only for link self-loop tests in the service deployment phase.
To prevent security risks, disable this function after services are
running properly.

Perform the following steps on target Routers:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) **gigabitethernet** *interface-number*
   
   
   
   The specified GE interface view is displayed.
3. Run [**loopback-detect enable**](cmdqueryname=loopback-detect+enable)
   
   
   
   The self-loop detection function is enabled for the GE interface.
4. Run [**loopback-detect block**](cmdqueryname=loopback-detect+block) *block-time*
   
   
   
   The delay time for interface recovery after the self-loop on the interface is eliminated is set.