Generating User Login Failure and Logout Records
================================================

You can determine the cause and time of users' online and offline behavior from their login and logout records.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Enable the function to generate user login failure and logout records.
   1. Run [**aaa offline-record**](cmdqueryname=aaa+offline-record)
      
      
      
      The function to generate logout records is enabled.
   2. Run [**aaa online-fail-record**](cmdqueryname=aaa+online-fail-record)
      
      
      
      The function to generate login failure records is enabled.
   3. Run [**aaa abnormal-offline-record**](cmdqueryname=aaa+abnormal-offline-record)
      
      
      
      The function to generate unexpected logout records is enabled.
   4. Run [**aaa normal-offline-record**](cmdqueryname=aaa+normal-offline-record)
      
      
      
      The function to generate normal logout records is enabled.
3. (Optional) Run [**aaa offline-record mib-order lexicographical-order**](cmdqueryname=aaa+offline-record+mib-order+lexicographical-order)
   
   
   
   The device is configured to display user offline records in the MIB table **hwAAAOfflineRecordTable** in lexicographical order.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.