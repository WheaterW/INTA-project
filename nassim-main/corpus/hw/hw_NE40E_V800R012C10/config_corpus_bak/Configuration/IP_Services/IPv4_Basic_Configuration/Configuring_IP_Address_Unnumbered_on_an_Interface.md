Configuring IP Address Unnumbered on an Interface
=================================================

IP address unnumbered allows an interface that is not assigned an IP address to borrow an IP address from another interface.

#### Usage Scenario

To save IP address resources, you can configure an interface to borrow an IP address from another interface. For example, if an interface is only occasionally used, it is unnecessary to configure an IP address for it. Instead, you can configure the interface to borrow an IP address of another interface.

When configuring IP address unnumbered on an interface, note the following points:

* The IP address of the numbered interface cannot be a borrowed IP address.
* The IP address of the numbered interface can be lent to multiple interfaces.
* If the numbered interface has multiple IP addresses, the unnumbered interface borrows only the primary IP address.
* If the numbered interface is not configured with an IP address, the unnumbered interface borrows the IP address 0.0.0.0.
* The IP address of the virtual loopback interface can be borrowed by other interfaces, but the virtual loopback interface cannot borrow an IP address from another interface.

#### Pre-configuration Tasks

Before configuring IP address unnumbered on an interface, configure link layer protocol parameters for the interfaces to ensure that the link layer protocol status of the interfaces is Up.


[Configuring the Primary IP Address for a Numbered Interface](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ipv4_cfg_0012.html)

Only the primary IP address of an interface can be borrowed.

[Configuring an Unnumbered Interface to Borrow an IP Address from Another Interface](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ipv4_cfg_0013.html)

An Ethernet interface can borrow the IP address of another interface.

[Verifying the Configuration of IP Address Unnumbered](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ipv4_cfg_0014.html)

After configuring IP address unnumbered, verify the configuration.