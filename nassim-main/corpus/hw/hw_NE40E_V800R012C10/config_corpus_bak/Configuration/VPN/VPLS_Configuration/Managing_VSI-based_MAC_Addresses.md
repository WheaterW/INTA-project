Managing VSI-based MAC Addresses
================================

VPLS forwards data according to MAC entries. In most cases, MAC address learning is automatically performed among devices. To protect services against attacks and faults, VPLS provides an additional set of MAC control mechanisms.

#### Usage Scenario

The NE40E supports VSI-based MAC address management, which includes:

* Enabling MAC address learning
* Configuring static MAC entries
* Protecting MAC address security
* Clearing MAC addresses learned from a PW
* Resending MAC Withdraw messages after a delay

#### Pre-configuration Tasks

Before configuring VSI-based MAC address management, complete the following task:

* Configure LDP VPLS.


[Enabling MAC Address Learning](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vpls_cfg_5019.html)

Packets can be forwarded according to MAC addresses only after MAC address learning is enabled.

[Configuring Static MAC Address Entries](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vpls_cfg_5020.html)

This section describes how to configure static MAC address entries, including static blackhole MAC address entries. After a static MAC address entry is configured, the packets with a specified destination MAC address are forwarded through the specified interface. This protects the device against attacks with forged MAC addresses. After a blackhole MAC address entry is configured, the packets with a specified destination MAC address are discarded. This process prevents hackers from launching network attacks based on MAC addresses.

[Configuring MAC Address Safety](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vpls_cfg_5021.html)

You can limit the number of MAC addresses to be learned and the rate of MAC address learning and specify the action to be taken when MAC address learning in the VSI exceeds the limit.

[Configuring the Function of Clearing the MAC Addresses of Specific PWs](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vpls_cfg_5063.html)

After you configure the function, a VSI deletes the MAC address of the PW carried in a received MAC Withdraw message carrying 0x404 TLV but retains the MAC addresses of the other PWs and AC interfaces. 

[Configuring Delayed Resending of MAC-Withdraw Messages](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vpls_cfg_5064.html)

This section describes how to configure delayed resending of MAC-Withdraw messages. This configuration allows a device to resend a MAC-Withdraw message to the peer PE after a specified delay if the VRRP status changes to backup.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vpls_cfg_5022.html)

After configuring VSI-based MAC address management, check the set limits of MAC address learning and the aging time of MAC address entries.