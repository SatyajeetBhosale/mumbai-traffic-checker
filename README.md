# mumbai-traffic-checker
Live Mumbai traffic using TomTom API



**Live congestion insights for South Mumbai using the TomTom API.**  
This app doesn’t tell you where to go — it helps you understand what’s happening on the roads.

---

##  Why This App?

Products don’t have to beat giants. They just need to solve a different problem.

Google Maps excels at real-time, route-level navigation — telling an individual user how to get from Point A to Point B. That problem is already solved extremely well.

This app intentionally focuses on a different challenge:  
**Understanding city-level traffic congestion patterns**, not individual routes.

---

## What This App Does?

Instead of navigation, the app provides:

- City-wide congestion indicators  
- Comparison of current speed vs free-flow speed  
- Simple, explainable congestion metrics  
- A high-level view of how bad traffic is — not where to turn

This makes traffic **measurable, comparable, and observable over time**, which navigation apps typically do not expose.

---

## When This App Is Useful?

Use this app **before** opening a navigation tool — not during navigation.

Typical use cases:

- Deciding *when* to travel, not *which route* to take  
- Comparing congestion across cities  
- Understanding peak congestion windows  
- Supporting mobility, operations, or planning discussions  
- Demonstrating how live data can be turned into actionable insights



This is an **insight tool**, not a consumer navigation product.

---

## 🚀 Setup Instructions

1. Clone the repo or download the files  
2. Create a `.streamlit/secrets.toml` file with your TomTom API key:

```toml
[tomtom]
api_key = "your_api_key_here"
