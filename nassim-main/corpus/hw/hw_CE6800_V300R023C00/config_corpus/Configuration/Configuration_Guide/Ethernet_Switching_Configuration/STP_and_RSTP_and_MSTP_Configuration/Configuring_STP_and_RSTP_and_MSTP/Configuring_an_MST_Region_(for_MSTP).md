Configuring an MST Region (for MSTP)
====================================

Configuring an MST Region (for MSTP)

#### Context

If the MSTP mode is used, you need to configure an MST region.

An MST region contains a collection of interconnected devices that have the same MST configuration. These devices with MSTP enabled are directly connected and have the same region name, same VLAN-to-MSTI mapping, and the same MST region revision level. One network can have multiple MST regions.

Two devices belong to the same MST region when they have the same:

* MST region name
* VLAN-to-MSTI mapping
* MST region revision level

An MST BPDU has a field that indicates the number of remaining hops.

* The number of remaining hops in a BPDU sent by the root bridge equals the maximum number of hops in the MST region.
* The number of remaining hops in a BPDU sent by a non-root bridge equals the maximum number of hops minus the number of hops from the non-root bridge to the root bridge.

The device will discard the BPDU in which the number of remaining hops is 0. Therefore, the maximum number of hops of a spanning tree in an MST region determines the network scale.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the MST region view.
   
   
   ```
   [stp region-configuration](cmdqueryname=stp+region-configuration)
   ```
3. Specify the MST region name.
   
   
   ```
   [region-name](cmdqueryname=region-name) name
   ```
4. (Optional) Set the MSTP revision level for the MST region.
   
   
   ```
   [revision-level](cmdqueryname=revision-level) level
   ```
   
   
   
   The default MSTP revision level for an MST region is 0.
   
   Perform this step if the MSTP revision level for the MST region where the device belongs is not 0.
5. Configure VLAN-to-MSTI mappings. Three methods are available.
   
   
   
   Complete this step in the MST region view if you use the following method 1 or 2, or in the VLAN instance view if you use method 3. The configuration in the VLAN instance view and that in the MST region view are mutually exclusive. If you have mapped a VLAN to an MSTI in the MST region view, you must first delete the mapping to reconfigure it in the VLAN instance view.
   
   Method 1: In the MST region view, map VLANs to MSTIs.
   ```
   [instance](cmdqueryname=instance) instance-id vlan { vlan-id1 [ to vlan-id2 ] }&<1-10>
   ```
   
   Method 2: In the MST region view, enable VLAN-to-MSTI mapping assignment based on a default algorithm.
   ```
   [vlan-mapping modulo](cmdqueryname=vlan-mapping+modulo) modulo
   ```
   
   Method 3: In the VLAN instance view, map VLANs to MSTIs. Before committing the configuration, run the [**check vlan instance mapping**](cmdqueryname=check+vlan+instance+mapping) command in the VLAN instance view to check whether the mappings between the MSTIs and VLANs are correct.
   ```
   [quit](cmdqueryname=quit)
   [vlan instance](cmdqueryname=vlan+instance)
   [instance](cmdqueryname=instance) instance-id vlan { vlan-id [ to vlan-id ] }&<1-10>
   ```
   
   
   
   By default, all VLANs in an MST region are mapped to MSTI 0.
   
   A VLAN can be mapped to only one instance. If you map an already mapped VLAN to another instance, the earlier mapping will be disabled.
   
   After the preceding configuration is complete, you are advised to run the **check region-configuration** command in the MST region view to verify that the MST region configuration is correct.
6. Return to the system view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
7. (Optional) Enter the MSTP process view.
   
   
   ```
   [stp process](cmdqueryname=stp+process) process-id
   ```
   
   Perform this step to set system parameters only when the MSTP process ID is not 0.
8. Set the maximum number of hops for the MST region.
   
   
   ```
   [stp max-hops](cmdqueryname=stp+max-hops) hop
   ```
   
   The default maximum number of hops in an MST region is 20.
9. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

* Run the [**display stp region-configuration**](cmdqueryname=display+stp+region-configuration) [ **digest** ] command and check the MST region configuration.
* Run the [**display vlan instance mapping**](cmdqueryname=display+vlan+instance+mapping) command and check the VLAN-to-MSTI mappings.