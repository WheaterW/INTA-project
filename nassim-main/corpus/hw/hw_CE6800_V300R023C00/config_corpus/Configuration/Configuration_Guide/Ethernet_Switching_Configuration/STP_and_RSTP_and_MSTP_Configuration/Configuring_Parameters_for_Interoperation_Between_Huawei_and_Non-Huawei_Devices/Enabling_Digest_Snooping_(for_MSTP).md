Enabling Digest Snooping (for MSTP)
===================================

Enabling Digest Snooping (for MSTP)

#### Context

On an MSTP-enabled network, interconnected Huawei and non-Huawei devices cannot communicate with each other if they have the same region name, revision level, and VLAN-to-instance mappings but different BPDU keys. Enable digest snooping on the Huawei device to address this problem.

This function allows the Huawei device to keep its BPDU key consistent with that used on the non-Huawei device.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
3. Switch the interface working mode to Layer 2.
   
   
   ```
   [portswitch](cmdqueryname=portswitch)
   ```
   
   Determine whether to perform this step based on the current interface working mode.
4. Enable digest snooping.
   
   
   ```
   [stp config-digest-snoop](cmdqueryname=stp+config-digest-snoop)
   ```
   
   By default, digest snooping is disabled.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display stp**](cmdqueryname=display+stp) [ **process** *process-id* ] [ **instance** *instance-id* ] **interface** *interface-type* *interface-number* command and check the Config-digest-snoop field to verify digest snooping configuration.