Checking BRAS Access Statistics
===============================

This section describes how to check BRAS access statistics to facilitate fault diagnosis and traffic tracing.

#### Procedure

* Run the [**display access statistics packet discard mac-spoofing**](cmdqueryname=display+access+statistics+packet+discard+mac-spoofing) [ **ipoe** | **pppoe** ] [ **ipv4** | **ipv6** ] { **interface** { *interface-name* | *interface-type* *interface-number* } | **slot** *slot-id* } command in any view to display statistics about MAC-spoofing-dropped packets of access users.
* Run the [**display access statistics trigger slot**](cmdqueryname=display+access+statistics+trigger+slot) *slot-id* command in any view to display user packet statistics about a specified board.
* Run the [**display layer3-subscriber statistics port-mismatch**](cmdqueryname=display+layer3-subscriber+statistics+port-mismatch) command in any view to display statistics about Layer 3 users' packets that are discarded due to an interface mismatch.

#### Example

Run the [**display access statistics packet discard mac-spoofing**](cmdqueryname=display+access+statistics+packet+discard+mac-spoofing) **slot** *slot-id* command, you can view statistics about MAC-spoofing-dropped packets on the board in slot 1.

```
<HUAWEI> display access statistics packet discard mac-spoofing slot 1
```
```
 Slot 1 discard statistics:
--------------------------------------------------------------------------
             IPv4 packets(high, low)    IPv6 packets(high, low)
--------------------------------------------------------------------------
 pppoe       (4294967295, 4294967295)    (4294967295, 4294967295)
 ipoe        (4294967295, 4294967295)    (4294967295, 4294967295)
--------------------------------------------------------------------------

```
Run the [**display access statistics trigger slot**](cmdqueryname=display+access+statistics+trigger+slot) *slot-id* command, you can view statistics about user packets on the board inslot 1.
```
<HUAWEI> display access-statistics trigger slot 1
```
```
IPv4 Packet information:
Passed packet(s)   : 0
Dropped packet(s)  : 0    
IPv6 Packet information:
Passed packet(s)    : 0
Dropped packet(s)  : 0

```

Run the [**display layer3-subscriber statistics port-mismatch**](cmdqueryname=display+layer3-subscriber+statistics+port-mismatch) command, you can view statistics about Layer 3 users' packets that are discarded due to an interface mismatch.
```
<HUAWEI> display layer3-subscriber statistics port-mismatch
```
```
  ---------------------------------------------------------------------------   
   Interface                       Statistics
  ---------------------------------------------------------------------------   
   Eth-Trunk1.1                    4            
   Eth-Trunk6                      3     
   Eth-Trunk6.1                    3     
   GigabitEthernet0/1/0.1          2     
   GigabitEthernet0/1/0.2          100    
  ---------------------------------------------------------------------------   
  Total 5,5 printed  

```