Checking and Clearing Proxy ND Entries in a BD
==============================================

Checking and Clearing Proxy ND Entries in a BD

#### Context

Before collecting new statistics about proxy ND entries in a BD, you can clear the existing statistics to improve information accuracy.


#### Procedure

* In the user view, clear the proxy ND entries of a BD.
  
  
  ```
  [reset ipv6 nd multicast-suppress dynamic bridge-domain](cmdqueryname=reset+ipv6+nd+multicast-suppress+dynamic+bridge-domain) [ bd-id ]
  ```
  
  If the *bd-id* parameter is not specified, the proxy ND entries of all BDs are cleared.
* Check the proxy ND entries of a BD in any view.
  
  
  ```
  [display ipv6 nd multicast-suppress bridge-domain](cmdqueryname=display+ipv6+nd+multicast-suppress+bridge-domain) [ bd-id ] [ verbose ]
  ```
  
  If the *bd-id* parameter is not specified, the proxy ND entries of all BDs are displayed.