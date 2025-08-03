Checking and Clearing ND Message Statistics in a BD
===================================================

Checking and Clearing ND Message Statistics in a BD

#### Context

Before collecting new statistics about ND messages in a BD, you can clear the existing statistics to improve information accuracy.


#### Procedure

* In the user view, clear ND packet statistics about a BD.
  
  
  ```
  [reset ipv6 nd packet statistics bridge-domain](cmdqueryname=reset+ipv6+nd+packet+statistics+bridge-domain) [ bd-id ]
  ```
  
  If the *bd-id* parameter is not specified, the ND message statistics of all BDs are cleared.
* Display the ND message statistics of a BD in any view.
  
  
  ```
  [display ipv6 nd packet statistics bridge-domain](cmdqueryname=display+ipv6+nd+packet+statistics+bridge-domain) [ bd-id ]
  ```
  
  If the *bd-id* parameter is not specified, the ND message statistics of all BDs are displayed.