(Optional) Configuring the Precise Loop Blocking Function
=========================================================

Precise loop blocking determines trusted and untrusted interfaces by analyzing the frequency of MAC address entry flapping. When a MAC address entry changes repeatedly, precise blocking can precisely locate and block the untrusted interface with a loop.

#### Context

After MAC flapping-based loop detection is deployed on a device and the device detects a loop, the device blocks an AC interface with a lower blocking priority by default. However, MAC address entries of interfaces without loops may change due to the impact from a remote loop, and traffic over the interfaces with lower blocking priorities is interrupted. To address this problem, deploy accurate blocking of MAC flapping-based loop detection. Accurate blocking determines trusted and untrusted interfaces by analyzing the frequency of MAC address entry flapping. When a MAC address entry changes repeatedly, accurate blocking can accurately locate and block the interface with a loop, which is an untrusted interface.

For boards that do not support precise loop blocking, if only MAC address change information about these boards is received in the last loop detection interval, interfaces in the VLAN to which these boards connect are blocked based on their blocking priorities. In this situation, precise loop blocking does not work.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. (Optional) Run [**loop-detect eth-loop precise-block trust-port**](cmdqueryname=loop-detect+eth-loop+precise-block+trust-port) **generate-time** *generate-time*
   
   
   
   The interval for generating a trusted interface is configured.
3. (Optional) Run [**loop-detect eth-loop precise-block policy no-block**](cmdqueryname=loop-detect+eth-loop+precise-block+policy+no-block)
   
   
   
   The blocking policy is specified for the local device that does not have trusted interfaces when MAC addresses change.
4. Run [**vlan**](cmdqueryname=vlan) *vlan-id*
   
   
   
   The VLAN view is displayed.
5. Run [**loop-detect eth-loop precise-block enable**](cmdqueryname=loop-detect+eth-loop+precise-block+enable)
   
   
   
   Precise blocking for MAC flapping-based loop detection is enabled. This means that the device blocks only untrusted interfaces.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Follow-up Procedure

After MAC flapping-based loop detection is configured, if an interface on a VLAN is blocked due to a loop, the interface does not forward user traffic. To unblock the interface so that it can forward user traffic, run the [**reset loop-detect eth-loop**](cmdqueryname=reset+loop-detect+eth-loop) command.