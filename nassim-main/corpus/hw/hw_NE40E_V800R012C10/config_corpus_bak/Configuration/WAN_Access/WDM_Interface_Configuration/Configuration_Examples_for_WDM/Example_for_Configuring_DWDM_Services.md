Example for Configuring DWDM Services
=====================================

This section provides an example for configuring DWDM services.

#### Networking Requirements

As shown in [Figure 1](#EN-US_TASK_0000001211159179__fig1876110773113), colored optical modules are installed on router interfaces to directly output colored optical signals that comply with ITU-T G.694. The interfaces send optical signals with different wavelengths directly to the MUX of a DWDM device. The MUX multiplexes optical signals with specific wavelengths from multiple interfaces and then sends the signals to the DMUX. After receiving the signals with different wavelengths from the same MUX interface, the DMUX demultiplexes them and sends them through different interfaces. In this way, the optical signals are transmitted to the colored optical module interfaces with the corresponding wavelengths on the receive end.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 through 4 in this example represent GigabitEthernet0/1/0, GigabitEthernet0/1/1, GigabitEthernet0/1/0, and GigabitEthernet0/1/1, respectively.


**Figure 1** Networking diagram of DWDM colored optical interfaces on routers  
![](figure/en-us_image_0000001176154090.png)

#### Configuration Roadmap

1. Configure a transmission mode for specified interfaces.
2. Set channel IDs for the center wavelengths of the optical modules on the interfaces.
3. Check the center wavelengths of the optical modules on the interfaces.

#### Procedure

1. Configure a transmission mode for the specified interfaces on DeviceA and set channel IDs for the center wavelengths of the corresponding optical modules.
   
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] interface GigabitEthernet0/1/0
   [~DeviceA-GigabitEthernet0/1/0] set transfer-mode otn
   [*DeviceA-GigabitEthernet0/1/0] wavelength-channel 48
   [*DeviceA-GigabitEthernet0/1/0] quit
   [*DeviceA] interface GigabitEthernet0/1/1
   [*DeviceA-GigabitEthernet0/1/1] set transfer-mode otn
   [*DeviceA-GigabitEthernet0/1/1] wavelength-channel 48
   [*DeviceA-GigabitEthernet0/1/1] quit
   [~DeviceA] commit
   ```
2. Configure a transmission mode for the specified interfaces on DeviceB and set channel IDs for the center wavelengths of the corresponding optical modules.
   
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceB
   [*HUAWEI] commit
   [~DeviceB] interface GigabitEthernet0/1/0
   [~DeviceB-GigabitEthernet0/1/0] set transfer-mode otn
   [*DeviceB-GigabitEthernet0/1/0] wavelength-channel 49
   [*DeviceB-GigabitEthernet0/1/0] quit
   [*DeviceB] interface GigabitEthernet0/1/1
   [*DeviceB-GigabitEthernet0/1/1] set transfer-mode otn
   [*DeviceB-GigabitEthernet0/1/1] wavelength-channel 49
   [*DeviceB-GigabitEthernet0/1/1] quit
   [~DeviceB] commit
   ```
3. Verify the configuration.
   
   
   
   GigabitEthernet0/1/0 on DeviceA is used as an example.
   
   You can run the [**display interface**](cmdqueryname=display+interface) command to check the effective transmission mode and center wavelength of the specified interface. The mapping between the center wavelength and channel ID of the optical module can be queried through the [**display wavelength-capability**](cmdqueryname=display+wavelength-capability) command.
   
   ```
   [~DeviceA] display interface GigabitEthernet0/1/0
   ```
   ```
   GigabitEthernet0/1/0 current state : UP (ifindex: 521)
   Line protocol current state : DOWN
   Link quality grade : GOOD
   Description:
   Route Port,The Maximum Transmit Unit is 1500
   Internet protocol processing : disabled
   IP Sending Frames' Format is PKTFMT_ETHNT_2, Hardware address is xxxx-xxxx-xxxx
   The Vendor PN is LTF8502-BC+
   The Vendor Name is Hisense
   Port BW: 10G, Transceiver max BW: 10G, Transceiver Mode: MultiMode
   WaveLength: 1547.715nm, Transmission Distance: 300m
   Rx Power:  -2.90dBm, Warning range: [-9.901,  -1.000]dBm
   Tx Power:  -2.03dBm, Warning range: [-7.300,  -1.000]dBm
   Loopback: none, OTN full-duplex mode, Pause Flowcontrol: Receive Enable and Send Enable
   Last physical up time   : 2021-10-11 09:21:18
   Last physical down time : 2021-10-11 09:20:20
   Current system time: 2021-10-11 16:47:55
   Statistics last cleared:never
       Last 300 seconds input rate: 79 bits/sec, 0 packets/sec
       Last 300 seconds output rate: 79 bits/sec, 0 packets/sec
       Input peak rate 127 bits/sec, Record time: 2021-10-11 09:22:08
       Output peak rate 127 bits/sec, Record time: 2021-10-11 09:22:08
       Input: 293740 bytes, 895 packets
       Output: 293740 bytes, 895 packets
       Input:
         Unicast: 0 packets, Multicast: 895 packets
         Broadcast: 0 packets, JumboOctets: 0 packets
         CRC: 0 packets, Symbol: 0 packets
         Overrun: 0 packets, InRangeLength: 0 packets
         LongPacket: 0 packets, Jabber: 0 packets, Alignment: 0 packets
         Fragment: 0 packets, Undersized Frame: 0 packets
         RxPause: 0 packets
       Output:
         Unicast: 0 packets, Multicast: 895 packets
         Broadcast: 0 packets, JumboOctets: 0 packets
         Lost: 0 packets, Overflow: 0 packets, Underrun: 0 packets
         System: 0 packets, Overruns: 0 packets
         TxPause: 0 packets
       Local fault: normal, Remote fault: normal.
       Last 300 seconds input utility rate:  0.01%
       Last 300 seconds output utility rate: 0.01%
   ```
   ```
   [~DeviceA] display wavelength-capability interface GigabitEthernet0/1/0
   ```
   ```
   -----------------------------------------------
   index     Frequency(THz)     Wavelength(nm)
   -----------------------------------------------
   01        196.050            1529.163
   02        196.000            1529.553
   03        195.950            1529.944
   04        195.900            1530.334
   05        195.850            1530.725
   06        195.800            1531.116
   07        195.750            1531.507
   08        195.700            1531.898
   09        195.650            1532.290
   10        195.600            1532.681
   11        195.550            1533.073
   12        195.500            1533.465
   13        195.450            1533.858
   14        195.400            1534.250
   15        195.350            1534.643
   16        195.300            1535.036
   17        195.250            1535.429
   18        195.200            1535.822
   19        195.150            1536.216
   20        195.100            1536.609
   21        195.050            1537.003
   22        195.000            1537.397
   23        194.950            1537.792
   24        194.900            1538.186
   25        194.850            1538.581
   26        194.800            1538.976
   27        194.750            1539.371
   28        194.700            1539.766
   29        194.650            1540.162
   30        194.600            1540.557
   31        194.550            1540.953
   32        194.500            1541.349
   33        194.450            1541.746
   34        194.400            1542.142
   35        194.350            1542.539
   36        194.300            1542.936
   37        194.250            1543.333
   38        194.200            1543.730
   39        194.150            1544.128
   40        194.100            1544.526
   41        194.050            1544.924
   42        194.000            1545.322
   43        193.950            1545.720
   44        193.900            1546.119
   45        193.850            1546.518
   46        193.800            1546.917
   47        193.750            1547.316
   48        193.700            1547.715
   49        193.650            1548.115
   50        193.600            1548.515
   ```

#### Configuration Files

* DeviceA configuration file
  
  ```
  #
  sysname DeviceA
  #
  interface GigabitEthernet0/1/0
   set transfer-mode otn
   wavelength-channel 48
  #
  interface GigabitEthernet0/1/1
   set transfer-mode otn
   wavelength-channel 48
  #
  return
  ```
* DeviceB configuration file
  
  ```
  #
  sysname DeviceB
  #
  interface GigabitEthernet0/1/0
   set transfer-mode otn
   wavelength-channel 49
  #
  interface GigabitEthernet0/1/1
   set transfer-mode otn
   wavelength-channel 49
  #
  return
  ```