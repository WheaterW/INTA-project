Configuring LACP Alarm Control
==============================

Configuring LACP Alarm Control

#### Context

A device reports an LACP alarm if its Eth-Trunk service in LACP mode fails. To prevent a device from frequently reporting LACP alarms, enable LACP alarm control on the device. After this function is enabled, the device reports hwLacpNegotiateFailed, hwLacpPartialLinkLoss, hwLacpTotalLinkLoss, or Eth-Trunk linkdown alarms only when LACP negotiation fails due to one of the following reasons:

* The device's physical link goes down.
* LACP negotiation times out.
* LACP determines that packets are looped back.
* LACP determines that the system ID and port key in the LACPDU received by the local port from the peer end are inconsistent with those by the reference port from the peer end.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enable LACP alarm control.
   
   
   ```
   [lacp alarm-control link-failure](cmdqueryname=lacp+alarm-control+link-failure)
   ```
   
   
   
   After the [**lacp alarm-control link-failure**](cmdqueryname=lacp+alarm-control+link-failure) command is run on a device that has reported an hwLacpNegotiateFailed, hwLacpPartialLinkLoss, hwLacpTotalLinkLoss, or Eth-Trunk linkdown alarm, the device will report a clear alarm if the trigger conditions for the reported alarm are beyond the four reasons for failed LACP negotiation. Although a clear alarm is reported, the problem triggering the alarm persists.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   After the [**lacp alarm-control link-failure**](cmdqueryname=lacp+alarm-control+link-failure) command is run, the hwLacpNegotiateFailed, hwLacpPartialLinkLoss, hwLacpTotalLinkLoss, and Eth-Trunk linkdown alarms are not reported unless caused by one of the preceding four reasons. Therefore, exercise caution when running this command.
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```