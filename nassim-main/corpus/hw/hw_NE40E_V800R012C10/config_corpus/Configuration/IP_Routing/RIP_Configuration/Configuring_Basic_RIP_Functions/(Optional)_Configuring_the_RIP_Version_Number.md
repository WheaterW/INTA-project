(Optional) Configuring the RIP Version Number
=============================================

RIP includes RIP-1 and RIP-2. The two versions have different functions.

#### Procedure

* Configure the global RIP version number.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**rip**](cmdqueryname=rip) [ *process-id* ]
     
     
     
     A RIP process is created, and the RIP view is displayed.
  3. Run [**version**](cmdqueryname=version) *version-num*
     
     
     
     The global RIP version number is specified.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     The RIP-1 protocol poses a security risk, and therefore the RIP-2 protocol is recommended.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure the RIP version number on an interface.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run **interface** *interface-type* *interface-number*
     
     
     
     The interface view is displayed.
  3. Run [**rip version**](cmdqueryname=rip+version) { 1 | 2 [ **broadcast** | **multicast** ] }
     
     
     
     The RIP version number is specified for the interface.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     The RIP-1 protocol poses a security risk, and therefore the RIP-2 protocol is recommended.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.