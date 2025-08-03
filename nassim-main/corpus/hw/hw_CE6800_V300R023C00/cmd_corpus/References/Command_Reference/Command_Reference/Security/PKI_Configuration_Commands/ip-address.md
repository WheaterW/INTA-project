ip-address
==========

ip-address

Function
--------



The **ip-address** command configures an IP address for an entity.

The **undo ip-address** command deletes the configuration.



By default, a PKI entity does not have an IP address.


Format
------

**ip-address** { *ipv4-address* | *ipv6-address* | *interface-type* *interface-number* [ **ipv6** ] }

**ip-address** *interface-name* [ **ipv6** ]

**undo ip-address**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv4-address* | Specifies the IPv4 address of a PKI entity. | The value is in dotted decimal notation. |
| *ipv6-address* | Specifies the IPv6 address of a PKI entity. | The value is in colon hexadecimal notation. |
| *interface-type* | interface-type specifies the interface type. | - |
| *interface-number* | interface-number specifies the interface number. | - |
| **ipv6** | Specifies an interface IP address of a PKI entity as an IPv6 address.  By default, an interface IP address of a PKI entity is an IPv4 address. | - |
| *interface-name* | Specifies the name of an interface. | - |



Views
-----

PKI entity view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

The parameters of a PKI entity include the identity information of the PKI entity. The CA identifies a certificate applicant based on identity information provided by a PKI entity. To facilitate applicant identification, configure an IP address for the PKI entity, which is used as an alias of the PKI entity. After an IP address is configured for a PKI entity, the certificate request packet sent by the device to the CA server carries this IP address. After receiving the certificate request packet, the CA server verifies the packet. For each valid packet, the CA server generates a digital certificate carrying the device IP


Example
-------

# Set the IP address for a PKI entity to 10.1.1.1.
```
<HUAWEI> system-view
[~HUAWEI] pki entity entity1
[*HUAWEI-pki-entity-entity1] ip-address 10.1.1.1

```