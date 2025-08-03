Binding a Channel Group to a Board Group
========================================

After an eMDI channel group and a board group are created, bind the channel group to the board group to achieve eMDI distributed board detection.

#### Context

As a distributed board detection solution, eMDI requires the binding of a channel group to a board group. After the channel group and board group are bound, the board NP in the board group performs real-time monitoring of the video streams of a specified channel in order to obtain detection indicators such as the packet loss rate and packet out-of-order rate.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**emdi**](cmdqueryname=emdi)
   
   
   
   The eMDI view is displayed.
3. Run either of the following commands:
   
   
   * To bind an eMDI channel group to an eMDI board group in a BIER eMDI scenario, run the [**emdi bier bind lpu-group**](cmdqueryname=emdi+bier+bind+lpu-group) *lpu-group-name* command.
   * To bind an eMDI channel group to an eMDI board group in other scenarios, run the [**emdi bind channel-group**](cmdqueryname=emdi+bind+channel-group) *channel-group-name* **lpu-group** *lpu-group-name* [ **outbound** ] command.
4. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
5. (Optional) Run [**interface**](cmdqueryname=interface) { *interface-name* | *interface-type* *interface-number* }
   
   
   
   The interface view is displayed.
6. (Optional) Run [**emdi channel**](cmdqueryname=emdi+channel) *channel-name* **outbound**
   
   
   
   An eMDI channel is bound to the outbound interface.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Before binding an eMDI channel to the outbound interface, bind the corresponding eMDI channel group to an eMDI board group in the downstream direction.
7. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.