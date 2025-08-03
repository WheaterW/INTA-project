(Optional) Modifying BFD Parameters
===================================

BFD parameters, such as BFD detection intervals and detection multipliers, can be modified.

#### Context

Perform the following steps on the ingress.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bfd**](cmdqueryname=bfd)
   
   
   
   The BFD view is displayed.
3. Run [**mpls ping interval**](cmdqueryname=mpls+ping+interval) *interval*
   
   
   
   The interval at which LSP Ping packets are sent is changed.
4. Run [**quit**](cmdqueryname=quit)
   
   
   
   Exit from the BFD view.
5. Run [**mpls**](cmdqueryname=mpls)
   
   
   
   The MPLS view is displayed.
6. (Optional) Run [**mpls bfd**](cmdqueryname=mpls+bfd+min-tx-interval+min-rx-interval+detect-multiplier) { **min-tx-interval** *min-tx-interval-value* | **min-rx-interval** *min-rx-interval-value* | **detect-multiplier** *detect-multiplier-value* }\*
   
   
   
   BFD parameters are set.
   
   
   
   Effective local interval at which BFD packets are sent = MAX { Locally configured interval at which BFD packets are sent, Remotely configured interval at which BFD packets are received}
   
   Effective local interval at which BFD packets are received = MAX { Remotely configured interval at which BFD packets are sent, Locally configured interval at which BFD packets are received }
   
   Local BFD detection period = Actual local interval at which BFD packets are received x Remotely configured BFD detection multiplier
   
   Therefore, you can adjust the minimum interval at which BFD packets are sent, the minimum interval at which BFD packets are received, and the detection multiplier only on the ingress to update BFD detection time parameters on both the ingress and egress.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   When POS-Trunk interfaces work in 1:1 mode, the local actual receiving interval must be greater than or equal to three times of the POS-Trunk interface switching time. Otherwise, the BFD session may go Down during the POS-Trunk interface switching.
7. (Optional) Run [**mpls bfd-tunnel**](cmdqueryname=mpls+bfd-tunnel+min-tx-interval+min-rx-interval) { **min-tx-interval** *min-tx-interval-value* | **min-rx-interval** *min-rx-interval-value* | **detect-multiplier** *detect-multiplier-value* }\*
   
   
   
   BFD parameters are set.
   
   
   
   Effective local interval at which BFD packets are sent = MAX { Locally configured interval at which BFD packets are sent, Remotely configured interval at which BFD packets are received}
   
   Effective local interval at which BFD packets are received = MAX { Remotely configured interval at which BFD packets are sent, Locally configured interval at which BFD packets are received }
   
   Local BFD detection period = Actual local interval at which BFD packets are received x Remotely configured BFD detection multiplier
   
   If both the [**mpls bfd-tunnel**](cmdqueryname=mpls+bfd-tunnel) and [**mpls bfd**](cmdqueryname=mpls+bfd) commands are run, the parameters configured using the [**mpls bfd-tunnel**](cmdqueryname=mpls+bfd-tunnel) command take precedence over those configured using the [**mpls bfd**](cmdqueryname=mpls+bfd) command.
8. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.