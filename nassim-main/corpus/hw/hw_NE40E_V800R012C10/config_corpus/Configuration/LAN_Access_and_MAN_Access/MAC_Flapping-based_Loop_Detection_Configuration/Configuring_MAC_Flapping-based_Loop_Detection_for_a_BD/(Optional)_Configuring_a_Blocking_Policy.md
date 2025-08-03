(Optional) Configuring a Blocking Policy
========================================

After deploying MAC flapping-based loop detection, you can configure a blocking policy for AC-side interfaces (AC is short for attachment circuit).

#### Context

MAC flapping-based
loop detection has the following blocking policies:

* Blocking interfaces based on their blocking priorities
  
  The blocking priority of an interface can be configured. When detecting
  a loop, a device blocks the interface with a lower blocking priority.
* Blocking interfaces based on their trusted or untrusted states
  (accurate blocking)
  
  If a dynamic MAC address entry remains the
  same in the MAC address table within a specified period and is not
  deleted, the outbound interface in the MAC address entry is trusted.
  When detecting a loop, a device blocks an interface that is not trusted.

After MAC flapping-based
loop detection is deployed on a device and the device detects a loop,
the device blocks an AC interface with a lower blocking priority by
default. However, MAC address entries of interfaces without loops
may change due to the impact from a remote loop, and traffic over
the interfaces with lower blocking priorities is interrupted. To address
this problem, deploy accurate blocking of MAC flapping-based loop
detection. Accurate blocking determines trusted and untrusted interfaces
by analyzing the frequency of MAC address entry flapping. When a MAC
address entry changes repeatedly, accurate blocking can accurately
locate and block the interface with a loop, which is an untrusted
interface.


#### Procedure

* Configure a blocking policy for an AC-side interface.
  
  
  + Blocking interfaces based on their blocking priorities
    
    1. Run [**system-view**](cmdqueryname=system-view)
       
       The system view is displayed.
    2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number*
       
       The AC-side interface view is displayed.
    3. Run [**loop-detect eth-loop priority**](cmdqueryname=loop-detect+eth-loop+priority) *priority*
       
       A blocking policy is configured for the AC-side interface.
    4. Run [**commit**](cmdqueryname=commit)
       
       The configuration is committed.
  + Blocking interfaces based on their trusted or untrusted states (precise blocking)
    
    1. Run [**system-view**](cmdqueryname=system-view)
       
       The system view is displayed.
    2. Run [**loop-detect eth-loop precise-block trust-port**](cmdqueryname=loop-detect+eth-loop+precise-block+trust-port) **generate-time** *generate-time*
       
       The interval for generating a trusted interface is configured.
    3. (Optional) Run [**loop-detect eth-loop precise-block policy no-block**](cmdqueryname=loop-detect+eth-loop+precise-block+policy+no-block)
       
       The device is configured not to block any interfaces with MAC address entry flapping in a BD if the device does not have any trusted interfaces.
    4. Run [**bridge-domain**](cmdqueryname=bridge-domain) *bd-id*
       
       The bridge domain (BD) view is displayed.
    5. Run [**loop-detect eth-loop precise-block enable**](cmdqueryname=loop-detect+eth-loop+precise-block+enable)
       
       Precise blocking for MAC flapping-based loop detection is enabled. This enables the device to block only untrusted interfaces.
    6. Run [**commit**](cmdqueryname=commit)
       
       The configuration is committed.

#### Follow-up Procedure

After MAC flapping-based loop detection is configured, if an AC-side interface is blocked due to a loop, the interface does not forward user traffic. To unblock the interface so that it can forward user traffic, run the [**reset loop-detect eth-loop**](cmdqueryname=reset+loop-detect+eth-loop) command.