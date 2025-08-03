Configuring the Locking Function for Administrators Who Fail Remote Authentication
==================================================================================

To ensure account and password security of administrators, enable the account locking function for administrators who fail remote authentication.

#### Context

After the account locking function is enabled for administrators who fail remote authentication, the account will be locked if the number of consecutive incorrect account or password attempts reaches the upper limit within the retry interval. The account will be automatically unlocked after the locking period expires.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**aaa**](cmdqueryname=aaa)
   
   
   
   The AAA view is displayed.
3. Run [**administrator remote authen-fail retry-interval**](cmdqueryname=administrator+remote+authen-fail+retry-interval) *retry-interval* **retry-time** *retry-time* **block-time** *block-time*
   
   
   
   The account locking function is enabled for administrators who fail remote authentication.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
5. Run [**remote-user authen-fail unblock**](cmdqueryname=remote-user+authen-fail+unblock)  { **all** | **username** *username* }
   
   
   
   The remote authentication accounts that fail authentication are unlocked.

#### Result

Run the [**display remote-user authen-fail**](cmdqueryname=display+remote-user+authen-fail) [ **blocked** | **username** *username* ] command to check the accounts that fail remote AAA authentication.