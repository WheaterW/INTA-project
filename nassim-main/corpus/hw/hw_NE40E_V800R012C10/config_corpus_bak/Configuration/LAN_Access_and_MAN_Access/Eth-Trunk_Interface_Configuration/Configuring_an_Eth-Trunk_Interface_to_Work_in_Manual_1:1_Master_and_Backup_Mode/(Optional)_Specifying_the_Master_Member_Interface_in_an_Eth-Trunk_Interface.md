(Optional) Specifying the Master Member Interface in an Eth-Trunk Interface
===========================================================================

By default, the member interface that is first added to the Eth-Trunk interface and the interface status is up in manual 1:1 master/backup mode will automatically become the master one. To ensure a reliable communication, specifying a master interface is recommended.

#### Context

In normal situations, the master member interface in an Eth-Trunk interface in manual 1:1 master/backup mode is active and can forward data. The backup member interface is inactive and cannot forward data. To change the backup interface to the master interface, perform either of the following operations:

* Run the [**undo port-master**](cmdqueryname=undo+port-master) command in the master interface view to delete the master interface configuration, and run the [**port-master**](cmdqueryname=port-master) command in the backup interface view to specify the interface as the master interface. Specifying a new master interface causes a short data interruption.
* Run the [**protect-switch**](cmdqueryname=protect-switch) command in the view of the Eth-Trunk interface in manual 1:1 master/backup mode to manually switch the active and inactive interfaces. Each time the [**protect-switch**](cmdqueryname=protect-switch) command is run, the active and inactive interfaces are switched once. This switching does not cause any data interruption.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The Eth-Trunk member interface view is displayed.
3. Run [**port-master**](cmdqueryname=port-master)
   
   
   
   The master member interface is specified.
   
   Only one master interface can be specified between the two member interfaces in the Eth-Trunk interface in manual 1:1 master/backup mode.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Follow-up Procedure

When the master member interface needs to be switched back to the forwarding state after it recovers, you can run the [**preempt enable**](cmdqueryname=preempt+enable) [ **delay** *delay-time* | **delay** *delay-time* *seconds* | **delay** *delay-time* *seconds* *milliseconds* ] command in the view of the Eth-Trunk interface in 1:1 master/backup mode to enable the delayed switchback function and configure a switchback delay.

* If you want the master member interface to enter the forwarding state immediately after it recovers, do not specify a switchback delay.
* If you want the recovered master member interface to enter the forwarding state after a delay, specify a switchback delay.