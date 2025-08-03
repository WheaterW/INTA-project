DHCPv4 Data Planning Guidance
=============================

DHCPv4 Data Planning Guidance

#### Server Planning

A DHCPv4 client broadcasts DHCPv4 request messages. If multiple DHCPv4 servers (or DHCPv4 relay agents) are deployed on the same network segment as the client, the client accepts only the first received DHCPOFFER message and therefore may obtain an IPv4 address from an unexpected DHCPv4 server. Proper server planning can ensure that a client applies for network parameters from an expected DHCPv4 server.

When planning DHCPv4 servers, plan VLANs properly to ensure that only one DHCPv4 server (or DHCPv4 relay agent) can receive DHCPv4 request messages from clients in a VLAN.


#### IPv4 Address Planning

Plan the range of IPv4 addresses that can be automatically allocated by a DHCPv4 server and the IPv4 address allocation mechanism (dynamic or static allocation).

Plan IPv4 addresses that cannot be automatically allocated. For example, an enterprise requires that the device function as a DHCPv4 server, network segment 192.168.1.0/24 be used as the IPv4 addresses of employees' office computers, and 192.168.1.10 be used as the IPv4 address of the DNS server. During the configuration, 192.168.1.10 needs to be excluded from DHCPv4 automatic allocation.


#### Lease Planning

Plan an IPv4 address lease for a client based on the online duration of the client. The default IPv4 address lease is one day.

* In locations where clients often move and stay online for a short period of time, for example, in cafes, Internet bars, and airports, plan a short lease to ensure that IPv4 addresses are released promptly after the clients go offline.
* In locations where clients seldom move and stay online for a long period of time, for example, in office areas of an enterprise, plan a long lease to prevent system resources from being occupied by frequent lease or address renewals.


#### Planning of Other Network Parameters

In addition to allocating IPv4 addresses to clients, a DHCPv4 server allocates other network parameters to them. You can configure a DHCPv4 server to allocate other network parameters as required. For example, to enable a client to communicate with other network devices through a domain name and to obtain DNS parameters using DHCPv4, plan the IPv4 address of the DNS server and the domain name of the client.