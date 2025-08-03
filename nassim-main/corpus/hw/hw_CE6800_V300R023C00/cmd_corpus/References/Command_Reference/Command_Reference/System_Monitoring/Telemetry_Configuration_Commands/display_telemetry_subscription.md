display telemetry subscription
==============================

display telemetry subscription

Function
--------



The **display telemetry subscription** command displays subscription information.




Format
------

**display telemetry subscription** [ *subscription-name* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *subscription-name* | Specifies a subscription name. | The value is a string of 1 to 64 case-sensitive characters containing letters and digits. Spaces are not supported between letters or digits. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

To view subscription information, including the subscription name, subscription status, sampling sensor group associated, and destination group associated, run the display telemetry subscription command.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display all subscription information.
```
<HUAWEI> display telemetry subscription
---------------------------------------------------------------------------
Sub-name           : a
Sensor group:
----------------------------------------------------
Sensor-name     Sample-interval(ms)  State          
----------------------------------------------------
senso1          60000                RESOLVED       
----------------------------------------------------
Destination group:
----------------------------------------------------------------------
Dest-name   Dest-IP          Dest-port   State        Vpn-name     Protocol   Compression
----------------------------------------------------------------------
dest1       10.135.84.185    50000       RESOLVED     -            GRPC       GZIP
----------------------------------------------------------------------
Sub-state          : PASSIVE 
---------------------------------------------------------------------------

Total subscription number is :  1

```

# Display information about subscription a.
```
<HUAWEI> display telemetry subscription a
---------------------------------------------------------------------------
Sub-name           : a
Source Address     : 10.1.1.1
Dscp               : 0
Protocol           : GRPC 
Encoding           : GPB 
Send bytes         : 0 
Send packets       : 0 
Total send delay   : 0 
Total send error   : 0 
Total send drop    : 302 
Total other error  : 0 
Last send-time     : 2017-08-31 15:42:35
Sensor group:
----------------------------------------------------------------------
Sensor-name Sample-interval(ms) Heartbeat-interval(s) Suppression State     
----------------------------------------------------------------------
senso1      60000               -                     NO          RESOLVED  
----------------------------------------------------------------------
Destination group:
----------------------------------------------------------------------
Dest-name   Dest-IP          Dest-port   State        Vpn-name     Protocol   Compression
----------------------------------------------------------------------
dest1       10.135.84.185    50000       RESOLVED     -            GRPC       GZIP
----------------------------------------------------------------------
Sub-state          : PASSIVE 
---------------------------------------------------------------------------
                
Total subscription number is :  1

```

**Table 1** Description of the **display telemetry subscription** command output
| Item | Description |
| --- | --- |
| Sub-name | Subscription name. |
| Sensor group | Sampling sensor group information. |
| Sensor-name | Name of a sampling sensor group. |
| Sample-interval(ms) | Sampling interval, in milliseconds. |
| State | Status of the sampling sensor group or destination group:   * RESOLVED: subscribed. * NA: not subscribed. |
| Destination group | Destination group information. |
| Dest-name | Name of the destination group. |
| Dest-IP | IP address of the destination group. |
| Dest-port | Port number of the destination group. |
| Vpn-name | VPN instance name. |
| Protocol | Data sending protocol. |
| Compression | gGPC compression type. |
| Sub-state | Subscription status:   * PASSIVE: The collector is not connected. * ACTIVE: The device has been connected to the collector. |
| Total subscription number is | Total number of queried subscriptions. |
| Total send delay | Number of packets that are delayed to be sent.  A hyphen (-) indicates that this parameter is not supported. |
| Total send error | Number of sent error packets.  A hyphen (-) indicates that this parameter is not supported. |
| Total send drop | Number of discarded packets.  A hyphen (-) indicates that this parameter is not supported. |
| Total other error | Number of other error packets.  A hyphen (-) indicates that this parameter is not supported. |
| Source Address | Source IP address. |
| Dscp | DSCP value of the data packets to be sent to the collector. |
| Encoding | Data encoding format:   * GPB: The data coding format is GPB. * JSON: The data encoding format is JSON. |
| Send bytes | Number of sent bytes.  A hyphen (-) indicates that this parameter is not supported. |
| Send packets | Number of sent packets.  A hyphen (-) indicates that this parameter is not supported. |
| Last send-time | Time when packets are sent previously.  A hyphen (-) indicates that this parameter is not supported. |
| Heartbeat-interval(s) | Heartbeat interval, in seconds. |
| Suppression | Redundancy suppression. |