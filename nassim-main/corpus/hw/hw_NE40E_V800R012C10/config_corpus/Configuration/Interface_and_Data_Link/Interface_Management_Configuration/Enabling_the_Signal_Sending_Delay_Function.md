Enabling the Signal Sending Delay Function
==========================================

This section describes how to configure the signal sending delay function.

#### Usage Scenario

After a device is restarted or a board is replaced, if an interface sends signals immediately after initialization before the link completes a switchover or configuration restoration, data loss may occur. To prevent data loss, configure the signal sending delay function.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

* Only physical interfaces can be configured with signal sending delays. Logical interfaces do not support this function.
* Configuring a signal sending delay does not affect an interface that has sent signals to the peer, and the configuration takes effect after the interface is initialized.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number* or [**controller**](cmdqueryname=controller) *interface-type* *interface-number*
   
   
   
   The corresponding interface view is displayed.
3. Run [**port-tx-enabling-delay**](cmdqueryname=port-tx-enabling-delay) *delay-value*
   
   
   
   The signal sending delay function is enabled, and the signal sending delay is configured.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

After the configuration is complete, run the [**display port-tx-enabling-delay**](cmdqueryname=display+port-tx-enabling-delay) **interface** command to check information about the signal sending delay on an interface.