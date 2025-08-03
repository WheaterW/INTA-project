(Optional) Configuring a Blocking Policy
========================================

After deploying MAC flapping-based loop detection, you can configure a blocking policy for AC-side interfaces or PWs (AC is short for attachment circuit, and PW for pseudo wire).

#### Context

The blocking policy for AC-side interfaces is different from that for PWs.

* MAC flapping-based loop detection has the following blocking policies:
  + Blocking interfaces based on their blocking priorities
    
    The blocking priority of an interface can be configured. When detecting a loop, a device blocks the interface with a lower blocking priority.
  + Blocking interfaces based on their trusted or untrusted states (accurate blocking)
    
    If a dynamic MAC address entry remains the same in the MAC address table within a specified period and is not deleted, the outbound interface in the MAC address entry is trusted. When detecting a loop, a device blocks an interface that is not trusted.
  
  After MAC flapping-based loop detection is deployed on a device and the device detects a loop, the device blocks an AC interface with a lower blocking priority by default. However, MAC address entries of interfaces without loops may change due to the impact from a remote loop, and traffic over the interfaces with lower blocking priorities is interrupted. To address this problem, deploy accurate blocking of MAC flapping-based loop detection. Accurate blocking determines trusted and untrusted interfaces by analyzing the frequency of MAC address entry flapping. When a MAC address entry changes repeatedly, accurate blocking can accurately locate and block the interface with a loop, which is an untrusted interface.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

If no blocking policies are configured, both AC-side interfaces and PWs are blocked based on their blocking priorities. If a loop occurs and the AC-side interfaces or PWs have the same blocking priority, the AC-side interfaces or PWs are all blocked.



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
       
       The device is configured not to block any interfaces with MAC address entry flapping in a virtual switching instance (VSI) or a bridge-domain (BD) if the device does not have any trusted interfaces.
    4. Run [**vsi**](cmdqueryname=vsi) *vsi-name* or [**bridge-domain**](cmdqueryname=bridge-domain) *bd-id*
       
       The VSI view or the bridge domain (BD) view is displayed.
    5. Run [**loop-detect eth-loop precise-block enable**](cmdqueryname=loop-detect+eth-loop+precise-block+enable)
       
       Precise blocking is enabled. This means that the device blocks only untrusted interfaces.
    6. Run [**commit**](cmdqueryname=commit)
       
       The configuration is committed.
* Configure a blocking policy for a PW.
  
  
  + Blocking a PW based on its blocking priority
    1. Run [**system-view**](cmdqueryname=system-view)
       
       The system view is displayed.
    2. Run [**vsi**](cmdqueryname=vsi) *vsi-name*
       
       The VSI view is displayed.
    3. Run [**pwsignal ldp**](cmdqueryname=pwsignal+ldp)
       
       The VSI-LDP view is displayed (LDP is short for Label Distribution Protocol).
    4. Run [**vsi-id**](cmdqueryname=vsi-id) *vsi-id*
       
       An ID is configured for the VSI.
    5. Run [**peer**](cmdqueryname=peer) *peer-address* [ **negotiation-vc-id** *vc-id* ] [ **tnl-policy** *policy-name* ] [ **upe** ] [ **ignore-standby-state** ]
       
       A peer IP address is configured for the VSI.
    6. Run [**peer**](cmdqueryname=peer) *peer-address* [ **negotiation-vc-id** *vc-id* ] **pw** *pw-name*
       
       The VSI-LDP-PW view is displayed.
    7. Run [**loop-detect eth-loop priority**](cmdqueryname=loop-detect+eth-loop+priority) *priority*
       
       A blocking priority is configured for the PW.
    8. Run [**commit**](cmdqueryname=commit)
       
       The configuration is committed.
  + Blocking PWs based on their trusted or untrusted states (precise blocking)
    1. Run [**system-view**](cmdqueryname=system-view)
       
       The system view is displayed.
    2. Run [**loop-detect eth-loop precise-block trust-port**](cmdqueryname=loop-detect+eth-loop+precise-block+trust-port) **generate-time** *generate-time*
       
       The interval for generating a trusted PW is configured.
    3. (Optional) Run [**loop-detect eth-loop precise-block policy no-block**](cmdqueryname=loop-detect+eth-loop+precise-block+policy+no-block)
       
       The device is configured not to block any PWs with MAC address entry flapping in a VSI if the device does not have any trusted PW.
    4. Run [**vsi**](cmdqueryname=vsi) *vsi-name*
       
       The VSI view is displayed.
    5. Run [**loop-detect eth-loop precise-block enable**](cmdqueryname=loop-detect+eth-loop+precise-block+enable)
       
       Precise blocking is enabled. This means that the device blocks only untrusted PWs.
    6. Run [**commit**](cmdqueryname=commit)
       
       The configuration is committed.

#### Follow-up Procedure

After MAC flapping-based loop detection is configured, if an AC-side interface or PW is blocked due to a loop, the interface or PW does not forward user traffic. To unblock the interface or PW so that it can forward user traffic, run the [**reset loop-detect eth-loop**](cmdqueryname=reset+loop-detect+eth-loop) command.