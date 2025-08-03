(Optional) Switching MAC Address Models for MPs
===============================================

This section describes how to switch Media Access Control (MAC) address models for maintenance points (MPs).

#### Context

IEEE 802.1ag defines the following MAC address models for MPs:

* Individual MAC address model: MPs are mapped to interface MAC addresses. If the individual MAC address model is configured, each MP on a device uses an interface MAC address as its MAC address. If the interfaces are Layer 2 interfaces switched from Layer 3 interfaces using the [**portswitch**](cmdqueryname=portswitch) command, the MAC addresses of Layer 3 interfaces are used.
* Shared MAC address model: MPs share a bridge MAC address. If the shared MAC address model is configured, all MPs on a device use the same bridge MAC address as their MAC addresses. This model reduces the amount of space reserved for storing MAC entries.

Perform the following steps on each device on which MAC address models need to be switched for MPs:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**cfm mp-address-model**](cmdqueryname=cfm+mp-address-model) { **bridge** | **individual** }
   
   
   
   MAC address models are switched for MPs.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If connectivity fault management (CFM) has been enabled, run the [**undo cfm enable**](cmdqueryname=undo+cfm+enable) command to disable it before switching MAC address models for MPs.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.