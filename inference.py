from env import SQLEnv

env = SQLEnv()

tasks = ["easy", "medium", "hard"]

print("[START]")

for task in tasks:
    state = env.reset(task)
    query = state["query"]

    # simple rule-based agent
    if "OR 1=1" in query:
        action = "block"
    elif "UNION" in query:
        action = "sanitize"
    elif "--" in query:
        action = "block"
    else:
        action = "allow"

    new_state, reward, done = env.step(action)

    print(f"[STEP] Task: {task}, Action: {action}, Reward: {reward}")

print("[END]")