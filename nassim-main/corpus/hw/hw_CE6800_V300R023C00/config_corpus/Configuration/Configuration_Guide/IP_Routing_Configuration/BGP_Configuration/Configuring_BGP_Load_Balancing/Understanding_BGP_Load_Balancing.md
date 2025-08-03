Understanding BGP Load Balancing
================================

There may be multiple valid routes to the same destination on a large network. BGP advertises only the optimal routes to its peers, which may result in traffic imbalance.

Either of the following methods can be used to resolve the problem:

* Use BGP route-policies for load balancing. For example, use a route-policy to modify the Local\_Pref, AS\_Path, Origin, or MED attribute of BGP routes to control traffic forwarding paths, helping implement load balancing.
* Using multiple paths to implement traffic load balancing. This method requires that multiple equal-cost routes exist. The number of routes that are allowed to participate in load balancing can be set. Load balancing can be implemented globally or for a specified peer or peer group.

#### Conditions for Load Balancing Among BGP Routes

After BGP load balancing is configured, the BGP routes that meet all of the following conditions are equal-cost routes that carry out load balancing:

* Route origins are the same.
* PrefVal values are the same.
* Local\_Pref values are the same.
* All the routes are summary routes, or none of them are summary routes.
* AIGP values are the same.
* AS\_Path attributes are the same.
* Origin types (IGP, EGP, or incomplete) are the same.
* MED values are the same. If the [**load-balancing med-ignore**](cmdqueryname=load-balancing+med-ignore) command is run, BGP does not compare the MED attributes of routes when deciding the routes used for load balancing.
* All the routes are EBGP or IBGP routes. After the [**maximum load-balancing eibgp**](cmdqueryname=maximum+load-balancing+eibgp) command is run, BGP does not use this rule in optimal VPN route selection.
* The metric values of the IGP routes to which BGP routes recurse within an AS are the same. After the [**maximum load-balancing eibgp**](cmdqueryname=maximum+load-balancing+eibgp) command is run, BGP does not use this rule in optimal VPN route selection.

Even if the preceding conditions are met, load balancing cannot be implemented among labeled BGP routes and non-labeled BGP routes.


#### UCMP Based on the BGP Link Bandwidth Extended Community Attribute of Routes

In a scenario where load balancing is performed among outbound routes on some devices, equal-cost multi-path (ECMP) results may fail to meet expectations due to uneven outbound link bandwidth. To solve this problem, you can configure the BGP Link Bandwidth extended community attribute function on corresponding devices. With the function, the devices add the BGP Link Bandwidth extended community attribute that reflects link bandwidth to BGP routes so that unequal cost multipath (UCMP) is implemented based on the outbound link bandwidth proportion.

In [Figure 1](#EN-US_CONCEPT_0000001176663637__fig92385441276), Device A and Device B reside in AS 100, whereas devices C through F reside in AS 200. After Device C receives a route from its directly connected EBGP peer (Device A), Device C adds the Link Bandwidth extended community attribute (indicating the bandwidth of external links) to the route and advertises the route to its IBGP peers.

![](public_sys-resources/note_3.0-en-us.png) 

The next hops of the routes that form UCMP must be of the same type.


**Figure 1** UCMP based on the BGP Link Bandwidth extended community attribute  
![](figure/en-us_image_0000001194905447.png)

The process to implement UCMP is as follows:

1. Device A and Device B advertise the BGP route 10.10.10.10/32 without the BGP Link Bandwidth extended community attribute to Device C.

2. Device C selects both the links to A and B to implement load balancing, with each link's outbound bandwidth being 200 Gbit/s.

3. Device C sends the route with the BGP Link Bandwidth extended community attribute (400 Gbit/s) to Device F.

4. Device D and Device E perform similar operations to those performed by Device C.

5. Device F receives three routes destined for 10.10.10.10/32 from Device C, Device D, and Device E, with the bandwidth values being 400 Gbit/s, 200 Gbit/s, and 200 Gbit/s, respectively.

6. Device F implements UCMP among the three links based on the outbound link bandwidth proportion of 2:1:1.