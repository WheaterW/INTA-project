Overview of MAP
===============

Mapping address and port (MAP) technology is used to carry IPv4 and IPv6 services on IPv6-only networks. MAP-T (stateless dual translation) and the MAP-E (stateless dual encapsulation) techniques have advantages in performance, reliability, and customer deployment costs.

#### Background

IPv4-to-IPv6 evolution faces the following challenges:

* IPv4 address shortage holds back the rapid IPv4 service development.
* An immense number of IPv6 addresses are available, whereas a few IPv6 applications are implemented.

IPv4 address reusing (address and port) seems to relieve the pressure posed by rapid IPv4 address consumption. However, a great number of devices are deployed, which more or less affects various services and applications. In IPv6 development, users, ICPs, ISPs, and carriers show different sensitivity levels to IPv4 address exhaustion, which results in an imbalance in the IPv6 industry chain. Each party has its own considerations when promoting IPv6 development. In addition, the IPv4 address sharing mechanism seems to slow down the development of the IPv6 industry chain. The ongoing development of the IPv6 industry chain, however, seems to challenge the deployment scale of the IPv4 address sharing mechanism.

To ensure IPv4 service continuity and IPv6 industry development, the 4over6 scenario that is compatible with both IPv4 service and IPv6 development becomes the focus in long term evolution.

In the 4over6 scenario, various types of transition techniques are also generated. MAP technology combines the stateless and dual translation and encapsulation techniques and becomes the most concerned solution of the IETF.


#### Technical Characteristics

MAP is a stateless, distributed, and tunneling transition technique. MAP allows stateless reuse of addresses and ports. MAP is classified as MAP-T or MAP-E based on packet formats.