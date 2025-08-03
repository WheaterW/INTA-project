(Optional) Configuring Network Access Rights for Users When the 802.1X Client Does Not Respond
==============================================================================================

(Optional) Configuring Network Access Rights for Users When the 802.1X Client Does Not Respond

#### Prerequisites

Before configuring the network access rights available to users when the 802.1X client does not respond, you need to configure the following authorization information on the device.

* Configure a VLAN and associated network resources on the device.
* Configure a service scheme. For details, see [(Optional) Configuring a Service Scheme](galaxy_aaa_cfg_0014.html).

#### Context

If the 802.1X client does not respond, users cannot pass authentication and thereby have no network access rights. Before being successfully authenticated, some users may need certain basic network access rights to download client software and update the antivirus database. The network access rights can be configured for the users when the 802.1X client does not respond, so that the users can access specified network resources.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the 802.1X access profile view.
   
   
   ```
   [dot1x-access-profile](cmdqueryname=dot1x-access-profile) name access-profile-name
   ```
3. Configure network access rights available to users when the 802.1X client does not respond.
   
   
   ```
   [authentication event client-no-response action authorize](cmdqueryname=authentication+event+client-no-response+action+authorize) { service-scheme service-scheme-name | vlan vlan-id }
   ```
   
   By default, network access rights available to users when the 802.1X client does not respond are not configured.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```