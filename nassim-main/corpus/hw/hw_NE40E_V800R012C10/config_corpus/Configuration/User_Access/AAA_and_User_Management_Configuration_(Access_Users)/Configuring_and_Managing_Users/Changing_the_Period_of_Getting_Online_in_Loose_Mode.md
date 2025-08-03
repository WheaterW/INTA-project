Changing the Period of Getting Online in Loose Mode
===================================================

Getting online in loose mode after the NE40E restarts due to an exception reduces client restarts, but may consume a lot of resources. You can change the period during which users can get online in loose mode.

#### Prerequisites

IP/ARP packet-triggered user login has been enabled on a BAS interface.


#### Context

By default, the user information backup table cannot be queried within two hours after the NE40E restarts due to an exception, but original online users can still go online by sending IP/ARP packets, which is getting online in loose mode within the two hours. This ensures that the users who go offline can get online again before a lease renewal failure or terminal restart. To change the period of getting online in loose mode, perform the following steps on the NE40E.


#### Procedure

* Configure a period for user access in loose mode in the AAA view.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**aaa**](cmdqueryname=aaa)
     
     
     
     The AAA view is displayed.
  3. Run [**access-trigger**](cmdqueryname=access-trigger) **loose** { *loose-time* | **all-time** }
     
     
     
     The period during which users can get online in loose mode after the NE40E restarts is set.
     
     By default, users can get online in loose mode for 120 minutes after the NE40E restarts.
  4. Run [**access-trigger loose infinite-lease**](cmdqueryname=access-trigger+loose+infinite-lease)
     
     
     
     Users with an infinite lease are enabled to go online by sending IP/ARP packets when backup entries for unexpected logout are not generated.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure a period for user access in loose mode in the AAA domain view.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**aaa**](cmdqueryname=aaa)
     
     
     
     The AAA view is displayed.
  3. Run [**domain**](cmdqueryname=domain) *domain-name*
     
     
     
     The AAA domain view is displayed.
  4. Run [**access-trigger**](cmdqueryname=access-trigger) **loose** { *loose-time* | **all-time** }
     
     
     
     The period, during which users in the authentication domain bound to the BAS interface can go online in loose mode after the NE40E restarts, is set.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     If the period is configured in both the AAA view and AAA domain view, the configuration in the AAA domain view takes effect.
  5. Run [**access-trigger loose infinite-lease**](cmdqueryname=access-trigger+loose+infinite-lease)
     
     
     
     Users with an infinite lease in the authentication domain bound to the BAS interface are enabled to go online by sending IP/ARP packets when backup entries for unexpected logout are not generated.
  6. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.