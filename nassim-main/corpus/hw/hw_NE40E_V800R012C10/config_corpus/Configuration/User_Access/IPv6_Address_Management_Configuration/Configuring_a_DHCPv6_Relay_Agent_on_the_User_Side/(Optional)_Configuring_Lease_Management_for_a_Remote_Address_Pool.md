(Optional) Configuring Lease Management for a Remote Address Pool
=================================================================

The Router supports lease management on addresses in a remote address pool.

#### Context

When the Router functions as a DHCP relay agent, if the ARP probe function is disabled on the user access interface due to reasons (for example, some clients do not respond to the ARP probe packets sent by the Router), the Router cannot detect user logout when clients are powered off or go offline abnormally. As a result, the Router does not send Release packets to the DHCP server, causing IP addresses in a remote address pool to fail to be released. To prevent this problem, enable lease management for the remote address pool.


#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. Run the [**ip pool**](cmdqueryname=ip+pool) *pool-name* **bas** **remote** [ **rui-slave** ] command to enter the remote address pool view.
3. Run the [**remote-ip lease manage**](cmdqueryname=remote-ip+lease+manage) command to enable lease management for the remote address pool.
4. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.