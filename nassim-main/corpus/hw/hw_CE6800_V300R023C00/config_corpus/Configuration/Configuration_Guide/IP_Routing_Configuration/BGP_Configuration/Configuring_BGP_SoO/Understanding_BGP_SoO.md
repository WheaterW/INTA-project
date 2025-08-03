Understanding BGP SoO
=====================

Understanding BGP SoO

#### Definition

BGP Site of Origin (SoO) is a BGP extended community attribute. BGP SoO is used to uniquely identify the site where a route originates and prevent the route from being forwarded back to this site.

In earlier versions where the BGP SoO function is not supported, the BGP SoO extended community attribute can be set using a route-policy, but the route-policy is complex to configure. With the BGP SoO function, you can directly configure a peer-based SoO value, which simplifies the BGP SoO configuration.


#### Fundamentals

When BGP SoO is applied to a BGP public network scenario:

* When advertising public network unicast routes to peers, the device adds the SoO attribute to theses routes.
* When receiving a public network unicast route with the SoO attribute, the device checks the SoO attribute. It accepts the route only if the SoO attribute of the route is different from the locally configured SoO attribute.

#### BGP SoO Application on a Public Network

On the network shown in [Figure 1](#EN-US_CONCEPT_0000001533380697__fig20544202814319), DeviceA, DeviceB, Server, and Leaf reside in different ASs. DeviceA and DeviceB are connected to Server and establish EBGP peer relationships with Leaf and Server to transmit public network unicast routes. For example, Server sends routes to DeviceB through two paths: Server -> DeviceA -> Leaf -> DeviceB and Server - > DeviceB. In this case, DeviceB receives two routes from the same site (Server). Because a large number of routes usually exist on the live network, for DeviceB, redundant routes affect device memory and route selection costs.

To solve this problem, configure BGP SoO on DeviceA and DeviceB. When DeviceA advertises a route to Leaf, it adds the SoO attribute to the route. After receiving the route forwarded by Leaf, DeviceB checks the SoO attribute carried in the route. If the SoO attribute is the same as that configured on DeviceB, DeviceB does not accept this route, reducing memory usage and route selection costs. On the network shown in [Figure 1](#EN-US_CONCEPT_0000001533380697__fig20544202814319), after the BGP SoO function is configured on DeviceA and DeviceB, DeviceA adds the SoO attribute 10:10 to the route 1.1.1.1/32 before advertising the route to Leaf. After receiving the route, DeviceB compares the SoO of the route with the SoO configured using the **peer soo-reverse** command on DeviceB. Finding that both SoOs are 10:10, DeviceB discards the route.

**Figure 1** BGP SoO application on a public network  
![](figure/en-us_image_0000001535945485.png)