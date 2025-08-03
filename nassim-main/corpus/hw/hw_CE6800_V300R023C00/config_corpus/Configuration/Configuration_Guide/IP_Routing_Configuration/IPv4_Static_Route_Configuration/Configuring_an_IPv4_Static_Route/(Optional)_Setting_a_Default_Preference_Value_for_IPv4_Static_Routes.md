(Optional) Setting a Default Preference Value for IPv4 Static Routes
====================================================================

(Optional) Setting a Default Preference Value for IPv4 Static Routes

#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Set a default preference value for static routes.
   
   
   ```
   [ip route-static default-preference](cmdqueryname=ip+route-static+default-preference) preference
   ```
   
   You can run this command to change the active attribute of an IPv4 static route. By default, the preference value of IPv4 static routes is 60.
   
   
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   After the default preference value is set, it takes effect only on newly configured IPv4 static routes.
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```