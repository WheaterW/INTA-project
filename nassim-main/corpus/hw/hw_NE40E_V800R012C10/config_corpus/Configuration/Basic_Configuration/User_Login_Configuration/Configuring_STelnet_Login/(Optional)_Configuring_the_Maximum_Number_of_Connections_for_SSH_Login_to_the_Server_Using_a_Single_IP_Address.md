(Optional) Configuring the Maximum Number of Connections for SSH Login to the Server Using a Single IP Address
==============================================================================================================

You can configure the maximum number of SSH connections established using a single IP address. This prevents the situation where other IP addresses fail in login because an IP address has been used to establish too many connections to a server.

#### Context

When a device functions as an SSH server, you can configure the maximum number of connections established using a single IP address to prevent malicious attacks, thereby enhancing security.

Perform the following steps on a device that functions as an SSH server.


#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. Run the [**ssh server ip-limit-session**](cmdqueryname=ssh+server+ip-limit-session) *limit-session-num* command to configure the maximum number of connections allowed for SSH login to the server through a single IP address.
3. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.