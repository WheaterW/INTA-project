Configuring a Service Interface and Loopback Interface as Management Interfaces
===============================================================================

Configuring_a_Service_Interface_and_Loopback_Interface_as_Management_Interfaces

#### Networking Requirements

None


#### Configuration Roadmap

Configure IP addresses for the service interfaces and loopback interface for management. Bind no VPNs to the interfaces.


#### Data Preparation

None


#### Procedure

# Configure IP addresses for the management interface and loopback interface for management.

```
[*HUAWEI-GigabitEthernet0/3/1] ip address 10.3.1.1 24
[*HUAWEI-GigabitEthernet0/3/1] commit
[~HUAWEI-GigabitEthernet0/3/1] display this
#
interface GigabitEthernet0/3/1
 undo shutdown
 ip address 10.3.1.1 255.255.255.0 
#
```
```
[~HUAWEI-GigabitEthernet0/3/1] quit
[~HUAWEI] interface LoopBack 0
[~HUAWEI-LoopBack0] ip address 1.1.1.1 32
[*HUAWEI-LoopBack0] commit
[~HUAWEI-LoopBack0] display this
#
interface LoopBack0
  ip address 1.1.1.1 255.255.255.255
#
```

#### Verifying the Security Hardening Result

* Run the [**display this**](cmdqueryname=display+this) command to check the configuration.
* Run the [**display ip routing-table**](cmdqueryname=display+ip+routing-table) command to check route information.