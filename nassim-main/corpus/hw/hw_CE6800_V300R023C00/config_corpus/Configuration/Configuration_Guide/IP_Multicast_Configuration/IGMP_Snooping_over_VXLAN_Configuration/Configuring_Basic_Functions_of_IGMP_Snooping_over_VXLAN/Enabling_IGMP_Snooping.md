Enabling IGMP Snooping
======================

Enabling IGMP Snooping

#### Context

IGMP snooping must be enabled globally before it can be enabled in a BD. Enabling IGMP snooping in a BD is the prerequisite for other IGMP snooping configurations in the BD to take effect.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enable IGMP snooping globally.
   
   
   ```
   [igmp snooping enable](cmdqueryname=igmp+snooping+enable)
   ```
3. Enter the BD view.
   
   
   ```
   [bridge-domain](cmdqueryname=bridge-domain) bd-id
   ```
4. Enable IGMP snooping in the BD.
   
   
   ```
   [igmp snooping enable](cmdqueryname=igmp+snooping+enable)
   ```
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```