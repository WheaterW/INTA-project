Defining a GQ Profile and Configuring Scheduling Parameters
===========================================================

A GQ profile contains user group queues' scheduling parameters, which include the CIR and PIR of user group queues.

#### Context

Perform the following steps on the Router:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**user-group-queue**](cmdqueryname=user-group-queue) *group-name*
   
   
   
   The user group queue view is displayed.
3. Perform one of the following operations based on actual requirements:
   
   
   * Run the [**shaping**](cmdqueryname=shaping) *shaping-value* [ **pbs** *pbs-value* ] { **inbound** | **outbound** } command to set a shaping value.
   * Run the [**weight**](cmdqueryname=weight) *weight-value* **outbound** command to set a weight value.
   * Run the [**cir**](cmdqueryname=cir) *cir-value* [ **cbs** *cbs-value* ] [ **pir** *pir-value* [ **pbs** *pbs-value* ] ] **outbound** command to set a CIR.![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The [**shaping**](cmdqueryname=shaping) *shaping-value* [ **pbs** *pbs-value* ] { **inbound** | **outbound** } and [**cir**](cmdqueryname=cir) *cir-value* [ **cbs** *cbs-value* ] [ **pir** *pir-value* [ **pbs** *pbs-value* ] ] **outbound** commands are mutually exclusive.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.