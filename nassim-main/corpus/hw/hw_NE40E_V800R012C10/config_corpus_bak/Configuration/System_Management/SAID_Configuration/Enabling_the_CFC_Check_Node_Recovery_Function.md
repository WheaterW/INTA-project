Enabling the CFC Check Node Recovery Function
=============================================

Enabling_the_CFC_Check_Node_Recovery_Function

#### Prerequisites

The function of checking the consistency between the control plane and forwarding plane has been enabled. If the function is disabled, run the [**undo set said-node cfc disable**](cmdqueryname=undo+set+said-node+cfc+disable) command to enable it.


#### Context

A large number of forwarding failures occur on the network and cannot recover automatically. As a result, services are interrupted and cannot be automatically restored for a long time. A mechanism is required to detect forwarding failures that cannot recover automatically. After a forwarding entry (such as route forwarding entry and ARP forwarding entry) failure is detected, proper measures are taken to rectify the fault quickly.

The control plane and forwarding plane consistency check (CFC) service node is a specific service node in the SAID framework. The CFC node selects some typical routes and compares the outbound interface, MAC address, and label encapsulation information on the control plane with those on the forwarding plane. If the information is inconsistent, the system enters the diagnosis state and performs the consistency check for multiple times. If the comparison result remains, an alarm is generated.

The SAID system diagnoses the CFC service node through three phases: flow selection, check, and troubleshooting. In this case, devices can perform automatic diagnosis, collect fault information automatically, and generate alarms.

After the control and forwarding plane consistency (CFC) check node recovery function is enabled, if a fault occurs and the system enters the diagnosis state, the interface is restarted after a flow is considered faulty for three consecutive times.

In VS mode, this configuration task is supported only by the admin VS.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**set said-cfc recovery enable**](cmdqueryname=set+said-cfc+recovery+enable)
   
   
   
   The CFC check node recovery function is enabled.
   
   
   
   To disable the CFC check node recovery function, run the [**undo set said-cfc recovery enable**](cmdqueryname=undo+set+said-cfc+recovery+enable) command.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.