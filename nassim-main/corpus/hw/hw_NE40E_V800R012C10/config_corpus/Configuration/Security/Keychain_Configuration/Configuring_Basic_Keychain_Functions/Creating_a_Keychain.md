Creating a Keychain
===================

Creating a Keychain

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is entered.
2. Run [**keychain**](cmdqueryname=keychain) *keychain-name* **mode** { **absolute** | **periodic** { **daily** | **weekly** | **monthly** | **yearly** } }
   
   
   
   Keychain is created and keychain view is entered.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   When creating a keychain, timing mode is mandatory. Once a keychain
   is created, to enter the keychain view timing mode need not be specified.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configurations are
   committed.