Controlling RIPng Routing Information
=====================================

In most cases, multiple protocols run on the same network.
Therefore, you need to control routing information of every protocol
to meet different networking requirements.

#### Applicable Environment

To meet
the requirements of complex networking, accurately control the sending
and receiving of RIPng routing information.


#### Pre-configuration Tasks

Before configuring
a Router to control RIPng routing information, complete the following tasks:

* Configure IPv6 addresses for interfaces to ensure that neighboring
  nodes are reachable at the network layer.
* [Configuring Basic RIPng Functions](dc_vrp_ripng_cfg_0003.html)

#### Configuration Procedure

Perform one or more
of the following configurations as required.


[Configuring RIPng to Import External Routes](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ripng_cfg_0019.html)

RIPng can import routing information from other RIPng processes or routing protocols to enrich the RIPng routing table.

[Configuring RIPng to Filter the Received Routes](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ripng_cfg_0039.html)

You can configure a router to selectively receive routes.

[Configuring RIPng to Filter the Routes to be Sent](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ripng_cfg_0040.html)

You can configure RIPng to filter the routes to be sent.

[Configuring RIPng to Advertise the Default Routes](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ripng_cfg_0020.html)

There are two methods of advertising RIPng default routes. You can configure a router to advertise RIPng default routes as required. Alternatively, you can specify the cost of the default routes to be advertised.

[Configuring RIPng Route Summarization](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ripng_cfg_0029.html)

Configuring RIPng route summarization reduces the routing table size and prevents route flapping.

[Verifying the Configuration of RIPng Routing Information Control](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ripng_cfg_0021.html)

After controlling RIPng routing information, verify all activated routes in the RIPng database.