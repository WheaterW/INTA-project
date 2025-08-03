(Optional) Setting a Default Preference Value for IPv6 Static Routes
====================================================================

(Optional) Setting a Default Preference Value for IPv6 Static Routes

#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Set a default preference value for static routes.
   
   
   ```
   [ipv6 route-static default-preference](cmdqueryname=ipv6+route-static+default-preference) preference
   ```
   
   By default, the preference value of IPv6 static routes is 60.
   
   
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   After the default preference value is set, this setting is valid only for new IPv6 static routes.
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```