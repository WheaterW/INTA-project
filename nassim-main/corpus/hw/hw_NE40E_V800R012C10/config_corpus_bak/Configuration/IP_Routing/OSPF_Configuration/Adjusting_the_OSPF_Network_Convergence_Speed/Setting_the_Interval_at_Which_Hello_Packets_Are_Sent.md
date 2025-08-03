Setting the Interval at Which Hello Packets Are Sent
====================================================

You can adjust the value of the Hello timer to change the speed of the OSPF neighbor relationship establishment and change the network convergence speed.

#### Context

Hello packets are periodically sent between OSPF interfaces to establish and maintain neighbor relationships. The intervals set on the interfaces at both ends must be the same. Otherwise, the OSPF neighbor relationship cannot be established.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The OSPF interface view is displayed.
3. Run [**ospf timer hello**](cmdqueryname=ospf+timer+hello) *interval* [ **conservative** ]
   
   
   
   The interval at which Hello packets are sent is set on the interface.
   
   
   
   The **conservative** parameter indicates that the conservative mode is enabled for the neighbor dead timer. If the conservative mode is enabled, the value configured for the dead timer using the [**ospf timer dead**](cmdqueryname=ospf+timer+dead) command takes effect even when the value is less than 10s.
   
   To speed up OSPF convergence in the case of a link failure, configuring BFD for OSPF is recommended. If the remote end does not support BFD for OSPF or the user does not want to have BFD for OSPF enabled, you are advised to specify **conservative** when running the [**ospf timer dead**](cmdqueryname=ospf+timer+dead) command. In conservative mode, the value set for the dead timer using the [**ospf timer dead**](cmdqueryname=ospf+timer+dead) command takes effect even if the value is less than 10 seconds; otherwise, route convergence is performed based on the OSPF neighbor dead timer, which takes a long time and has a great impact on services.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.