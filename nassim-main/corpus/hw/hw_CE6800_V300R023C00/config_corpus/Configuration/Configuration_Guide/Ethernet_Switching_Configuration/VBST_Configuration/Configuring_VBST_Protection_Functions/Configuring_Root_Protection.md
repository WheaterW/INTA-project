Configuring Root Protection
===========================

Configuring Root Protection

#### Context

If a valid root bridge receives a superior BPDU due to incorrect configuration or malicious attacks, then the root bridge will become a non-root bridge and the network topology will change unexpectedly. As a result, traffic may be switched from high-rate links to low-rate links, leading to network congestion. To prevent this, you can configure root protection on a designated port to maintain the device's root bridge role.

In most cases, root protection is configured on a root bridge's port and takes effect only on a designated port.

Root protection and loop prevention cannot be configured on the same port.


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
4. Configure root protection.
   
   
   ```
   [stp root-protection](cmdqueryname=stp+root-protection)
   ```
   
   By default, root protection is disabled on a port.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display stp vlan**](cmdqueryname=display+stp+vlan) [ *vlan-id* ] **information** [ **brief** ] command and check the Protection Type field to verify the root protection configuration.