# Moneta: HFT system for fun and profit

**Project Goals**

    I) Learning about the theory, the design, and the implementation of a High Frequency Trading System, the  ecosystem it lives in.
    II) Provide the writer with a fun project in which to experiment with the latest and greatest C++17/20 features, Rust, Python, and Mojo.
    III) Act as a pedagogical spring-board for others interested in these fascinating pieces of technology. Moneta is and will always remain open source.



**Building blocks**

    (Intial design, details TBD)

    - Data Feed Simulator:  It will provide updated prices to subscribers.
    - Broker/Exchange Simulator: it will host the order book and provide basic Order Matching (OM) features 

    - Gateway in (quotes): This component will interact with the Data Feed Sim and ingest the price datafeed.
    - Gateway out (orders): This component interfaces with the Broker Simulator to send orders and receive trade updates/confirmations.
    - Book Builder: Stores & aggregates info on orders, prices, and volumes obtained by the gateway from all venues.
    - Stragies and Strat Manager: Takes market data in input and generates market orders. The soul of the system.
    - Order Manager (or, Order Management System OMS): gathers, validates, and tracks the lifecycle of the orders sent by strategies 
    - C&C: Data visualization, start and stop functionalities 



┌─────────────────────┐       ┌────────────────────┐    ┌────────────────────┐     ┌────────────────────────────┐
│                     │       │                    │    │                    │     │                            │
│ Data Feed Simulator │       │                    │    │    Book            │     │   ┌─s1────────┐            │
│                     ├───────►    Gateway IN      ├────►    Builder         ├─────►   │           │            │
│                     │       │     (quotes)       │    │                    │     │   │  ┌─s2─────┼───┐        │
└─────────────────────┘       │                    │    │                    │     │   │  │        │   │        │
                              └────────────────────┘    └────────────────────┘     │   └──┼────────┘   │        │
                                                                                   │      │            │        │
                                                                                   │      └────────────┘        │
                                                                                   │                            │
┌─────────────────────┐       ┌────────────────────┐    ┌────────────────────┐     │                            │
│                     │       │                    │    │                    │     │                            │
│  Broker Exchange    ◄───────┤                    ◄────┤    Order           │     │   Strategy Manager         │
│  Simulator          │       │   Gateway OUT      │    │    Manager         ◄─────┤                            │
│                     ├───────►     (orders)       ├────►                    │     └────────────────────────────┘
└─────────────────────┘       │                    │    │                    │
                              └────────────────────┘    └────────────────────┘     ┌────────────────────────────┐
                                                                                   │                            │
                                                                                   │                            │
                                                                                   │           C&C              │
                                                                                   │                            │
                                                                                   │                            │
                                                                                   └────────────────────────────┘

