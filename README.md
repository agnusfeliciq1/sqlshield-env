# SQLShield: SQL Injection Defense Environment

## Description
SQLShield is an OpenEnv environment that simulates SQL injection attacks.

## Objective
The agent must:
- allow
- block
- sanitize

## Tasks
### Easy
Detect simple attacks

### Medium
Detect moderate attacks

### Hard
Detect advanced attacks

## Action Space
- allow
- block
- sanitize

## Reward
- correct → +1.0
- wrong → -1.0

## How to Run
python inference.py
