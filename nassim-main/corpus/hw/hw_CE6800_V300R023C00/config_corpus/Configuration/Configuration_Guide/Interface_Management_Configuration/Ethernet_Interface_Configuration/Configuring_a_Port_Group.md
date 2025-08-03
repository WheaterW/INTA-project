Configuring a Port Group
========================

Configuring a Port Group

#### Context

To configure commands on multiple interfaces in batches, you can add them to a port group. This reduces errors caused by separate configurations on each interface and saves manpower. Port groups are classified as permanent or temporary ones. A permanent port group cannot be automatically deleted, but can have a configuration file generated. A temporary port group can be automatically deleted, but cannot have a configuration file generated. Their functions are similar, as described in [Table 1](#EN-US_TASK_0000001564001189__table16571183983715).

**Table 1** Differences between permanent and temporary port groups
| Port Group | Whether to Automatically Delete the Port Group | Whether the [**display port-group**](cmdqueryname=display+port-group) Command Can Be Used for Query | Whether to Generate a Configuration File |
| --- | --- | --- | --- |
| Permanent port group | No (deleted using the [**undo port-group**](cmdqueryname=undo+port-group) command) | Yes | Yes |
| Temporary port group | Yes | No | No |

The command executed in the port group view takes effect only when the member interfaces support the command configuration. Therefore, batch configurations may not take effect for all member interfaces. For example, a port group consists of optical and electrical interfaces. If you run the [**port transceiver-power-low trigger error-down**](cmdqueryname=port+transceiver-power-low+trigger+error-down) command in the port group view, the configuration takes effect only on the optical interfaces.


#### Procedure

* Configure a permanent port group.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Create a permanent port group and enter its view.
     
     
     ```
     [port-group](cmdqueryname=port-group) port-group-name
     ```
  3. Add interfaces to the permanent port group.
     
     
     ```
     [group-member](cmdqueryname=group-member) { interface-type-start interface-number-start [ to interface-type-end interface-number-end ] } &<1-10>
     ```
  4. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Configure a temporary port group. 
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Create a temporary port group and add interfaces to this group.
     
     
     ```
     [port-group group-member](cmdqueryname=port-group+group-member) { interface-type-start interface-number-start [ to interface-type-end interface-number-end ] } &<1-10>
     ```
     
     or
     
     ```
     [interface range](cmdqueryname=interface+range) { interface-type-start interface-number-start [ to interface-type-end interface-number-end ] } &<1-10>
     ```
  3. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```

#### Verifying the Configuration

Run the [**display port-group**](cmdqueryname=display+port-group) [ **all** | *port-group-name* ] command to check information about all port groups or a specified one.

The port group function enables batch configuration, but the port group configuration cannot be checked or saved. To check configurations of member interfaces in a port group, run the [**display this**](cmdqueryname=display+this) command in the member interface view.


#### Follow-up Procedure

In the port group view, you can deliver the following configurations to member interfaces in batches as required:

* [Configuring Layer 2/Layer 3 Mode Switching on an Ethernet Interface](galaxy_ethernet-int_0012.html)
* [Configuring an Ethernet Interface to Work in Auto-negotiation Mode](galaxy_ethernet-int_0022.html)
* [Configuring General Attributes for Ethernet Optical or Electrical Interfaces](galaxy_ethernet-int_0023.html)
* [Pre-configuring a Transmission Medium Type for an Optical Interface](galaxy_ethernet-int_0015.html)
* [Configuring FEC](galaxy_ethernet-int_0016.html)
* [Configuring Unidirectional Single-Fiber Communication](galaxy_ethernet-int_0024.html)
* [Configuring an Interface to Enter the Error-Down State When the Receive Optical Power Is Low](galaxy_ethernet-int_0018.html)
* [Configuring Loopback Detection on an Interface](galaxy_ethernet-int_0020.html)
* Enabling or disabling interfaces in batches by referring to section "Enabling or Disabling an Interface" in Configuration Guide > Basic Interface Configuration.

You can configure both interface attribute commands and service commands in the port group view. For details about the service commands, see the related documentation.