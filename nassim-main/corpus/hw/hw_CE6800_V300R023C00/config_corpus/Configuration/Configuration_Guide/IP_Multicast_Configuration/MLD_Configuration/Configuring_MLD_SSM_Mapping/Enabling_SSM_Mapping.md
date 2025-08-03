Enabling SSM Mapping
====================

Enabling SSM Mapping

#### Context

Enabling SSM mapping on an interface of a multicast device connected to a user network segment is a basic condition for using SSM services. The configured SSM source-group address mapping entries take effect only after SSM mapping is enabled on the interface.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the view of the interface connected to the user network segment.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
3. Switch the interface working mode from Layer 2 to Layer 3.
   
   
   ```
   [undo portswitch](cmdqueryname=undo+portswitch)
   ```
   
   Determine whether to perform this step based on the current interface working mode.
4. (Optional) Set the MLD version number to 2.
   
   
   ```
   [mld version](cmdqueryname=mld+version) 2
   ```
   
   
   
   To ensure that hosts running any MLD version on the user network segment can obtain SSM services, you are advised to run MLDv2 on the interface connected to the user network segment.
5. Enable SSM mapping.
   
   
   ```
   [mld ssm-mapping enable](cmdqueryname=mld+ssm-mapping+enable)
   ```
6. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```