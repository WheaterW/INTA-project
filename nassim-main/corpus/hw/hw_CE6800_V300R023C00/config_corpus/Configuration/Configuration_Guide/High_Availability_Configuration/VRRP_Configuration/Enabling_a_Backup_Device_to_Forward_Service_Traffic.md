Enabling a Backup Device to Forward Service Traffic
===================================================

Enabling a Backup Device to Forward Service Traffic

#### Context

On a large enterprise aggregation network, users access aggregation devices with a VRRP group deployed over primary and secondary links. If the aggregation device that serves as the master in the VRRP group fails or the link between the master and terminal fails, service traffic immediately switches from the primary link to the secondary link. However, the master/backup VRRP switchover is not instant, causing service traffic to be lost during the period before the switchover is complete.

To resolve this issue and deliver carrier-grade reliability, enable the backup device to forward service traffic. Once this is enabled, the backup device forwards service traffic without waiting for the master/backup VRRP switchover to complete, which prevents service traffic loss.

**Figure 1** Network diagram of enabling a backup device to forward service traffic  
![](figure/en-us_image_0000001130624294.png)

#### Procedure

1. Enter the system view.
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the view of the sub-interface where a VRRP group resides.
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
3. Enable the backup device to forward service traffic.
   ```
   [vrrp vrid](cmdqueryname=vrrp+vrid) virtual-router-id backup-forward
   ```
   
   By default, a backup device is disabled from forwarding service traffic.
4. Commit the configuration.
   ```
   [commit](cmdqueryname=commit)
   ```