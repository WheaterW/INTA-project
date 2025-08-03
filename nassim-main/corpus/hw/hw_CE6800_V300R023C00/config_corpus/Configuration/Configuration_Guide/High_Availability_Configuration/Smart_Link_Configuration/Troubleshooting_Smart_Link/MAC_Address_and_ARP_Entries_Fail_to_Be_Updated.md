MAC Address and ARP Entries Fail to Be Updated
==============================================

MAC Address and ARP Entries Fail to Be Updated

#### Possible Causes

The functions to send and receive Flush packets are not enabled.


#### Procedure

1. Check whether the function to send Flush packets is enabled.
   1. Enter the Smart Link group view.
      
      
      ```
      [smart-link group](cmdqueryname=smart-link+group) group-id
      ```
   2. Check the Flush packet sending configuration.
      
      
      ```
      [display this](cmdqueryname=display+this)
      ```
      
      If the function to send Flush packets is enabled, go to Step 2. If it is not enabled, refer to [Configuring Sending and Receiving of Smart Link Flush Packets](vrp_smlk_cfg_0007.html) to enable this function.
2. Check whether the function to receive Flush packets is enabled.
   1. Enter the interface view.
      
      
      ```
      [interface](cmdqueryname=interface) {interface-name|interface-type interface-number}
      ```
   2. Check interface configurations.
      
      
      ```
      [display this](cmdqueryname=display+this)
      ```
      
      Configure the interface to receive Flush packets if this function has not already been enabled. For details about how to enable the function to send and receive Flush packets, see [Configuring Sending and Receiving of Smart Link Flush Packets](vrp_smlk_cfg_0007.html).