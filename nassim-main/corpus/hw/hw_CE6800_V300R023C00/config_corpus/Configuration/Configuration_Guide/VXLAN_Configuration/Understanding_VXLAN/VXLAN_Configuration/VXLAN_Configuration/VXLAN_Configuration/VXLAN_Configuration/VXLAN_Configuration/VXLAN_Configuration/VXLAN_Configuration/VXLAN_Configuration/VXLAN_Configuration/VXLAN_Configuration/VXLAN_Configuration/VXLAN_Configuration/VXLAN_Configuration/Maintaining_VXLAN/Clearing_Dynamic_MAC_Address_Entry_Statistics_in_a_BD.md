Clearing Dynamic MAC Address Entry Statistics in a BD
=====================================================

Clearing Dynamic MAC Address Entry Statistics in a BD

#### Context

Before collecting new statistics about dynamic MAC address entries in a BD, you can clear the existing statistics to improve information accuracy.

![](../public_sys-resources/note_3.0-en-us.png) 

Because cleared statistics about dynamic MAC address entries of a BD cannot be restored, exercise caution when performing this operation.



#### Procedure

* In the user view, clear statistics about dynamic MAC address entries in a specified BD.
  
  
  ```
  [reset mac-address bridge-domain](cmdqueryname=reset+mac-address+bridge-domain) bd-id
  ```