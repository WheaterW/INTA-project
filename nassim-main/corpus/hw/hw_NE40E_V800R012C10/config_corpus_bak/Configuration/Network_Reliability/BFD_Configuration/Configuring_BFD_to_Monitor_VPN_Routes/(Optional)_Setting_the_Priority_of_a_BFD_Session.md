(Optional) Setting the Priority of a BFD Session
================================================

Setting the priority of a BFD session can ensure that packets with a higher priority are forwarded.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. (Optional) Run [**bfd**](cmdqueryname=bfd)
   
   
   
   The BFD view is displayed.
3. (Optional) Run [**tos-exp**](cmdqueryname=tos-exp) *tos-value* **static**
   
   
   
   A priority is configured for all the static BFD session.
   
   
   
   To specify priorities for static BFD sessions in batches, run this command in the BFD view.
4. (Optional) Run **quit**
   
   
   
   Return to the system view.
5. Run [**bfd**](cmdqueryname=bfd) *session-name*
   
   
   
   The BFD session view is displayed.
6. Run [**tos-exp**](cmdqueryname=tos-exp) *tos-value*
   
   
   
   The priority of the static BFD session is set.
   
   
   
   If the [**tos-exp**](cmdqueryname=tos-exp) command is run in the BFD view and BFD session view, the configuration in the BFD session view takes effect.
7. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.