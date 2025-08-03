Enabling/Disabling a SAID Node
==============================

This section describes how to enable or disable a system of active immunization and diagnosis (SAID) node using commands.

#### Context

The diagnosis and recovery durations of a single SAID node must not exceed 10 and 30 minutes, respectively. If either duration is exceeded, the SAID node is disabled by default. When a SAID node is processing a large number of services, the processing efficiency of other SAID nodes may be reduced because of performance insufficiency. To guarantee the processing efficiency, you can run the [**set said-node**](cmdqueryname=set+said-node) command to disable this node.

If the node is not in the detecting state after being disabled, it automatically returns to the detecting state upon completion of the operation in the current phase. When the next SAID task is started to perform detection, the system detects that the SAID node is disabled and therefore skips it.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**set said-node**](cmdqueryname=set+said-node) { **all** | *said-name* [ **slot** *slot-id* ] } **disable**
   
   
   
   The SAID node is disabled.
   
   In VS mode, this command is supported only by the admin VS.

#### Checking the Configurations

After enabling/disabling a SAID node, check the configurations.

* Run the [**display said-node**](cmdqueryname=display+said-node) **status** [ **slot** *slot-id*  ] **brief** command to check the status of the SAID node.