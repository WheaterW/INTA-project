Setting the Mode of Processing the Packets Sent to the CPU
==========================================================

This section describes the default mode of handling protocol packets when association between the application layer and lower layers is enabled whereas no upper layer protocol is enabled.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**cpu-defend policy**](cmdqueryname=cpu-defend+policy) *policy-number*
   
   
   
   An attack defense policy is created and the attack defense policy view is displayed.
3. (Optional) Run [**undo application-apperceive disable**](cmdqueryname=undo+application-apperceive+disable)
   
   
   
   The application layer association is enabled.
   
   To disable application layer association, you need to run the [**application-apperceive disable**](cmdqueryname=application-apperceive+disable) command.
4. Run [**application-apperceive default-action**](cmdqueryname=application-apperceive+default-action+drop+min-to-cp) { **drop** | **min-to-cp** }
   
   
   
   The default mode of processing the packets to be sent to the CPU through application layer association is set. The default mode can be drop or min-to-cp.
   
   The advantage of the min-to-cp mode is that when a certain protocol for application layer association is disabled because of attack, you can gather information about the attack through attack source tracing. If the default mode is set to drop, the possibility of being attacked is reduced, but the attack source may be untraceable. You can select either mode as required.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.