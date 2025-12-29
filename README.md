**🤖 Hugo – Procurement AI Agent**

Hugo is an agentic AI system that helps industrial companies run procurement and inventory operations intelligently.
It reasons across ERP style data and supplier emails to detect risks, explain constraints, and recommend actions.

**What Hugo Does?**

Reactive Intelligence

- Detects low inventory and stockout risks

- Parses supplier emails for delays, price increases, shortages, and changes

- Flags production and delivery risks automatically

Build Capacity Reasoning

- Calculates how many products can be built with current inventory

- Identifies production bottlenecks using BOM and stock levels

Inventory and Dispatch Optimization

- Recommends changes to safety stock and reorder quantities

- Flags unnecessary reorders and aging inventory

- Helps balance cost, space, and service level

Automation Layer

- Generates daily operational summaries

- Recommends next actions without manual analysis

- Surfaces critical risks proactively


**Example Questions**

- How many scooters can we build right now?

- Which parts need urgent attention?

- Optimize inventory settings

- What should we do right now?

- Give me today’s operations summary


**How to run code?**

Step 1: Clone the repository
Step 2: Install dependencies
Step 3: Run the application

#here are the bash command

git clone https://github.com/MAquantum/hugo-procurement-ai-agent.git
cd hugo-procurement-ai-agent

pip install pandas streamlit

streamlit run ui/app.py

