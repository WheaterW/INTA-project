Overview of IP Multicast Basic
==============================

Overview of IP Multicast Basic

#### Definition

IP multicast is one of the three IP transmission modes and allows IP packets to be sent from a source and forwarded to a group of specific receivers. Only one copy of the same multicast data flow exists on each link. Compared with traditional unicast and broadcast, IP multicast can effectively save network bandwidth and reduce network load. Therefore, IP multicast is widely used in network services, such as IPTV, real-time data transmission, and multimedia conferencing.


#### Purpose

More and more data, voice, and video information is exchanged on a network, coupled with the emergence of new services, such as e-commerce, online conferencing and auctions, video on demand, and distance education. Most of these services comply with the point-to-multipoint mode and pose high requirements on information security, paid services, and network bandwidth.

Traditional IP communication supports two modes: unicast and broadcast. In unicast communication, an information source sends an individual message to each host requesting information. In broadcast communication, an information source sends information to all hosts on the network segment regardless of whether it is required.

On the network shown in [Figure 1](#EN-US_CONCEPT_0000001176741513__fig_01), to transmit data to multiple, but not all, destination hosts, a source host can broadcast the data or unicast multiple copies of data to the destination hosts.

**Figure 1** Point-to-multipoint data transmission in unicast and broadcast modes  
![](figure/en-us_image_0000001130781862.png)

In unicast mode, the amount of data transmitted on the network is proportional to the number of users who have requested the data. If a large number of users require the same data, the source host must send multiple copies of the data to these users, consuming high bandwidth on the source host and network. Therefore, this mode is not suitable for batch data transmission and is applicable only to networks with a small number of users.

In broadcast mode, data is sent to all hosts on a network segment, regardless of whether they have requested it. This threatens information security and may cause broadcast storms on the network segment. As such, this mode is not suitable for transmitting data from a source to specific destinations. It also wastes considerable bandwidth resources.

In summary, traditional unicast and broadcast modes cannot effectively implement point-to-multipoint data transmission. The multicast technology can be used to effectively implement point-to-multipoint data transmission. On the network shown in [Figure 2](#EN-US_CONCEPT_0000001176741513__fig_02), Source sends only one copy of data. Only the hosts (HostA and HostC) that require the data can receive it, whereas other hosts (HostB) cannot.

**Figure 2** Network diagram of point-to-multipoint data transmission in multicast mode  
![](figure/en-us_image_0000001130781860.png)

Multicast is applicable to data transmission in any point-to-multipoint scenarios, such as multimedia/streaming media, data warehouse, finance (stock), training, and joint operation. Internet information services provided by ISPs use IP multicast technologies, such as online live telecasting, streaming television, distance education, and web radio.


#### Benefits

Compared with unicast and broadcast, multicast has the following advantages:

* Compared with unicast, multicast starts to copy data and distribute data copies on a network node as far away from the source as possible. Therefore, the amount of data and network resource consumption will not increase significantly when the number of receivers increases.
* Compared with broadcast, multicast transmits data only to the receivers that have requested the data. This conserves network resources and enhances data transmission security.