Understanding IP Unnumbered on an Interface
===========================================

Understanding IP Unnumbered on an Interface

#### Application Scenarios

To save IP address resources, you can configure IP unnumbered on an interface that is not assigned an IP address to borrow an IP address from another interface. For example, if an interface is rarely used, configure IP unnumbered on this interface to enable the interface to share an IP address with another interface.

When configuring IP unnumbered on an interface, note the following:

* A numbered interface cannot be configured with a borrowed IP address.
* Multiple interfaces can borrow the IP address of a numbered interface.
* Interfaces can borrow only the primary IP address of a numbered interface that has multiple IP addresses.
* If a numbered interface is not configured with any IP address, the IP address 0.0.0.0 is borrowed.
* Interfaces can borrow the IP address of a loopback interface, but the loopback interface cannot borrow an IP address from another interface.