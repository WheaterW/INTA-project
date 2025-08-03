Configuring VRRP Time Parameters
================================

Configuring VRRP Time Parameters

#### Context

A VRRP group performs a master/backup switchover if the master device fails or if a network is busy. After the original master device recovers or network communication is restored, VRRP reselects the master device based on device priorities.

Setting appropriate VRRP time parameters based on network flapping status. This minimizes the network interruptions or packet loss caused by frequent master/backup VRRP switchovers.


[Enabling VRRP Preemption and Configuring a Preemption Delay](vrp_vrrp_cfg_0133.html)



[Configuring an Interval for Sending VRRP Advertisement Packets](vrp_vrrp_cfg_0134.html)



[Configuring a VRRP Status Recovery Delay](vrp_vrrp_cfg_0135.html)



[Configuring a Timeout Period for a Backup Device in a VRRP Group](vrp_vrrp_cfg_0136.html)



[Configuring an Interval at Which the Master Device Sends Gratuitous ARP Packets](vrp_vrrp_cfg_0138.html)