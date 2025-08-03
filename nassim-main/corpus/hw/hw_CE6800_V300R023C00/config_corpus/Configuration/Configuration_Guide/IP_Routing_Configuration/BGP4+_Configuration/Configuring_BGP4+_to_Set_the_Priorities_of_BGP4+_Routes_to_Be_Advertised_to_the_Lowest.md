Configuring BGP4+ to Set the Priorities of BGP4+ Routes to Be Advertised to the Lowest
======================================================================================

Configuring BGP4+ to Set the Priorities of BGP4+ Routes to Be Advertised to the Lowest

#### Context

[Figure 1](#EN-US_TASK_0000001130622434__fig_dc_vrp_bgp_cfg_410401) shows an inter-device Eth-Trunk scenario, in which DeviceA needs to be upgraded. To prevent traffic on the path DeviceD->DeviceA->DeviceC from being lost during the device upgrade, switch service traffic from DeviceA to DeviceB before the device upgrade. To achieve this, configure BGP4+ on DeviceA to forcibly set the priorities of BGP routes to be advertised to the lowest (changing the MED to the maximum value and the Local\_Pref to the minimum value). This configuration ensures that other devices on the network are instructed not to use DeviceA to forward data, allowing service traffic to be switched to DeviceB.

**Figure 1** Implementing service switching by enabling BGP4+ to set the priorities of BGP4+ routes to be advertised to the lowest  
![](figure/en-us_image_0000001130782242.png)

#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the maintenance view.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   The maintenance view is controlled by a license (CE-LIC-LU). You need to load the license before entering the maintenance view.
   
   ```
   [maintenance](cmdqueryname=maintenance)
   ```
3. Enable BGP4+ to set the priorities of BGP4+ routes to be advertised to the lowest.
   
   
   ```
   [advertise bgp ipv6-family unicast lowest-priority enable](cmdqueryname=advertise+bgp+ipv6-family+unicast+lowest-priority+enable)
   ```
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

After completing the configuration, perform the following operations to verify it:

* Run the [**display bgp ipv6 routing-table**](cmdqueryname=display+bgp+ipv6+routing-table) command on DeviceB to check the MED and LocPrf values.