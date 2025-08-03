Maintaining PFC
===============

Maintaining PFC

#### Context

To diagnose and locate PFC faults, collect statistics on PFC frames within a given period of time. When statistics on PFC frames need to be re-collected, clear the existing statistics first.

![](public_sys-resources/notice_3.0-en-us.png) 

The cleared statistics cannot be restored. Exercise caution when you perform this operation.



#### Procedure

* Run the [**display dcb pfc**](cmdqueryname=display+dcb+pfc) [ **interface** { **interface-name** | *interface-type* **interface-num** } ] command to check statistics on PFC frames on an interface.
* Run the [**reset dcb pfc**](cmdqueryname=reset+dcb+pfc) [ **interface** { **interface-name** | *interface-type* **interface-num** } ] command in the user view to clear statistics on PFC frames on an interface.
  
  ![](public_sys-resources/note_3.0-en-us.png) 
  
  An interface collects statistics on received PFC MAC control frames even when PFC is disabled. You can run the [**reset dcb pfc**](cmdqueryname=reset+dcb+pfc) command to clear the current PFC statistics.