# SQLShield: SQL Injection Defense Environment

## 📌 Description
SQLShield is an OpenEnv environment that simulates SQL injection attacks and trains AI agents to detect and prevent malicious queries.

## 🎯 Objective
The agent must analyze SQL queries and decide whether to:
- allow
- block
- sanitize

## 🧩 Tasks

### Easy
Detect obvious SQL injection (e.g., OR 1=1)

### Medium
Detect moderate attacks (e.g., comments --)

### Hard
Detect advanced attacks (e.g., UNION queries)

## ⚙️ Action Space
- allow
- block
- sanitize

## 📊 Reward System
- Correct detection → +1.0
- Partial handling → +0.8 / +0.5
- Wrong action → -1.0

## 🚀 How to Run

```bash
python inference.py