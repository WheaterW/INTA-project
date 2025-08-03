Configuring Send-time of a Key-id
=================================

Configuring_Send-time_of_a_Key-id

#### Context

The time modes for sending key IDs vary according to keychain configuration modes.


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
  5. Run [**send-time**](cmdqueryname=send-time) *start-time* *start-date* { **duration** { *duration-value* | **infinite** } | { **to** *end-time* *end-date* } }
     
     
     
     The send-time for the key-id is configured.
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
  5. Run [**send-time**](cmdqueryname=send-time) **daily** *start-time* **to** *end-time*
     
     
     
     The send-time for the key-id is configured.
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
  5. Run [**send-time**](cmdqueryname=send-time) **day** { *start-day* **to** *end-day* | *start-day* &<1-7> }
     
     
     
     The send-time for the key-id is configured.
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
  5. Run [**send-time**](cmdqueryname=send-time) **date** { *start-date* **to** *end-date* | *start-date* &<1-31> }
     
     
     
     The send-time for the key-id is configured.
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
  5. Run [**send-time**](cmdqueryname=send-time) **month** { *start-month* **to** *end-month* | *start-month* &<1-12> }
     
     
     
     The send-time for the key-id is configured.
     
     Send-time for a key-id is configured according to the timing mode defined for the keychain. Only one send key-id in a keychain can be active at a time. The send-time of different key-ids in a keychain must not overlap each other.
     
     To re-configure send-time, we need to undo the send-time that is currently configured.
  6. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configurations are committed.