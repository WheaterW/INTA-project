Configuring LFA Link Attribute Advertisement
============================================

Configuring LFA link attribute advertisement in an IS-IS process helps collect and flood the SRLG information applied by LFA in a domain.

#### Prerequisites

Before configuring LFA link attribute advertisement, complete the following tasks:

* Run the [**cost-style**](cmdqueryname=cost-style) command to set the IS-IS cost style to wide, wide-compatible, or compatible.

#### Context

Without the SRLG link attribute used by LFA on the remote device, the local device can only preferentially select a local link that is not in the same SRLG as the primary path when using IS-IS TI-LFA to calculate a backup path. If a remote link on the backup path is in the same SRLG as the primary path and the primary path fails, the backup path may also fail. After traffic is switched to the backup path, network traffic may be interrupted. To solve the preceding problem, you can configure the advertisement of SRLG link attribute information applied by LFA through IS-IS LSPs. When the local device uses TI-LFA to calculate a backup path, it can preferentially select a remote link that is not in the same SRLG as the local link as the backup path based on the LFA link attribute information advertised by the remote device, reducing the possibility of network traffic interruption.


#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. Run the [**isis**](cmdqueryname=isis) [ *process-id* ] command to create an IS-IS process and enter its view.
3. Run the [**cost-style**](cmdqueryname=cost-style) { **wide** | **wide-compatible** | **compatible** } command to set an IS-IS cost style.
4. Run the [**advertise link-attributes application lfa**](cmdqueryname=advertise+link-attributes+application+lfa) command to configure LFA link attribute advertisement.
5. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.

#### Verifying the Configuration

After the configuration is complete, verify it.

* Run the **[**display isis lsdb verbose**](cmdqueryname=display+isis+lsdb+verbose)** command to check LFA link attributes.