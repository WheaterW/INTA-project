(Optional) Configuring the Receive Tolerance Time for a Keychain
================================================================

(Optional)_Configuring_the_Receive_Tolerance_Time_for_a_Keychain

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**keychain**](cmdqueryname=keychain) *keychain-name*
   
   
   
   The keychain view is displayed.
3. Run [**receive-tolerance**](cmdqueryname=receive-tolerance) { *value* | **infinite** | **seconds** *secvalue* }
   
   
   
   The receive tolerance time is configured for the keychain.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The receive tolerance time can be configured in the following two ways:
   
   * Set a specific time, in minutes or seconds. The maximum value is 14400 minutes (10 days) or 864000 seconds (10 days).
   * If the **infinite** parameter is set, the receive tolerance time of a key-ID is infinite.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.