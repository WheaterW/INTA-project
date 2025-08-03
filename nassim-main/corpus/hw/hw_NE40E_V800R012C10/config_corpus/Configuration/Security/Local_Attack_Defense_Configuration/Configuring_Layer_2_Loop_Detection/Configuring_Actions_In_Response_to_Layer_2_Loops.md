Configuring Actions In Response to Layer 2 Loops
================================================

The CPU determines whether to enable or disable Layer 2 loop detection based on packet loss caused by the committed access rate (CAR). After Layer 2 loop detection is enabled, the CPU will take the configured actions in response to Layer 2 loops after the system detects an existing or a potential loop on an interface.

#### Context

The system can be configured to take one of the following actions in response to an existing or possible Layer 2 loop on an interface:

* Shut down the interface: The system will shut down the interface only after detecting an existing Layer 2 loop on the interface. This action stops the interface from sending numerous packets to the CPU.
* Send a trap: The system will send a trap after detecting an existing or a potential Layer 2 loop. The trap message can help a user locate the interface where the Layer 2 loop has occurred or may occur.
* Send a trap and shut down the interface: The system will send a trap and shut down the interface after detecting an existing Layer 2 loop on the interface.
* Ignore Layer 2 loops: The system will stop Layer 2 loop, but not shut down the interface or send a trap.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**slot**](cmdqueryname=slot) *slot-id*
   
   
   
   The slot view is displayed.
3. Run [**l2-loop-detect action**](cmdqueryname=l2-loop-detect+action+shutdown+up-times+up-interval+trap+disable) { **shutdown** [ **up-times** *up-times* | **up-interval** *up-interval* ] \* | **trap** **disable** }
   
   
   
   A responsive action for Layer 2 loops is configured.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * To enable the system to shut down the interface, run the [**l2-loop-detect action**](cmdqueryname=l2-loop-detect+action+shutdown+up-times+up-interval) **shutdown** [ **up-times** *up-times* | **up-interval** *up-interval* ] \* command.
   * By default, the function of sending a trap is enabled. If the function is disabled, running the [**undo l2-loop-detect action**](cmdqueryname=undo+l2-loop-detect+action+trap+disable) **trap** **disable** command will enable it.
   * To enable the system to send a trap and shut down the interface, run the [**undo l2-loop-detect action**](cmdqueryname=undo+l2-loop-detect+action+trap+disable) **trap** **disable** command to enable the function of sending a trap, and run the [**l2-loop-detect action**](cmdqueryname=l2-loop-detect+action+shutdown+up-times+up-interval) **shutdown** [ **up-times** *up-times* | **up-interval** *up-interval* ] \* command to enable the system to shut down the interface.
   * To configure the system to ignore Layer 2 loops, run the [**undo l2-loop-detect action**](cmdqueryname=undo+l2-loop-detect+action+shutdown) **shutdown** and [**l2-loop-detect action**](cmdqueryname=l2-loop-detect+action+trap+disable) **trap** **disable** commands to disable the function of shutting down the interface and the function of sending a trap, respectively.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.