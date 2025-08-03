Configuring Receive-time of a Key-id
====================================

Configuring_Receive-time_of_a_Key-id

#### Context

The time modes for receiving key IDs vary according to keychain configuration modes.


#### Procedure

* **Absolute Timing Mode**
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is entered.
  2. Run [**keychain**](cmdqueryname=keychain) *keychain-name* **mode** **absolute**
     
     
     
     The keychain is created in absolute timing mode and keychain view is entered.
  3. Run [**time mode**](cmdqueryname=time+mode) { **utc** | **lmt** }
     
     
     
     The time mode for keychain is configured.
  4. Run [**key-id**](cmdqueryname=key-id) *key-id*
     
     
     
     The key-id is created and key-id view is entered.
  5. Run [**receive-time**](cmdqueryname=receive-time) *start-time* *start-date* { **duration** { *duration-value* | **infinite** } | { **to** *end-time* *end-date* } }
     
     
     
     The receive-time for the key-id is configured.
  6. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configurations are committed.
* **Daily Periodic Timing Mode**
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is entered.
  2. Run [**keychain**](cmdqueryname=keychain) *keychain-name* **mode** **periodic** **daily**
     
     
     
     The keychain is created in daily periodic timing mode and keychain view is entered.
  3. Run [**time mode**](cmdqueryname=time+mode) { **utc** | **lmt** }
     
     
     
     The time mode for keychain is configured.
  4. Run [**key-id**](cmdqueryname=key-id) *key-id*
     
     
     
     The key-id is created and key-id view is entered.
  5. Run [**receive-time**](cmdqueryname=receive-time) **daily** *start-time* **to** *end-time*
     
     
     
     The receive-time for the key-id is configured.
  6. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configurations are committed.
* **Weekly Periodic Timing Mode**
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is entered.
  2. Run [**keychain**](cmdqueryname=keychain) *keychain-name* **mode** **periodic** **weekly**
     
     
     
     The keychain is created in weekly periodic timing mode and keychain view is entered.
  3. Run [**time mode**](cmdqueryname=time+mode) { **utc** | **lmt** }
     
     
     
     The time mode for keychain is configured.
  4. Run [**key-id**](cmdqueryname=key-id) *key-id*
     
     
     
     The key-id is created and key-id view is entered.
  5. Run [**receive-time**](cmdqueryname=receive-time) **day** { *start-day* **to** *end-day* | *start-day* &<1-7> }
     
     
     
     The receive-time for the key-id is configured.
  6. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configurations are committed.
* **Monthly Periodic Timing Mode**
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is entered.
  2. Run [**keychain**](cmdqueryname=keychain) *keychain-name* **mode** **periodic** **monthly**
     
     
     
     The keychain is created in monthly periodic timing mode and keychain view is entered.
  3. Run [**time mode**](cmdqueryname=time+mode) { **utc** | **lmt** }
     
     
     
     The time mode for keychain is configured.
  4. Run [**key-id**](cmdqueryname=key-id) *key-id*
     
     
     
     The key-id is created and key-id view is entered.
  5. Run [**receive-time**](cmdqueryname=receive-time) **date** { *start-date* **to** *end-date* | *start-date* &<1-31> }
     
     
     
     The receive-time for the key-id is configured.
  6. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configurations are committed.
* **Yearly Periodic Timing Mode**
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is entered.
  2. Run [**keychain**](cmdqueryname=keychain) *keychain-name* **mode** **periodic** **yearly**
     
     
     
     The keychain is created in yearly periodic timing mode and keychain view is entered.
  3. Run [**time mode**](cmdqueryname=time+mode) { **utc** | **lmt** }
     
     
     
     The time mode for keychain is configured.
  4. Run [**key-id**](cmdqueryname=key-id) *key-id*
     
     
     
     The key-id is created and key-id view is entered.
  5. Run [**receive-time**](cmdqueryname=receive-time) **month** { *start-month* **to** *end-month* | *start-month* &<1-12> }
     
     
     
     The receive-time for the key-id is configured.
     
     Receive-time for a key-id is configured in accordance with the timing mode defined for the keychain.
     
     To re-configure receive time you need to undo the receive time that is currently configured.
  6. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configurations are committed.