Applying an ETS Profile
=======================

Applying an ETS Profile

#### Context

You can apply an ETS profile to an interface so that the interface can provide differentiated services.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the view of the interface to which an ETS profile is to be applied.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
3. Apply an ETS profile.
   
   
   ```
   [dcb ets enable](cmdqueryname=dcb+ets+enable) etsprofile
   ```
   
   
   
   By default, no ETS profile is applied to an interface.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```