(Optional) Configuring a Static MAC Address Entry
=================================================

Using static MAC address entries to forward user packets helps reduce BUM traffic on the network and prevent bogus attacks.

#### Context

When the source NVE on a VXLAN tunnel receives BUM packets, the NVE sends these packets along paths specified in static MAC address entries if there are such entries. This helps reduce BUM traffic on the network and prevent unauthorized data access from bogus users.


#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. Run the [**mac-address static**](cmdqueryname=mac-address+static) *mac-address* **bridge-domain** *bd-id* **source** *source-ip-address* **peer** *peer-ip* **vni** *vni-id* command to configure a static MAC address entry.
3. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.