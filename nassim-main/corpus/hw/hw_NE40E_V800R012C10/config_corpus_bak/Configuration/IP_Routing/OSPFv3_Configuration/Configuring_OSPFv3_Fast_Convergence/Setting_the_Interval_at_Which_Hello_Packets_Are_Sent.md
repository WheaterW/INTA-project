Setting the Interval at Which Hello Packets Are Sent
====================================================

You can adjust the value of the Hello timer to change the speed of OSPFv3 neighbor relationship establishment and the network convergence speed.

#### Context

Hello packets are periodically sent to the neighbor Router to detect and maintain the neighbor relationship and to elect the DR and the BDR. Based on standard protocols, the Hello timer values of neighbors must be the same. The value of the Hello timer is inversely proportional to the route convergence speed and network load.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
3. Run [**ospfv3 timer hello**](cmdqueryname=ospfv3+timer+hello) *interval* [ **conservative** ] [ **instance** *instance-id* ]
   
   
   
   The interval at which the interface sends Hello packets is set.
   
   
   
   The **conservative** parameter indicates that the conservative mode is enabled for the neighbor dead timer. If the conservative mode is enabled, the value configured for the dead timer using the [**ospfv3 timer dead**](cmdqueryname=ospfv3+timer+dead) command takes effect even when the value is less than 10s.
   
   To speed up OSPFv3 convergence in the case of a link failure, configuring BFD for OSPFv3 is recommended. If the remote end does not support BFD for OSPFv3 or the user does not want to have BFD for OSPFv3 enabled, you are advised to specify **conservative** when running the [**ospfv3 timer hello**](cmdqueryname=ospfv3+timer+hello) command. In conservative mode, the value set for the dead timer using the [**ospfv3 timer dead**](cmdqueryname=ospfv3+timer+dead) command takes effect even if the value is less than 10 seconds; otherwise, route convergence is performed based on the OSPFv3 neighbor dead timer, which takes a long time and has a great impact on services.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.