Checking MAC Address Entries in a BD
====================================

Checking MAC Address Entries in a BD

#### Context

During routine maintenance, you can run the following commands in any view to check MAC address entries in a BD and to learn the VXLAN operating status.


#### Procedure

* Display all MAC address entries in a BD.
  
  
  ```
  [display mac-address](cmdqueryname=display+mac-address) [ mac-address ] bridge-domain bd-id [ verbose ]
  ```
* Display the number of MAC address entries in a BD.
  
  
  ```
  [display mac-address total-number](cmdqueryname=display+mac-address+total-number) [ static ] bridge-domain bd-id
  ```